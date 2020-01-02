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

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>
#include <arpa/inet.h>
#include <sys/queue.h>
#include <sys/epoll.h>
#include <unistd.h>
#include <linux/un.h>
#include <linux/if_arp.h>
#include <sys/ioctl.h>
#include "../include/system.h"
#include "../include/logger.h"
#include "../include/mlacp_tlv.h"

#include "../include/iccp_csm.h"
#include "mclagdctl/mclagdctl.h"
#include "../include/iccp_cmd_show.h"
#include "../include/iccp_cli.h"
#include "../include/iccp_cmd.h"
#include "../include/mlacp_link_handler.h"
#include "../include/iccp_netlink.h"
#include "../include/stp_handler.h"
#include "../include/stpiccplink.h"
#include "../include/stpiccp.h"
#include "../include/stp_tlv.h"

char g_stp_iccp_syncd_recv_buf[ICCP_STP_SYNCD_RECV_MSG_BUFFER_SIZE] = { 0 };
char bridge_id_print_str[BRIDGE_ID_DISPLAY_STR_LEN];

extern void stp_sync_receiver_handler(struct CSM* csm, struct Msg* msg);
extern void stpiccp_send_connect_to_syncd(struct System* sys, struct CSM *csm, OPER_STATUS_t status);

char *bridge_id_to_str(char bridge_id[BRIDGE_ID_STR_LEN])
{
  memset(bridge_id_print_str, 0, sizeof(bridge_id_print_str));
  snprintf(bridge_id_print_str, sizeof(bridge_id_print_str), 
      "%02x:%02x:%02x:%02x:%02x:%02x:%02x:%02x:%02x:%02x:%02x:%02x:%02x:%02x:%02x:%02x:%02x:%02x:%02x:%02x",
      bridge_id[0], bridge_id[1], bridge_id[2], bridge_id[3], bridge_id[4], bridge_id[5],
      bridge_id[6], bridge_id[7], bridge_id[8], bridge_id[9], bridge_id[10], bridge_id[11],
      bridge_id[12], bridge_id[13], bridge_id[14], bridge_id[15], bridge_id[16], bridge_id[17],
      bridge_id[18], bridge_id[19]);

  return bridge_id_print_str;
}

static int stpiccp_fill_icc_header(struct CSM* csm, ICCHdr* icc_hdr, size_t msg_len)
{
    if (csm == NULL || icc_hdr == NULL)
        return MCLAG_ERROR;

    /* ICC header */
    icc_hdr->ldp_hdr.u_bit = 0x0;
    icc_hdr->ldp_hdr.msg_type = htons(MSG_T_RG_APP_DATA);

    icc_hdr->ldp_hdr.msg_len = htons(msg_len - MSG_L_INCLUD_U_BIT_MSG_T_L_FIELDS);
    icc_hdr->ldp_hdr.msg_id = htonl(ICCP_MSG_ID);
    ICCP_MSG_ID++;
    iccp_csm_fill_icc_rg_id_tlv(csm, icc_hdr);

    return 0;
}

static int stp_iccp_csm_send(struct System *sys, char *msg_buf, size_t msg_len) 
{
  struct CSM* csm = NULL;
  ICCHdr *icc_hdr;
  ICCParameter *icc_param;

  LIST_FOREACH(csm, &(sys->csm_list), next)
  {
    icc_hdr = (ICCHdr *)msg_buf;
    icc_param = (ICCParameter*)&(msg_buf[sizeof(ICCHdr)]);
    stpiccp_fill_icc_header(csm, icc_hdr, msg_len);

    ICCPD_LOG_DEBUG(__FUNCTION__, "Send to peer iccp. len=[%d] msg_type=[%s (0x%X, 0x%X)]", msg_len, get_tlv_type_string(ntohs(icc_param->type)), ntohs(icc_param->type));
    iccp_csm_send(csm, msg_buf, msg_len);
   }

   return 0;
}

