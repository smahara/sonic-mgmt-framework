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
#include <time.h>

#include <sys/queue.h>

#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#include <msg_format.h>
#include <system.h>
#include <logger.h>
#include <assert.h>
#include "../include/stp_tlv.h"
#include "../include/stpiccp.h"
#include "../include/stpiccplink.h"
#include "../include/system.h"
#include "../include/iccp_csm.h"

#include <signal.h>

/*****************************************
* Define
*
* ***************************************/
#define STP_MSG_QUEUE_REINIT(list) \
    { \
        struct Msg* msg = NULL; \
        while (!TAILQ_EMPTY(&(list))) { \
            msg = TAILQ_FIRST(&(list)); \
            TAILQ_REMOVE(&(list), msg, tail); \
            free(msg->buf); \
            free(msg); \
        } \
        TAILQ_INIT(&(list)); \
    }

/*****************************************
* Static Function
*
* ***************************************/
char *stp_state(struct CSM* csm);
/* Sync Sender APIs*/
static void stp_sync_send_sysConf(struct CSM* csm);
/* Sync Reciever APIs*/
static void stp_process_peer_tc_by_instance(struct CSM* csm, struct Msg* msg);
static void stp_process_peer_po_port_map(struct CSM* csm, struct Msg* msg);
static void stp_process_peer_tx_config(struct CSM* csm, struct Msg* msg);
static void stp_process_peer_age_out(struct CSM* csm, struct Msg* msg);
static void stp_process_peer_common_info(struct CSM* csm, struct Msg* msg);
static void stp_process_peer_sync_request(struct CSM* csm, struct Msg* msg);
static void stp_process_peer_sync_data(struct CSM* csm, struct Msg* msg);
/* Sync Handler*/
static void stp_sync_send_nak_handler(struct CSM* csm,  struct Msg* msg);
static void stp_sync_recv_nak_handler(struct CSM* csm,  struct Msg* msg);
static void stp_sync_sender_handler(struct CSM* csm);
void stp_sync_receiver_handler(struct CSM* csm, struct Msg* msg);
static void stp_sync_send_all_info_handler(struct CSM* csm);

/* Sync State Handler*/
static void stp_stage_sync_send_handler(struct CSM* csm, struct Msg* msg);
static void stp_stage_sync_request_handler(struct CSM* csm, struct Msg* msg);
static void stp_stage_handler(struct CSM* csm, struct Msg* msg);
static void stp_exchange_handler(struct CSM* csm, struct Msg* msg);

static void stp_sync_send_msg(struct System *sys, char *msg_buf, size_t msg_len)
{
  ssize_t  rc = 0;

  if (!sys || !msg_buf || msg_len == 0)
    return;

  if (sys->stp_sync_fd)
  {
    rc = write(sys->stp_sync_fd, msg_buf, msg_len);
    if ((rc <= 0) || (rc != msg_len))
    {
      ICCPD_LOG_ERR(__FUNCTION__, "Failed to write, rc %d", rc);
    }
  }

  ICCPD_LOG_DEBUG(__FUNCTION__, "notify stpiccpsyncd");

  return;
}

/******************************************************************
 * Sync Sender APIs -- TBD
 *
 *****************************************************************/
static void stp_sync_send_sysConf(struct CSM* csm)
{
    int msg_len = 0;

    memset(g_csm_buf, 0, CSM_BUFFER_SIZE);
    //msg_len = stp_prepare_for_sys_config(csm, g_csm_buf, CSM_BUFFER_SIZE);
    if (msg_len > 0)
        iccp_csm_send(csm, g_csm_buf, msg_len);
    else
        ICCPD_LOG_WARN("stp_fsm", "    Invalid sysconf packet.");

    /*ICCPD_LOG_DEBUG("stp_fsm", "  [SYNC_Send] SysConf, len=[%d]", msg_len);*/

    return;
}

/******************************************************************
 * Connect/Disconnect APIs
 *
 *****************************************************************/
/* Function to send a Connection ready message to stpiccpsyncd */
void stpiccp_send_connect_to_syncd(struct System* sys, struct CSM *csm, OPER_STATUS_t status)
{
    stpiccp_msg_hdr_t *msg_hdr;
    struct stpiccp_oper_vmac_info *stp_oper_info = NULL;
    char msg_buf[512];

    memset(msg_buf, 0, 512);

    if (!csm)
    {
      ICCPD_LOG_ERR(__FUNCTION__, "Invalid Input. No CSM");
      return;
    }

    msg_hdr = (stpiccp_msg_hdr_t *)msg_buf;
    msg_hdr->version = STPICCP_PROTO_VERSION;
    msg_hdr->msg_type = STPICCP_MSG_TYPE_OPER_STATE_SET;
    msg_hdr->msg_len = sizeof(stpiccp_msg_hdr_t) + sizeof(struct stpiccp_oper_vmac_info);

    stp_oper_info = (struct stpiccp_oper_vmac_info *)&msg_buf[sizeof(stpiccp_msg_hdr_t)];

    stp_oper_info->mclag_id =  csm->mlag_id;
    stp_oper_info->oper_status =  status;
    if ((status == STP_ICCP_OPER_STATUS_UP) && (csm->role_type == STP_ROLE_STANDBY))
    {
      snprintf(stp_oper_info->system_mac, ETHER_ADDR_STR_LEN, "%02x:%02x:%02x:%02x:%02x:%02x",
        MLACP(csm).remote_system.system_id[0],MLACP(csm).remote_system.system_id[1],
        MLACP(csm).remote_system.system_id[2],MLACP(csm).remote_system.system_id[3],
        MLACP(csm).remote_system.system_id[4],MLACP(csm).remote_system.system_id[5]);
    }
    else
    {
      snprintf(stp_oper_info->system_mac, ETHER_ADDR_STR_LEN, "%02x:%02x:%02x:%02x:%02x:%02x",
        MLACP(csm).system_id[0], MLACP(csm).system_id[1], MLACP(csm).system_id[2], 
        MLACP(csm).system_id[3], MLACP(csm).system_id[4], MLACP(csm).system_id[5]);
    }

    ICCPD_LOG_DEBUG(__FUNCTION__,"Send STPICCP_MSG_TYPE_OPER_STATE_SET msg to stpiccpsyncd. ");
    stp_sync_send_msg(sys, msg_buf, msg_hdr->msg_len);

    STP(csm).csm_state = STP_OPERATIONAL;

    return;
}

