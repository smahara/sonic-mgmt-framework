/*
 * $Id: bcm-ptp-clock.c,v 1.90 2013/09/25 10:02:36 vipin sharma Exp $
 * $Copyright: (c) 2018 Broadcom Corp.
 * All Rights Reserved.$
 */

/*
 * This module implements a Linux PTP Clock driver for Broadcom
 * XGS switch devices.
 *
 * For a list of supported module parameters, please see below.
 *   debug: Debug level (default 0)
 *   network_transport : Transport Type (default 0 - Raw)
 *   base_dev_name: Base device name (default ptp0, ptp1, etc.)
 */

#include <gmodule.h> /* Must be included first */
#include <linux/ptp_clock_kernel.h>
#include <linux/clocksource.h>
#include <linux/net_tstamp.h>
#include <linux/ptp_clock_kernel.h>
#include <linux-bde.h>
#include <kcom.h>
#include <bcm-knet.h>
#include <linux/time64.h>
#include <linux/delay.h>
#include <linux/etherdevice.h>
#include <linux/netdevice.h>
#include <linux/time.h>
#include <linux/types.h>

MODULE_AUTHOR("Broadcom Corporation");
MODULE_DESCRIPTION("PTP Clock Driver for Broadcom XGS Switch");
MODULE_LICENSE("GPL");

/* Configuration Parameters */
static int debug;
LKM_MOD_PARAM(debug, "i", int, 0);
MODULE_PARM_DESC(debug,
        "Debug level (default 0)");

static int network_transport;
LKM_MOD_PARAM(network_transport, "i", int, 0);
MODULE_PARM_DESC(network_transport,
        "Transport Type (default 0 - Raw)");

static char *base_dev_name = "ptp0";
LKM_MOD_PARAM(base_dev_name, "s", charp, 0);
MODULE_PARM_DESC(base_dev_name,
        "Base device name (default ptp0, ptp1, etc.)");

/* Debug levels */
#define DBG_LVL_VERB    0x1
#define DBG_LVL_WARN    0x2

#define DBG_VERB(_s)    do { if (debug & DBG_LVL_VERB) gprintk _s; } while (0)
#define DBG_WARN(_s)    do { if (debug & DBG_LVL_WARN) gprintk _s; } while (0)


/* Module Information */
#define MODULE_MAJOR 125
#define MODULE_NAME "linux-bcm-ptp-clock"


/* Clock Private Data */
struct bcm_ptp_priv {
    struct device dev;
    struct ptp_clock *ptp_clock;
    struct ptp_clock_info ptp_caps;
    spinlock_t ptp_lock;
    volatile void *base_addr;   /* Base address for PCI register access */
    volatile void *base_addr1;   /* Base address for shadow memory access */
    s64        phase_offset;
    u64        ref_counter_48;
    s64        ref_time_64;
    struct delayed_work time_keep;
};

static struct bcm_ptp_priv *ptp_priv;


/* SOBMH HEDER information for TH for Timestamp Enable */
uint32_t sobmhrawpkts[4] = { 0x00000000, 0x00010e00, 0x00000000, 0x00000000 };
uint32_t sobmhudpipv4[4] = { 0x00000000, 0x00012A00, 0x00000000, 0x00000000 };
uint32_t sobmhudpipv6[4] = { 0x00000000, 0x00012A00, 0x00000000, 0x00000000 };
#define HOST_BASED_PHC
#if defined(HOST_BASED_PHC)
uint64_t freq_ctrl_low_nominal = 0x40000000;
uint64_t freq_ctrl_low_extended = 0;
#endif


/* Data Structure for TX Timestamp FIFO Access */
#define BCM_TX_TS_QUEUE_SIZE 128

#define BCM_KSYNC_INIT   0xBCBC1234
#define BCM_KSYNC_DEINIT 0xDEAD1234
#define BCM_KSYNC_EXIT   0xDEAD4321