int stpiccp_send_stp_vlan_tc_info_to_peer(struct System *sys,  struct stpiccp_vlan_tc_info * stp_tc_info)
{
  size_t msg_len = sizeof(ICCHdr) + sizeof (stpTCInstancesTLV);
  stpTCInstancesTLV *data;

  memset (g_csm_buf, 0x00, CSM_BUFFER_SIZE);

  data = (stpTCInstancesTLV *)&g_csm_buf[sizeof(ICCHdr)];
  data->icc_parameter.u_bit = 0;
  data->icc_parameter.f_bit = 0;
  data->icc_parameter.type = htons(TLV_T_STP_TC_INSTANCES);
  data->icc_parameter.len = htons(sizeof(stpTCInstancesTLV) - sizeof(ICCParameter));

  data->instance_id = htons(stp_tc_info->vid);
  data->state = stp_tc_info->state;

  stp_iccp_csm_send(sys, g_csm_buf, msg_len);

  return 0;
}

int stpiccp_send_po_port_map_info_to_peer(struct System *sys,  struct stpiccp_portchannel_portid_map_info *info)
{
  size_t msg_len = sizeof(ICCHdr) + sizeof (stpPortChannelToPortIdMapTLV);
  stpPortChannelToPortIdMapTLV *data;

  memset (g_csm_buf, 0x00, CSM_BUFFER_SIZE);

  data = (stpPortChannelToPortIdMapTLV*)&g_csm_buf[sizeof(ICCHdr)];
  data->icc_parameter.u_bit = 0;
  data->icc_parameter.f_bit = 0;
  data->icc_parameter.type = htons(TLV_T_STP_PORTCHANNEL_PORTID_MAP);
  data->icc_parameter.len = htons(sizeof(stpPortChannelToPortIdMapTLV) - sizeof(ICCParameter));

  data->port_channel_id = htonl(info->po_id);
  data->port_id = htonl(info->internal_port_id);

  stp_iccp_csm_send(sys, g_csm_buf, msg_len);

  return 0;
}

int stpiccp_send_tx_config_info_to_peer(struct System *sys, struct stpiccp_tx_config_info *info)
{
  size_t msg_len = sizeof(ICCHdr) + sizeof (stpTxConfigTLV);
  stpTxConfigTLV *data;

  memset (g_csm_buf, 0x00, CSM_BUFFER_SIZE);

  data = (stpTxConfigTLV*)&g_csm_buf[sizeof(ICCHdr)];
  data->icc_parameter.u_bit = 0;
  data->icc_parameter.f_bit = 0;
  data->icc_parameter.type = htons(TLV_T_STP_TX_CNFIG);
  data->icc_parameter.len = htons(sizeof(stpTxConfigTLV) - sizeof(ICCParameter));

  data->vlan_id = htons(info->vid);
  data->message_age = htonl(info->message_age);
  data->tx_on = info->tx_on;

  stp_iccp_csm_send(sys, g_csm_buf, msg_len);

  return 0;
}

int stpiccp_send_age_out_info_to_peer(struct System *sys, struct stpiccp_age_out_info *info)
{
  size_t msg_len = sizeof(ICCHdr) + sizeof (stpAgeOutTLV);
  stpAgeOutTLV *data;

  memset (g_csm_buf, 0x00, CSM_BUFFER_SIZE);

  data = (stpAgeOutTLV *)&g_csm_buf[sizeof(ICCHdr)];
  data->icc_parameter.u_bit = 0;
  data->icc_parameter.f_bit = 0;
  data->icc_parameter.type = htons(TLV_T_STP_AGE_OUT);
  data->icc_parameter.len = htons(sizeof(stpAgeOutTLV) - sizeof(ICCParameter));

  data->vlan_id = htons(info->vid);
  strncpy(data->designated_bridge, info->designated_bridge, BRIDGE_ID_STR_LEN);

  stp_iccp_csm_send(sys, g_csm_buf, msg_len);

  return 0;
}