static void stp_process_peer_connect(struct CSM* csm, struct Msg* msg)
{
    struct System *sys;
    ssize_t rc;
    AppConnectTLV *data;
    data = (AppConnectTLV *)&(msg->buf[sizeof(ICCHdr)]);

    ICCPD_LOG_DEBUG(__FUNCTION__,"Process Connect TLV (type: %u, len: %u, protocol version: %x)",
           data->icc_parameter.type, data->icc_parameter.len, data->protocol_version);

    sys = system_get_instance();
    if (sys == NULL)
    {
        ICCPD_LOG_ERR(__FUNCTION__, "Invalid system instance");
        return;
    }

    if (STP(csm).csm_state == STP_CONNSENT)
    {
      STP(csm).csm_state = STP_CONNECTING;
    }
    else
    {
      STP(csm).csm_state = STP_CONNREC;
    }

    stpiccp_send_connect_to_syncd(sys, csm, STP_ICCP_OPER_STATUS_UP);

    return;
}

static void stp_process_peer_disconnect(struct CSM* csm, struct Msg* msg)
{
    stpiccp_msg_hdr_t *msg_hdr;
    struct stpiccp_oper_vmac_info *stp_oper_info = NULL;
    char msg_buf[512];
    struct System *sys;

    sys = system_get_instance();
    if (sys == NULL)
    {
        ICCPD_LOG_ERR(__FUNCTION__, "Invalid system instance");
        return;
    }

    if (STP(csm).csm_state == STP_OPERATIONAL)
    {
      memset(msg_buf, 0, 512);
      msg_hdr = (stpiccp_msg_hdr_t *)msg_buf;
      msg_hdr->version = STPICCP_PROTO_VERSION;
      msg_hdr->msg_type = STPICCP_MSG_TYPE_OPER_STATE_SET;
      msg_hdr->msg_len = sizeof(stpiccp_msg_hdr_t) + sizeof(struct stpiccp_oper_vmac_info);

      stp_oper_info = (struct stpiccp_oper_vmac_info *)&msg_buf[sizeof(stpiccp_msg_hdr_t)];

      stp_oper_info->mclag_id =  csm->mlag_id;
      stp_oper_info->oper_status =  STP_ICCP_OPER_STATUS_DOWN;

      stp_sync_send_msg(sys, msg_buf, msg_hdr->msg_len);
      STP(csm).csm_state = STP_CONNSENT;
    }

    return;
}

static void stp_process_peer_tc_by_instance(struct CSM* csm, struct Msg* msg)
{
    stpiccp_msg_hdr_t *msg_hdr;
    struct stpiccp_vlan_tc_info *info = NULL;
    char msg_buf[512];
    struct System *sys;
    stpTCInstancesTLV *data;

    data = (stpTCInstancesTLV *)&(msg->buf[sizeof(ICCHdr)]);

    ICCPD_LOG_DEBUG(__FUNCTION__,"Process TLV_T_STP_TC_INSTANCES (type: %u, len: %u)",
           data->icc_parameter.type, data->icc_parameter.len);

    sys = system_get_instance();
    if (sys == NULL)
    {
        ICCPD_LOG_ERR(__FUNCTION__, "Invalid system instance");
        return;
    }

    if (STP(csm).csm_state != STP_OPERATIONAL)
    {
        ICCPD_LOG_NOTICE("STP_FSM", "Receive message TLV_T_STP_TC_INSTANCES from peer when STP_ICCP is not operational");
        return;
    }

    memset(msg_buf, 0, 512);
    msg_hdr = (stpiccp_msg_hdr_t *)msg_buf;
    msg_hdr->version = STPICCP_PROTO_VERSION;
    msg_hdr->msg_type = STPICCP_MSG_TYPE_STP_VLAN_TC_SET;
    msg_hdr->msg_len = sizeof(stpiccp_msg_hdr_t) + sizeof(struct stpiccp_vlan_tc_info);
   
    info = (struct stpiccp_vlan_tc_info *)&msg_buf[sizeof(stpiccp_msg_hdr_t)];
    info->vid = ntohs(data->instance_id);
    info->state = data->state;

    ICCPD_LOG_DEBUG(__FUNCTION__, "VLAN TC info from peer - vlan_id %u tc_state: %u ", info->vid, info->state);  
    stp_sync_send_msg(sys, msg_buf, msg_hdr->msg_len);
    ICCPD_LOG_DEBUG(__FUNCTION__,"Fwd'ed TC for Vlan %d", info->vid);

    return;
}