typedef struct _bcm_tx_ts_data_s
{
    u32 ts_valid; // 16
    u32 port_id;  // 20
    u32 ts_seq_id; // 22
    u32 res;       // 22
    u64 timestamp; // 24
} bcm_tx_ts_data_t;

typedef struct _bcm_uc_linux_ipc_s
{
    u32 ksyncinit; // 0
    u32 res; // 0
    s64 freqcorr;
    u64 portmap[8];      // 8
    bcm_tx_ts_data_t port_ts_data[BCM_TX_TS_QUEUE_SIZE];
} bcm_uc_linux_ipc_t;

bcm_uc_linux_ipc_t *linuxPTPMemory = (bcm_uc_linux_ipc_t*)(0);

uint32_t linux_timestamps_idx_head = 0;

/* Shadow Memory and CMIC Memory Access Macros */
//#define BCM_CMIC_SHADOW_MEM_BASE 0x60006000
#define BCM_CMIC_SHADOW_MEM_BASE 0xfb006000
#define BCM_CMIC_SHADOW_MEM_SIZE 4096

#if defined(CMIC_SOFT_BYTE_SWAP)

#define CMIC_SWAP32(_x)   ((((_x) & 0xff000000) >> 24) \
        | (((_x) & 0x00ff0000) >>  8) \
        | (((_x) & 0x0000ff00) <<  8) \
        | (((_x) & 0x000000ff) << 24))

#define DEV_READ32(_d, _a, _p) \
    do { \
        uint32_t _data; \
        _data = (((volatile uint32_t *)(_d)->base_addr)[(_a)/4]); \
        *(_p) = CMIC_SWAP32(_data); \
    } while(0)

#define DEV_WRITE32(_d, _a, _v) \
    do { \
        uint32_t _data = CMIC_SWAP32(_v); \
        ((volatile uint32_t *)(_d)->base_addr)[(_a)/4] = (_data); \
    } while(0)

#else

#define DEV_READ32(_d, _a, _p) \
    do { \
        *(_p) = (((volatile uint32_t *)(_d)->base_addr)[(_a)/4]); \
    } while(0)

#define DEV_WRITE32(_d, _a, _v) \
    do { \
        ((volatile uint32_t *)(_d)->base_addr)[(_a)/4] = (_v); \
    } while(0)
#define UC_LINUX_SH_MEM
#ifdef UC_LINUX_SH_MEM

#define DEV_SHWRITE8(_d, _a, _v) \
    do { \
        ((volatile uint8_t *)(_d)->base_addr1)[(_a)] = (_v); \
    } while(0)
#define DEV_SHREAD8(_d, _a, _p) \
    do { \
        *(_p) = (((volatile uint8_t *)(_d)->base_addr1)[(_a)]); \
    } while(0)
#define DEV_SHREAD16(_d, _a, _p) \
    do { \
        *(_p) = (((volatile uint16_t *)(_d)->base_addr1)[(_a)/2]); \
    } while(0)
#define DEV_SHWRITE16(_d, _a, _v) \
    do { \
        ((volatile uint16_t *)(_d)->base_addr1)[(_a)/2] = (_v); \
    } while(0)
#define DEV_SHREAD32(_d, _a, _p) \
    do { \
        *(_p) = (((volatile uint32_t *)(_d)->base_addr1)[(_a)/4]); \
    } while(0)
#define DEV_SHWRITE32(_d, _a, _v) \
    do { \
        ((volatile uint32_t *)(_d)->base_addr1)[(_a)/4] = (_v); \
    } while(0)
#define DEV_SHREAD64(_d, _a, _p) \
    do { \
        *(_p) = (((volatile uint64_t *)(_d)->base_addr1)[(_a)/8]); \
    } while(0)
#define DEV_SHWRITE64(_d, _a, _v) \
    do { \
        ((volatile uint64_t *)(_d)->base_addr1)[(_a)/8] = (_v); \
    } while(0)