int stpiccp_send_common_info_to_peer(struct System *sys, struct stpiccp_common_info *info)
{
  size_t msg_len = sizeof(ICCHdr) + sizeof (stpCommonInfoTLV);
  stpCommonInfoTLV *data;

  memset (g_csm_buf, 0x00, CSM_BUFFER_SIZE);

  data = (stpCommonInfoTLV *)&g_csm_buf[sizeof(ICCHdr)];
  data->icc_parameter.u_bit = 0;
  data->icc_parameter.f_bit = 0;
  data->icc_parameter.type = htons(TLV_T_STP_COMMON_INFO);
  data->icc_parameter.len = htons(sizeof(stpCommonInfoTLV) - sizeof(ICCParameter));

  data->vlan_port_parameter.vlan_id = htons(info->vid);
  strncpy(data->vlan_port_parameter.port_name, info->port_name, IFNAMSIZ);

  data->tc_type = info->vlan_port_tc_type;

  strncpy(data->root_bridge_id, info->root_bridge_id, BRIDGE_ID_STR_LEN);
  data->root_path_cost = htonl(info->root_path_cost);
  strncpy(data->designated_bridge_id, info->desig_bridge_id, BRIDGE_ID_STR_LEN);
  data->designated_port = htons(info->desig_port);
  

  data->nrpv_valid = info->nrpv_valid;
  data->port_id = htonl(info->port_id);
  data->port_path_cost = htonl(info->port_path_cost);
  data->max_age = info->max_age;
  data->message_age = htonl(info->message_age);
  data->hello_time = htonl(info->hello_time);
  data->fwd_delay = htonl(info->fwd_delay);
  data->root_port_req_resp_field = info->root_port_req_resp_field;
  data->seq_no = htonl(info->seq_no);
  data->state= info->state;
  data->tc_ack = info->tc_ack;
  data->change_detection_enabled = info->change_detection_enabled;
  data->self_loop = info->self_loop;
  data->auto_config = info->auto_config;
  data->oper_edge = info->oper_edge;
  data->desig_cost = htonl(info->desig_cost);

  data->master_node_req_resp_field = info->master_node_req_resp_field;
  data->rpvst_req_proposal_ack_flag = info->rpvst_req_proposal_ack_flag;
  data->message_type = info->message_type;

  stp_iccp_csm_send(sys, g_csm_buf, msg_len);

  return 0;
}

int stpiccp_send_sync_req_to_peer(struct System *sys, struct stpiccp_synch_req_info *info)
{
  size_t msg_len = sizeof(ICCHdr) + sizeof (stpSyncReqTLV);
  stpSyncReqTLV *data;

  memset (g_csm_buf, 0x00, CSM_BUFFER_SIZE);

  data = (stpSyncReqTLV *)&g_csm_buf[sizeof(ICCHdr)];
  data->icc_parameter.u_bit = 0;
  data->icc_parameter.f_bit = 0;
  data->icc_parameter.type = htons(TLV_T_STP_SYNC_REQUEST);
  data->icc_parameter.len = htons(sizeof(stpSyncReqTLV) - sizeof(ICCParameter));

  ICCPD_LOG_DEBUG(__FUNCTION__, "Sync Request to peer - req_num %d, req_type %d, s_bit: %x c_bit %x",
      info->request_number, info->request_type, info->s_bit, info->c_bit);

  data->req_num = htons(info->request_number);
  data->req_type = htons(info->request_type);
  data->s_bit = info->s_bit;
  data->c_bit = info->c_bit;

  stp_iccp_csm_send(sys, g_csm_buf, msg_len);

  return 0;
}

