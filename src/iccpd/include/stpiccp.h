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

#ifndef _STPICCP_H
#define _STPICCP_H

#define STPICCP_DEFAULT_IP   0x7f000006

/*
 * default port for stpiccp connections
 */
#define STPICCP_DEFAULT_PORT 2627

/*
 * Largest message that can be sent to or received from the STPICCP.
 */
#define STPICCP_MAX_MSG_LEN 4096
#define STPICCP_MAX_SEND_MSG_LEN 4096

typedef struct stpiccp_msg_hdr_t_ {
    /*
     * Protocol version.
     */
    uint8_t version;

    /*
     * Type of message, see below.
     */
    uint8_t msg_type;

    /*
     * Length of entire message, including the header.
     */
    uint16_t msg_len;
}stpiccp_msg_hdr_t;

#define STPICCP_PROTO_VERSION 1
#define STPICCP_MSG_HDR_LEN (sizeof (stpiccp_msg_hdr_t))

/*syncd send msg type to iccpd*/
typedef enum stpiccp_syncd_msg_type_e_ {
    STPICCP_SYNCD_MSG_TYPE_NONE = 0,
    STPICCP_SYNCD_MSG_TYPE_STP_VLAN_TC_OPERATION,
    STPICCP_SYNCD_MSG_TYPE_PORTCHANNEL_PORT_ID_MAP_OPERATION,
    STPICCP_SYNCD_MSG_TYPE_TX_CONFIG_OPERATION,
    STPICCP_SYNCD_MSG_TYPE_AGE_OUT_OPERATION,
    STPICCP_SYNCD_MSG_TYPE_SYNC_REQ_OPERATION,
    STPICCP_SYNCD_MSG_TYPE_SYNC_RESPONSE_OPERATION,
    STPICCP_SYNCD_MSG_TYPE_STP_CONNECT_TLV_EXCHANGE_OPERATION,
    STPICCP_SYNCD_MSG_TYPE_STP_DISCONNECT_TLV_EXCHANGE_OPERATION,
    STPICCP_SYNCD_MSG_TYPE_COMMON_INFO_OPERATION
}stpiccp_syncd_msg_type_e;

/*iccpd send msg type to syncd*/
typedef enum stpiccp_msg_type_e_ {
    STPICCP_MSG_TYPE_NONE = 0,
    STPICCP_MSG_TYPE_OPER_STATE_SET,           
    STPICCP_MSG_TYPE_STP_VLAN_TC_SET,
    STPICCP_MSG_TYPE_PORTCHANNEL_PORT_ID_MAP_SET,
    STPICCP_MSG_TYPE_TX_CONFIG_SET,
    STPICCP_MSG_TYPE_AGE_OUT_SET,
    STPICCP_MSG_TYPE_SYNC_REQ_SET,
    STPICCP_MSG_TYPE_SYNC_RESPONSE_SET,
    STPICCP_MSG_TYPE_COMMON_INFO_SET
}stpiccp_msg_type_e;

typedef struct stpiccp_sub_option_hdr_t_ {    
    uint8_t op_type;

    /*
     * Length of option value, not including the header.
     */
    uint16_t op_len;
    uint8_t data[];
}stpiccp_sub_option_hdr_t;

#define STPICCP_SUB_OPTION_HDR_LEN (sizeof (stpiccp_sub_option_hdr_t))

typedef enum stpiccp_sub_option_type_e_ {
    STPICCP_SUB_OPTION_TYPE_NONE = 0,
} stpiccp_sub_option_type_e;

static inline size_t
stpiccp_msg_len (const stpiccp_msg_hdr_t *hdr)
{
    return hdr->msg_len;
}

/*
 * stpiccp_msg_data_len
 */
static inline size_t
stpiccp_msg_data_len (const stpiccp_msg_hdr_t *hdr)
{
  return (stpiccp_msg_len (hdr) - STPICCP_MSG_HDR_LEN);
}

/*
 * stpiccp_msg_hdr_ok
 *
 * Returns TRUE if a message header looks well-formed.
 */
static inline int
stpiccp_msg_hdr_ok (const stpiccp_msg_hdr_t *hdr)
{
  size_t msg_len;

  if (hdr->msg_type == STPICCP_MSG_TYPE_NONE)
    return 0;

  msg_len = stpiccp_msg_len (hdr);

  if (msg_len < STPICCP_MSG_HDR_LEN || msg_len > STPICCP_MAX_MSG_LEN)
    return 0;

  return 1;
}

/*
 * stpiccp_msg_ok
 *
 * Returns TRUE if a message looks well-formed.
 *
 * @param len The length in bytes from 'hdr' to the end of the buffer.
 */
static inline int
stpiccp_msg_ok (const stpiccp_msg_hdr_t *hdr, size_t len)
{
  if (len < STPICCP_MSG_HDR_LEN)
    return 0;

  if (!stpiccp_msg_hdr_ok (hdr))
    return 0;

  if (stpiccp_msg_len (hdr) > len)
    return 0;

  return 1;
}


#endif