#else 
#define DEV_SHWRITE8(_d, _a, _v) \
    do { \
    } while(0)
#define DEV_SHREAD8(_d, _a, _p) \
    do { \
    } while(0)
#define DEV_SHREAD16(_d, _a, _p) \
    do { \
    } while(0)
#define DEV_SHWRITE16(_d, _a, _v) \
    do { \
    } while(0)
#define DEV_SHREAD32(_d, _a, _p) \
    do { \
    } while(0)
#define DEV_SHWRITE32(_d, _a, _v) \
    do { \
    } while(0)
#define DEV_SHREAD64(_d, _a, _p) \
    do { \
    } while(0)
#define DEV_SHWRITE64(_d, _a, _v) \
    do { \
    } while(0)

#endif
#endif  /* defined(CMIC_SOFT_BYTE_SWAP) */

/*
 *  Hardware specific register information 
 *
 */

/* CMIC registers */
#define CMIC_TS_FREQ_CTRL_LOWER 0x00010400
#define CMIC_TS_FREQ_CTRL_UPPER 0x00010404
#define CMIC_TS_FREQ_CTRL_ENABLE(val) ((0x1 << 28)|(val))
#define CMIC_TS_FREQ_CTRL_DISABLE(val) (~(0x1 << 28)&(val))

#define CMIC_TIMESYNC_TS0_FREQ_CTRL_UPPER 0x00010610
#define CMIC_TIMESYNC_TS0_FREQ_CTRL_LOWER 0x0001060C

#define CMIC_TIMESYNC_TS1_FREQ_CTRL_UPPER 0x00010620
#define CMIC_TIMESYNC_TS1_FREQ_CTRL_LOWER 0x0001061C

#if defined(HOST_BASED_PHC)
#define CMIC_TIMESYNC_TS0_FREQ_CTRL_FRAC  0x00010608
#define CMIC_TIMESYNC_TS1_FREQ_CTRL_FRAC  0x00010618

#define CMIC_TIMESYNC_TS0_COUNTER_ENABLE  0x00010604
#define CMIC_TIMESYNC_TS1_COUNTER_ENABLE  0x00010614
#endif

static s64 bcm_ptp_extend_32b_hwts_to_64b(u32 hwts)
{
    s64 reftime;
    
    u32 ref_lower;
    s32 diff;
 
    reftime = ptp_priv->ref_time_64;
    ref_lower = (u32)(reftime & 0xFFFFFFFF);
    diff = (s32)(hwts - ref_lower);
    
    return (reftime + diff);
}

static s64 bcm_ptp_extend_48b_hwts_to_64b(u64 hwts)
{
    s64 reftime;
    u64 ref_lower;
    s64 diff;
 
    reftime = ptp_priv->ref_time_64;
    ref_lower = (u64)(reftime & 0xFFFFFFFFFFFFLL);
    diff = (s64)((hwts & 0xFFFFFFFFFFFFLL)- ref_lower);

    return (reftime + diff);
}   


/**
 * bcm_ptp_adjfreq
 *
 * @ptp: pointer to ptp_clock_info structure
 * @ppb: desired period change in parts ber billion
 *
 * Description: this function will adjust the frequency of hardware clock.
 */
#if defined(HOST_BASED_PHC)
static void knetsync_ptp_adjfreq(struct ptp_clock_info *ptp, int32_t ppb)
{
    int64_t correction;
    uint32_t regVal;
    struct bcm_ptp_priv *priv = container_of(ptp, struct bcm_ptp_priv, ptp_caps);

    correction = (((int64_t)(freq_ctrl_low_nominal) * (int64_t)ppb * 2199 + (2^40)) >> 41);
    freq_ctrl_low_extended = freq_ctrl_low_nominal + (int32_t)correction;
    regVal = (uint32_t)(freq_ctrl_low_extended & 0xFFFFFFFF);
    DEV_WRITE32(priv, CMIC_TIMESYNC_TS1_FREQ_CTRL_FRAC, regVal);
}
#endif