int stpiccp_send_sync_data_to_peer(struct System *sys, struct stpiccp_synch_response_info *info)
{
  size_t msg_len = sizeof(ICCHdr) + sizeof (stpSyncDataTLV);
  stpSyncDataTLV *data;

  memset (g_csm_buf, 0x00, CSM_BUFFER_SIZE);

  data = (stpSyncDataTLV *)&g_csm_buf[sizeof(ICCHdr)];
  data->icc_parameter.u_bit = 0;
  data->icc_parameter.f_bit = 0;
  data->icc_parameter.type = htons(TLV_T_STP_SYNC_DATA);
  data->icc_parameter.len = htons(sizeof(stpSyncDataTLV) - sizeof(ICCParameter));

  data->req_num = htons(info->request_number);
  if (info->status == STP_ICCP_SYNC_RESPONSE_BEGIN)
    data->s_bit = 0;
  else if (info->status == STP_ICCP_SYNC_RESPONSE_END)
    data->s_bit = 1;
  else
  {
    ICCPD_LOG_ERR(__FUNCTION__, "Invalid Response State");
    return MCLAG_ERROR;
  }

  stp_iccp_csm_send(sys, g_csm_buf, msg_len);

  return 0;
}

/********************************************************************/
/* Recieve from STP-ICCP-Syncd APIs */
/********************************************************************/
int stpiccp_receive_stp_vlan_tc_info(struct System *sys, char *msg_buf)
{
    int count = 0;
    int i = 0;
    stpiccp_msg_hdr_t * msg_hdr;
    struct stpiccp_vlan_tc_info * stp_tc_info;

    msg_hdr = (stpiccp_msg_hdr_t*)msg_buf;

    count = (msg_hdr->msg_len - sizeof(stpiccp_msg_hdr_t))/sizeof(struct stpiccp_vlan_tc_info);
    ICCPD_LOG_DEBUG(__FUNCTION__, "recv msg stp_vlan_tc msg count %d",count );  

    for (i=0; i<count;i++)
    {
        stp_tc_info = (struct stpiccp_vlan_tc_info *)&msg_buf[sizeof(stpiccp_msg_hdr_t)+ i * sizeof(stp_tc_info)];
        ICCPD_LOG_DEBUG(__FUNCTION__, "stp_vlan_tc vlan_id %u tc_state: %u ", stp_tc_info->vid, stp_tc_info->state);  
        stpiccp_send_stp_vlan_tc_info_to_peer(sys, stp_tc_info);
    } 
    return 0;
}

int stpiccp_receive_stp_po_port_map_info(struct System *sys, char *msg_buf)
{
    int count = 0;
    int i = 0;
    stpiccp_msg_hdr_t * msg_hdr;
    struct stpiccp_portchannel_portid_map_info *info;

    msg_hdr = (stpiccp_msg_hdr_t*)msg_buf;

    count = (msg_hdr->msg_len - sizeof(stpiccp_msg_hdr_t))/sizeof(struct stpiccp_portchannel_portid_map_info);
    ICCPD_LOG_DEBUG(__FUNCTION__, "recv msg stpiccp_receive_stp_po_port_map_info msg count %d",count );  

    for (i=0; i<count;i++)
    {
        info = (struct stpiccp_portchannel_portid_map_info *)&msg_buf[sizeof(stpiccp_msg_hdr_t)+ i * sizeof(struct stpiccp_portchannel_portid_map_info)];
        ICCPD_LOG_DEBUG(__FUNCTION__, "stpiccp_receive_stp_po_port_map_info po_id %u internal_port_id: %u ", info->po_id, info->internal_port_id);  
        stpiccp_send_po_port_map_info_to_peer(sys, info);
    } 
    return 0;
}

int stpiccp_receive_stp_tx_config(struct System *sys, char *msg_buf)
{
    int count = 0;
    int i = 0;
    stpiccp_msg_hdr_t * msg_hdr;
    struct stpiccp_tx_config_info *info;

    msg_hdr = (stpiccp_msg_hdr_t*)msg_buf;

    count = (msg_hdr->msg_len - sizeof(stpiccp_msg_hdr_t))/sizeof(struct stpiccp_tx_config_info);
    ICCPD_LOG_DEBUG(__FUNCTION__, "recv msg stp_config_conifg msg count %d",count );  

    for (i=0; i<count;i++)
    {
        info = (struct stpiccp_tx_config_info*)&msg_buf[sizeof(stpiccp_msg_hdr_t)+ i * sizeof(struct stpiccp_tx_config_info)];
        ICCPD_LOG_DEBUG(__FUNCTION__, "TC Config to peer-- vlan_id %u message_age: %u ", info->vid, info->message_age);  
        stpiccp_send_tx_config_info_to_peer(sys, info);
    } 
    return 0;
}