static void stp_process_peer_po_port_map(struct CSM* csm, struct Msg* msg)
{
    stpiccp_msg_hdr_t *msg_hdr;
    struct stpiccp_portchannel_portid_map_info *info = NULL;
    char msg_buf[512];
    struct System *sys;
    stpPortChannelToPortIdMapTLV *data = NULL;

    sys = system_get_instance();
    if (sys == NULL)
    {
        ICCPD_LOG_ERR(__FUNCTION__, "Invalid system instance");
        return;
    }

    data = (stpPortChannelToPortIdMapTLV *)&(msg->buf[sizeof(ICCHdr)]);

    ICCPD_LOG_DEBUG(__FUNCTION__,"Process TLV_T_STP_PORTCHANNEL_PORTID_MAP(type: %u, len: %u) [po id: %u port: %u]",
           data->icc_parameter.type, data->icc_parameter.len, data->port_channel_id, data->port_id);

    if (STP(csm).csm_state != STP_OPERATIONAL)
    {
        ICCPD_LOG_NOTICE("STP_FSM", "Receive message TLV_T_STP_PORTCHANNEL_PORTID_MAP from peer when STP_ICCP is not operational");
        return;
    }

    memset(msg_buf, 0, 512);
    msg_hdr = (stpiccp_msg_hdr_t *)msg_buf;
    msg_hdr->version = STPICCP_PROTO_VERSION;
    msg_hdr->msg_type = STPICCP_MSG_TYPE_PORTCHANNEL_PORT_ID_MAP_SET;
    msg_hdr->msg_len = sizeof(stpiccp_msg_hdr_t) + sizeof(struct stpiccp_portchannel_portid_map_info);

    info = (struct stpiccp_portchannel_portid_map_info *)&msg_buf[sizeof(stpiccp_msg_hdr_t)];
    info->po_id = ntohl(data->port_channel_id);
    info->internal_port_id = ntohl(data->port_id);

    ICCPD_LOG_DEBUG(__FUNCTION__, "Po-PortId mapping info from peer - po_id %u internal_port_id: %u ", info->po_id, info->internal_port_id);  
    stp_sync_send_msg(sys, msg_buf, msg_hdr->msg_len);
    ICCPD_LOG_DEBUG(__FUNCTION__,"Fwd'ed PO:Port pair %u:%u to sync", info->po_id, 
        info->internal_port_id);

    return;
}

static void stp_process_peer_tx_config(struct CSM* csm, struct Msg* msg)
{
    stpiccp_msg_hdr_t *msg_hdr;
    struct stpiccp_tx_config_info *info;
    char msg_buf[512];
    struct System *sys;
    stpTxConfigTLV *data;

    sys = system_get_instance();
    if (sys == NULL)
    {
        ICCPD_LOG_ERR(__FUNCTION__, "Invalid system instance");
        return;
    }

    if (STP(csm).csm_state != STP_OPERATIONAL)
    {
        ICCPD_LOG_NOTICE("STP_FSM", "Receive message TLV_T_STP_TX_CNFIG from peer when STP_ICCP is not operational");
        return;
    }

    data = (stpTxConfigTLV *)&(msg->buf[sizeof(ICCHdr)]);

    memset(msg_buf, 0, 512);
    msg_hdr = (stpiccp_msg_hdr_t *)msg_buf;
    msg_hdr->version = STPICCP_PROTO_VERSION;
    msg_hdr->msg_type = STPICCP_MSG_TYPE_TX_CONFIG_SET;
    msg_hdr->msg_len = sizeof(stpiccp_msg_hdr_t) + sizeof(struct stpiccp_tx_config_info);

    info = (struct stpiccp_tx_config_info *)&msg_buf[sizeof(stpiccp_msg_hdr_t)];
    info->vid = ntohs(data->vlan_id);
    info->message_age = ntohl(data->message_age);
    info->tx_on = data->tx_on;

    ICCPD_LOG_DEBUG(__FUNCTION__, "TC Config from peer -- vlan_id %u message_age: %u ", info->vid, info->message_age);  

    stp_sync_send_msg(sys, msg_buf, msg_hdr->msg_len);
    ICCPD_LOG_DEBUG(__FUNCTION__,"Fwd'ed TX config to sync");

    return;
}

