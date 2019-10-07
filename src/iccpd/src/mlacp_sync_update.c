/********************************************************************************
 * mlacp_sync_update.c
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
 *
 *******************************************************************************/
#include <stdio.h>
#include <stdlib.h>

#include <sys/queue.h>
#include <netinet/ip.h>

#include "../include/system.h"
#include "../include/logger.h"
#include "../include/mlacp_tlv.h"
#include "../include/iccp_csm.h"
#include "../include/mlacp_link_handler.h"
#include "../include/iccp_consistency_check.h"
#include "../include/port.h"
#include "../include/openbsd_tree.h"

/*****************************************
* Port-Conf Update
*
* ***************************************/
extern void update_if_ipmac_on_standby(struct LocalInterface* lif_po);
int mlacp_fsm_update_system_conf(struct CSM* csm, mLACPSysConfigTLV*sysconf)
{
    struct LocalInterface* lif = NULL;
    uint8_t old_remote_system_id[ETHER_ADDR_LEN];

    ICCPD_LOG_DEBUG("ICCP_FSM", "RX system_conf: systemID %s, priority %d, remote nodeID %d, nodeID %d",
        mac_addr_to_str(MLACP(csm).remote_system.system_id),
        MLACP(csm).remote_system.system_priority,
        MLACP(csm).remote_system.node_id,
        MLACP(csm).node_id);

    /*NOTE
       a little tricky, we change the NodeID local side if collision happened first time*/
    if (sysconf->node_id == MLACP(csm).node_id)
        MLACP(csm).node_id++;

    if (csm->role_type == STP_ROLE_STANDBY)
        memcpy(old_remote_system_id, MLACP(csm).remote_system.system_id, ETHER_ADDR_LEN);

    memcpy(MLACP(csm).remote_system.system_id, sysconf->sys_id, ETHER_ADDR_LEN);
    MLACP(csm).remote_system.system_priority = ntohs(sysconf->sys_priority);
    MLACP(csm).remote_system.node_id = sysconf->node_id;

    LIST_FOREACH(lif, &(MLACP(csm).lif_list), mlacp_next)
    {
        update_if_ipmac_on_standby(lif);
    }

    /* On standby, update system ID upon receiving change from active */
    if ((csm->role_type == STP_ROLE_STANDBY) &&
        (memcmp(old_remote_system_id, sysconf->sys_id, ETHER_ADDR_LEN) != 0))
    {
        mlacp_link_set_iccp_system_id(csm->mlag_id, sysconf->sys_id);
    }
    return 0;
}

/*****************************************
* Port-Conf Update
*
* ***************************************/
int mlacp_fsm_update_Agg_conf(struct CSM* csm, mLACPAggConfigTLV* portconf)
{
    struct PeerInterface* pif = NULL;
    uint8_t po_active;
    uint8_t new_create = 0;

    ICCPD_LOG_DEBUG("ICCP_FSM", "RX aggrport_config: name %s, po_id %d, flag 0x%x, MAC %s",
        portconf->agg_name, ntohs(portconf->agg_id), portconf->flags,
        mac_addr_to_str(portconf->mac_addr));

    /* Looking for the peer port instance, is any peer if exist?*/
    pif = peer_if_find_by_name(csm, portconf->agg_name);

    /* Process purge*/
    if (portconf->flags & 0x02)
    {
        /*Purge*/
        if (pif != NULL )
        {
            /* Delete remote interface info from STATE_DB */
            if (csm)
                mlacp_link_del_remote_if_info(csm->mlag_id, pif->name);
            peer_if_destroy(pif);
        }
        else
            MLACP(csm).need_to_sync = 1;
        /*ICCPD_LOG_INFO("mlacp_fsm",
            "    Peer port %s is removed from port-channel member.",portconf->port_name);*/

        return 0;
    }

    if (pif == NULL && portconf->flags & 0x01)
    {
        pif = peer_if_create(csm, ntohs(portconf->agg_id), IF_T_PORT_CHANNEL);
        if (pif == NULL)
            return MCLAG_ERROR;

        new_create = 1;
    }

    pif->po_id = ntohs(portconf->agg_id);
    memcpy(pif->name, portconf->agg_name, portconf->agg_name_len);
    memcpy(pif->mac_addr, portconf->mac_addr, ETHER_ADDR_LEN);

    po_active = (pif->state == PORT_STATE_UP);
    update_stp_peer_link(csm, pif, po_active, new_create);
    update_peerlink_isolate_from_pif(csm, pif, po_active, new_create);
    pif->po_active = po_active;

    return 0;
}