int stpiccp_receive_stp_age_out(struct System *sys, char *msg_buf)
{
    int count = 0;
    int i = 0;
    stpiccp_msg_hdr_t * msg_hdr;
    struct stpiccp_age_out_info *info;

    msg_hdr = (stpiccp_msg_hdr_t*)msg_buf;

    count = (msg_hdr->msg_len - sizeof(stpiccp_msg_hdr_t))/sizeof(struct stpiccp_age_out_info);
    ICCPD_LOG_DEBUG(__FUNCTION__, "recv msg stp_age_out msg count %d",count );  

    for (i=0; i<count;i++)
    {
        info = (struct stpiccp_age_out_info *)&msg_buf[sizeof(stpiccp_msg_hdr_t)+ i * sizeof(struct stpiccp_age_out_info)];
        ICCPD_LOG_DEBUG(__FUNCTION__, "stp_age_out to peer -- vlan_id %u desig_bridge: %s ", info->vid, info->designated_bridge);  
        stpiccp_send_age_out_info_to_peer(sys, info);
    } 
    return 0;
}

int stpiccp_receive_stp_common_info(struct System *sys, char *msg_buf)
{
    int count = 0;
    int i = 0;
    stpiccp_msg_hdr_t * msg_hdr;
    struct stpiccp_common_info *info;

    msg_hdr = (stpiccp_msg_hdr_t*)msg_buf;

    count = (msg_hdr->msg_len - sizeof(stpiccp_msg_hdr_t))/sizeof(struct stpiccp_common_info);
    ICCPD_LOG_DEBUG(__FUNCTION__, "recv msg stp_common_info. msg count %d",count );

    for (i=0; i<count;i++)
    {
        info = (struct stpiccp_common_info *)&msg_buf[sizeof(stpiccp_msg_hdr_t)+ i * sizeof(struct stpiccp_common_info)];
        ICCPD_LOG_DEBUG(__FUNCTION__, "stp_common_info to peer (1)-- vlan_id %u port:%s tc_type:%d root_bridge %s root path cst %u desig bridge %s desig port %u root_port_req_resp: %d ", info->vid, info->port_name, info->vlan_port_tc_type, info->root_bridge_id, info->root_path_cost, info->desig_bridge_id, info->desig_port, info->root_port_req_resp_field);  
        ICCPD_LOG_DEBUG(__FUNCTION__, "stp_common_info to peer (2)-- state:%d tc_ack:%d change_detection_enabled:%d self_loop:%d auto_config:%d oper_edge:%d path_cost:%d desig_cost:%d forward_delay:%d ", info->state, info->tc_ack, info->change_detection_enabled, info->self_loop, info->auto_config, info->oper_edge, info->port_path_cost, info->desig_cost, info->fwd_delay);
        ICCPD_LOG_DEBUG(__FUNCTION__, "stp_common_info to peer (3)-- master_node_req_resp %d rpvst_req_prop_ack_flag %d message_type: %d", info->master_node_req_resp_field, info->rpvst_req_proposal_ack_flag, info->message_type);

        stpiccp_send_common_info_to_peer(sys, info);
    } 
    return 0;
}

