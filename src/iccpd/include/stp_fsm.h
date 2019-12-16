/*
 * Copyright 2019 Broadcom. The term "Broadcom" refers to Broadcom Inc. and/or
 * its subsidiaries.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef _STP_FSM_H
#define _STP_FSM_H

#include "../include/port.h"

#define MLCAP_SYNC_PHY_DEV_SEC     1     /*every 1 sec*/

#define STP(csm_ptr)  (csm_ptr->app_csm.stp)

struct CSM;

enum STP_ICCP_STATE
{
    STP_NONEXISTENT,
    STP_RESET,
    STP_CONNSENT,
    STP_CONNREC,
    STP_CONNECTING,
    STP_OPERATIONAL
};

typedef enum STP_ICCP_STATE STP_ICCP_STATE_E;

enum STP_APP_STATE
{
    STP_STATE_INIT,
    STP_STATE_STAGE1,
    STP_STATE_STAGE2,
    STP_STATE_EXCHANGE,
    STP_STATE_ERROR,
};

typedef enum STP_APP_STATE STP_APP_STATE_E;

/* for sender only*/
enum STP_SYNC_STATE
{
    STP_SYNC_SYSCONF = 0,
    STP_SYNC_AGGCONF,
    STP_SYNC_AGGSTATE,
    STP_SYNC_AGGINFO,
    STP_SYNC_PEERLINKINFO,
    STP_SYNC_ARP_INFO,
    STP_SYNC_NDISC_INFO,
    STP_SYNC_DONE,
};

typedef enum STP_SYNC_STATE STP_SYNC_STATE_E;

/****************************************************************
 * Debug counters to track message sent and received between
 * MC-LAG peers over ICCP
 ***************************************************************/
typedef uint8_t STP_ICCP_DBG_CNTR_DIR_e;
enum STP_ICCP_DBG_CNTR_DIR_e
{
    STP_ICCP_DBG_CNTR_DIR_TX  = 0,
    STP_ICCP_DBG_CNTR_DIR_RX  = 1,
    STP_ICCP_DBG_CNTR_DIR_MAX
};

typedef uint8_t STP_ICCP_DBG_CNTR_STS_e;
enum STP_ICCP_DBG_CNTR_STS_e
{
    STP_ICCP_DBG_CNTR_STS_OK  = 0,
    STP_ICCP_DBG_CNTR_STS_ERR = 1,     /* Send error or receive processing error*/
    STP_ICCP_DBG_CNTR_STS_MAX
};

/* Change MCLAGDCTL_MAX_DBG_COUNTERS if STP_ICCP_DBG_CNTR_MSG_MAX is more than 32 */
enum STP_ICCP_DBG_CNTR_MSG
{
    STP_ICCP_DBG_CNTR_MSG_SYS_CONFIG       = 0,
    STP_ICCP_DBG_CNTR_MSG_NAK              = 9,
    STP_ICCP_DBG_CNTR_MSG_SYNC_DATA        = 10,
    STP_ICCP_DBG_CNTR_MSG_SYNC_REQ         = 11,
    STP_ICCP_DBG_CNTR_MSG_MAX
};
typedef enum STP_ICCP_DBG_CNTR_MSG STP_ICCP_DBG_CNTR_MSG_e;

/* Count messages sent to MCLAG peer */
#define STP_SET_ICCP_TX_DBG_COUNTER(csm, tlv_type, status)\
do{\
    STP_ICCP_DBG_CNTR_MSG_e dbg_type;\
    dbg_type = stp_fsm_iccp_to_dbg_msg_type(tlv_type);\
    if (csm && ((dbg_type) < STP_ICCP_DBG_CNTR_MSG_MAX) && ((status) < STP_ICCP_DBG_CNTR_STS_MAX))\
        ++STP(csm).dbg_counters.iccp_counters[dbg_type][STP_ICCP_DBG_CNTR_DIR_TX][status];\
}while(0);

/* Count messages received from MCLAG peer */
#define STP_SET_ICCP_RX_DBG_COUNTER(csm, tlv_type, status)\
do{\
    STP_ICCP_DBG_CNTR_MSG_e dbg_type;\
    dbg_type = stp_fsm_iccp_to_dbg_msg_type(tlv_type);\
    if (csm && ((dbg_type) < STP_ICCP_DBG_CNTR_MSG_MAX) && ((status) < STP_ICCP_DBG_CNTR_STS_MAX))\
        ++STP(csm).dbg_counters.iccp_counters[dbg_type][STP_ICCP_DBG_CNTR_DIR_RX][status];\
}while(0);

typedef struct stp_dbg_counter_info
{
    uint64_t iccp_counters[STP_ICCP_DBG_CNTR_MSG_MAX][STP_ICCP_DBG_CNTR_DIR_MAX][STP_ICCP_DBG_CNTR_STS_MAX];
}stp_dbg_counter_info_t;

struct stp
{
    int id;
    int sync_req_num;

    STP_APP_STATE_E current_state;
    STP_SYNC_STATE_E sync_state;
    STP_ICCP_STATE_E csm_state;

    uint8_t wait_for_sync_data;
    uint8_t need_to_sync;
    uint8_t node_id;
    uint8_t system_id[ETHER_ADDR_LEN];
    uint16_t system_priority;
    uint8_t system_config_changed;

    const char* error_msg;
    TAILQ_HEAD(stp_msg_list, Msg) stp_msg_list;

    /* STP ICCP message tx/rx debug counters */
    stp_dbg_counter_info_t  dbg_counters;
};

void stp_init(struct CSM* csm, int all);
void stp_finalize(struct CSM* csm);
void stp_fsm_transit(struct CSM* csm);
void stp_enqueue_msg(struct CSM*, struct Msg*);
struct Msg* stp_dequeue_msg(struct CSM*);
char* stp_state(struct CSM* csm);

/* Debug counter API */
STP_ICCP_DBG_CNTR_MSG_e stp_fsm_iccp_to_dbg_msg_type(uint32_t tlv_type);

#endif /* _STP_HANDLER_H */