static void stp_process_peer_age_out(struct CSM* csm, struct Msg* msg)
{
    stpiccp_msg_hdr_t *msg_hdr;
    struct stpiccp_age_out_info *info;
    char msg_buf[512];
    struct System *sys;
    stpAgeOutTLV *data;

    sys = system_get_instance();
    if (sys == NULL)
    {
        ICCPD_LOG_ERR(__FUNCTION__, "Invalid system instance");
        return;
    }

    if (STP(csm).csm_state != STP_OPERATIONAL)
    {
        ICCPD_LOG_NOTICE("STP_FSM", "Receive message TLV_T_STP_AGE_OUT from peer when STP_ICCP is not operational");
        return;
    }

    data = (stpAgeOutTLV *)&(msg->buf[sizeof(ICCHdr)]);

    memset(msg_buf, 0, 512);
    msg_hdr = (stpiccp_msg_hdr_t *)msg_buf;
    msg_hdr->version = STPICCP_PROTO_VERSION;
    msg_hdr->msg_type = STPICCP_MSG_TYPE_AGE_OUT_SET;
    msg_hdr->msg_len = sizeof(stpiccp_msg_hdr_t) + sizeof(struct stpiccp_age_out_info);

    info = (struct stpiccp_age_out_info *)&msg_buf[sizeof(stpiccp_msg_hdr_t)];
    info->vid = ntohs(data->vlan_id);
    strncpy(info->designated_bridge, data->designated_bridge, BRIDGE_ID_STR_LEN);

    ICCPD_LOG_DEBUG(__FUNCTION__, "stp_age_out from  peer -- vlan_id %u desig_bridge: %s ", info->vid, info->designated_bridge);  

    stp_sync_send_msg(sys, msg_buf, msg_hdr->msg_len);
    ICCPD_LOG_DEBUG(__FUNCTION__,"Fwd'ed Age out message to Sync");

    return;
}

static void stp_process_peer_common_info(struct CSM* csm, struct Msg* msg)
{
    stpiccp_msg_hdr_t *msg_hdr;
    struct stpiccp_common_info *info;
    char msg_buf[512];
    struct System *sys;
    stpCommonInfoTLV *data;

    sys = system_get_instance();
    if (sys == NULL)
    {
        ICCPD_LOG_ERR(__FUNCTION__, "Invalid system instance");
        return;
    }

    if (STP(csm).csm_state != STP_OPERATIONAL)
    {
        ICCPD_LOG_NOTICE("STP_FSM", "Receive message TLV_T_STP_COMMON_INFO from peer when STP_ICCP is not operational");
        return;
    }

    data = (stpCommonInfoTLV*)&(msg->buf[sizeof(ICCHdr)]);

    memset(msg_buf, 0, 512);
    msg_hdr = (stpiccp_msg_hdr_t *)msg_buf;
    msg_hdr->version = STPICCP_PROTO_VERSION;
    msg_hdr->msg_type = STPICCP_MSG_TYPE_COMMON_INFO_SET;
    msg_hdr->msg_len = sizeof(stpiccp_msg_hdr_t) + sizeof(struct stpiccp_common_info);

    info = (struct stpiccp_common_info *)&msg_buf[sizeof(stpiccp_msg_hdr_t)];
    info->vid = ntohs(data->vlan_port_parameter.vlan_id);
    strncpy(info->port_name, data->vlan_port_parameter.port_name, IFNAMSIZ);

    info->vlan_port_tc_type = data->tc_type;

    strncpy(info->root_bridge_id, data->root_bridge_id, BRIDGE_ID_STR_LEN);
    info->root_path_cost = ntohl(data->root_path_cost);
    strncpy(info->desig_bridge_id, data->designated_bridge_id, BRIDGE_ID_STR_LEN);
    info->desig_port = ntohs(data->designated_port);

    info->nrpv_valid = data->nrpv_valid;
    info->peer_nrpv_valid = data->peer_nrpv_valid;
    info->port_id = ntohl(data->port_id);
    info->port_path_cost = ntohl(data->port_path_cost);
    info->max_age = data->max_age;
    info->message_age = ntohl(data->message_age);
    info->hello_time = ntohl(data->hello_time);
    info->fwd_delay = ntohl(data->fwd_delay);

    info->root_port_req_resp_field = data->root_port_req_resp_field;

    info->seq_no = ntohl(data->seq_no);
    info->state = data->state;
    info->tc_ack = data->tc_ack;
    info->change_detection_enabled = data->change_detection_enabled;
    info->self_loop = data->self_loop;
    info->auto_config = data->auto_config;
    info->oper_edge = data->oper_edge;
    info->desig_cost = ntohl(data->desig_cost);

    info->master_node_req_resp_field = data->master_node_req_resp_field;
    info->rpvst_req_proposal_ack_flag = data->rpvst_req_proposal_ack_flag;

    info->message_type =  data->message_type;

    ICCPD_LOG_DEBUG(__FUNCTION__, "stp_common_info from peer (1)-- vlan_id %u port:%s tc_type:%d root_bridge %s root path cst %u desig bridge %s desig port %u root_port_req_resp: %d ", info->vid, info->port_name, info->vlan_port_tc_type, info->root_bridge_id, info->root_path_cost, info->desig_bridge_id, info->desig_port, info->root_port_req_resp_field);  
    ICCPD_LOG_DEBUG(__FUNCTION__, "stp_common_info from peer (2)-- nrpv:%d peer_nrpv:%d port_id:%d path_cost:%d max_age:%d msg_age:%d hello:%d fwd_del:%d ", info->nrpv_valid, info->peer_nrpv_valid, info->port_id, info->port_path_cost, info->max_age, info->message_age, info->hello_time, info->fwd_delay);
    ICCPD_LOG_DEBUG(__FUNCTION__, "stp_common_info from peer (3)-- state:%d tc_ack:%d change_detection_enabled:%d self_loop:%d auto_config:%d oper_edge:%d desig_cost:%d ", info->state, info->tc_ack, info->change_detection_enabled, info->self_loop, info->auto_config, info->oper_edge, info->desig_cost);
    ICCPD_LOG_DEBUG(__FUNCTION__, "stp_common_info from peer (4)-- master_node_req_resp %d rpvst_req_prop_ack_flag %d message_type: %u", info->master_node_req_resp_field, info->rpvst_req_proposal_ack_flag, info->message_type);

    stp_sync_send_msg(sys, msg_buf, msg_hdr->msg_len);
    ICCPD_LOG_DEBUG(__FUNCTION__,"Fwd'ed Common Info to Sync");

    return;
}