int stpiccp_receive_stp_sync_request(struct System *sys, char *msg_buf)
{
    int count = 0;
    int i = 0;
    stpiccp_msg_hdr_t * msg_hdr;
    struct stpiccp_synch_req_info *info;

    msg_hdr = (stpiccp_msg_hdr_t*)msg_buf;

    count = (msg_hdr->msg_len - sizeof(stpiccp_msg_hdr_t))/sizeof(struct stpiccp_synch_req_info);
    ICCPD_LOG_DEBUG(__FUNCTION__, "recv msg stp_sync_req msg count %d",count );

    for (i=0; i<count;i++)
    {
        info = (struct stpiccp_synch_req_info *)&msg_buf[sizeof(stpiccp_msg_hdr_t)+ i * sizeof(struct stpiccp_synch_req_info)];
        ICCPD_LOG_DEBUG(__FUNCTION__, "stp_sync_req req_num: %d c_bit:%x s_bit: %x req_type:%d", info->request_number, info->c_bit, info->s_bit, info->request_type);

        stpiccp_send_sync_req_to_peer(sys, info);
    } 
    return 0;
}

int stpiccp_receive_stp_sync_response(struct System *sys, char *msg_buf)
{
    int count = 0;
    int i = 0;
    stpiccp_msg_hdr_t * msg_hdr;
    struct stpiccp_synch_response_info *info;

    msg_hdr = (stpiccp_msg_hdr_t*)msg_buf;

    count = (msg_hdr->msg_len - sizeof(stpiccp_msg_hdr_t))/sizeof(struct stpiccp_synch_response_info);
    ICCPD_LOG_DEBUG(__FUNCTION__, "recv msg stp_sync_request msg count %d",count );

    for (i=0; i<count;i++)
    {
        info = (struct stpiccp_synch_response_info *)&msg_buf[sizeof(stpiccp_msg_hdr_t)+ i * sizeof(struct stpiccp_synch_response_info)];
        ICCPD_LOG_DEBUG(__FUNCTION__, "stp_sync_resp req_num: %d status: %x", info->request_number, info->status);
        stpiccp_send_sync_data_to_peer(sys, info);
    } 
    return 0;
}

int stpiccp_receive_stp_connect_request(void)
{
  struct System* sys = NULL;
  size_t msg_len = sizeof(ICCHdr) + sizeof (AppConnectTLV);
  struct CSM* csm = NULL;
  ICCHdr *icc_hdr;
  AppConnectTLV *data;

  if ((sys = system_get_instance()) == NULL)
    return MCLAG_ERROR;

  LIST_FOREACH(csm, &(sys->csm_list), next)
  {
    ICCPD_LOG_DEBUG(__FUNCTION__, "process the stp connect_msg request from stp_iccp_syncd. Current CSM State: %d",  STP(csm).csm_state);  

    memset (g_csm_buf, 0x00, CSM_BUFFER_SIZE);

    icc_hdr = (ICCHdr *)g_csm_buf;
    stpiccp_fill_icc_header(csm, icc_hdr, msg_len);

    data = (AppConnectTLV *)&g_csm_buf[sizeof(ICCHdr)];
    data->icc_parameter.u_bit = 0;
    data->icc_parameter.f_bit = 0;
    data->icc_parameter.type = htons(TLV_T_STP_CONNECT);
    data->icc_parameter.len = htons(sizeof(AppConnectTLV) - sizeof(ICCParameter));

    data->protocol_version = htons(0x0001);

    if(STP(csm).csm_state == STP_CONNREC)
    {
      data->a_bit = 1;
    }
    else
    {
      STP(csm).csm_state = STP_CONNSENT;
      data->a_bit = 0;
    }

    stpiccp_send_connect_to_syncd(sys, csm, STP_ICCP_OPER_STATUS_UP);
    iccp_csm_send(csm, g_csm_buf, msg_len);
  }

  return 0;
}

