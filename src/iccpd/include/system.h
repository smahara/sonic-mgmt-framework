/*
 * system.h
 *
 * Copyright(c) 2016-2019 Nephos/Estinet.
 *
 * This program is free software; you can redistribute it and/or modify it
 * under the terms and conditions of the GNU General Public License,
 * version 2, as published by the Free Software Foundation.
 *
 * This program is distributed in the hope it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
 * more details.
 *
 * You should have received a copy of the GNU General Public License along with
 * this program; if not, see <http://www.gnu.org/licenses/>.
 *
 * The full GNU General Public License is included in this distribution in
 * the file called "COPYING".
 *
 *  Maintainer: jianjun, grace Li from nephos
 */

#ifndef SYSTEM_H_
#define SYSTEM_H_

#include <err.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/select.h>

#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>

#include <sys/socket.h>

#include "../include/port.h"

#define FRONT_PANEL_PORT_PREFIX "Ethernet"
#define PORTCHANNEL_PREFIX      "PortChannel"
#define VLAN_PREFIX             "Vlan"
#define VXLAN_TUNNEL_PREFIX     "VTTNL"

#define WARM_REBOOT 1

#define MCLAG_ERROR -1

struct CSM;

#ifndef MAX_BUFSIZE
    #define MAX_BUFSIZE 4096
#endif

extern char mac_print_str[ETHER_ADDR_STR_LEN];

#define MAC_IN_MSG_LIST(head, elm, field)   \
    (((elm)->field.tqe_next != NULL) ||     \
    ((elm)->field.tqe_prev != NULL))

#define MAC_TAILQ_REMOVE(head, elm, field) do {  \
    TAILQ_REMOVE(head, elm, field);              \
    (elm)->field.tqe_next = NULL;                \
    (elm)->field.tqe_prev = NULL;                \
} while (/*CONSTCOND*/0)

#define MAC_RB_REMOVE(name, head, elm) do {  \
    RB_REMOVE(name, head, elm);              \
    (elm)->mac_entry_rb.rbt_parent = NULL;   \
    (elm)->mac_entry_rb.rbt_left = NULL;     \
    (elm)->mac_entry_rb.rbt_right = NULL;    \
} while (/*CONSTCOND*/0)


/* Debug counters */
/* Debug counters to track messages ICCPd sent to MclagSyncd */
typedef uint8_t SYNCD_DBG_CNTR_STS_e;
enum SYNCD_DBG_CNTR_STS_e
{
    SYNCD_DBG_CNTR_STS_OK  = 0,
    SYNCD_DBG_CNTR_STS_ERR = 1,    /* Send error or receive processing error*/
    SYNCD_DBG_CNTR_STS_MAX
};

typedef uint8_t SYNCD_TX_DBG_CNTR_MSG_e;
enum SYNCD_TX_DBG_CNTR_MSG_e
{
    SYNCD_TX_DBG_CNTR_MSG_PORT_ISOLATE               = 0,
    SYNCD_TX_DBG_CNTR_MSG_PORT_MAC_LEARN_MODE        = 1,
    SYNCD_TX_DBG_CNTR_MSG_FLUSH_FDB                  = 2,
    SYNCD_TX_DBG_CNTR_MSG_SET_IF_MAC                 = 3,
    SYNCD_TX_DBG_CNTR_MSG_SET_FDB                    = 4,
    SYNCD_TX_DBG_CNTR_MSG_SET_TRAFFIC_DIST_ENABLE    = 5,
    SYNCD_TX_DBG_CNTR_MSG_SET_TRAFFIC_DIST_DISABLE   = 6,
    SYNCD_TX_DBG_CNTR_MSG_SET_ICCP_STATE             = 7,
    SYNCD_TX_DBG_CNTR_MSG_SET_ICCP_ROLE              = 8,
    SYNCD_TX_DBG_CNTR_MSG_SET_ICCP_SYSTEM_ID         = 9,
    SYNCD_TX_DBG_CNTR_MSG_DEL_ICCP_INFO              = 10,
    SYNCD_TX_DBG_CNTR_MSG_SET_REMOTE_IF_STATE        = 11,
    SYNCD_TX_DBG_CNTR_MSG_DEL_REMOTE_IF_INFO         = 12,
    SYNCD_TX_DBG_CNTR_MSG_MAX
};

typedef uint8_t SYNCD_RX_DBG_CNTR_MSG_e;
enum SYNCD_RX_DBG_CNTR_MSG_e
{
    SYNCD_RX_DBG_CNTR_MSG_MAC = 0,
    SYNCD_RX_DBG_CNTR_MSG_CFG_MCLAG_DOMAIN = 1,
    SYNCD_RX_DBG_CNTR_MSG_CFG_MCLAG_IFACE  = 2,
    SYNCD_RX_DBG_CNTR_MSG_MAX
};