static void stp_process_peer_sync_request(struct CSM* csm, struct Msg* msg)
{
    stpiccp_msg_hdr_t *msg_hdr;
    struct stpiccp_synch_req_info *info;
    char msg_buf[512];
    struct System *sys;
    stpSyncReqTLV *data;

    sys = system_get_instance();
    if (sys == NULL)
    {
        ICCPD_LOG_ERR(__FUNCTION__, "Invalid system instance");
        return;
    }

    if (STP(csm).csm_state != STP_OPERATIONAL)
    {
        ICCPD_LOG_NOTICE("STP_FSM", "Receive message TLV_T_STP_SYNC_REQUEST from peer when STP_ICCP is not operational");
        return;
    }

    data = (stpSyncReqTLV *)&(msg->buf[sizeof(ICCHdr)]);

    memset(msg_buf, 0, 512);
    msg_hdr = (stpiccp_msg_hdr_t *)msg_buf;
    msg_hdr->version = STPICCP_PROTO_VERSION;
    msg_hdr->msg_type = STPICCP_MSG_TYPE_SYNC_REQ_SET;
    msg_hdr->msg_len = sizeof(stpiccp_msg_hdr_t) + sizeof(struct stpiccp_synch_req_info);

    info = (struct stpiccp_synch_req_info *)&msg_buf[sizeof(stpiccp_msg_hdr_t)];
    info->request_number = ntohs(data->req_num);
    info->request_type = htons(data->req_type);
    info->s_bit = data->s_bit;
    info->c_bit = data->c_bit;

  ICCPD_LOG_DEBUG(__FUNCTION__, "Sync Request from peer - req_num %d, req_type %d, s_bit: %x c_bit %x",
      info->request_number, info->request_type, info->s_bit, info->c_bit);

    stp_sync_send_msg(sys, msg_buf, msg_hdr->msg_len);
    ICCPD_LOG_DEBUG(__FUNCTION__,"Fwd'ed Sync Request Info to Sync");

    return;
}

static void stp_process_peer_sync_data(struct CSM* csm, struct Msg* msg)
{
    stpiccp_msg_hdr_t *msg_hdr;
    struct stpiccp_synch_response_info *info;
    char msg_buf[512];
    struct System *sys;
    stpSyncDataTLV *data;

    sys = system_get_instance();
    if (sys == NULL)
    {
        ICCPD_LOG_ERR(__FUNCTION__, "Invalid system instance");
        return;
    }

    if (STP(csm).csm_state != STP_OPERATIONAL)
    {
        ICCPD_LOG_NOTICE("STP_FSM", "Receive message TLV_T_STP_SYNC_DATA from peer when STP_ICCP is not operational");
        return;
    }

    data = (stpSyncDataTLV *)&(msg->buf[sizeof(ICCHdr)]);

    ICCPD_LOG_NOTICE(__FUNCTION__, "Received Sync Data from peer. Request number: %d, s_bit: %u", ntohs(data->req_num), data->s_bit);

    memset(msg_buf, 0, 512);
    msg_hdr = (stpiccp_msg_hdr_t *)msg_buf;
    msg_hdr->version = STPICCP_PROTO_VERSION;
    msg_hdr->msg_type = STPICCP_MSG_TYPE_SYNC_RESPONSE_SET;
    msg_hdr->msg_len = sizeof(stpiccp_msg_hdr_t) + sizeof(struct stpiccp_synch_response_info);

    info = (struct stpiccp_synch_response_info*)&msg_buf[sizeof(stpiccp_msg_hdr_t)];
    info->request_number = ntohs(data->req_num);
    if (data->s_bit == 0)
      info->status = STP_ICCP_SYNC_RESPONSE_BEGIN;
    else if (data->s_bit == 1)
      info->status = STP_ICCP_SYNC_RESPONSE_END;

    stp_sync_send_msg(sys, msg_buf, msg_hdr->msg_len);
    ICCPD_LOG_DEBUG(__FUNCTION__,"Fwd'ed Sync Response Info to Sync");
    return;
}


/*****************************************
* STP Init
*
* ***************************************/
void stp_init(struct CSM* csm, int all)
{
    if (csm == NULL)
        return;

    STP(csm).sync_req_num = -1;
    STP(csm).need_to_sync = 0;
    STP(csm).error_msg = NULL;

    STP(csm).current_state = STP_STATE_INIT;
    STP(csm).csm_state = STP_NONEXISTENT;

    STP_MSG_QUEUE_REINIT(STP(csm).stp_msg_list);

    if (all != 0)
    {
      /*Does STP have an action here?*/
    }

    return;
}

/*****************************************
* STP finalize
*
* ***************************************/
void stp_finalize(struct CSM* csm)
{
    if (csm == NULL)
        return;

    /* msg destroy*/
    STP_MSG_QUEUE_REINIT(STP(csm).stp_msg_list);
    return;
}