static int bcm_ptp_adjfreq(struct ptp_clock_info *ptp, s32 ppb)
{
    struct bcm_ptp_priv *priv =
        container_of(ptp, struct bcm_ptp_priv, ptp_caps);
    unsigned long flags;
    spin_lock_irqsave(&priv->ptp_lock, flags);
#if defined(HOST_BASED_PHC)
    knetsync_ptp_adjfreq(ptp, ppb);
#else
    DEV_SHWRITE32(priv,(int)&linuxPTPMemory->freqcorr,ppb);
#endif
    spin_unlock_irqrestore(&priv->ptp_lock, flags);
    return 0;
}

/**
 * bcm_ptp_adjtime
 *
 * @ptp: pointer to ptp_clock_info structure
 * @delta: desired change in nanoseconds
 *
 * Description: this function will shift/adjust the hardware clock time.
 */
static int bcm_ptp_adjtime(struct ptp_clock_info *ptp, s64 delta)
{
    struct bcm_ptp_priv *priv =
        container_of(ptp, struct bcm_ptp_priv, ptp_caps);
    unsigned long flags;
    spin_lock_irqsave(&priv->ptp_lock, flags);
    priv->phase_offset += delta;
    spin_unlock_irqrestore(&priv->ptp_lock, flags);
    return 0;
}

/**
 * bcm_ptp_gettime
 *
 * @ptp: pointer to ptp_clock_info structure
 * @ts: pointer to hold time/result
 *
 * Description: this function will read the current time from the
 * hardware clock and store it in @ts.
 */
static int bcm_ptp_gettime(struct ptp_clock_info *ptp, struct timespec64 *ts)
{
    struct bcm_ptp_priv *priv =
        container_of(ptp, struct bcm_ptp_priv, ptp_caps);
    unsigned long flags;
    u64 current_counter = 0;
    uint32_t lower;
    uint32_t upper;
    u64 upper64; 

    s64 reftime;
    u64 ref_counter;
    
    spin_lock_irqsave(&priv->ptp_lock, flags);
    reftime = priv->ref_time_64;
    ref_counter = priv->ref_counter_48;

    DEV_READ32(priv, CMIC_TIMESYNC_TS1_FREQ_CTRL_LOWER, &lower);
    DEV_READ32(priv, CMIC_TIMESYNC_TS1_FREQ_CTRL_UPPER, &upper);

    upper64 = (u64)upper;

    current_counter = (upper64 << 32)  | lower;
    if (current_counter > ref_counter) { 
        reftime += (current_counter - ref_counter);
    } else { 
        reftime += ((1LL<<48) + current_counter - ref_counter);
    }

    priv->ref_counter_48 = reftime & 0xFFFFFFFFFFFFLL;
    priv->ref_time_64 = reftime;
    reftime += priv->phase_offset;

    spin_unlock_irqrestore(&priv->ptp_lock, flags);

    *ts = ns_to_timespec64(reftime);
    return 0;
}


/**
 * bcm_ptp_settime
 *
 * @ptp: pointer to ptp_clock_info structure
 * @ts: time value to set
 *
 * Description: this function will set the current time on the
 * hardware clock.
 */