/*****************************************
* Agg Port-State Update
*
* ***************************************/
int mlacp_fsm_update_Aggport_state(struct CSM* csm, mLACPAggPortStateTLV* tlv)
{
    struct PeerInterface* peer_if = NULL;
    uint8_t po_active;

    if (csm == NULL || tlv == NULL)
        return MCLAG_ERROR;

    ICCPD_LOG_DEBUG("ICCP_FSM", "RX aggrport_state: po_id %d, state %s, sync_state %s",
        ntohs(tlv->agg_id), (tlv->agg_state == PORT_STATE_UP) ? "up" : "down",
        mlacp_state(csm));

    po_active = (tlv->agg_state == PORT_STATE_UP);

    LIST_FOREACH(peer_if, &(MLACP(csm).pif_list), mlacp_next)
    {
        if (peer_if->type != IF_T_PORT_CHANNEL)
            continue;

        if (peer_if->po_id != ntohs(tlv->agg_id))
            continue;

        peer_if->state = tlv->agg_state;

        update_stp_peer_link(csm, peer_if, po_active, 0);
        update_peerlink_isolate_from_pif(csm, peer_if, po_active, 0);

        peer_if->po_active = po_active;
        ICCPD_LOG_DEBUG(__FUNCTION__, "Update  Msg for %s  state %s", peer_if->name, tlv->agg_state ? "down" : "up");

        /* Update remote interface state if ICCP reaches EXCHANGE state.
         * Otherwise, it is updated after the session comes up
         */
        if (MLACP(csm).current_state == MLACP_STATE_EXCHANGE)
        {
            mlacp_link_set_remote_if_state(
                csm->mlag_id, peer_if->name,
                (tlv->agg_state == PORT_STATE_UP)? true : false);
        }
        break;
    }

    return 0;
}