/*****************************************
* STP FSM Transit
*
* ***************************************/
void stp_fsm_transit(struct CSM* csm)
{
    struct System* sys = NULL;
    struct Msg* msg = NULL;
    static STP_APP_STATE_E prev_state = STP_SYNC_SYSCONF;
    ICCHdr* icc_hdr = NULL;
    ICCParameter* icc_param = NULL;
    int have_msg = 1;

    if (csm == NULL)
        return;
    if ((sys = system_get_instance()) == NULL)
        return;

    /* torn down event */
    if (csm->sock_fd <= 0 || csm->app_csm.current_state != APP_OPERATIONAL)
    {
        /* drop all legacy stp msg*/
        if (STP(csm).current_state != STP_STATE_INIT)
        {
            STP_MSG_QUEUE_REINIT(STP(csm).stp_msg_list);
            STP(csm).current_state = STP_STATE_INIT;
        }
        return;
    }

    /* Dequeue msg if any*/
    while (have_msg)
    {
        if (STP(csm).current_state != STP_STATE_INIT)
        {
            /* Handler NAK First*/
            msg = stp_dequeue_msg(csm);
            if (msg != NULL)
            {
                have_msg = 1;
                icc_hdr = (ICCHdr*)msg->buf;
                icc_param = (ICCParameter*)&msg->buf[sizeof(ICCHdr)];
                ICCPD_LOG_DEBUG("stp_fsm", "  Message Type = %X, TLV=%s, Len=%d", icc_hdr->ldp_hdr.msg_type, get_tlv_type_string(icc_param->type), msg->len);

                if (icc_hdr->ldp_hdr.msg_type == MSG_T_NOTIFICATION && icc_param->type == TLV_T_NAK)
                {
                    stp_sync_recv_nak_handler(csm, msg);
                    free(msg->buf);
                    free(msg);
                    continue;
                }
            }
            else
            {
                have_msg = 0;
            }
        }

        if (prev_state != STP(csm).current_state)
        {
            prev_state = STP(csm).current_state;
        }

        /* Sync State */
        if (STP(csm).current_state == STP_STATE_INIT)
        {
            STP(csm).wait_for_sync_data = 0;
            STP(csm).current_state = STP_STATE_EXCHANGE;
        }

        switch (STP(csm).current_state)
        {
            case STP_STATE_INIT:
            case STP_STATE_ERROR:
                /* should not be here*/
                break;

            case STP_STATE_STAGE1:
            case STP_STATE_STAGE2:
                //stp_stage_handler(csm, msg);
                STP(csm).current_state = STP_STATE_EXCHANGE;
                break;

            case STP_STATE_EXCHANGE:
                stp_sync_receiver_handler(csm, msg);
                //stp_exchange_handler(csm, msg);
                break;
        }

        /*ICCPD_LOG_DEBUG("stp_fsm", "  Next State = %s", stp_state(csm));*/
        if (msg)
        {
            free(msg->buf);
            free(msg);
        }
    }
}

/* Helper function for dumping application state machine */
char* stp_state(struct CSM* csm)
{
    if (csm == NULL )
        return "STP_NULL";

    switch (STP(csm).current_state)
    {
        case STP_STATE_INIT:
            return "STP_STATE_INIT";

        case STP_STATE_STAGE1:
            return "STP_STATE_STAGE1";

        case STP_STATE_STAGE2:
            return "STP_STATE_STAGE2";

        case STP_STATE_EXCHANGE:
            return "STP_STATE_EXCHANGE";

        case STP_STATE_ERROR:
            return "STP_STATE_ERROR";
    }

    return "STP_UNKNOWN";
}

/* Add received message into message list */
void stp_enqueue_msg(struct CSM* csm, struct Msg* msg)
{
    ICCHdr       *icc_hdr;
    ICCParameter *icc_param;

    if (csm == NULL )
    {
        if (msg != NULL )
            free(msg);
        return;
    }

    if (msg == NULL )
        return;

    icc_hdr = (ICCHdr*)msg->buf;
    icc_param = (ICCParameter*)&msg->buf[sizeof(ICCHdr)];

    ICCPD_LOG_DEBUG("stp_fsm", "  stp enqueue: tlv = 0x%04x/%s", icc_param->type, get_tlv_type_string(icc_param->type));

    TAILQ_INSERT_TAIL(&(STP(csm).stp_msg_list), msg, tail);

    return;
}

/* Get received message from message list */
struct Msg* stp_dequeue_msg(struct CSM* csm)
{
    struct Msg* msg = NULL;

    if (!TAILQ_EMPTY(&(STP(csm).stp_msg_list)))
    {
        msg = TAILQ_FIRST(&(STP(csm).stp_msg_list));
        TAILQ_REMOVE(&(STP(csm).stp_msg_list), msg, tail);
    }

    return msg;
}

/*****************************************
* NAK handler
*
* ***************************************/
static void stp_sync_send_nak_handler(struct CSM* csm,  struct Msg* msg)
{
    int msg_len;
    ICCHdr* icc_hdr = NULL;

    icc_hdr = (ICCHdr*)msg->buf;

    ICCPD_LOG_WARN("stp_fsm", "  ### Send NAK ###");

    memset(g_csm_buf, 0, CSM_BUFFER_SIZE);
    csm->app_csm.invalid_msg_id = ntohl(icc_hdr->ldp_hdr.msg_id);
    msg_len = app_csm_prepare_nak_msg(csm, g_csm_buf, CSM_BUFFER_SIZE);
    iccp_csm_send(csm, g_csm_buf, msg_len);
}