static int bcm_ptp_settime(struct ptp_clock_info *ptp,
        const struct timespec64 *ts)
{
    struct bcm_ptp_priv *priv =
        container_of(ptp, struct bcm_ptp_priv, ptp_caps);
    unsigned long flags;

    s64 reftime;

    reftime = timespec64_to_ns(ts);
    
    spin_lock_irqsave(&priv->ptp_lock, flags);
    priv->ref_time_64 = reftime; 
    priv->ref_counter_48 = reftime & 0xFFFFFFFFFFFFLL;
    /* Write TS COUNTER */
    DEV_WRITE32(priv, CMIC_TIMESYNC_TS1_FREQ_CTRL_LOWER, (reftime & 0xFFFFFFFF));
    DEV_WRITE32(priv, CMIC_TIMESYNC_TS1_FREQ_CTRL_UPPER, ((reftime >> 32) & 0xFFFF));
    priv->phase_offset = 0;

    spin_unlock_irqrestore(&priv->ptp_lock, flags);
    return 0;
}
static int bcm_ptp_enable(struct ptp_clock_info *ptp,
        struct ptp_clock_request *rq, int on)
{
    return 0;
}
/* structure describing a PTP hardware clock */
static struct ptp_clock_info bcm_ptp_caps = {
    .owner = THIS_MODULE,
    .name = "bcm_ptp_clock",
    .max_adj = 200000,
    .n_alarm = 0,
    .n_ext_ts = 0,
    .n_per_out = 0, /* will be overwritten in bcm_ptp_register */
    .n_pins = 0,
    .pps = 0,
    .adjfreq = bcm_ptp_adjfreq,
    .adjtime = bcm_ptp_adjtime,
    .gettime64 = bcm_ptp_gettime,
    .settime64 = bcm_ptp_settime,
    .enable = bcm_ptp_enable,
};
int bcm_ptp_hw_tstamp_enable(int dev_no, int port)
{
    uint32_t portmap = 0;
    DEV_SHREAD32(ptp_priv,8,&portmap);
    portmap |= 0x1 << port;
    DEV_SHWRITE32(ptp_priv,8,portmap);

    return 0;
}
int bcm_ptp_hw_tstamp_disable(int dev_no, int port)
{
    uint32_t portmap = 0;
    DEV_SHREAD32(ptp_priv,8,&portmap);
    portmap &= ~(0x1 << port);
    DEV_SHWRITE32(ptp_priv,8,portmap);
    return 0;
}

int bcm_ptp_hw_tstamp_tx_time_get(int dev_no, int port, uint8_t *pkt, uint64_t *ts)
{
    /* Get Timestamp from R5 or CLMAC */
    uint32_t ts_valid = 0;
    uint32_t seq_id = 0;
    uint32_t pktseq_id = 0;
    uint32_t port_id = 0;
    uint64_t timestamp = 0;
#if defined(HOST_BASED_PHC)
    int count = 10000;
#else
    int count = 100;
#endif
    int pkt_offset; 

    if (!ptp_priv || !pkt || !ts)
        return -1;
    if (port < 1 || port > 255)
        return -1;

    *ts = 0;
    switch(network_transport)
    {
        case 0:
            pkt_offset = 0x2c;
            break;
        case 1:
            pkt_offset = 0x48;
            break;
        case 2:
            pkt_offset = 0x2c;
            break;
        default: 
            pkt_offset = 0x2c;
            break;
    }

    pktseq_id = *((uint16_t *)(pkt + pkt_offset));
    port = port - 1;
    /* Fetch the TX timestamp from shadow memory */
    do {
        DEV_SHREAD32(ptp_priv,(uintptr_t)&linuxPTPMemory->port_ts_data[port].ts_valid,&ts_valid); 
        if (ts_valid)
        {
            DEV_SHREAD32(ptp_priv,(uintptr_t)&linuxPTPMemory->port_ts_data[port].port_id,&port_id); 
            DEV_SHREAD32(ptp_priv,(uintptr_t)&linuxPTPMemory->port_ts_data[port].ts_seq_id,&seq_id); 
            DEV_SHREAD64(ptp_priv,(uintptr_t)&linuxPTPMemory->port_ts_data[port].timestamp,&timestamp); 
            /* Clear the shadow memory to get next entry */
            DEV_SHWRITE64(ptp_priv,(uintptr_t)&linuxPTPMemory->port_ts_data[port].timestamp,0); 
            DEV_SHWRITE32(ptp_priv,(uintptr_t)&linuxPTPMemory->port_ts_data[port].port_id,0); 
            DEV_SHWRITE32(ptp_priv,(uintptr_t)&linuxPTPMemory->port_ts_data[port].ts_seq_id,0); 
            DEV_SHWRITE32(ptp_priv,(uintptr_t)&linuxPTPMemory->port_ts_data[port].ts_valid,0); 
            if (seq_id == pktseq_id)
            {
                *ts = bcm_ptp_extend_48b_hwts_to_64b(timestamp) + ptp_priv->phase_offset;
                break;
            } else 
                continue;

        }
        count--;
    } while(count);
    return 0;
}