/*****************************************
* Recv from peer, MAC-Info Update
* ***************************************/
int mlacp_fsm_update_mac_entry_from_peer( struct CSM* csm, struct mLACPMACData *MacData)
{
    struct Msg* msg = NULL;
    struct MACMsg *mac_msg = NULL, mac_data, *new_mac_msg = NULL;
    struct MACMsg mac_find;
    struct LocalInterface* local_if = NULL;
    uint8_t from_mclag_intf = 0;/*0: orphan port, 1: MCLAG port*/

    #if 1
    ICCPD_LOG_INFO(__FUNCTION__,
        "Received MAC Info, itf=[%s] vid[%d] MAC[%s] Oper type %d, Mac type: %d ",
        MacData->ifname, ntohs(MacData->vid), mac_addr_to_str(MacData->mac_addr),
        MacData->type, MacData->mac_type);
    #endif

    /*Find the interface in MCLAG interface list*/
    LIST_FOREACH(local_if, &(MLACP(csm).lif_list), mlacp_next)
    {
        if (local_if->type == IF_T_PORT_CHANNEL && strcmp(local_if->name, MacData->ifname) == 0)
        {
            from_mclag_intf = 1;
            break;
        }
    }

    mac_find.vid = ntohs(MacData->vid);
    memcpy(&mac_find.mac_addr, MacData->mac_addr, ETHER_ADDR_LEN);
    mac_msg = RB_FIND(mac_rb_tree, &MLACP(csm).mac_rb ,&mac_find);

    /*Same MAC is exist in local switch, this may be mac move*/
    //if (strcmp(mac_msg->mac_str, MacData->mac_str) == 0 && mac_msg->vid == ntohs(MacData->vid))
    if (mac_msg)
    {
        if (MacData->type == MAC_SYNC_ADD)
        {
            mac_msg->age_flag &= ~MAC_AGE_PEER;
            ICCPD_LOG_DEBUG(__FUNCTION__, "Recv ADD, Remove peer age flag:%d ifname  %s, "
                "add %s vlan-id %d, op_type %d", mac_msg->age_flag, mac_msg->ifname,
                mac_addr_to_str(mac_msg->mac_addr), mac_msg->vid, mac_msg->op_type);

            /*mac_msg->fdb_type = tlv->fdb_type;*/
            /*The port ifname is different to the local item*/
            if (strcmp(mac_msg->ifname, MacData->ifname) != 0 || strcmp(mac_msg->origin_ifname, MacData->ifname) != 0)
            {
                if (mac_msg->fdb_type != MAC_TYPE_STATIC)
                {
                    /*Update local item*/
                    memcpy(&mac_msg->origin_ifname, MacData->ifname, MAX_L_PORT_NAME);
                }
                else
                {
                    ICCPD_LOG_DEBUG(__FUNCTION__, "Ignore Recv MAC ADD, Local static present,"
                        " ifname  %s, MAC %s vlan-id %d ", mac_msg->ifname,
                        mac_addr_to_str(mac_msg->mac_addr), mac_msg->vid);
                    //set back the peer age flag
                    mac_msg->age_flag |= MAC_AGE_PEER;
                    return 0;
                }

                /*If the MAC is learned from orphan port, or from MCLAG port but the local port is down*/
                if (from_mclag_intf == 0 || (local_if->state == PORT_STATE_DOWN && strcmp(mac_msg->ifname, csm->peer_itf_name) != 0))
                {
                    /*Set MAC_AGE_LOCAL flag*/
                    mac_msg->age_flag = set_mac_local_age_flag(csm, mac_msg, 1, 1);

                    if (strlen(csm->peer_itf_name) != 0)
                    {
                        if (csm->peer_link_if && csm->peer_link_if->state == PORT_STATE_UP)
                        {
                            /*Redirect the mac to peer-link*/
                            memcpy(&mac_msg->ifname, csm->peer_itf_name, MAX_L_PORT_NAME);

                            /*Send mac add message to mclagsyncd*/
                            add_mac_to_chip(mac_msg, MAC_TYPE_DYNAMIC);
                        }
                        else
                        {
                            /*must redirect but peerlink is down, del mac from ASIC*/
                            /*if peerlink change to up, mac will add back to ASIC*/
                            del_mac_from_chip(mac_msg);

                            /*Redirect the mac to peer-link*/
                            memcpy(&mac_msg->ifname, csm->peer_itf_name, MAX_L_PORT_NAME);
                        }
                    }
                    else
                    {
                        /*must redirect but no peerlink, del mac from ASIC*/
                        del_mac_from_chip(mac_msg);

                        /*Update local item*/
                        memcpy(&mac_msg->ifname, MacData->ifname, MAX_L_PORT_NAME);

                        /*if orphan port mac but no peerlink, don't keep this mac*/
                        if (from_mclag_intf == 0)
                        {
                            RB_REMOVE(mac_rb_tree, &MLACP(csm).mac_rb, mac_msg);
                            free(mac_msg);
                            return 0;
                        }
                    }
                }
                else
                {
                    /*Update local item*/
                    memcpy(&mac_msg->ifname, MacData->ifname, MAX_L_PORT_NAME);

                    /*from MCLAG port and the local port is up, add mac to ASIC to update port*/
                    add_mac_to_chip(mac_msg, MAC_TYPE_DYNAMIC);
                }
            }

            // Code to exchange MAC_SYNC_ACK notifications can be enabled in future, if MAC SYNC issues observed.
            #if 0
            mac_msg->op_type = MAC_SYNC_ACK;
            if (iccp_csm_init_msg(&msg_send, (char*)mac_msg, sizeof(struct MACMsg)) == 0)
            {
                /*Reply mac ack message to peer, peer will clean MAC_AGE_PEER flag*/
                TAILQ_INSERT_TAIL(&(MLACP(csm).mac_msg_list), msg_send, tail);
                ICCPD_LOG_DEBUG(__FUNCTION__, "Recv ADD, MAC-msg-list enqueue: %s, "
                    "add %s vlan-id %d, op_type %d", mac_msg->ifname,
                    mac_addr_to_str(mac_msg->mac_addr), mac_msg->vid, mac_msg->op_type);
            }
            #endif
        }
        // Code to exchange MAC_SYNC_ACK notifications can be enabled in future, if MAC SYNC issues observed.
        #if 0
        else if (tlv->type == MAC_SYNC_ACK)
        {
            /*Clean the MAC_AGE_PEER flag*/
            mac_msg->age_flag &= ~MAC_AGE_PEER;
            ICCPD_LOG_DEBUG(__FUNCTION__, "Recv ACK, Remove peer age flag:%d ifname  %s, "
                "add %s vlan-id %d, op_type %d", mac_msg->age_flag, mac_msg->ifname,
                mac_addr_to_str(mac_msg->mac_addr), mac_msg->vid, mac_msg->op_type);
        }
        #endif

    }

    /* delete/add MAC list*/
    if (mac_msg && (MacData->type == MAC_SYNC_DEL))
    {
        mac_msg->age_flag |= MAC_AGE_PEER;
        ICCPD_LOG_DEBUG(__FUNCTION__, "Add peer age flag: %d   ifname %s, "
            "add %s vlan-id %d, op_type %d", mac_msg->age_flag, mac_msg->ifname,
            mac_addr_to_str(mac_msg->mac_addr), mac_msg->vid, mac_msg->op_type);

        if (mac_msg->age_flag == (MAC_AGE_LOCAL | MAC_AGE_PEER))
        {
            /*send mac del message to mclagsyncd.*/
            del_mac_from_chip(mac_msg);

            /*If local and peer both aged, del the mac*/
            RB_REMOVE(mac_rb_tree, &MLACP(csm).mac_rb, mac_msg);
            free(mac_msg);
        }
        else
        {
            return 0;
        }
    }
    else if (!mac_msg && (MacData->type == MAC_SYNC_ADD))
    {
        mac_msg = (struct MACMsg*)&mac_data;
        mac_msg->fdb_type = MacData->mac_type;
        mac_msg->vid = ntohs(MacData->vid);
        memcpy(mac_msg->mac_addr, MacData->mac_addr, ETHER_ADDR_LEN);
        sprintf(mac_msg->ifname, "%s", MacData->ifname);
        sprintf(mac_msg->origin_ifname, "%s", MacData->ifname);
        mac_msg->age_flag = 0;

        /*Set MAC_AGE_LOCAL flag*/
        mac_msg->age_flag = set_mac_local_age_flag(csm, mac_msg, 1, 0);

        /*If the MAC is learned from orphan port, or from MCLAG port but the local port is down*/
        if (from_mclag_intf == 0 || local_if->state == PORT_STATE_DOWN)
        {

            if (strlen(csm->peer_itf_name) == 0)
            {
                ICCPD_LOG_DEBUG(__FUNCTION__, "orphan port %d or portchannel is down, but peer-link is not configured: "
                        "ifname %s, add %s vlan-id %d, op_type %d", from_mclag_intf,
                        mac_msg->ifname, mac_addr_to_str(mac_msg->mac_addr), mac_msg->vid, mac_msg->op_type);

                /*if orphan port mac but no peerlink, don't keep this mac*/
                if (from_mclag_intf == 0)
                    return 0;
            }
            else
            {
                /*Redirect the mac to peer-link*/
                memcpy(&mac_msg->ifname, csm->peer_itf_name, MAX_L_PORT_NAME);

                ICCPD_LOG_DEBUG(__FUNCTION__, "Redirect to peerlink for orphan port or portchannel is down,"
                    " Add local age flag: %d   ifname %s, add %s vlan-id %d, op_type %d",
                    mac_msg->age_flag, mac_msg->ifname, mac_addr_to_str(mac_msg->mac_addr),
                    mac_msg->vid, mac_msg->op_type);
            }
        }

        if (iccp_csm_init_mac_msg(&new_mac_msg, (char*)mac_msg, sizeof(struct MACMsg)) == 0)
        {
            /*ICCPD_LOG_INFO(__FUNCTION__, "add mac queue successfully");*/
            RB_INSERT(mac_rb_tree, &MLACP(csm).mac_rb, new_mac_msg);

            /*If the mac is from orphan port, or from MCLAG port but the local port is down*/
            if (strcmp(mac_msg->ifname, csm->peer_itf_name) == 0)
            {
                /*Send mac add message to mclagsyncd*/
                if (csm->peer_link_if && csm->peer_link_if->state == PORT_STATE_UP)
                    add_mac_to_chip(mac_msg, mac_msg->fdb_type);
            }
            else
            {
                /*from MCLAG port and the local port is up*/
                add_mac_to_chip(mac_msg, mac_msg->fdb_type);
            }
            // Code to exchange MAC_SYNC_ACK notifications can be enabled in future, if MAC SYNC issues observed.
            #if 0
            mac_msg->op_type = MAC_SYNC_ACK;
            if (iccp_csm_init_msg(&msg_send, (char*)mac_msg, sizeof(struct MACMsg)) == 0)
            {
                /*Reply mac ack message to peer, peer will clean MAC_AGE_PEER flag*/
                TAILQ_INSERT_TAIL(&(MLACP(csm).mac_msg_list), msg_send, tail);
                ICCPD_LOG_DEBUG(__FUNCTION__, "MAC-msg-list enqueue: %s, add %s vlan-id %d, op_type %d",
                    mac_msg->ifname, mac_addr_to_str(mac_msg->mac_addr), mac_msg->vid, mac_msg->op_type);
            }
            #endif
        }
    }

    return 0;
}

