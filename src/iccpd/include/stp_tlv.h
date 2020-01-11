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

#ifndef STP_TLV_H_
#define STP_TLV_H_

#include "../include/msg_format.h"
#include "../include/iccp_csm.h"
#include "../include/stpiccplink.h"

/*
 * RFC 7727 STP System Config TLV
 */
struct stpSysConfigTLV
{
    ICCParameter icc_parameter;
    uint8_t ro_id[8];
    uint8_t mac_addr[ETHER_ADDR_LEN];
} __attribute__ ((packed));

typedef struct stpSysConfigTLV stpSysConfigTLV;
/*
 * RFC 7727 STP Topology Changed Instances
 */
struct stpTCInstancesTLV
{
  ICCParameter icc_parameter;
  uint16_t     instance_id;
  uint8_t      state;
} __attribute__ ((packed));

typedef struct stpTCInstancesTLV stpTCInstancesTLV;

/*
 * RFC 7727 STP CIST Root Time Parameters
 */
struct stpCistRootTimeParametersTLV
{
  ICCParameter icc_parameter;
  uint16_t     max_age;
  uint16_t     message_age;
  uint16_t     fwd_delay;
  uint16_t     hello_time;
  uint16_t     remaining_hops;
} __attribute__ ((packed));

typedef struct stpCistRootTimeParametersTLV stpCistRootTimeParametersTLV;

/*
 * RFC 7727 STP Synchronization Request TLV
 */
struct stpSyncReqTLV
{
  ICCParameter icc_parameter;
  uint16_t     req_num;

#if __BYTE_ORDER == __BIG_ENDIAN
  uint16_t     c_bit : 1;
  uint16_t     s_bit : 1;
  uint16_t     req_type : 14;
#elif __BYTE_ORDER == __LITTLE_ENDIAN
  uint16_t     req_type : 14;
  uint16_t     s_bit : 1;
  uint16_t     c_bit : 1;
#endif
  uint16_t     instance_id_list[0];  
} __attribute__ ((packed));

typedef struct stpSyncReqTLV  stpSyncReqTLV;

/*
 * RFC 7727 STP Synchronization Data TLV
 */
struct stpSyncDataTLV
{
  ICCParameter icc_parameter;
  uint16_t     req_num;
#if __BYTE_ORDER == __BIG_ENDIAN
  uint16_t     reserved: 15;
  uint16_t     s_bit : 1;
#elif __BYTE_ORDER == __LITTLE_ENDIAN
  uint16_t     s_bit : 1;
  uint16_t     reserved: 15;
#endif
} __attribute__ ((packed));

typedef struct stpSyncDataTLV stpSyncDataTLV;

/* STP_PORTCHANNEL_PORTID_MAP_TABLE */
struct stpPortChannelToPortIdMapTLV
{
  ICCParameter icc_parameter;
  uint32_t     port_channel_id;
  uint32_t     port_id;
} __attribute__ ((packed));

typedef struct stpPortChannelToPortIdMapTLV stpPortChannelToPortIdMapTLV;

struct VlanPortParameter
{
    uint16_t vlan_id;
    char     port_name[IFNAMSIZ];
} __attribute__ ((packed));

typedef struct VlanPortParameter VlanPortParameter;

struct stpTxConfigTLV
{
  ICCParameter icc_parameter;
  uint16_t     vlan_id;
  uint32_t     message_age;
  char         tx_on;
} __attribute__ ((packed));

typedef struct stpTxConfigTLV stpTxConfigTLV;

struct stpAgeOutTLV
{
  ICCParameter icc_parameter;
  uint16_t     vlan_id;
  char         designated_bridge[BRIDGE_ID_STR_LEN];
} __attribute__ ((packed));

typedef struct stpAgeOutTLV stpAgeOutTLV;

struct stpCommonInfoTLV
{
  ICCParameter icc_parameter;
  VlanPortParameter vlan_port_parameter;
 
  uint8_t      tc_type; 

  char         root_bridge_id[BRIDGE_ID_STR_LEN];
  uint32_t     root_path_cost;
  char         designated_bridge_id[BRIDGE_ID_STR_LEN];
  uint16_t     designated_port;

  uint8_t	   nrpv_valid;
  uint8_t	   peer_nrpv_valid;
  uint32_t     port_id;
  uint32_t     port_path_cost;
  uint8_t      max_age;
  uint32_t     message_age;
  uint32_t     hello_time;
  uint32_t     fwd_delay;
  uint8_t      root_port_req_resp_field;

  uint32_t     seq_no;
  uint8_t      state;
  uint8_t      tc_ack;
  uint8_t      change_detection_enabled;
  uint8_t      self_loop;
  uint8_t      auto_config;
  uint8_t      oper_edge;
  uint32_t     desig_cost;

  uint8_t      master_node_req_resp_field;

  uint8_t      rpvst_req_proposal_ack_flag;

  uint8_t      message_type;
} __attribute__ ((packed));

typedef struct stpCommonInfoTLV stpCommonInfoTLV;

#endif