int bcm_ptp_hw_tstamp_rx_time_upscale(int dev_no, uint64_t *ts)
{
    uint32_t hwts;
    
    if (!ptp_priv && ts == NULL)
        return -1;
    hwts = (uint32_t) (*ts & 0xFFFFFFFF);

    *ts = bcm_ptp_extend_32b_hwts_to_64b(hwts) + ptp_priv->phase_offset;

    return 0;
}

int bcm_ptp_hw_tstamp_tx_meta_get(int dev_no, struct sk_buff *skb, uint32_t **md)
{
    switch(network_transport)
    {
        case 0:
            *md = &sobmhrawpkts[0];
            break;
        case 1:
            *md = &sobmhudpipv4[0];
            break;
        case 2:
            *md = &sobmhudpipv6[0];
            break;
        default: 
            *md = &sobmhudpipv4[0];
            break;
    }
    return 0;
}


int bcm_ptp_hw_tstamp_ptp_clock_index_get(int dev_no)
{
    if (!ptp_priv)
        return -1;
    return 0;
}

/**
 * bcm_ptp_time_keep - call timecounter_read every second to avoid timer overrun
 *                 because  a 32bit counter, will timeout in 4s
 */
static void bcm_ptp_time_keep(struct work_struct *work)
{
    struct delayed_work *dwork = to_delayed_work(work);
    struct bcm_ptp_priv *priv =
                   container_of(dwork, struct bcm_ptp_priv, time_keep);
    struct timespec64 ts;
    
    /* Call bcm_ptp_gettime function to keep the ref_time_64 and ref_counter_48 in sync */
    bcm_ptp_gettime(&(priv->ptp_caps), &ts);

    schedule_delayed_work(&priv->time_keep, HZ);
}

#if defined(HOST_BASED_PHC)
static void knetsync_timer_enable(struct ptp_clock_info *ptp)
{
    struct bcm_ptp_priv *priv =
        container_of(ptp, struct bcm_ptp_priv, ptp_caps);

    /* Enable TS0 COUNTER */
    DEV_WRITE32(priv, CMIC_TIMESYNC_TS0_FREQ_CTRL_FRAC, (uint32_t)(freq_ctrl_low_nominal));
    DEV_WRITE32(priv, CMIC_TIMESYNC_TS0_FREQ_CTRL_LOWER, 0);
    DEV_WRITE32(priv, CMIC_TIMESYNC_TS0_FREQ_CTRL_UPPER, 0);
    DEV_WRITE32(priv, CMIC_TIMESYNC_TS0_COUNTER_ENABLE, 1);

    /* Enable TS1 COUNTER */
    DEV_WRITE32(priv, CMIC_TIMESYNC_TS1_FREQ_CTRL_FRAC, (uint32_t)(freq_ctrl_low_nominal));
    DEV_WRITE32(priv, CMIC_TIMESYNC_TS1_FREQ_CTRL_LOWER, 0);
    DEV_WRITE32(priv, CMIC_TIMESYNC_TS1_FREQ_CTRL_UPPER, 0);
    DEV_WRITE32(priv, CMIC_TIMESYNC_TS1_COUNTER_ENABLE, 1);
}