int mlacp_fsm_update_mac_info_from_peer(struct CSM* csm, struct mLACPMACInfoTLV* tlv)
{
    int count = 0;
    int i;

    if (!csm || !tlv)
        return MCLAG_ERROR;
    count = ntohs(tlv->num_of_entry);
    ICCPD_LOG_INFO(__FUNCTION__, "Received MAC Info count  %d ", count );

    for (i = 0; i < count; i++)
    {
        mlacp_fsm_update_mac_entry_from_peer(csm, &(tlv->MacEntry[i]));
    }
}

/*****************************************
 * Tool : Add ARP Info into ARP list
 *
 ****************************************/
void mlacp_enqueue_arp(struct CSM* csm, struct Msg* msg)
{
    struct ARPMsg *arp_msg = NULL;

    if (!csm)
    {
        if (msg)
            free(msg);
        return;
    }
    if (!msg)
        return;

    arp_msg = (struct ARPMsg*)msg->buf;
    if (arp_msg->op_type != ARP_SYNC_DEL)
    {
        TAILQ_INSERT_TAIL(&(MLACP(csm).arp_list), msg, tail);
    }

    return;
}

/*****************************************
* ARP-Info Update
* ***************************************/
int mlacp_fsm_update_arp_entry(struct CSM* csm, struct ARPMsg *arp_entry)
{
    struct Msg* msg = NULL;
    struct ARPMsg *arp_msg = NULL, arp_data;
    struct LocalInterface* local_if;
    struct LocalInterface *peer_link_if = NULL;
    struct VLAN_ID *vlan_id_list = NULL;
    int set_arp_flag = 0;
    char mac_str[18] = "";

    if (!csm || !arp_entry)
        return MCLAG_ERROR;

    #if 1
    ICCPD_LOG_INFO(__FUNCTION__,
                   "%s: Received ARP Info,"
                   "itf=[%s] ARP IP[%s],MAC[%02x:%02x:%02x:%02x:%02x:%02x]",
                   __FUNCTION__,
                   arp_entry->ifname, show_ip_str(arp_entry->ipv4_addr),
                   arp_entry->mac_addr[0], arp_entry->mac_addr[1], arp_entry->mac_addr[2],
                   arp_entry->mac_addr[3], arp_entry->mac_addr[4], arp_entry->mac_addr[5]);
    #endif

    sprintf(mac_str, "%02x:%02x:%02x:%02x:%02x:%02x", arp_entry->mac_addr[0], arp_entry->mac_addr[1], arp_entry->mac_addr[2],
            arp_entry->mac_addr[3], arp_entry->mac_addr[4], arp_entry->mac_addr[5]);

    if (strncmp(arp_entry->ifname, "Vlan", 4) == 0)
    {
        peer_link_if = local_if_find_by_name(csm->peer_itf_name);

        if (peer_link_if && !local_if_is_l3_mode(peer_link_if))
        {
            /* Is peer-linlk itf belong to a vlan the same as peer?*/
            LIST_FOREACH(vlan_id_list, &(peer_link_if->vlan_list), port_next)
            {
                if (!vlan_id_list->vlan_itf)
                    continue;
                if (strcmp(vlan_id_list->vlan_itf->name, arp_entry->ifname) != 0)
                    continue;
                if (!local_if_is_l3_mode(vlan_id_list->vlan_itf))
                    continue;

                ICCPD_LOG_DEBUG(__FUNCTION__,
                                "%s:  ==> Find ARP itf on L3 bridge, peer-link %s of %s",
                                __FUNCTION__,
                                peer_link_if->name, vlan_id_list->vlan_itf->name);

                /* Peer-link belong to L3 vlan is alive, set the ARP info*/
                set_arp_flag = 1;

                break;
            }
        }
    }

    if (set_arp_flag == 0)
    {
        LIST_FOREACH(local_if, &(MLACP(csm).lif_list), mlacp_next)
        {
            if (local_if->type == IF_T_PORT_CHANNEL)
            {
                if (!local_if_is_l3_mode(local_if))
                {
                    /* Is the L2 MLAG itf belong to a vlan the same as peer?*/
                    LIST_FOREACH(vlan_id_list, &(local_if->vlan_list), port_next)
                    {
                        if (!vlan_id_list->vlan_itf)
                            continue;
                        if (strcmp(vlan_id_list->vlan_itf->name, arp_entry->ifname) != 0)
                            continue;
                        if (!local_if_is_l3_mode(vlan_id_list->vlan_itf))
                            continue;

                        ICCPD_LOG_DEBUG(__FUNCTION__,
                                        "%s:  ==> Find ARP itf on L3 bridge, %s of %s",
                                        __FUNCTION__,
                                        local_if->name, vlan_id_list->vlan_itf->name);
                        break;
                    }

                    if (vlan_id_list && local_if->po_active == 1)
                    {
                        /* Any po of L3 vlan is alive, set the ARP info*/
                        set_arp_flag = 1;
                        break;
                    }
                }
                else
                {
                    /* Is the ARP belong to a L3 mode MLAG itf?*/
                    if (strcmp(local_if->name, arp_entry->ifname) == 0)
                    {
                        ICCPD_LOG_DEBUG(__FUNCTION__,
                                        "%s:  ==> Find ARP itf on L3 port-channel, %s",
                                        __FUNCTION__,
                                        local_if->name);
                        if (local_if->po_active == 1)
                        {
                            /* po is alive, set the ARP info*/
                            set_arp_flag = 1;
                            break;
                        }
                    }
                    else
                    {
                        continue;
                    }
                }
            }
        }
    }

    /* set dynamic ARP*/
    if (set_arp_flag == 1)
    {
        if (arp_entry->op_type == ARP_SYNC_ADD)
        {
            if (mlacp_fsm_arp_set(arp_entry->ifname, ntohl(arp_entry->ipv4_addr), mac_str) < 0)
            {
                ICCPD_LOG_DEBUG(__FUNCTION__, "%s: ARP set for %s %s %s",
                                __FUNCTION__, arp_entry->ifname, show_ip_str(arp_entry->ipv4_addr), mac_str);
                return MCLAG_ERROR;
            }
        }
        else
        {
            if (mlacp_fsm_arp_del(arp_entry->ifname, ntohl(arp_entry->ipv4_addr)) < 0)
            {
                ICCPD_LOG_DEBUG(__FUNCTION__, "%s: ARP delete for %s %s %s",
                                __FUNCTION__, arp_entry->ifname, show_ip_str(arp_entry->ipv4_addr), mac_str);
                return MCLAG_ERROR;
            }
        }

        ICCPD_LOG_DEBUG(__FUNCTION__, "%s: ARP update for %s %s %s",
                        __FUNCTION__, arp_entry->ifname, show_ip_str(arp_entry->ipv4_addr), mac_str);
    }
    else
    {
        ICCPD_LOG_DEBUG(__FUNCTION__, "%s:  ==> port-channel is not alive",
                        __FUNCTION__);
        /*TODO Set static route through peer-link or just skip it?*/
    }

    /* update ARP list*/
    TAILQ_FOREACH(msg, &(MLACP(csm).arp_list), tail)
    {
        arp_msg = (struct ARPMsg*)msg->buf;
        if (arp_msg->ipv4_addr == ntohl(arp_entry->ipv4_addr))
        {
            /*arp_msg->op_type = tlv->type;*/
            sprintf(arp_msg->ifname, "%s", arp_entry->ifname);
            memcpy(arp_msg->mac_addr, arp_entry->mac_addr, ETHER_ADDR_LEN);
            break;
        }
    }

    /* delete/add ARP list*/
    if (msg && arp_entry->op_type == ARP_SYNC_DEL)
    {
        TAILQ_REMOVE(&(MLACP(csm).arp_list), msg, tail);
        free(msg->buf); free(msg);
        ICCPD_LOG_INFO(__FUNCTION__, "%s: del arp queue successfully",
                       __FUNCTION__);
    }
    else if (!msg && arp_entry->op_type == ARP_SYNC_ADD)
    {
        arp_msg = (struct ARPMsg*)&arp_data;
        sprintf(arp_msg->ifname, "%s", arp_entry->ifname);
        arp_msg->ipv4_addr = ntohl(arp_entry->ipv4_addr);
        arp_msg->op_type = arp_entry->op_type;
        memcpy(arp_msg->mac_addr, arp_entry->mac_addr, ETHER_ADDR_LEN);
        if (iccp_csm_init_msg(&msg, (char*)arp_msg, sizeof(struct ARPMsg)) == 0)
        {
            mlacp_enqueue_arp(csm, msg);
            ICCPD_LOG_INFO(__FUNCTION__, "%s: add arp queue successfully",
                           __FUNCTION__);
        }
    }

    /* remove all ARP msg queue, when receive peer's ARP list at the same time*/
    TAILQ_FOREACH(msg, &(MLACP(csm).arp_msg_list), tail)
    {
        arp_msg = (struct ARPMsg*)msg->buf;
        if (arp_msg->ipv4_addr == ntohl(arp_entry->ipv4_addr))
            break;
    }

    while (msg)
    {
        arp_msg = (struct ARPMsg*)msg->buf;
        TAILQ_REMOVE(&(MLACP(csm).arp_msg_list), msg, tail);
        free(msg->buf);
        free(msg);
        TAILQ_FOREACH(msg, &(MLACP(csm).arp_msg_list), tail)
        {
            arp_msg = (struct ARPMsg*)msg->buf;
            if (arp_msg->ipv4_addr == ntohl(arp_entry->ipv4_addr))
                break;
        }
    }

    return 0;
}