int stpiccp_receive_stp_disconnect_request(void)
{
  struct System* sys = NULL;
  struct CSM* csm = NULL;
  ICCHdr *icc_hdr;
  size_t msg_len = sizeof(ICCHdr) + sizeof (AppDisconnectTLV);
  AppDisconnectTLV *data;

  if ((sys = system_get_instance()) == NULL)
    return MCLAG_ERROR;

  ICCPD_LOG_DEBUG(__FUNCTION__, "process the stp disconnect_msg request from stp_iccp_syncd");  

  data = (AppDisconnectTLV *)&g_csm_buf[sizeof(ICCHdr)];
  data->icc_parameter.u_bit = 0;
  data->icc_parameter.f_bit = 0;
  data->icc_parameter.type = htons(TLV_T_STP_DISCONNECT);
  /*TBD: Account for optional sub-TLVs length. Currently not sending cause*/
  data->icc_parameter.len = htons(sizeof(AppDisconnectTLV) - sizeof(ICCParameter));

  LIST_FOREACH(csm, &(sys->csm_list), next)
  {
    icc_hdr = (ICCHdr *)g_csm_buf;
    stpiccp_fill_icc_header(csm, icc_hdr, msg_len);

    stpiccp_send_connect_to_syncd(sys, csm, STP_ICCP_OPER_STATUS_DOWN);
    iccp_csm_send(csm, g_csm_buf, msg_len);
    STP(csm).csm_state = STP_NONEXISTENT;
  }

  return 0;
}

void stp_syncd_info_close()
{
    struct System* sys = NULL;

    if ((sys = system_get_instance()) == NULL)
    {
        ICCPD_LOG_ERR(__FUNCTION__, "Invalid system instance");
        return;
    }

    if (sys->stp_sync_fd > 0)
    {
        close(sys->stp_sync_fd);
        sys->stp_sync_fd = -1;
    }

    return;
}

int iccp_connect_stp_syncd()
{
    struct System* sys = NULL;
    int ret = 0;
    int fd = 0;
    struct sockaddr_in serv;
    static int count = 0;
    struct epoll_event event;

    if ((sys = system_get_instance()) == NULL)
    {
        ICCPD_LOG_ERR(__FUNCTION__, "Invalid system instance");
        goto conn_fail;
    }
    if (sys->stp_sync_fd > 0)
        return sys->stp_sync_fd;

    /*Print the fail log message every 60s*/
    if (count >= 5/*600*/)
    {
        count = 0;
    }

    fd = socket(AF_INET, SOCK_STREAM, 0);
    if (fd < 0)
    {
        if (count == 0)
            ICCPD_LOG_WARN(__FUNCTION__, "Failed to create unix socket: %s", strerror(errno));
        goto conn_fail;
    }

    /* Make server socket. */
    memset(&serv, 0, sizeof(serv));
    serv.sin_family = AF_INET;
    serv.sin_port = htons(2627);
#ifdef HAVE_STRUCT_SOCKADDR_IN_SIN_LEN
    serv.sin_len = sizeof(struct sockaddr_in);
#endif /* HAVE_STRUCT_SOCKADDR_IN_SIN_LEN */
    serv.sin_addr.s_addr = htonl(0x7f000006);

    ret = connect(fd, (struct sockaddr *)&serv, sizeof(serv));
    if (ret < 0)
    {
        if (count == 0)
            ICCPD_LOG_WARN(__FUNCTION__, "Failed to connect to stp syncd: errno str %s", strerror(errno));
        close(fd);
        goto conn_fail;
    }

    ICCPD_LOG_WARN(__FUNCTION__, "success to link stp-iccp-syncd. Fd: %u", fd);
    sys->stp_sync_fd = fd;

    event.data.fd = fd;
    event.events = EPOLLIN;
    ret = epoll_ctl(sys->epoll_fd, EPOLL_CTL_ADD, fd, &event);

    count = 0;
    return 0;

conn_fail:
    if (count == 0)
        ICCPD_LOG_DEBUG(__FUNCTION__, "%s:%d, stp syncd socket connect fail",
                        __FUNCTION__, __LINE__);

    count++;

    return MCLAG_ERROR;
}