static void knetsync_timer_disable(struct ptp_clock_info *ptp)
{
    struct bcm_ptp_priv *priv =
        container_of(ptp, struct bcm_ptp_priv, ptp_caps);

    /* Disable TS0 COUNTER */
    DEV_WRITE32(priv, CMIC_TIMESYNC_TS0_FREQ_CTRL_FRAC, 0);
    DEV_WRITE32(priv, CMIC_TIMESYNC_TS0_FREQ_CTRL_LOWER,0);
    DEV_WRITE32(priv, CMIC_TIMESYNC_TS0_FREQ_CTRL_UPPER,0);
    DEV_WRITE32(priv, CMIC_TIMESYNC_TS0_COUNTER_ENABLE, 0);
    /* Disable TS1 COUNTER */
    DEV_WRITE32(priv, CMIC_TIMESYNC_TS1_FREQ_CTRL_FRAC, 0);
    DEV_WRITE32(priv, CMIC_TIMESYNC_TS1_FREQ_CTRL_LOWER,0);
    DEV_WRITE32(priv, CMIC_TIMESYNC_TS1_FREQ_CTRL_UPPER,0);
    DEV_WRITE32(priv, CMIC_TIMESYNC_TS1_COUNTER_ENABLE, 0);
}
#endif

static void bcm_ptp_init(struct ptp_clock_info *ptp)
{
    struct bcm_ptp_priv *priv =
        container_of(ptp, struct bcm_ptp_priv, ptp_caps);
    unsigned long flags;
    /* Enabling Timestamper */
    spin_lock_irqsave(&priv->ptp_lock, flags);
    /* Set current phase_offset as ZERO */
    priv->phase_offset = 0;
    DEV_SHWRITE32(priv,(uintptr_t)&linuxPTPMemory->ksyncinit,BCM_KSYNC_INIT);
 
#if defined(HOST_BASED_PHC)
    knetsync_timer_enable(ptp);
#endif

    spin_unlock_irqrestore(&priv->ptp_lock, flags);
}

static void bcm_ptp_deinit(struct ptp_clock_info *ptp)
{
    struct bcm_ptp_priv *priv =
        container_of(ptp, struct bcm_ptp_priv, ptp_caps);
    unsigned long flags;
    /* Disabling Timestamper */
    spin_lock_irqsave(&priv->ptp_lock, flags);
    
    DEV_SHWRITE32(priv,(uintptr_t)&linuxPTPMemory->ksyncinit,BCM_KSYNC_DEINIT);

#if defined(HOST_BASED_PHC)
    /* Disable the timer */
    knetsync_timer_disable(ptp);
#endif
 
    spin_unlock_irqrestore(&priv->ptp_lock, flags);
}

/**
 * bcm_ptp_register
 * @priv: driver private structure
 * Description: this function will register the ptp clock driver
 * to kernel. It also does some house keeping work.
 */

static int bcm_ptp_register(void)
{
    int err = -ENOMEM;
    
    ptp_priv = kzalloc(sizeof(*ptp_priv), GFP_KERNEL);
    
    if (!ptp_priv)
        goto no_memory;

    err = -ENODEV;

    /* Initialize the Base address for CMIC and Shadow Memory access */
    ptp_priv->base_addr = lkbde_get_dev_virt(0);
    ptp_priv->base_addr1 = ioremap_nocache(BCM_CMIC_SHADOW_MEM_BASE, BCM_CMIC_SHADOW_MEM_SIZE);

    if (debug & DBG_LVL_VERB)
        printk(KERN_EMERG"%s %lx:%lx\n",__FUNCTION__,(uintptr_t)ptp_priv->base_addr,(uintptr_t)ptp_priv->base_addr1);
    

    ptp_priv->ptp_caps = bcm_ptp_caps;

    spin_lock_init(&ptp_priv->ptp_lock);
    
    bcm_ptp_init(&(ptp_priv->ptp_caps));
    
    /* Register ptp clock driver with bcm_ptp_caps */
    ptp_priv->ptp_clock = ptp_clock_register(&ptp_priv->ptp_caps,
            NULL);

    if (IS_ERR(ptp_priv->ptp_clock)) {
        ptp_priv->ptp_clock = NULL;
    } else if (ptp_priv->ptp_clock) {
        err = 0;
       
        /* Register BCM-KNET HW Timestamp Callback Functions */
        bkn_hw_tstamp_enable_cb_register(bcm_ptp_hw_tstamp_enable);
        bkn_hw_tstamp_disable_cb_register(bcm_ptp_hw_tstamp_disable);
        bkn_hw_tstamp_tx_time_get_cb_register(bcm_ptp_hw_tstamp_tx_time_get);
        bkn_hw_tstamp_tx_meta_get_cb_register(bcm_ptp_hw_tstamp_tx_meta_get);
        bkn_hw_tstamp_rx_time_upscale_cb_register(bcm_ptp_hw_tstamp_rx_time_upscale);
        bkn_hw_tstamp_ptp_clock_index_cb_register(bcm_ptp_hw_tstamp_ptp_clock_index_get);
    
        /* Initialized and schedule time keep delayed work */
        INIT_DELAYED_WORK(&(ptp_priv->time_keep), bcm_ptp_time_keep);
        schedule_delayed_work(&(ptp_priv->time_keep), HZ);
    }
    
no_memory:
    return err;
}

