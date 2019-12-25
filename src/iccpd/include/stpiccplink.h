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

#ifndef __STPICCPLINK__
#define __STPICCPLINK__

#include <arpa/inet.h>
#include <sys/socket.h>
#include <linux/netlink.h>
#include <linux/rtnetlink.h>
#include <../include/port.h>

//#define MAX_L_PORT_NAME 20
#define ETHER_ADDR_LEN 6
#define MESSAGE_TYPE_LEN 40
#define BRIDGE_ID_STR_LEN 20
#define BRIDGE_ID_DISPLAY_STR_LEN 20

typedef enum 
{
  STP_ICCP_OPER_STATUS_NONE = 0,
  STP_ICCP_OPER_STATUS_UP,
  STP_ICCP_OPER_STATUS_DOWN
} OPER_STATUS_t;

typedef enum 
{
  STP_ICCP_VLAN_TC_NONE = 0,
  STP_ICCP_VLAN_TC_TRUE,
  STP_ICCP_VLAN_TC_FALSE
} VLAN_TC_STATE_t;

typedef enum 
{
  STP_ICCP_VLAN_PORT_TC_NONE = 0,
  STP_ICCP_RCVD_TCN,
  STP_ICCP_DET_TC,
  STP_ICCP_DET_TC_1,
  STP_ICCP_SYNC_TC
} VLAN_PORT_TC_TYPE_t;

typedef enum 
{
  STP_ICCP_ROOT_PORT_NONE = 0,
  STP_ICCP_ROOT_PORT_REQUEST,
  STP_ICCP_ROOT_PORT_RESPONSE
} ROOT_PORT_REQUEST_t;

typedef enum 
{
  STP_ICCP_TX_CONFIG_NONE = 0,
  STP_ICCP_TX_CONFIG_ON,
  STP_ICCP_TX_CONFIG_OFF
} TX_CONFIG_STATE_t;

typedef enum 
{
  STP_ICCP_MASTER_NODE_REQUEST_NONE = 0,
  STP_ICCP_MASTER_NODE_REQUEST,
  STP_ICCP_MASTER_NODE_RESPONSE
} MASTER_NODE_REQUEST_t;

typedef enum 
{
  STP_ICCP_RPVST_PROPOSAL_NONE = 0,
  STP_ICCP_RPVST_PROPOSAL_REQUEST,
  STP_ICCP_RPVST_PROPOSAL_ACK
} RPVST_PROPOSAL_t;

typedef enum 
{
  STP_ICCP_SYNC_REQUEST_NONE = 0,
  STP_ICCP_SYNC_REQUEST_SYS_DATA,
  STP_ICCP_SYNC_REQUEST_INSTANCE,
  STP_ICCP_SYNC_REQUEST_SYS_DATA_INSTANCE
} SYNC_REQUEST_t;

typedef enum 
{
  STP_ICCP_SYNC_RESPONSE_NONE = 0,
  STP_ICCP_SYNC_RESPONSE_BEGIN,
  STP_ICCP_SYNC_RESPONSE_END
} SYNC_RESPONSE_t;

struct stpiccp_oper_vmac_info
{
    uint16_t mclag_id;
    OPER_STATUS_t oper_status; /* up or down */
    char system_mac[ETHER_ADDR_STR_LEN];
};

struct stpiccp_vlan_tc_info
{
    uint16_t vid;
    VLAN_TC_STATE_t state; /* true or false */
};

struct stpiccp_portchannel_portid_map_info
{
    uint32_t po_id;
    uint32_t internal_port_id;
};

struct stpiccp_tx_config_info
{
    uint16_t vid;
    uint32_t message_age;
    TX_CONFIG_STATE_t tx_on; /* on or off */
};

struct stpiccp_age_out_info
{
    uint16_t vid;
    char designated_bridge[BRIDGE_ID_STR_LEN];
};

struct stpiccp_synch_req_info
{
    uint16_t request_number;
    uint8_t c_bit;
    uint8_t s_bit;
    SYNC_REQUEST_t request_type; /* "sys_data" / "instance" / "sys_data and instance" */
};

struct stpiccp_synch_response_info
{
    uint16_t request_number;
    SYNC_RESPONSE_t status; /* "begin" or "end" */
};

struct stpiccp_common_info
{
    uint16_t vid;
    char port_name[IFNAMSIZ];

    VLAN_PORT_TC_TYPE_t vlan_port_tc_type; /* "TC Update Message" / "TC ACK Update Message" / "TCN Update Message" */

    char		root_bridge_id[BRIDGE_ID_STR_LEN];
    uint32_t	root_path_cost;
    char		desig_bridge_id[BRIDGE_ID_STR_LEN];
    uint16_t	desig_port;
	bool		nrpv_valid;
    uint32_t    port_id;
    uint32_t    port_path_cost;
    uint8_t     max_age;
    uint32_t    message_age;
    uint32_t    hello_time;
    uint32_t    fwd_delay;

    ROOT_PORT_REQUEST_t root_port_req_resp_field; /* request or response */
	uint32_t    seq_no;

    uint16_t    stp_port_id;//will be removed
    uint8_t		state;
    uint8_t		tc_ack;
    uint8_t		change_detection_enabled;
    uint8_t		self_loop;
    uint8_t		auto_config;
    uint8_t		oper_edge;
    uint32_t	desig_cost;

    MASTER_NODE_REQUEST_t master_node_req_resp_field; /* request or response */

    RPVST_PROPOSAL_t rpvst_req_proposal_ack_flag; /* request or ack */

    uint8_t message_type;
};


#endif