/* Handle messages from stpiccpsyncd */
int iccp_stpiccpsyncd_msg_handler(struct System *sys)
{
    int num_bytes_rxed = 0;
    char *msg_buf = g_stp_iccp_syncd_recv_buf;
    stpiccp_msg_hdr_t *msg_hdr;
    int pos = 0;

    if (sys == NULL)
        return MCLAG_ERROR;
    memset(msg_buf, 0, CSM_BUFFER_SIZE);

    num_bytes_rxed = read(sys->stp_sync_fd, msg_buf, CSM_BUFFER_SIZE);

    if (num_bytes_rxed <= 0)
    {
        ICCPD_LOG_ERR(__FUNCTION__, "fd %d read error ret = %d  errno = %d ",sys->stp_sync_fd, num_bytes_rxed, errno);  
        return MCLAG_ERROR;
    }	

    while (pos < num_bytes_rxed) //iterate through all msgs
    {
        msg_hdr = (stpiccp_msg_hdr_t*)(&msg_buf[pos]);
        ICCPD_LOG_DEBUG(__FUNCTION__, "recv msg version %d type %d len %d pos:%d num_bytes_rxed:%d ",
                msg_hdr->version , msg_hdr->msg_type, msg_hdr->msg_len, pos, num_bytes_rxed);
        if (!msg_hdr->msg_len)
        {
            ICCPD_LOG_ERR(__FUNCTION__, "msg length zero!!!!! ");  
            return MCLAG_ERROR; 
        }
        if (msg_hdr->version != 1)
        {
            ICCPD_LOG_ERR(__FUNCTION__, "msg version %d wrong!!!!! ", msg_hdr->version);
            pos += msg_hdr->msg_len;
            continue;
        }

        if (msg_hdr->msg_type == STPICCP_SYNCD_MSG_TYPE_STP_VLAN_TC_OPERATION)
        {
          stpiccp_receive_stp_vlan_tc_info(sys, &msg_buf[pos]);
        }
        else if (msg_hdr->msg_type == STPICCP_SYNCD_MSG_TYPE_PORTCHANNEL_PORT_ID_MAP_OPERATION)
        {
          stpiccp_receive_stp_po_port_map_info(sys, &msg_buf[pos]);
        }
        else if (msg_hdr->msg_type == STPICCP_SYNCD_MSG_TYPE_TX_CONFIG_OPERATION)
        {
          stpiccp_receive_stp_tx_config(sys, &msg_buf[pos]);
        }
        else if (msg_hdr->msg_type == STPICCP_SYNCD_MSG_TYPE_AGE_OUT_OPERATION)
        {
          stpiccp_receive_stp_age_out(sys, &msg_buf[pos]);
        }
        else if (msg_hdr->msg_type == STPICCP_SYNCD_MSG_TYPE_COMMON_INFO_OPERATION)
        {
          stpiccp_receive_stp_common_info(sys, &msg_buf[pos]);
        }
        else if (msg_hdr->msg_type == STPICCP_SYNCD_MSG_TYPE_SYNC_REQ_OPERATION)
        {
          stpiccp_receive_stp_sync_request(sys, &msg_buf[pos]);
        }
        else if (msg_hdr->msg_type == STPICCP_SYNCD_MSG_TYPE_SYNC_RESPONSE_OPERATION)
        {
          stpiccp_receive_stp_sync_response(sys, &msg_buf[pos]);
        }
        else if (msg_hdr->msg_type == STPICCP_SYNCD_MSG_TYPE_STP_CONNECT_TLV_EXCHANGE_OPERATION)
        {
          stpiccp_receive_stp_connect_request();
        }
        else if (msg_hdr->msg_type == STPICCP_SYNCD_MSG_TYPE_STP_DISCONNECT_TLV_EXCHANGE_OPERATION)
        {
          stpiccp_receive_stp_disconnect_request();
        }
        else 
        {
            ICCPD_LOG_ERR(__FUNCTION__, "recv unknown msg type %d ", msg_hdr->msg_type);          
            pos += msg_hdr->msg_len;
            continue;
        }
        pos += msg_hdr->msg_len;
    }
    return 0;
}