int mlacp_fsm_update_arp_info(struct CSM* csm, struct mLACPARPInfoTLV* tlv)
{
    int count = 0;
    int i;

    if (!csm || !tlv)
        return MCLAG_ERROR;
    count = ntohs(tlv->num_of_entry);
    ICCPD_LOG_INFO(__FUNCTION__, "Received ARP Info count  %d ", count );

    for (i = 0; i < count; i++)
    {
        mlacp_fsm_update_arp_entry(csm, &(tlv->ArpEntry[i]));
    }
}

/*****************************************
* Port-Channel-Info Update
* ***************************************/
int mlacp_fsm_update_port_channel_info(struct CSM* csm,
                                       struct mLACPPortChannelInfoTLV* tlv)
{
    struct PeerInterface* peer_if = NULL;
    struct VLAN_ID* peer_vlan_id = NULL;
    int i = 0;

    if (csm == NULL || tlv == NULL )
        return MCLAG_ERROR;

    LIST_FOREACH(peer_if, &(MLACP(csm).pif_list), mlacp_next)
    {
        if (peer_if->type != IF_T_PORT_CHANNEL)
            continue;

        if (peer_if->po_id != ntohs(tlv->agg_id))
            continue;

        LIST_FOREACH(peer_vlan_id, &(peer_if->vlan_list), port_next)
        {
            peer_vlan_id->vlan_removed = 1;
        }

        /* Record peer info*/
        peer_if->ipv4_addr = ntohl(tlv->ipv4_addr);
        peer_if->l3_mode = tlv->l3_mode;

        for (i = 0; i < ntohs(tlv->num_of_vlan_id); i++)
        {
            peer_if_add_vlan(peer_if, ntohs(tlv->vlanData[i].vlan_id));
        }

        peer_if_clean_unused_vlan(peer_if);

        iccp_consistency_check(peer_if->name);

        ICCPD_LOG_DEBUG("ICCP_FSM", "RX po_info: %s ip %s l3 mode  %d",
            peer_if->name, show_ip_str( tlv->ipv4_addr), peer_if->l3_mode);
        break;
    }