/* Count messages ICCP daemon sent to MclagSyncd */
#define SYSTEM_SET_SYNCD_TX_DBG_COUNTER(sys, syncd_msg_type, status)\
do{\
    SYNCD_TX_DBG_CNTR_MSG_e dbg_type;\
    dbg_type = system_syncdtx_to_dbg_msg_type(syncd_msg_type);\
    if (sys && ((dbg_type) < SYNCD_TX_DBG_CNTR_MSG_MAX) && ((status) < SYNCD_DBG_CNTR_STS_MAX))\
    {\
      ++sys->dbg_counters.syncd_tx_counters[dbg_type][status];\
    }\
}while(0);

/* Count messages ICCP daemon received from MclagSyncd */
#define SYSTEM_SET_SYNCD_RX_DBG_COUNTER(sys, syncd_msg_type, status)\
do{\
    SYNCD_RX_DBG_CNTR_MSG_e dbg_type;\
    dbg_type = system_syncdrx_to_dbg_msg_type(syncd_msg_type);\
    if (sys && ((dbg_type) < SYNCD_RX_DBG_CNTR_MSG_MAX) && ((status) < SYNCD_DBG_CNTR_STS_MAX))\
    {\
        ++sys->dbg_counters.syncd_rx_counters[dbg_type][status];\
    }\
}while(0);

#define SYSTEM_INCR_SESSION_DOWN_COUNTER(sys)\
    if (sys)\
        ++sys->dbg_counters.session_down_counter;\

#define SYSTEM_GET_SESSION_DOWN_COUNTER(sys)\
    sys->dbg_counters.session_down_counter

#define SYSTEM_INCR_PEER_LINK_DOWN_COUNTER(sys)\
    if (sys)\
        ++sys->dbg_counters.peer_link_down_counter;\

#define SYSTEM_INCR_WARMBOOT_COUNTER(sys)\
    if (sys)\
        ++sys->dbg_counters.warmboot_counter;

typedef struct system_dbg_counter_info
{
    uint32_t session_down_counter;    //not counting down due to warmboot
    uint32_t peer_link_down_counter;
    uint32_t warmboot_counter;
    uint64_t syncd_tx_counters[SYNCD_TX_DBG_CNTR_MSG_MAX][SYNCD_DBG_CNTR_STS_MAX];
    uint64_t syncd_rx_counters[SYNCD_RX_DBG_CNTR_MSG_MAX][SYNCD_DBG_CNTR_STS_MAX];
}system_dbg_counter_info_t;

struct System
{
    int server_fd;/* Peer-Link Socket*/
    int sync_fd;
    int sync_ctrl_fd;
    int arp_receive_fd;
    int ndisc_receive_fd;
    int epoll_fd;

    struct nl_sock * genric_sock;
    int genric_sock_seq;
    int family;
    struct nl_sock * route_sock;
    int route_sock_seq;
    struct nl_sock * genric_event_sock;
    struct nl_sock * route_event_sock;

    int sig_pipe_r;
    int sig_pipe_w;
    int warmboot_start;
    int warmboot_exit;

    /* Info List*/
    LIST_HEAD(csm_list, CSM) csm_list;
    LIST_HEAD(lif_all_list, LocalInterface) lif_list;
    LIST_HEAD(lif_purge_all_list, LocalInterface) lif_purge_list;

    /* Settings */
    char* log_file_path;
    char* cmd_file_path;
    char* config_file_path;
    char* mclagdctl_file_path;
    int pid_file_fd;
    int telnet_port;
    fd_set readfd; /*record socket need to listen*/
    int readfd_count;
    time_t csm_trans_time;
    int need_sync_team_again;
    int need_sync_netlink_again;

    /* ICCDd/MclagSyncd debug counters */
    system_dbg_counter_info_t dbg_counters;
};

struct CSM* system_create_csm();
struct CSM* system_get_csm_by_peer_ip(const char*);
struct CSM* system_get_csm_by_mlacp_id(int id);
struct System* system_get_instance();
void system_finalize();
void system_init(struct System*);
SYNCD_TX_DBG_CNTR_MSG_e system_syncdtx_to_dbg_msg_type(uint32_t msg_type);
SYNCD_RX_DBG_CNTR_MSG_e system_syncdrx_to_dbg_msg_type(uint32_t msg_type);

char *mac_addr_to_str(uint8_t mac_addr[ETHER_ADDR_LEN]);

#endif /* SYSTEM_H_ */