static void stp_sync_recv_nak_handler(struct CSM* csm,  struct Msg* msg)
{
    NAKTLV* naktlv = NULL;
    uint16_t tlvType = -1;
    int i;

    ICCPD_LOG_WARN("stp_fsm", "  ### Receive NAK ###");

    /* Dequeuq NAK*/
    naktlv = (NAKTLV*)&msg->buf[sizeof(ICCHdr)];

    /* Check NAK Type*/
    for (i = 0; i < MAX_MSG_LOG_SIZE; ++i)
    {
        if (ntohl(naktlv->rejected_msg_id) == csm->msg_log.msg[i].msg_id)
        {
            tlvType = csm->msg_log.msg[i].tlv;
            break;
        }
    }

    if (tlvType)
    {
        switch (tlvType)
        {
            case TLV_T_STP_SYSTEM_CONFIG:
                STP(csm).node_id--;
                STP(csm).system_config_changed = 1;
                ICCPD_LOG_WARN("stp_fsm", "    [%X] change NodeID as %d", tlvType & 0x00FF, STP(csm).node_id);
                break;

            default:
                ICCPD_LOG_WARN("stp_fsm", "    [%X]", tlvType & 0x00FF);
                STP(csm).need_to_sync = 1;
                break;
        }
    }
    else
    {
        ICCPD_LOG_WARN("stp_fsm", "    Unknow NAK");
        STP(csm).need_to_sync = 1;
    }

    return;
}

/*****************************************
* STP sync receiver
*
* ***************************************/
void stp_sync_receiver_handler(struct CSM* csm, struct Msg* msg)
{
    ICCParameter *icc_param;
    uint16_t iccparam_type = 0;

    /* No receive message...*/
    if (!csm || !msg)
        return;

    icc_param = (ICCParameter*)&(msg->buf[sizeof(ICCHdr)]); 
    iccparam_type = icc_param->type;

    ICCPD_LOG_DEBUG(__FUNCTION__, "process the iccp_stp msg from peer. param->type: %s param->type:%x. Current CSM State: %d", get_tlv_type_string(iccparam_type), iccparam_type, STP(csm).csm_state);  
    switch (iccparam_type) 
    {
      case TLV_T_STP_CONNECT:
        stp_process_peer_connect(csm, msg);
        break;

      case TLV_T_STP_DISCONNECT:
        stp_process_peer_disconnect(csm, msg);
        break;

      case TLV_T_STP_SYSTEM_CONFIG:
        /*Not supported*/
        break;

      case TLV_T_STP_REGION_NAME:
        /*Not supported*/
        break;

      case TLV_T_STP_REVISION_LEVEL:
        /*Not supported*/
        break;

      case TLV_T_STP_INSTANCE_PRIORITY:
        /*Not supported*/
        break;

      case TLV_T_STP_CONFIGURATION_DIGEST:
        /*Not supported*/
        break;

      case TLV_T_STP_TC_INSTANCES:
        stp_process_peer_tc_by_instance(csm, msg);
        break;

      case TLV_T_STP_CIST_ROOT_TIME_PARAMETER:
        /*Not supported*/
        break;

      case TLV_T_STP_MIST_ROOT_TIME_PARAMETER:
        /*Not supported*/
        break;

      case TLV_T_STP_SYNC_REQUEST:
        stp_process_peer_sync_request(csm, msg);
        break;

      case TLV_T_STP_SYNC_DATA:
        stp_process_peer_sync_data(csm, msg);
        break;

      case TLV_T_STP_PORTCHANNEL_PORTID_MAP:
        stp_process_peer_po_port_map(csm, msg);
        break;

      case TLV_T_STP_TX_CNFIG:
        stp_process_peer_tx_config(csm, msg);
        break;

      case TLV_T_STP_AGE_OUT:
        stp_process_peer_age_out(csm, msg);
        break;

      case TLV_T_STP_COMMON_INFO:
        stp_process_peer_common_info(csm, msg);
        break;
 
      default:
        ICCPD_LOG_ERR("STP_FSM", "Receive unsupported msg 0x%x from peer",
            icc_param->type);
        break;
    }

    ICCPD_LOG_DEBUG("stp_fsm", "  [Sync Recv] %s... DONE", get_tlv_type_string(iccparam_type));

    return;
}

/*****************************************
* STP sync sender -- TBD
*
* ***************************************/
static void stp_sync_sender_handler(struct CSM* csm)
{
    switch (STP(csm).sync_state)
    {
        case STP_SYNC_SYSCONF:
            stp_sync_send_sysConf(csm);
            break;

        default:
            break;
    }

    return;
}

static void stp_sync_send_all_info_handler(struct CSM* csm)
{
    size_t len = 0;

    /* Prepare for sync start reply*/
    memset(g_csm_buf, 0, CSM_BUFFER_SIZE);
    //len = stp_prepare_for_sync_data_tlv(csm, g_csm_buf, CSM_BUFFER_SIZE, 0);
    iccp_csm_send(csm, g_csm_buf, len);

    STP(csm).sync_state = STP_SYNC_SYSCONF;

    while (1)
    {
        stp_sync_sender_handler(csm);
        if (STP(csm).sync_state != STP_SYNC_DONE)
        {
            STP(csm).sync_state++;
        }
        else
        {
            /*Next stage*/
            STP(csm).wait_for_sync_data = 0;
            STP(csm).current_state++;
            break;
        }
    }

    return;
}