    return 0;
}

/*****************************************
* Peerlink port Update
* ***************************************/
int mlacp_fsm_update_peerlink_info(struct CSM* csm,
                                   struct mLACPPeerLinkInfoTLV* tlv)
{
    if (csm == NULL || tlv == NULL )
        return MCLAG_ERROR;

    if (!csm->peer_link_if)
    {
        ICCPD_LOG_DEBUG(__FUNCTION__, "peerlink port info from peer, local peerlink is not exist!");
        return 0;
    }

    if (csm->peer_link_if->type != tlv->port_type)
        ICCPD_LOG_DEBUG(__FUNCTION__, "peerlink port type of peer %d is not same with local %d !", tlv->port_type, csm->peer_link_if->type);

    if (tlv->port_type == IF_T_VXLAN && strncmp(csm->peer_itf_name, tlv->if_name, strlen(csm->peer_itf_name)))
        ICCPD_LOG_DEBUG(__FUNCTION__, "peerlink port is vxlan port and peerlink port at peer %s is not same with local peerlink port %s !", tlv->if_name, csm->peer_itf_name);

    return 0;
}

/*****************************************
* Heartbeat Update
*****************************************/
int mlacp_fsm_update_heartbeat(struct CSM* csm, struct mLACPHeartbeatTLV* tlv)
{
    if (!csm || !tlv)
        return MCLAG_ERROR;

    time(&csm->heartbeat_update_time);

    return 0;
}

/*****************************************
* warm-reboot flag Update
*****************************************/
int mlacp_fsm_update_warmboot(struct CSM* csm, struct mLACPWarmbootTLV* tlv)
{
    if (!csm || !tlv)
        return MCLAG_ERROR;

    time(&csm->peer_warm_reboot_time);
    ICCPD_LOG_DEBUG("ICCP_FSM", "RX peer warm reboot: start, sync_state %s",
        mlacp_state(csm));
    return 0;
}