static int bcm_ptp_remove(void)
{
    if (!ptp_priv)
        return 0;
    /* Cancel delayed work */
    cancel_delayed_work_sync(&(ptp_priv->time_keep));
    
    /* UnRegister BCM-KNET HW Timestamp Callback Functions */
    bkn_hw_tstamp_enable_cb_unregister(bcm_ptp_hw_tstamp_enable);
    bkn_hw_tstamp_disable_cb_unregister(bcm_ptp_hw_tstamp_disable);
    bkn_hw_tstamp_tx_time_get_cb_unregister(bcm_ptp_hw_tstamp_tx_time_get);
    bkn_hw_tstamp_tx_meta_get_cb_unregister(bcm_ptp_hw_tstamp_tx_meta_get);
    bkn_hw_tstamp_rx_time_upscale_cb_unregister(bcm_ptp_hw_tstamp_rx_time_upscale);
    bkn_hw_tstamp_ptp_clock_index_cb_unregister(bcm_ptp_hw_tstamp_ptp_clock_index_get);
    
    /* Deinitialize the PTP */
    bcm_ptp_deinit(&(ptp_priv->ptp_caps));
    
    /* Unregister the bcm ptp clock driver */
    ptp_clock_unregister(ptp_priv->ptp_clock);
    
    /* Free Memory */
    kfree(ptp_priv);

    return 0;
}


/*
 * Generic module functions
 */

/*
 * Function: _pprint
 *
 * Purpose:
 *    Print proc filesystem information.
 * Parameters:
 *    None
 * Returns:
 *    Always 0
 */
    static int
_pprint(void)
{
    pprintf("Broadcom BCM PTP Hardware Clock Module\n");
    /* put some goodies here */
    return 0;
}

/*
 * Function: _init
 *
 * Purpose:
 *    Module initialization.
 *    Attached SOC all devices and optionally initializes these.
 * Parameters:
 *    None
 * Returns:
 *    0 on success, otherwise -1
 */
    static int
_init(void)
{
    bcm_ptp_register();
    return 0;
}

/*
 * Function: _cleanup
 *
 * Purpose:
 *    Module cleanup function
 * Parameters:
 *    None
 * Returns:
 *    Always 0
 */
    static int
_cleanup(void)
{
    bcm_ptp_remove();
    return 0;
}

static gmodule_t _gmodule = {
name: MODULE_NAME,
      major: MODULE_MAJOR,
      init: _init,
      cleanup: _cleanup,
      pprint: _pprint,
      ioctl: NULL,
      open: NULL,
      close: NULL,
};

    gmodule_t*
gmodule_get(void)
{
    EXPORT_NO_SYMBOLS;
    return &_gmodule;
}