static void stp_stage_sync_send_handler(struct CSM* csm, struct Msg* msg)
{
    ICCHdr* icc_hdr = NULL;
    ICCParameter* icc_param = NULL;
    stpSyncReqTLV* stp_sync_req = NULL;

    if (STP(csm).wait_for_sync_data == 0)
    {
        /* Waiting the peer sync request*/
        if (msg)
        {
            icc_hdr = (ICCHdr*)msg->buf;
            icc_param = (ICCParameter*)&msg->buf[sizeof(ICCHdr)];

            if (icc_hdr->ldp_hdr.msg_type == MSG_T_RG_APP_DATA && icc_param->type == TLV_T_STP_SYNC_REQUEST)
            {
                stp_sync_req = (stpSyncReqTLV*)&msg->buf[sizeof(ICCHdr)];
                STP(csm).wait_for_sync_data = 1;
                STP(csm).sync_req_num = ntohs(stp_sync_req->req_num);

                /* Reply the peer all sync info*/
                stp_sync_send_all_info_handler(csm);
            }
        }
    }

    return;
}

static void stp_stage_sync_request_handler(struct CSM* csm, struct Msg* msg)
{
    int msg_len = 0;

    /* Socket server send sync request first*/
    if (STP(csm).wait_for_sync_data == 0)
    {
        // Send out the request for ALL
        memset(g_csm_buf, 0, CSM_BUFFER_SIZE);
        //msg_len = stp_prepare_for_sync_request_tlv(csm, g_csm_buf, CSM_BUFFER_SIZE);
        iccp_csm_send(csm, g_csm_buf, msg_len);
        STP(csm).wait_for_sync_data = 1;
    }
    else
    {
        stp_sync_receiver_handler(csm, msg);
        if (STP(csm).wait_for_sync_data == 0)
        {
            STP(csm).current_state++;
        }
    }

    return;
}

static void stp_stage_handler(struct CSM* csm, struct Msg* msg)
{
    if (STP(csm).current_state == STP_STATE_STAGE1)
    {
        /*Stage 1, role active send info first*/
        if (csm->role_type == STP_ROLE_ACTIVE)
            stp_stage_sync_send_handler(csm, msg);
        else
            stp_stage_sync_request_handler(csm, msg);
    }
    else
    {
        /*Stage 2, role standby send info*/
        if (csm->role_type == STP_ROLE_ACTIVE)
            stp_stage_sync_request_handler(csm, msg);
        else
            stp_stage_sync_send_handler(csm, msg);
    }

    return;
}

static void stp_exchange_handler(struct CSM* csm, struct Msg* msg)
{
    int len=0;
    struct System* sys = NULL;
    struct LocalInterface* lif = NULL, *lif_purge = NULL;

    ICCHdr* icc_hdr = NULL;

    if ((sys = system_get_instance()) == NULL)
        return;

    /* update system id*/
    /*update_system_id(csm);*/

    /* Any msg?*/
    if (msg)
    {
        icc_hdr = (ICCHdr*)msg->buf;
        if (icc_hdr->ldp_hdr.msg_type == MSG_T_RG_APP_DATA)
        {
            /* Process receive APP info*/
            stp_sync_receiver_handler(csm, msg);
        }
    }

    if (STP(csm).need_to_sync != 0)
    {
        /* Send out the request for ALL info*/
        STP(csm).need_to_sync = 0;
        memset(g_csm_buf, 0, CSM_BUFFER_SIZE);
        //len = stp_prepare_for_sync_request_tlv(csm, g_csm_buf, CSM_BUFFER_SIZE);
        iccp_csm_send(csm, g_csm_buf, len);
    }

    /* Send system config*/
    if (STP(csm).system_config_changed != 0)
    {
        memset(g_csm_buf, 0, CSM_BUFFER_SIZE);
        //len = stp_prepare_for_sys_config(csm, g_csm_buf, CSM_BUFFER_SIZE);
        iccp_csm_send(csm, g_csm_buf, len);

        if (csm->peer_link_if)
        {
            memset(g_csm_buf, 0, CSM_BUFFER_SIZE);
            //len = stp_prepare_for_port_peerlink_info(csm, g_csm_buf, CSM_BUFFER_SIZE, csm->peer_link_if);
            iccp_csm_send(csm, g_csm_buf, len);
        }

        STP(csm).system_config_changed = 0;
    }
    return;
}

/* STP ICCP mesage type to debug counter type conversion */
STP_ICCP_DBG_CNTR_MSG_e stp_fsm_iccp_to_dbg_msg_type(uint32_t tlv_type)
{
    switch (tlv_type)
    {
        case TLV_T_STP_SYSTEM_CONFIG:
            return STP_ICCP_DBG_CNTR_MSG_SYS_CONFIG;

        case TLV_T_STP_SYNC_REQUEST:
            return STP_ICCP_DBG_CNTR_MSG_SYNC_REQ;

        case TLV_T_STP_SYNC_DATA:
            return STP_ICCP_DBG_CNTR_MSG_SYNC_DATA;

        default:
            ICCPD_LOG_DEBUG(__FUNCTION__, "No debug counter for TLV type %u",
                tlv_type);
            return STP_ICCP_DBG_CNTR_MSG_MAX;
    }
}
