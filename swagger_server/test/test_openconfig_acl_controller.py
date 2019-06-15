# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.acl import Acl  # noqa: E501
from swagger_server.models.acl_acl_sets import AclAclSets  # noqa: E501
from swagger_server.models.acl_acl_sets_acl_set import AclAclSetsAclSet  # noqa: E501
from swagger_server.models.acl_entry_actions import AclEntryActions  # noqa: E501
from swagger_server.models.acl_entry_config import AclEntryConfig  # noqa: E501
from swagger_server.models.acl_entry_config_description import AclEntryConfigDescription  # noqa: E501
from swagger_server.models.acl_entry_input_interface import AclEntryInputInterface  # noqa: E501
from swagger_server.models.acl_entry_ipv4 import AclEntryIpv4  # noqa: E501
from swagger_server.models.acl_entry_ipv6 import AclEntryIpv6  # noqa: E501
from swagger_server.models.acl_entry_l2 import AclEntryL2  # noqa: E501
from swagger_server.models.acl_entry_transport import AclEntryTransport  # noqa: E501
from swagger_server.models.acl_interfaces import AclInterfaces  # noqa: E501
from swagger_server.models.acl_interfaces_interface import AclInterfacesInterface  # noqa: E501
from swagger_server.models.acl_set_acl_entries import AclSetAclEntries  # noqa: E501
from swagger_server.models.acl_set_acl_entries_acl_entry import AclSetAclEntriesAclEntry  # noqa: E501
from swagger_server.models.acl_set_config import AclSetConfig  # noqa: E501
from swagger_server.models.actions_config import ActionsConfig  # noqa: E501
from swagger_server.models.config_description import ConfigDescription  # noqa: E501
from swagger_server.models.config_destination_address import ConfigDestinationAddress  # noqa: E501
from swagger_server.models.config_destination_flow_label import ConfigDestinationFlowLabel  # noqa: E501
from swagger_server.models.config_destination_mac import ConfigDestinationMac  # noqa: E501
from swagger_server.models.config_destination_mac_mask import ConfigDestinationMacMask  # noqa: E501
from swagger_server.models.config_destination_port import ConfigDestinationPort  # noqa: E501
from swagger_server.models.config_dscp import ConfigDscp  # noqa: E501
from swagger_server.models.config_ethertype import ConfigEthertype  # noqa: E501
from swagger_server.models.config_forwarding_action import ConfigForwardingAction  # noqa: E501
from swagger_server.models.config_hop_limit import ConfigHopLimit  # noqa: E501
from swagger_server.models.config_id import ConfigId  # noqa: E501
from swagger_server.models.config_interface import ConfigInterface  # noqa: E501
from swagger_server.models.config_log_action import ConfigLogAction  # noqa: E501
from swagger_server.models.config_name import ConfigName  # noqa: E501
from swagger_server.models.config_protocol import ConfigProtocol  # noqa: E501
from swagger_server.models.config_sequence_id import ConfigSequenceId  # noqa: E501
from swagger_server.models.config_set_name import ConfigSetName  # noqa: E501
from swagger_server.models.config_source_address import ConfigSourceAddress  # noqa: E501
from swagger_server.models.config_source_flow_label import ConfigSourceFlowLabel  # noqa: E501
from swagger_server.models.config_source_mac import ConfigSourceMac  # noqa: E501
from swagger_server.models.config_source_mac_mask import ConfigSourceMacMask  # noqa: E501
from swagger_server.models.config_source_port import ConfigSourcePort  # noqa: E501
from swagger_server.models.config_subinterface import ConfigSubinterface  # noqa: E501
from swagger_server.models.config_tcp_flags import ConfigTcpFlags  # noqa: E501
from swagger_server.models.config_type import ConfigType  # noqa: E501
from swagger_server.models.egress_acl_set_config import EgressAclSetConfig  # noqa: E501
from swagger_server.models.egress_acl_set_config_set_name import EgressAclSetConfigSetName  # noqa: E501
from swagger_server.models.egress_acl_set_config_type import EgressAclSetConfigType  # noqa: E501
from swagger_server.models.get_acl import GetAcl  # noqa: E501
from swagger_server.models.get_acl_acl_sets import GetAclAclSets  # noqa: E501
from swagger_server.models.get_acl_acl_sets_acl_set import GetAclAclSetsAclSet  # noqa: E501
from swagger_server.models.get_acl_entries_acl_entry_state import GetAclEntriesAclEntryState  # noqa: E501
from swagger_server.models.get_acl_entries_acl_entry_state_matched_octets import GetAclEntriesAclEntryStateMatchedOctets  # noqa: E501
from swagger_server.models.get_acl_entries_acl_entry_state_matched_packets import GetAclEntriesAclEntryStateMatchedPackets  # noqa: E501
from swagger_server.models.get_acl_entries_acl_entry_state_sequence_id import GetAclEntriesAclEntryStateSequenceId  # noqa: E501
from swagger_server.models.get_acl_entry_actions import GetAclEntryActions  # noqa: E501
from swagger_server.models.get_acl_entry_config import GetAclEntryConfig  # noqa: E501
from swagger_server.models.get_acl_entry_config_description import GetAclEntryConfigDescription  # noqa: E501
from swagger_server.models.get_acl_entry_input_interface import GetAclEntryInputInterface  # noqa: E501
from swagger_server.models.get_acl_entry_ipv4 import GetAclEntryIpv4  # noqa: E501
from swagger_server.models.get_acl_entry_ipv6 import GetAclEntryIpv6  # noqa: E501
from swagger_server.models.get_acl_entry_l2 import GetAclEntryL2  # noqa: E501
from swagger_server.models.get_acl_entry_state import GetAclEntryState  # noqa: E501
from swagger_server.models.get_acl_entry_state_description import GetAclEntryStateDescription  # noqa: E501
from swagger_server.models.get_acl_entry_state_matched_octets import GetAclEntryStateMatchedOctets  # noqa: E501
from swagger_server.models.get_acl_entry_state_matched_packets import GetAclEntryStateMatchedPackets  # noqa: E501
from swagger_server.models.get_acl_entry_state_sequence_id import GetAclEntryStateSequenceId  # noqa: E501
from swagger_server.models.get_acl_entry_transport import GetAclEntryTransport  # noqa: E501
from swagger_server.models.get_acl_interfaces import GetAclInterfaces  # noqa: E501
from swagger_server.models.get_acl_interfaces_interface import GetAclInterfacesInterface  # noqa: E501
from swagger_server.models.get_acl_set_acl_entries import GetAclSetAclEntries  # noqa: E501
from swagger_server.models.get_acl_set_acl_entries_acl_entry import GetAclSetAclEntriesAclEntry  # noqa: E501
from swagger_server.models.get_acl_set_config import GetAclSetConfig  # noqa: E501
from swagger_server.models.get_acl_set_state import GetAclSetState  # noqa: E501
from swagger_server.models.get_acl_state import GetAclState  # noqa: E501
from swagger_server.models.get_actions_config import GetActionsConfig  # noqa: E501
from swagger_server.models.get_actions_state import GetActionsState  # noqa: E501
from swagger_server.models.get_config_description import GetConfigDescription  # noqa: E501
from swagger_server.models.get_config_destination_address import GetConfigDestinationAddress  # noqa: E501
from swagger_server.models.get_config_destination_flow_label import GetConfigDestinationFlowLabel  # noqa: E501
from swagger_server.models.get_config_destination_mac import GetConfigDestinationMac  # noqa: E501
from swagger_server.models.get_config_destination_mac_mask import GetConfigDestinationMacMask  # noqa: E501
from swagger_server.models.get_config_destination_port import GetConfigDestinationPort  # noqa: E501
from swagger_server.models.get_config_dscp import GetConfigDscp  # noqa: E501
from swagger_server.models.get_config_ethertype import GetConfigEthertype  # noqa: E501
from swagger_server.models.get_config_forwarding_action import GetConfigForwardingAction  # noqa: E501
from swagger_server.models.get_config_hop_limit import GetConfigHopLimit  # noqa: E501
from swagger_server.models.get_config_id import GetConfigId  # noqa: E501
from swagger_server.models.get_config_interface import GetConfigInterface  # noqa: E501
from swagger_server.models.get_config_log_action import GetConfigLogAction  # noqa: E501
from swagger_server.models.get_config_name import GetConfigName  # noqa: E501
from swagger_server.models.get_config_protocol import GetConfigProtocol  # noqa: E501
from swagger_server.models.get_config_sequence_id import GetConfigSequenceId  # noqa: E501
from swagger_server.models.get_config_set_name import GetConfigSetName  # noqa: E501
from swagger_server.models.get_config_source_address import GetConfigSourceAddress  # noqa: E501
from swagger_server.models.get_config_source_flow_label import GetConfigSourceFlowLabel  # noqa: E501
from swagger_server.models.get_config_source_mac import GetConfigSourceMac  # noqa: E501
from swagger_server.models.get_config_source_mac_mask import GetConfigSourceMacMask  # noqa: E501
from swagger_server.models.get_config_source_port import GetConfigSourcePort  # noqa: E501
from swagger_server.models.get_config_subinterface import GetConfigSubinterface  # noqa: E501
from swagger_server.models.get_config_tcp_flags import GetConfigTcpFlags  # noqa: E501
from swagger_server.models.get_config_type import GetConfigType  # noqa: E501
from swagger_server.models.get_egress_acl_set_acl_entries import GetEgressAclSetAclEntries  # noqa: E501
from swagger_server.models.get_egress_acl_set_acl_entries_acl_entry_state import GetEgressAclSetAclEntriesAclEntryState  # noqa: E501
from swagger_server.models.get_egress_acl_set_config import GetEgressAclSetConfig  # noqa: E501
from swagger_server.models.get_egress_acl_set_config_set_name import GetEgressAclSetConfigSetName  # noqa: E501
from swagger_server.models.get_egress_acl_set_config_type import GetEgressAclSetConfigType  # noqa: E501
from swagger_server.models.get_egress_acl_set_state import GetEgressAclSetState  # noqa: E501
from swagger_server.models.get_egress_acl_set_state_set_name import GetEgressAclSetStateSetName  # noqa: E501
from swagger_server.models.get_egress_acl_set_state_type import GetEgressAclSetStateType  # noqa: E501
from swagger_server.models.get_egress_acl_sets_egress_acl_set_acl_entries_acl_entry import GetEgressAclSetsEgressAclSetAclEntriesAclEntry  # noqa: E501
from swagger_server.models.get_ingress_acl_set_acl_entries import GetIngressAclSetAclEntries  # noqa: E501
from swagger_server.models.get_ingress_acl_set_config import GetIngressAclSetConfig  # noqa: E501
from swagger_server.models.get_ingress_acl_set_config_type import GetIngressAclSetConfigType  # noqa: E501
from swagger_server.models.get_ingress_acl_set_state import GetIngressAclSetState  # noqa: E501
from swagger_server.models.get_ingress_acl_set_state_type import GetIngressAclSetStateType  # noqa: E501
from swagger_server.models.get_ingress_acl_sets_ingress_acl_set_acl_entries_acl_entry import GetIngressAclSetsIngressAclSetAclEntriesAclEntry  # noqa: E501
from swagger_server.models.get_input_interface_interface_ref import GetInputInterfaceInterfaceRef  # noqa: E501
from swagger_server.models.get_interface_config import GetInterfaceConfig  # noqa: E501
from swagger_server.models.get_interface_egress_acl_sets import GetInterfaceEgressAclSets  # noqa: E501
from swagger_server.models.get_interface_egress_acl_sets_egress_acl_set import GetInterfaceEgressAclSetsEgressAclSet  # noqa: E501
from swagger_server.models.get_interface_ingress_acl_sets import GetInterfaceIngressAclSets  # noqa: E501
from swagger_server.models.get_interface_ingress_acl_sets_ingress_acl_set import GetInterfaceIngressAclSetsIngressAclSet  # noqa: E501
from swagger_server.models.get_interface_interface_ref import GetInterfaceInterfaceRef  # noqa: E501
from swagger_server.models.get_interface_interface_ref_config import GetInterfaceInterfaceRefConfig  # noqa: E501
from swagger_server.models.get_interface_interface_ref_state import GetInterfaceInterfaceRefState  # noqa: E501
from swagger_server.models.get_interface_ref_config import GetInterfaceRefConfig  # noqa: E501
from swagger_server.models.get_interface_ref_config_interface import GetInterfaceRefConfigInterface  # noqa: E501
from swagger_server.models.get_interface_ref_config_subinterface import GetInterfaceRefConfigSubinterface  # noqa: E501
from swagger_server.models.get_interface_ref_state import GetInterfaceRefState  # noqa: E501
from swagger_server.models.get_interface_ref_state_interface import GetInterfaceRefStateInterface  # noqa: E501
from swagger_server.models.get_interface_ref_state_subinterface import GetInterfaceRefStateSubinterface  # noqa: E501
from swagger_server.models.get_interface_state import GetInterfaceState  # noqa: E501
from swagger_server.models.get_ipv4_config import GetIpv4Config  # noqa: E501
from swagger_server.models.get_ipv4_state import GetIpv4State  # noqa: E501
from swagger_server.models.get_ipv6_config import GetIpv6Config  # noqa: E501
from swagger_server.models.get_ipv6_config_destination_address import GetIpv6ConfigDestinationAddress  # noqa: E501
from swagger_server.models.get_ipv6_config_dscp import GetIpv6ConfigDscp  # noqa: E501
from swagger_server.models.get_ipv6_config_hop_limit import GetIpv6ConfigHopLimit  # noqa: E501
from swagger_server.models.get_ipv6_config_protocol import GetIpv6ConfigProtocol  # noqa: E501
from swagger_server.models.get_ipv6_config_source_address import GetIpv6ConfigSourceAddress  # noqa: E501
from swagger_server.models.get_ipv6_state import GetIpv6State  # noqa: E501
from swagger_server.models.get_ipv6_state_destination_address import GetIpv6StateDestinationAddress  # noqa: E501
from swagger_server.models.get_ipv6_state_dscp import GetIpv6StateDscp  # noqa: E501
from swagger_server.models.get_ipv6_state_hop_limit import GetIpv6StateHopLimit  # noqa: E501
from swagger_server.models.get_ipv6_state_protocol import GetIpv6StateProtocol  # noqa: E501
from swagger_server.models.get_ipv6_state_source_address import GetIpv6StateSourceAddress  # noqa: E501
from swagger_server.models.get_l2_config import GetL2Config  # noqa: E501
from swagger_server.models.get_l2_state import GetL2State  # noqa: E501
from swagger_server.models.get_list_base_acl_entries_acl_entry import GetListBaseAclEntriesAclEntry  # noqa: E501
from swagger_server.models.get_list_base_acl_sets_acl_set import GetListBaseAclSetsAclSet  # noqa: E501
from swagger_server.models.get_list_base_egress_acl_set_acl_entries_acl_entry import GetListBaseEgressAclSetAclEntriesAclEntry  # noqa: E501
from swagger_server.models.get_list_base_egress_acl_sets_egress_acl_set import GetListBaseEgressAclSetsEgressAclSet  # noqa: E501
from swagger_server.models.get_list_base_ingress_acl_set_acl_entries_acl_entry import GetListBaseIngressAclSetAclEntriesAclEntry  # noqa: E501
from swagger_server.models.get_list_base_ingress_acl_sets_ingress_acl_set import GetListBaseIngressAclSetsIngressAclSet  # noqa: E501
from swagger_server.models.get_list_base_interfaces_interface import GetListBaseInterfacesInterface  # noqa: E501
from swagger_server.models.get_state_counter_capability import GetStateCounterCapability  # noqa: E501
from swagger_server.models.get_state_description import GetStateDescription  # noqa: E501
from swagger_server.models.get_state_destination_address import GetStateDestinationAddress  # noqa: E501
from swagger_server.models.get_state_destination_flow_label import GetStateDestinationFlowLabel  # noqa: E501
from swagger_server.models.get_state_destination_mac import GetStateDestinationMac  # noqa: E501
from swagger_server.models.get_state_destination_mac_mask import GetStateDestinationMacMask  # noqa: E501
from swagger_server.models.get_state_destination_port import GetStateDestinationPort  # noqa: E501
from swagger_server.models.get_state_dscp import GetStateDscp  # noqa: E501
from swagger_server.models.get_state_ethertype import GetStateEthertype  # noqa: E501
from swagger_server.models.get_state_forwarding_action import GetStateForwardingAction  # noqa: E501
from swagger_server.models.get_state_hop_limit import GetStateHopLimit  # noqa: E501
from swagger_server.models.get_state_id import GetStateId  # noqa: E501
from swagger_server.models.get_state_interface import GetStateInterface  # noqa: E501
from swagger_server.models.get_state_log_action import GetStateLogAction  # noqa: E501
from swagger_server.models.get_state_matched_octets import GetStateMatchedOctets  # noqa: E501
from swagger_server.models.get_state_matched_packets import GetStateMatchedPackets  # noqa: E501
from swagger_server.models.get_state_name import GetStateName  # noqa: E501
from swagger_server.models.get_state_protocol import GetStateProtocol  # noqa: E501
from swagger_server.models.get_state_sequence_id import GetStateSequenceId  # noqa: E501
from swagger_server.models.get_state_set_name import GetStateSetName  # noqa: E501
from swagger_server.models.get_state_source_address import GetStateSourceAddress  # noqa: E501
from swagger_server.models.get_state_source_flow_label import GetStateSourceFlowLabel  # noqa: E501
from swagger_server.models.get_state_source_mac import GetStateSourceMac  # noqa: E501
from swagger_server.models.get_state_source_mac_mask import GetStateSourceMacMask  # noqa: E501
from swagger_server.models.get_state_source_port import GetStateSourcePort  # noqa: E501
from swagger_server.models.get_state_subinterface import GetStateSubinterface  # noqa: E501
from swagger_server.models.get_state_tcp_flags import GetStateTcpFlags  # noqa: E501
from swagger_server.models.get_state_type import GetStateType  # noqa: E501
from swagger_server.models.get_transport_config import GetTransportConfig  # noqa: E501
from swagger_server.models.get_transport_state import GetTransportState  # noqa: E501
from swagger_server.models.ingress_acl_set_config import IngressAclSetConfig  # noqa: E501
from swagger_server.models.ingress_acl_set_config_type import IngressAclSetConfigType  # noqa: E501
from swagger_server.models.input_interface_interface_ref import InputInterfaceInterfaceRef  # noqa: E501
from swagger_server.models.interface_config import InterfaceConfig  # noqa: E501
from swagger_server.models.interface_egress_acl_sets import InterfaceEgressAclSets  # noqa: E501
from swagger_server.models.interface_egress_acl_sets_egress_acl_set import InterfaceEgressAclSetsEgressAclSet  # noqa: E501
from swagger_server.models.interface_ingress_acl_sets import InterfaceIngressAclSets  # noqa: E501
from swagger_server.models.interface_ingress_acl_sets_ingress_acl_set import InterfaceIngressAclSetsIngressAclSet  # noqa: E501
from swagger_server.models.interface_interface_ref import InterfaceInterfaceRef  # noqa: E501
from swagger_server.models.interface_interface_ref_config import InterfaceInterfaceRefConfig  # noqa: E501
from swagger_server.models.interface_ref_config import InterfaceRefConfig  # noqa: E501
from swagger_server.models.interface_ref_config_interface import InterfaceRefConfigInterface  # noqa: E501
from swagger_server.models.interface_ref_config_subinterface import InterfaceRefConfigSubinterface  # noqa: E501
from swagger_server.models.ipv4_config import Ipv4Config  # noqa: E501
from swagger_server.models.ipv6_config import Ipv6Config  # noqa: E501
from swagger_server.models.ipv6_config_destination_address import Ipv6ConfigDestinationAddress  # noqa: E501
from swagger_server.models.ipv6_config_dscp import Ipv6ConfigDscp  # noqa: E501
from swagger_server.models.ipv6_config_hop_limit import Ipv6ConfigHopLimit  # noqa: E501
from swagger_server.models.ipv6_config_protocol import Ipv6ConfigProtocol  # noqa: E501
from swagger_server.models.ipv6_config_source_address import Ipv6ConfigSourceAddress  # noqa: E501
from swagger_server.models.l2_config import L2Config  # noqa: E501
from swagger_server.models.list_base_acl_entries_acl_entry import ListBaseAclEntriesAclEntry  # noqa: E501
from swagger_server.models.list_base_acl_sets_acl_set import ListBaseAclSetsAclSet  # noqa: E501
from swagger_server.models.list_base_egress_acl_sets_egress_acl_set import ListBaseEgressAclSetsEgressAclSet  # noqa: E501
from swagger_server.models.list_base_ingress_acl_sets_ingress_acl_set import ListBaseIngressAclSetsIngressAclSet  # noqa: E501
from swagger_server.models.list_base_interfaces_interface import ListBaseInterfacesInterface  # noqa: E501
from swagger_server.models.patch_acl import PatchAcl  # noqa: E501
from swagger_server.models.patch_acl_acl_sets import PatchAclAclSets  # noqa: E501
from swagger_server.models.patch_acl_acl_sets_acl_set import PatchAclAclSetsAclSet  # noqa: E501
from swagger_server.models.patch_acl_entry_actions import PatchAclEntryActions  # noqa: E501
from swagger_server.models.patch_acl_entry_config import PatchAclEntryConfig  # noqa: E501
from swagger_server.models.patch_acl_entry_config_description import PatchAclEntryConfigDescription  # noqa: E501
from swagger_server.models.patch_acl_entry_input_interface import PatchAclEntryInputInterface  # noqa: E501
from swagger_server.models.patch_acl_entry_ipv4 import PatchAclEntryIpv4  # noqa: E501
from swagger_server.models.patch_acl_entry_ipv6 import PatchAclEntryIpv6  # noqa: E501
from swagger_server.models.patch_acl_entry_l2 import PatchAclEntryL2  # noqa: E501
from swagger_server.models.patch_acl_entry_transport import PatchAclEntryTransport  # noqa: E501
from swagger_server.models.patch_acl_interfaces import PatchAclInterfaces  # noqa: E501
from swagger_server.models.patch_acl_interfaces_interface import PatchAclInterfacesInterface  # noqa: E501
from swagger_server.models.patch_acl_set_acl_entries import PatchAclSetAclEntries  # noqa: E501
from swagger_server.models.patch_acl_set_acl_entries_acl_entry import PatchAclSetAclEntriesAclEntry  # noqa: E501
from swagger_server.models.patch_acl_set_config import PatchAclSetConfig  # noqa: E501
from swagger_server.models.patch_actions_config import PatchActionsConfig  # noqa: E501
from swagger_server.models.patch_config_description import PatchConfigDescription  # noqa: E501
from swagger_server.models.patch_config_destination_address import PatchConfigDestinationAddress  # noqa: E501
from swagger_server.models.patch_config_destination_flow_label import PatchConfigDestinationFlowLabel  # noqa: E501
from swagger_server.models.patch_config_destination_mac import PatchConfigDestinationMac  # noqa: E501
from swagger_server.models.patch_config_destination_mac_mask import PatchConfigDestinationMacMask  # noqa: E501
from swagger_server.models.patch_config_destination_port import PatchConfigDestinationPort  # noqa: E501
from swagger_server.models.patch_config_dscp import PatchConfigDscp  # noqa: E501
from swagger_server.models.patch_config_ethertype import PatchConfigEthertype  # noqa: E501
from swagger_server.models.patch_config_forwarding_action import PatchConfigForwardingAction  # noqa: E501
from swagger_server.models.patch_config_hop_limit import PatchConfigHopLimit  # noqa: E501
from swagger_server.models.patch_config_id import PatchConfigId  # noqa: E501
from swagger_server.models.patch_config_interface import PatchConfigInterface  # noqa: E501
from swagger_server.models.patch_config_log_action import PatchConfigLogAction  # noqa: E501
from swagger_server.models.patch_config_name import PatchConfigName  # noqa: E501
from swagger_server.models.patch_config_protocol import PatchConfigProtocol  # noqa: E501
from swagger_server.models.patch_config_sequence_id import PatchConfigSequenceId  # noqa: E501
from swagger_server.models.patch_config_set_name import PatchConfigSetName  # noqa: E501
from swagger_server.models.patch_config_source_address import PatchConfigSourceAddress  # noqa: E501
from swagger_server.models.patch_config_source_flow_label import PatchConfigSourceFlowLabel  # noqa: E501
from swagger_server.models.patch_config_source_mac import PatchConfigSourceMac  # noqa: E501
from swagger_server.models.patch_config_source_mac_mask import PatchConfigSourceMacMask  # noqa: E501
from swagger_server.models.patch_config_source_port import PatchConfigSourcePort  # noqa: E501
from swagger_server.models.patch_config_subinterface import PatchConfigSubinterface  # noqa: E501
from swagger_server.models.patch_config_tcp_flags import PatchConfigTcpFlags  # noqa: E501
from swagger_server.models.patch_config_type import PatchConfigType  # noqa: E501
from swagger_server.models.patch_egress_acl_set_config import PatchEgressAclSetConfig  # noqa: E501
from swagger_server.models.patch_egress_acl_set_config_set_name import PatchEgressAclSetConfigSetName  # noqa: E501
from swagger_server.models.patch_egress_acl_set_config_type import PatchEgressAclSetConfigType  # noqa: E501
from swagger_server.models.patch_ingress_acl_set_config import PatchIngressAclSetConfig  # noqa: E501
from swagger_server.models.patch_ingress_acl_set_config_type import PatchIngressAclSetConfigType  # noqa: E501
from swagger_server.models.patch_input_interface_interface_ref import PatchInputInterfaceInterfaceRef  # noqa: E501
from swagger_server.models.patch_interface_config import PatchInterfaceConfig  # noqa: E501
from swagger_server.models.patch_interface_egress_acl_sets import PatchInterfaceEgressAclSets  # noqa: E501
from swagger_server.models.patch_interface_egress_acl_sets_egress_acl_set import PatchInterfaceEgressAclSetsEgressAclSet  # noqa: E501
from swagger_server.models.patch_interface_ingress_acl_sets import PatchInterfaceIngressAclSets  # noqa: E501
from swagger_server.models.patch_interface_ingress_acl_sets_ingress_acl_set import PatchInterfaceIngressAclSetsIngressAclSet  # noqa: E501
from swagger_server.models.patch_interface_interface_ref import PatchInterfaceInterfaceRef  # noqa: E501
from swagger_server.models.patch_interface_interface_ref_config import PatchInterfaceInterfaceRefConfig  # noqa: E501
from swagger_server.models.patch_interface_ref_config import PatchInterfaceRefConfig  # noqa: E501
from swagger_server.models.patch_interface_ref_config_interface import PatchInterfaceRefConfigInterface  # noqa: E501
from swagger_server.models.patch_interface_ref_config_subinterface import PatchInterfaceRefConfigSubinterface  # noqa: E501
from swagger_server.models.patch_ipv4_config import PatchIpv4Config  # noqa: E501
from swagger_server.models.patch_ipv6_config import PatchIpv6Config  # noqa: E501
from swagger_server.models.patch_ipv6_config_destination_address import PatchIpv6ConfigDestinationAddress  # noqa: E501
from swagger_server.models.patch_ipv6_config_dscp import PatchIpv6ConfigDscp  # noqa: E501
from swagger_server.models.patch_ipv6_config_hop_limit import PatchIpv6ConfigHopLimit  # noqa: E501
from swagger_server.models.patch_ipv6_config_protocol import PatchIpv6ConfigProtocol  # noqa: E501
from swagger_server.models.patch_ipv6_config_source_address import PatchIpv6ConfigSourceAddress  # noqa: E501
from swagger_server.models.patch_l2_config import PatchL2Config  # noqa: E501
from swagger_server.models.patch_list_base_acl_entries_acl_entry import PatchListBaseAclEntriesAclEntry  # noqa: E501
from swagger_server.models.patch_list_base_acl_sets_acl_set import PatchListBaseAclSetsAclSet  # noqa: E501
from swagger_server.models.patch_list_base_egress_acl_sets_egress_acl_set import PatchListBaseEgressAclSetsEgressAclSet  # noqa: E501
from swagger_server.models.patch_list_base_ingress_acl_sets_ingress_acl_set import PatchListBaseIngressAclSetsIngressAclSet  # noqa: E501
from swagger_server.models.patch_list_base_interfaces_interface import PatchListBaseInterfacesInterface  # noqa: E501
from swagger_server.models.patch_transport_config import PatchTransportConfig  # noqa: E501
from swagger_server.models.post_acl_acl_sets import PostAclAclSets  # noqa: E501
from swagger_server.models.post_acl_entry_config import PostAclEntryConfig  # noqa: E501
from swagger_server.models.post_acl_set_config import PostAclSetConfig  # noqa: E501
from swagger_server.models.post_actions_config import PostActionsConfig  # noqa: E501
from swagger_server.models.post_config_forwarding_action import PostConfigForwardingAction  # noqa: E501
from swagger_server.models.post_config_id import PostConfigId  # noqa: E501
from swagger_server.models.post_config_interface import PostConfigInterface  # noqa: E501
from swagger_server.models.post_config_name import PostConfigName  # noqa: E501
from swagger_server.models.post_config_sequence_id import PostConfigSequenceId  # noqa: E501
from swagger_server.models.post_config_set_name import PostConfigSetName  # noqa: E501
from swagger_server.models.post_config_source_address import PostConfigSourceAddress  # noqa: E501
from swagger_server.models.post_config_source_mac import PostConfigSourceMac  # noqa: E501
from swagger_server.models.post_config_source_port import PostConfigSourcePort  # noqa: E501
from swagger_server.models.post_egress_acl_set_config import PostEgressAclSetConfig  # noqa: E501
from swagger_server.models.post_egress_acl_set_config_set_name import PostEgressAclSetConfigSetName  # noqa: E501
from swagger_server.models.post_ingress_acl_set_config import PostIngressAclSetConfig  # noqa: E501
from swagger_server.models.post_input_interface_interface_ref import PostInputInterfaceInterfaceRef  # noqa: E501
from swagger_server.models.post_interface_config import PostInterfaceConfig  # noqa: E501
from swagger_server.models.post_interface_interface_ref_config import PostInterfaceInterfaceRefConfig  # noqa: E501
from swagger_server.models.post_interface_ref_config import PostInterfaceRefConfig  # noqa: E501
from swagger_server.models.post_interface_ref_config_interface import PostInterfaceRefConfigInterface  # noqa: E501
from swagger_server.models.post_ipv4_config import PostIpv4Config  # noqa: E501
from swagger_server.models.post_ipv6_config import PostIpv6Config  # noqa: E501
from swagger_server.models.post_ipv6_config_source_address import PostIpv6ConfigSourceAddress  # noqa: E501
from swagger_server.models.post_l2_config import PostL2Config  # noqa: E501
from swagger_server.models.post_list_base_acl_entries_acl_entry import PostListBaseAclEntriesAclEntry  # noqa: E501
from swagger_server.models.post_list_base_acl_sets_acl_set import PostListBaseAclSetsAclSet  # noqa: E501
from swagger_server.models.post_list_base_egress_acl_sets_egress_acl_set import PostListBaseEgressAclSetsEgressAclSet  # noqa: E501
from swagger_server.models.post_list_base_ingress_acl_sets_ingress_acl_set import PostListBaseIngressAclSetsIngressAclSet  # noqa: E501
from swagger_server.models.post_list_base_interfaces_interface import PostListBaseInterfacesInterface  # noqa: E501
from swagger_server.models.post_transport_config import PostTransportConfig  # noqa: E501
from swagger_server.models.put_acl import PutAcl  # noqa: E501
from swagger_server.models.put_acl_acl_sets import PutAclAclSets  # noqa: E501
from swagger_server.models.put_acl_acl_sets_acl_set import PutAclAclSetsAclSet  # noqa: E501
from swagger_server.models.put_acl_entry_actions import PutAclEntryActions  # noqa: E501
from swagger_server.models.put_acl_entry_config import PutAclEntryConfig  # noqa: E501
from swagger_server.models.put_acl_entry_config_description import PutAclEntryConfigDescription  # noqa: E501
from swagger_server.models.put_acl_entry_input_interface import PutAclEntryInputInterface  # noqa: E501
from swagger_server.models.put_acl_entry_ipv4 import PutAclEntryIpv4  # noqa: E501
from swagger_server.models.put_acl_entry_ipv6 import PutAclEntryIpv6  # noqa: E501
from swagger_server.models.put_acl_entry_l2 import PutAclEntryL2  # noqa: E501
from swagger_server.models.put_acl_entry_transport import PutAclEntryTransport  # noqa: E501
from swagger_server.models.put_acl_interfaces import PutAclInterfaces  # noqa: E501
from swagger_server.models.put_acl_interfaces_interface import PutAclInterfacesInterface  # noqa: E501
from swagger_server.models.put_acl_set_acl_entries import PutAclSetAclEntries  # noqa: E501
from swagger_server.models.put_acl_set_acl_entries_acl_entry import PutAclSetAclEntriesAclEntry  # noqa: E501
from swagger_server.models.put_acl_set_config import PutAclSetConfig  # noqa: E501
from swagger_server.models.put_actions_config import PutActionsConfig  # noqa: E501
from swagger_server.models.put_config_description import PutConfigDescription  # noqa: E501
from swagger_server.models.put_config_destination_address import PutConfigDestinationAddress  # noqa: E501
from swagger_server.models.put_config_destination_flow_label import PutConfigDestinationFlowLabel  # noqa: E501
from swagger_server.models.put_config_destination_mac import PutConfigDestinationMac  # noqa: E501
from swagger_server.models.put_config_destination_mac_mask import PutConfigDestinationMacMask  # noqa: E501
from swagger_server.models.put_config_destination_port import PutConfigDestinationPort  # noqa: E501
from swagger_server.models.put_config_dscp import PutConfigDscp  # noqa: E501
from swagger_server.models.put_config_ethertype import PutConfigEthertype  # noqa: E501
from swagger_server.models.put_config_forwarding_action import PutConfigForwardingAction  # noqa: E501
from swagger_server.models.put_config_hop_limit import PutConfigHopLimit  # noqa: E501
from swagger_server.models.put_config_id import PutConfigId  # noqa: E501
from swagger_server.models.put_config_interface import PutConfigInterface  # noqa: E501
from swagger_server.models.put_config_log_action import PutConfigLogAction  # noqa: E501
from swagger_server.models.put_config_name import PutConfigName  # noqa: E501
from swagger_server.models.put_config_protocol import PutConfigProtocol  # noqa: E501
from swagger_server.models.put_config_sequence_id import PutConfigSequenceId  # noqa: E501
from swagger_server.models.put_config_set_name import PutConfigSetName  # noqa: E501
from swagger_server.models.put_config_source_address import PutConfigSourceAddress  # noqa: E501
from swagger_server.models.put_config_source_flow_label import PutConfigSourceFlowLabel  # noqa: E501
from swagger_server.models.put_config_source_mac import PutConfigSourceMac  # noqa: E501
from swagger_server.models.put_config_source_mac_mask import PutConfigSourceMacMask  # noqa: E501
from swagger_server.models.put_config_source_port import PutConfigSourcePort  # noqa: E501
from swagger_server.models.put_config_subinterface import PutConfigSubinterface  # noqa: E501
from swagger_server.models.put_config_tcp_flags import PutConfigTcpFlags  # noqa: E501
from swagger_server.models.put_config_type import PutConfigType  # noqa: E501
from swagger_server.models.put_egress_acl_set_config import PutEgressAclSetConfig  # noqa: E501
from swagger_server.models.put_egress_acl_set_config_set_name import PutEgressAclSetConfigSetName  # noqa: E501
from swagger_server.models.put_egress_acl_set_config_type import PutEgressAclSetConfigType  # noqa: E501
from swagger_server.models.put_ingress_acl_set_config import PutIngressAclSetConfig  # noqa: E501
from swagger_server.models.put_ingress_acl_set_config_type import PutIngressAclSetConfigType  # noqa: E501
from swagger_server.models.put_input_interface_interface_ref import PutInputInterfaceInterfaceRef  # noqa: E501
from swagger_server.models.put_interface_config import PutInterfaceConfig  # noqa: E501
from swagger_server.models.put_interface_egress_acl_sets import PutInterfaceEgressAclSets  # noqa: E501
from swagger_server.models.put_interface_egress_acl_sets_egress_acl_set import PutInterfaceEgressAclSetsEgressAclSet  # noqa: E501
from swagger_server.models.put_interface_ingress_acl_sets import PutInterfaceIngressAclSets  # noqa: E501
from swagger_server.models.put_interface_ingress_acl_sets_ingress_acl_set import PutInterfaceIngressAclSetsIngressAclSet  # noqa: E501
from swagger_server.models.put_interface_interface_ref import PutInterfaceInterfaceRef  # noqa: E501
from swagger_server.models.put_interface_interface_ref_config import PutInterfaceInterfaceRefConfig  # noqa: E501
from swagger_server.models.put_interface_ref_config import PutInterfaceRefConfig  # noqa: E501
from swagger_server.models.put_interface_ref_config_interface import PutInterfaceRefConfigInterface  # noqa: E501
from swagger_server.models.put_interface_ref_config_subinterface import PutInterfaceRefConfigSubinterface  # noqa: E501
from swagger_server.models.put_ipv4_config import PutIpv4Config  # noqa: E501
from swagger_server.models.put_ipv6_config import PutIpv6Config  # noqa: E501
from swagger_server.models.put_ipv6_config_destination_address import PutIpv6ConfigDestinationAddress  # noqa: E501
from swagger_server.models.put_ipv6_config_dscp import PutIpv6ConfigDscp  # noqa: E501
from swagger_server.models.put_ipv6_config_hop_limit import PutIpv6ConfigHopLimit  # noqa: E501
from swagger_server.models.put_ipv6_config_protocol import PutIpv6ConfigProtocol  # noqa: E501
from swagger_server.models.put_ipv6_config_source_address import PutIpv6ConfigSourceAddress  # noqa: E501
from swagger_server.models.put_l2_config import PutL2Config  # noqa: E501
from swagger_server.models.put_list_base_acl_entries_acl_entry import PutListBaseAclEntriesAclEntry  # noqa: E501
from swagger_server.models.put_list_base_acl_sets_acl_set import PutListBaseAclSetsAclSet  # noqa: E501
from swagger_server.models.put_list_base_egress_acl_sets_egress_acl_set import PutListBaseEgressAclSetsEgressAclSet  # noqa: E501
from swagger_server.models.put_list_base_ingress_acl_sets_ingress_acl_set import PutListBaseIngressAclSetsIngressAclSet  # noqa: E501
from swagger_server.models.put_list_base_interfaces_interface import PutListBaseInterfacesInterface  # noqa: E501
from swagger_server.models.put_transport_config import PutTransportConfig  # noqa: E501
from swagger_server.models.transport_config import TransportConfig  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOpenconfigAclController(BaseTestCase):
    """OpenconfigAclController integration test stubs"""

    def test_delete_acl(self):
        """Test case for delete_acl

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_acl_acl_sets(self):
        """Test case for delete_acl_acl_sets

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_acl_acl_sets_acl_set(self):
        """Test case for delete_acl_acl_sets_acl_set

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}'.format(name='name_example', type='type_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_acl_entry_actions(self):
        """Test case for delete_acl_entry_actions

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/actions'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_acl_entry_config(self):
        """Test case for delete_acl_entry_config

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_acl_entry_config_description(self):
        """Test case for delete_acl_entry_config_description

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/config/description'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_acl_entry_input_interface(self):
        """Test case for delete_acl_entry_input_interface

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/input-interface'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_acl_entry_ipv4(self):
        """Test case for delete_acl_entry_ipv4

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_acl_entry_ipv6(self):
        """Test case for delete_acl_entry_ipv6

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_acl_entry_l2(self):
        """Test case for delete_acl_entry_l2

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_acl_entry_transport(self):
        """Test case for delete_acl_entry_transport

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/transport'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_acl_interfaces(self):
        """Test case for delete_acl_interfaces

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_acl_interfaces_interface(self):
        """Test case for delete_acl_interfaces_interface

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_acl_set_acl_entries(self):
        """Test case for delete_acl_set_acl_entries

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries'.format(name='name_example', type='type_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_acl_set_acl_entries_acl_entry(self):
        """Test case for delete_acl_set_acl_entries_acl_entry

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_acl_set_config(self):
        """Test case for delete_acl_set_config

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/config'.format(name='name_example', type='type_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_actions_config(self):
        """Test case for delete_actions_config

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/actions/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_config_description(self):
        """Test case for delete_config_description

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/config/description'.format(name='name_example', type='type_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_config_destination_address(self):
        """Test case for delete_config_destination_address

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/config/destination-address'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_config_destination_flow_label(self):
        """Test case for delete_config_destination_flow_label

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/destination-flow-label'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_config_destination_mac(self):
        """Test case for delete_config_destination_mac

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/config/destination-mac'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_config_destination_mac_mask(self):
        """Test case for delete_config_destination_mac_mask

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/config/destination-mac-mask'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_config_destination_port(self):
        """Test case for delete_config_destination_port

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/transport/config/destination-port'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_config_dscp(self):
        """Test case for delete_config_dscp

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/config/dscp'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_config_ethertype(self):
        """Test case for delete_config_ethertype

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/config/ethertype'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_config_forwarding_action(self):
        """Test case for delete_config_forwarding_action

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/actions/config/forwarding-action'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_config_hop_limit(self):
        """Test case for delete_config_hop_limit

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/config/hop-limit'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_config_id(self):
        """Test case for delete_config_id

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/config/id'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_config_interface(self):
        """Test case for delete_config_interface

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/input-interface/interface-ref/config/interface'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_config_log_action(self):
        """Test case for delete_config_log_action

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/actions/config/log-action'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_config_name(self):
        """Test case for delete_config_name

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/config/name'.format(name='name_example', type='type_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_config_protocol(self):
        """Test case for delete_config_protocol

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/config/protocol'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_config_sequence_id(self):
        """Test case for delete_config_sequence_id

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/config/sequence-id'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_config_set_name(self):
        """Test case for delete_config_set_name

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}/config/set-name'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_config_source_address(self):
        """Test case for delete_config_source_address

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/config/source-address'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_config_source_flow_label(self):
        """Test case for delete_config_source_flow_label

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/source-flow-label'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_config_source_mac(self):
        """Test case for delete_config_source_mac

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/config/source-mac'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_config_source_mac_mask(self):
        """Test case for delete_config_source_mac_mask

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/config/source-mac-mask'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_config_source_port(self):
        """Test case for delete_config_source_port

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/transport/config/source-port'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_config_subinterface(self):
        """Test case for delete_config_subinterface

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/input-interface/interface-ref/config/subinterface'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_config_tcp_flags(self):
        """Test case for delete_config_tcp_flags

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/transport/config/tcp-flags'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_config_type(self):
        """Test case for delete_config_type

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/config/type'.format(name='name_example', type='type_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_egress_acl_set_config(self):
        """Test case for delete_egress_acl_set_config

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}/config'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_egress_acl_set_config_set_name(self):
        """Test case for delete_egress_acl_set_config_set_name

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}/config/set-name'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_egress_acl_set_config_type(self):
        """Test case for delete_egress_acl_set_config_type

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}/config/type'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_ingress_acl_set_config(self):
        """Test case for delete_ingress_acl_set_config

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}/config'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_ingress_acl_set_config_type(self):
        """Test case for delete_ingress_acl_set_config_type

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}/config/type'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_input_interface_interface_ref(self):
        """Test case for delete_input_interface_interface_ref

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/input-interface/interface-ref'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_interface_config(self):
        """Test case for delete_interface_config

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/config'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_interface_egress_acl_sets(self):
        """Test case for delete_interface_egress_acl_sets

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_interface_egress_acl_sets_egress_acl_set(self):
        """Test case for delete_interface_egress_acl_sets_egress_acl_set

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_interface_ingress_acl_sets(self):
        """Test case for delete_interface_ingress_acl_sets

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_interface_ingress_acl_sets_ingress_acl_set(self):
        """Test case for delete_interface_ingress_acl_sets_ingress_acl_set

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_interface_interface_ref(self):
        """Test case for delete_interface_interface_ref

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/interface-ref'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_interface_interface_ref_config(self):
        """Test case for delete_interface_interface_ref_config

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/interface-ref/config'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_interface_ref_config(self):
        """Test case for delete_interface_ref_config

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/input-interface/interface-ref/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_interface_ref_config_interface(self):
        """Test case for delete_interface_ref_config_interface

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/interface-ref/config/interface'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_interface_ref_config_subinterface(self):
        """Test case for delete_interface_ref_config_subinterface

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/interface-ref/config/subinterface'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_ipv4_config(self):
        """Test case for delete_ipv4_config

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_ipv6_config(self):
        """Test case for delete_ipv6_config

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_ipv6_config_destination_address(self):
        """Test case for delete_ipv6_config_destination_address

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/destination-address'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_ipv6_config_dscp(self):
        """Test case for delete_ipv6_config_dscp

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/dscp'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_ipv6_config_hop_limit(self):
        """Test case for delete_ipv6_config_hop_limit

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/hop-limit'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_ipv6_config_protocol(self):
        """Test case for delete_ipv6_config_protocol

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/protocol'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_ipv6_config_source_address(self):
        """Test case for delete_ipv6_config_source_address

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/source-address'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_l2_config(self):
        """Test case for delete_l2_config

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_list_base_acl_entries_acl_entry(self):
        """Test case for delete_list_base_acl_entries_acl_entry

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry'.format(name='name_example', type='type_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_list_base_acl_sets_acl_set(self):
        """Test case for delete_list_base_acl_sets_acl_set

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_list_base_egress_acl_sets_egress_acl_set(self):
        """Test case for delete_list_base_egress_acl_sets_egress_acl_set

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_list_base_ingress_acl_sets_ingress_acl_set(self):
        """Test case for delete_list_base_ingress_acl_sets_ingress_acl_set

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_list_base_interfaces_interface(self):
        """Test case for delete_list_base_interfaces_interface

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_transport_config(self):
        """Test case for delete_transport_config

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/transport/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acl(self):
        """Test case for get_acl

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acl_acl_sets(self):
        """Test case for get_acl_acl_sets

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acl_acl_sets_acl_set(self):
        """Test case for get_acl_acl_sets_acl_set

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}'.format(name='name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acl_entries_acl_entry_state(self):
        """Test case for get_acl_entries_acl_entry_state

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}/acl-entries/acl-entry={sequence_id}/state'.format(id='id_example', set_name='set_name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acl_entries_acl_entry_state_matched_octets(self):
        """Test case for get_acl_entries_acl_entry_state_matched_octets

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}/acl-entries/acl-entry={sequence_id}/state/matched-octets'.format(id='id_example', set_name='set_name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acl_entries_acl_entry_state_matched_packets(self):
        """Test case for get_acl_entries_acl_entry_state_matched_packets

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}/acl-entries/acl-entry={sequence_id}/state/matched-packets'.format(id='id_example', set_name='set_name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acl_entries_acl_entry_state_sequence_id(self):
        """Test case for get_acl_entries_acl_entry_state_sequence_id

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}/acl-entries/acl-entry={sequence_id}/state/sequence-id'.format(id='id_example', set_name='set_name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acl_entry_actions(self):
        """Test case for get_acl_entry_actions

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/actions'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acl_entry_config(self):
        """Test case for get_acl_entry_config

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acl_entry_config_description(self):
        """Test case for get_acl_entry_config_description

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/config/description'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acl_entry_input_interface(self):
        """Test case for get_acl_entry_input_interface

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/input-interface'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acl_entry_ipv4(self):
        """Test case for get_acl_entry_ipv4

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acl_entry_ipv6(self):
        """Test case for get_acl_entry_ipv6

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acl_entry_l2(self):
        """Test case for get_acl_entry_l2

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acl_entry_state(self):
        """Test case for get_acl_entry_state

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/state'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acl_entry_state_description(self):
        """Test case for get_acl_entry_state_description

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/state/description'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acl_entry_state_matched_octets(self):
        """Test case for get_acl_entry_state_matched_octets

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}/acl-entries/acl-entry={sequence_id}/state/matched-octets'.format(id='id_example', set_name='set_name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acl_entry_state_matched_packets(self):
        """Test case for get_acl_entry_state_matched_packets

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}/acl-entries/acl-entry={sequence_id}/state/matched-packets'.format(id='id_example', set_name='set_name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acl_entry_state_sequence_id(self):
        """Test case for get_acl_entry_state_sequence_id

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}/acl-entries/acl-entry={sequence_id}/state/sequence-id'.format(id='id_example', set_name='set_name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acl_entry_transport(self):
        """Test case for get_acl_entry_transport

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/transport'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acl_interfaces(self):
        """Test case for get_acl_interfaces

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acl_interfaces_interface(self):
        """Test case for get_acl_interfaces_interface

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acl_set_acl_entries(self):
        """Test case for get_acl_set_acl_entries

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries'.format(name='name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acl_set_acl_entries_acl_entry(self):
        """Test case for get_acl_set_acl_entries_acl_entry

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acl_set_config(self):
        """Test case for get_acl_set_config

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/config'.format(name='name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acl_set_state(self):
        """Test case for get_acl_set_state

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/state'.format(name='name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acl_state(self):
        """Test case for get_acl_state

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/state',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_actions_config(self):
        """Test case for get_actions_config

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/actions/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_actions_state(self):
        """Test case for get_actions_state

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/actions/state'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_config_description(self):
        """Test case for get_config_description

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/config/description'.format(name='name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_config_destination_address(self):
        """Test case for get_config_destination_address

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/config/destination-address'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_config_destination_flow_label(self):
        """Test case for get_config_destination_flow_label

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/destination-flow-label'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_config_destination_mac(self):
        """Test case for get_config_destination_mac

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/config/destination-mac'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_config_destination_mac_mask(self):
        """Test case for get_config_destination_mac_mask

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/config/destination-mac-mask'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_config_destination_port(self):
        """Test case for get_config_destination_port

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/transport/config/destination-port'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_config_dscp(self):
        """Test case for get_config_dscp

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/config/dscp'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_config_ethertype(self):
        """Test case for get_config_ethertype

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/config/ethertype'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_config_forwarding_action(self):
        """Test case for get_config_forwarding_action

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/actions/config/forwarding-action'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_config_hop_limit(self):
        """Test case for get_config_hop_limit

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/config/hop-limit'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_config_id(self):
        """Test case for get_config_id

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/config/id'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_config_interface(self):
        """Test case for get_config_interface

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/input-interface/interface-ref/config/interface'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_config_log_action(self):
        """Test case for get_config_log_action

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/actions/config/log-action'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_config_name(self):
        """Test case for get_config_name

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/config/name'.format(name='name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_config_protocol(self):
        """Test case for get_config_protocol

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/config/protocol'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_config_sequence_id(self):
        """Test case for get_config_sequence_id

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/config/sequence-id'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_config_set_name(self):
        """Test case for get_config_set_name

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}/config/set-name'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_config_source_address(self):
        """Test case for get_config_source_address

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/config/source-address'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_config_source_flow_label(self):
        """Test case for get_config_source_flow_label

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/source-flow-label'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_config_source_mac(self):
        """Test case for get_config_source_mac

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/config/source-mac'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_config_source_mac_mask(self):
        """Test case for get_config_source_mac_mask

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/config/source-mac-mask'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_config_source_port(self):
        """Test case for get_config_source_port

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/transport/config/source-port'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_config_subinterface(self):
        """Test case for get_config_subinterface

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/input-interface/interface-ref/config/subinterface'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_config_tcp_flags(self):
        """Test case for get_config_tcp_flags

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/transport/config/tcp-flags'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_config_type(self):
        """Test case for get_config_type

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/config/type'.format(name='name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_egress_acl_set_acl_entries(self):
        """Test case for get_egress_acl_set_acl_entries

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}/acl-entries'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_egress_acl_set_acl_entries_acl_entry_state(self):
        """Test case for get_egress_acl_set_acl_entries_acl_entry_state

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}/acl-entries/acl-entry={sequence_id}/state'.format(id='id_example', set_name='set_name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_egress_acl_set_config(self):
        """Test case for get_egress_acl_set_config

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}/config'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_egress_acl_set_config_set_name(self):
        """Test case for get_egress_acl_set_config_set_name

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}/config/set-name'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_egress_acl_set_config_type(self):
        """Test case for get_egress_acl_set_config_type

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}/config/type'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_egress_acl_set_state(self):
        """Test case for get_egress_acl_set_state

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}/state'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_egress_acl_set_state_set_name(self):
        """Test case for get_egress_acl_set_state_set_name

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}/state/set-name'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_egress_acl_set_state_type(self):
        """Test case for get_egress_acl_set_state_type

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}/state/type'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_egress_acl_sets_egress_acl_set_acl_entries_acl_entry(self):
        """Test case for get_egress_acl_sets_egress_acl_set_acl_entries_acl_entry

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}/acl-entries/acl-entry={sequence_id}'.format(id='id_example', set_name='set_name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ingress_acl_set_acl_entries(self):
        """Test case for get_ingress_acl_set_acl_entries

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}/acl-entries'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ingress_acl_set_config(self):
        """Test case for get_ingress_acl_set_config

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}/config'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ingress_acl_set_config_type(self):
        """Test case for get_ingress_acl_set_config_type

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}/config/type'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ingress_acl_set_state(self):
        """Test case for get_ingress_acl_set_state

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}/state'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ingress_acl_set_state_type(self):
        """Test case for get_ingress_acl_set_state_type

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}/state/type'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ingress_acl_sets_ingress_acl_set_acl_entries_acl_entry(self):
        """Test case for get_ingress_acl_sets_ingress_acl_set_acl_entries_acl_entry

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}/acl-entries/acl-entry={sequence_id}'.format(id='id_example', set_name='set_name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_input_interface_interface_ref(self):
        """Test case for get_input_interface_interface_ref

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/input-interface/interface-ref'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_interface_config(self):
        """Test case for get_interface_config

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/config'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_interface_egress_acl_sets(self):
        """Test case for get_interface_egress_acl_sets

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_interface_egress_acl_sets_egress_acl_set(self):
        """Test case for get_interface_egress_acl_sets_egress_acl_set

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_interface_ingress_acl_sets(self):
        """Test case for get_interface_ingress_acl_sets

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_interface_ingress_acl_sets_ingress_acl_set(self):
        """Test case for get_interface_ingress_acl_sets_ingress_acl_set

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_interface_interface_ref(self):
        """Test case for get_interface_interface_ref

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/interface-ref'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_interface_interface_ref_config(self):
        """Test case for get_interface_interface_ref_config

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/interface-ref/config'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_interface_interface_ref_state(self):
        """Test case for get_interface_interface_ref_state

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/interface-ref/state'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_interface_ref_config(self):
        """Test case for get_interface_ref_config

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/input-interface/interface-ref/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_interface_ref_config_interface(self):
        """Test case for get_interface_ref_config_interface

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/interface-ref/config/interface'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_interface_ref_config_subinterface(self):
        """Test case for get_interface_ref_config_subinterface

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/interface-ref/config/subinterface'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_interface_ref_state(self):
        """Test case for get_interface_ref_state

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/input-interface/interface-ref/state'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_interface_ref_state_interface(self):
        """Test case for get_interface_ref_state_interface

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/interface-ref/state/interface'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_interface_ref_state_subinterface(self):
        """Test case for get_interface_ref_state_subinterface

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/interface-ref/state/subinterface'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_interface_state(self):
        """Test case for get_interface_state

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/state'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ipv4_config(self):
        """Test case for get_ipv4_config

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ipv4_state(self):
        """Test case for get_ipv4_state

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/state'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ipv6_config(self):
        """Test case for get_ipv6_config

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ipv6_config_destination_address(self):
        """Test case for get_ipv6_config_destination_address

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/destination-address'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ipv6_config_dscp(self):
        """Test case for get_ipv6_config_dscp

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/dscp'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ipv6_config_hop_limit(self):
        """Test case for get_ipv6_config_hop_limit

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/hop-limit'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ipv6_config_protocol(self):
        """Test case for get_ipv6_config_protocol

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/protocol'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ipv6_config_source_address(self):
        """Test case for get_ipv6_config_source_address

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/source-address'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ipv6_state(self):
        """Test case for get_ipv6_state

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/state'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ipv6_state_destination_address(self):
        """Test case for get_ipv6_state_destination_address

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/state/destination-address'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ipv6_state_dscp(self):
        """Test case for get_ipv6_state_dscp

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/state/dscp'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ipv6_state_hop_limit(self):
        """Test case for get_ipv6_state_hop_limit

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/state/hop-limit'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ipv6_state_protocol(self):
        """Test case for get_ipv6_state_protocol

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/state/protocol'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ipv6_state_source_address(self):
        """Test case for get_ipv6_state_source_address

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/state/source-address'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_l2_config(self):
        """Test case for get_l2_config

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_l2_state(self):
        """Test case for get_l2_state

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/state'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_list_base_acl_entries_acl_entry(self):
        """Test case for get_list_base_acl_entries_acl_entry

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry'.format(name='name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_list_base_acl_sets_acl_set(self):
        """Test case for get_list_base_acl_sets_acl_set

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_list_base_egress_acl_set_acl_entries_acl_entry(self):
        """Test case for get_list_base_egress_acl_set_acl_entries_acl_entry

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}/acl-entries/acl-entry'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_list_base_egress_acl_sets_egress_acl_set(self):
        """Test case for get_list_base_egress_acl_sets_egress_acl_set

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_list_base_ingress_acl_set_acl_entries_acl_entry(self):
        """Test case for get_list_base_ingress_acl_set_acl_entries_acl_entry

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}/acl-entries/acl-entry'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_list_base_ingress_acl_sets_ingress_acl_set(self):
        """Test case for get_list_base_ingress_acl_sets_ingress_acl_set

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_list_base_interfaces_interface(self):
        """Test case for get_list_base_interfaces_interface

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_counter_capability(self):
        """Test case for get_state_counter_capability

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/state/counter-capability',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_description(self):
        """Test case for get_state_description

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/state/description'.format(name='name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_destination_address(self):
        """Test case for get_state_destination_address

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/state/destination-address'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_destination_flow_label(self):
        """Test case for get_state_destination_flow_label

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/state/destination-flow-label'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_destination_mac(self):
        """Test case for get_state_destination_mac

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/state/destination-mac'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_destination_mac_mask(self):
        """Test case for get_state_destination_mac_mask

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/state/destination-mac-mask'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_destination_port(self):
        """Test case for get_state_destination_port

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/transport/state/destination-port'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_dscp(self):
        """Test case for get_state_dscp

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/state/dscp'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_ethertype(self):
        """Test case for get_state_ethertype

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/state/ethertype'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_forwarding_action(self):
        """Test case for get_state_forwarding_action

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/actions/state/forwarding-action'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_hop_limit(self):
        """Test case for get_state_hop_limit

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/state/hop-limit'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_id(self):
        """Test case for get_state_id

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/state/id'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_interface(self):
        """Test case for get_state_interface

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/input-interface/interface-ref/state/interface'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_log_action(self):
        """Test case for get_state_log_action

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/actions/state/log-action'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_matched_octets(self):
        """Test case for get_state_matched_octets

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/state/matched-octets'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_matched_packets(self):
        """Test case for get_state_matched_packets

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/state/matched-packets'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_name(self):
        """Test case for get_state_name

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/state/name'.format(name='name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_protocol(self):
        """Test case for get_state_protocol

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/state/protocol'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_sequence_id(self):
        """Test case for get_state_sequence_id

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/state/sequence-id'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_set_name(self):
        """Test case for get_state_set_name

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}/state/set-name'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_source_address(self):
        """Test case for get_state_source_address

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/state/source-address'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_source_flow_label(self):
        """Test case for get_state_source_flow_label

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/state/source-flow-label'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_source_mac(self):
        """Test case for get_state_source_mac

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/state/source-mac'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_source_mac_mask(self):
        """Test case for get_state_source_mac_mask

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/state/source-mac-mask'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_source_port(self):
        """Test case for get_state_source_port

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/transport/state/source-port'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_subinterface(self):
        """Test case for get_state_subinterface

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/input-interface/interface-ref/state/subinterface'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_tcp_flags(self):
        """Test case for get_state_tcp_flags

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/transport/state/tcp-flags'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_type(self):
        """Test case for get_state_type

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/state/type'.format(name='name_example', type='type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_transport_config(self):
        """Test case for get_transport_config

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/transport/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_transport_state(self):
        """Test case for get_transport_state

        
        """
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/transport/state'.format(name='name_example', type='type_example', sequence_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_acl(self):
        """Test case for patch_acl

        
        """
        body = PatchAcl()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl',
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_acl_acl_sets(self):
        """Test case for patch_acl_acl_sets

        
        """
        body = PatchAclAclSets()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets',
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_acl_acl_sets_acl_set(self):
        """Test case for patch_acl_acl_sets_acl_set

        
        """
        body = PatchAclAclSetsAclSet()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}'.format(name='name_example', type='type_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_acl_entry_actions(self):
        """Test case for patch_acl_entry_actions

        
        """
        body = PatchAclEntryActions()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/actions'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_acl_entry_config(self):
        """Test case for patch_acl_entry_config

        
        """
        body = PatchAclEntryConfig()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_acl_entry_config_description(self):
        """Test case for patch_acl_entry_config_description

        
        """
        body = PatchAclEntryConfigDescription()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/config/description'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_acl_entry_input_interface(self):
        """Test case for patch_acl_entry_input_interface

        
        """
        body = PatchAclEntryInputInterface()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/input-interface'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_acl_entry_ipv4(self):
        """Test case for patch_acl_entry_ipv4

        
        """
        body = PatchAclEntryIpv4()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_acl_entry_ipv6(self):
        """Test case for patch_acl_entry_ipv6

        
        """
        body = PatchAclEntryIpv6()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_acl_entry_l2(self):
        """Test case for patch_acl_entry_l2

        
        """
        body = PatchAclEntryL2()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_acl_entry_transport(self):
        """Test case for patch_acl_entry_transport

        
        """
        body = PatchAclEntryTransport()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/transport'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_acl_interfaces(self):
        """Test case for patch_acl_interfaces

        
        """
        body = PatchAclInterfaces()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces',
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_acl_interfaces_interface(self):
        """Test case for patch_acl_interfaces_interface

        
        """
        body = PatchAclInterfacesInterface()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}'.format(id='id_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_acl_set_acl_entries(self):
        """Test case for patch_acl_set_acl_entries

        
        """
        body = PatchAclSetAclEntries()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries'.format(name='name_example', type='type_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_acl_set_acl_entries_acl_entry(self):
        """Test case for patch_acl_set_acl_entries_acl_entry

        
        """
        body = PatchAclSetAclEntriesAclEntry()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_acl_set_config(self):
        """Test case for patch_acl_set_config

        
        """
        body = PatchAclSetConfig()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/config'.format(name='name_example', type='type_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_actions_config(self):
        """Test case for patch_actions_config

        
        """
        body = PatchActionsConfig()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/actions/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_config_description(self):
        """Test case for patch_config_description

        
        """
        body = PatchConfigDescription()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/config/description'.format(name='name_example', type='type_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_config_destination_address(self):
        """Test case for patch_config_destination_address

        
        """
        body = PatchConfigDestinationAddress()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/config/destination-address'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_config_destination_flow_label(self):
        """Test case for patch_config_destination_flow_label

        
        """
        body = PatchConfigDestinationFlowLabel()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/destination-flow-label'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_config_destination_mac(self):
        """Test case for patch_config_destination_mac

        
        """
        body = PatchConfigDestinationMac()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/config/destination-mac'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_config_destination_mac_mask(self):
        """Test case for patch_config_destination_mac_mask

        
        """
        body = PatchConfigDestinationMacMask()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/config/destination-mac-mask'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_config_destination_port(self):
        """Test case for patch_config_destination_port

        
        """
        body = PatchConfigDestinationPort()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/transport/config/destination-port'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_config_dscp(self):
        """Test case for patch_config_dscp

        
        """
        body = PatchConfigDscp()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/config/dscp'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_config_ethertype(self):
        """Test case for patch_config_ethertype

        
        """
        body = PatchConfigEthertype()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/config/ethertype'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_config_forwarding_action(self):
        """Test case for patch_config_forwarding_action

        
        """
        body = PatchConfigForwardingAction()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/actions/config/forwarding-action'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_config_hop_limit(self):
        """Test case for patch_config_hop_limit

        
        """
        body = PatchConfigHopLimit()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/config/hop-limit'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_config_id(self):
        """Test case for patch_config_id

        
        """
        body = PatchConfigId()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/config/id'.format(id='id_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_config_interface(self):
        """Test case for patch_config_interface

        
        """
        body = PatchConfigInterface()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/input-interface/interface-ref/config/interface'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_config_log_action(self):
        """Test case for patch_config_log_action

        
        """
        body = PatchConfigLogAction()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/actions/config/log-action'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_config_name(self):
        """Test case for patch_config_name

        
        """
        body = PatchConfigName()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/config/name'.format(name='name_example', type='type_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_config_protocol(self):
        """Test case for patch_config_protocol

        
        """
        body = PatchConfigProtocol()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/config/protocol'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_config_sequence_id(self):
        """Test case for patch_config_sequence_id

        
        """
        body = PatchConfigSequenceId()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/config/sequence-id'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_config_set_name(self):
        """Test case for patch_config_set_name

        
        """
        body = PatchConfigSetName()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}/config/set-name'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_config_source_address(self):
        """Test case for patch_config_source_address

        
        """
        body = PatchConfigSourceAddress()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/config/source-address'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_config_source_flow_label(self):
        """Test case for patch_config_source_flow_label

        
        """
        body = PatchConfigSourceFlowLabel()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/source-flow-label'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_config_source_mac(self):
        """Test case for patch_config_source_mac

        
        """
        body = PatchConfigSourceMac()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/config/source-mac'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_config_source_mac_mask(self):
        """Test case for patch_config_source_mac_mask

        
        """
        body = PatchConfigSourceMacMask()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/config/source-mac-mask'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_config_source_port(self):
        """Test case for patch_config_source_port

        
        """
        body = PatchConfigSourcePort()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/transport/config/source-port'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_config_subinterface(self):
        """Test case for patch_config_subinterface

        
        """
        body = PatchConfigSubinterface()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/input-interface/interface-ref/config/subinterface'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_config_tcp_flags(self):
        """Test case for patch_config_tcp_flags

        
        """
        body = PatchConfigTcpFlags()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/transport/config/tcp-flags'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_config_type(self):
        """Test case for patch_config_type

        
        """
        body = PatchConfigType()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/config/type'.format(name='name_example', type='type_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_egress_acl_set_config(self):
        """Test case for patch_egress_acl_set_config

        
        """
        body = PatchEgressAclSetConfig()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}/config'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_egress_acl_set_config_set_name(self):
        """Test case for patch_egress_acl_set_config_set_name

        
        """
        body = PatchEgressAclSetConfigSetName()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}/config/set-name'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_egress_acl_set_config_type(self):
        """Test case for patch_egress_acl_set_config_type

        
        """
        body = PatchEgressAclSetConfigType()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}/config/type'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_ingress_acl_set_config(self):
        """Test case for patch_ingress_acl_set_config

        
        """
        body = PatchIngressAclSetConfig()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}/config'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_ingress_acl_set_config_type(self):
        """Test case for patch_ingress_acl_set_config_type

        
        """
        body = PatchIngressAclSetConfigType()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}/config/type'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_input_interface_interface_ref(self):
        """Test case for patch_input_interface_interface_ref

        
        """
        body = PatchInputInterfaceInterfaceRef()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/input-interface/interface-ref'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_interface_config(self):
        """Test case for patch_interface_config

        
        """
        body = PatchInterfaceConfig()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/config'.format(id='id_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_interface_egress_acl_sets(self):
        """Test case for patch_interface_egress_acl_sets

        
        """
        body = PatchInterfaceEgressAclSets()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets'.format(id='id_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_interface_egress_acl_sets_egress_acl_set(self):
        """Test case for patch_interface_egress_acl_sets_egress_acl_set

        
        """
        body = PatchInterfaceEgressAclSetsEgressAclSet()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_interface_ingress_acl_sets(self):
        """Test case for patch_interface_ingress_acl_sets

        
        """
        body = PatchInterfaceIngressAclSets()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets'.format(id='id_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_interface_ingress_acl_sets_ingress_acl_set(self):
        """Test case for patch_interface_ingress_acl_sets_ingress_acl_set

        
        """
        body = PatchInterfaceIngressAclSetsIngressAclSet()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_interface_interface_ref(self):
        """Test case for patch_interface_interface_ref

        
        """
        body = PatchInterfaceInterfaceRef()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/interface-ref'.format(id='id_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_interface_interface_ref_config(self):
        """Test case for patch_interface_interface_ref_config

        
        """
        body = PatchInterfaceInterfaceRefConfig()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/interface-ref/config'.format(id='id_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_interface_ref_config(self):
        """Test case for patch_interface_ref_config

        
        """
        body = PatchInterfaceRefConfig()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/input-interface/interface-ref/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_interface_ref_config_interface(self):
        """Test case for patch_interface_ref_config_interface

        
        """
        body = PatchInterfaceRefConfigInterface()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/interface-ref/config/interface'.format(id='id_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_interface_ref_config_subinterface(self):
        """Test case for patch_interface_ref_config_subinterface

        
        """
        body = PatchInterfaceRefConfigSubinterface()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/interface-ref/config/subinterface'.format(id='id_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_ipv4_config(self):
        """Test case for patch_ipv4_config

        
        """
        body = PatchIpv4Config()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_ipv6_config(self):
        """Test case for patch_ipv6_config

        
        """
        body = PatchIpv6Config()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_ipv6_config_destination_address(self):
        """Test case for patch_ipv6_config_destination_address

        
        """
        body = PatchIpv6ConfigDestinationAddress()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/destination-address'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_ipv6_config_dscp(self):
        """Test case for patch_ipv6_config_dscp

        
        """
        body = PatchIpv6ConfigDscp()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/dscp'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_ipv6_config_hop_limit(self):
        """Test case for patch_ipv6_config_hop_limit

        
        """
        body = PatchIpv6ConfigHopLimit()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/hop-limit'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_ipv6_config_protocol(self):
        """Test case for patch_ipv6_config_protocol

        
        """
        body = PatchIpv6ConfigProtocol()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/protocol'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_ipv6_config_source_address(self):
        """Test case for patch_ipv6_config_source_address

        
        """
        body = PatchIpv6ConfigSourceAddress()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/source-address'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_l2_config(self):
        """Test case for patch_l2_config

        
        """
        body = PatchL2Config()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_list_base_acl_entries_acl_entry(self):
        """Test case for patch_list_base_acl_entries_acl_entry

        
        """
        body = PatchListBaseAclEntriesAclEntry()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry'.format(name='name_example', type='type_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_list_base_acl_sets_acl_set(self):
        """Test case for patch_list_base_acl_sets_acl_set

        
        """
        body = PatchListBaseAclSetsAclSet()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set',
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_list_base_egress_acl_sets_egress_acl_set(self):
        """Test case for patch_list_base_egress_acl_sets_egress_acl_set

        
        """
        body = PatchListBaseEgressAclSetsEgressAclSet()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set'.format(id='id_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_list_base_ingress_acl_sets_ingress_acl_set(self):
        """Test case for patch_list_base_ingress_acl_sets_ingress_acl_set

        
        """
        body = PatchListBaseIngressAclSetsIngressAclSet()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set'.format(id='id_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_list_base_interfaces_interface(self):
        """Test case for patch_list_base_interfaces_interface

        
        """
        body = PatchListBaseInterfacesInterface()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface',
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_transport_config(self):
        """Test case for patch_transport_config

        
        """
        body = PatchTransportConfig()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/transport/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_acl_acl_sets(self):
        """Test case for post_acl_acl_sets

        
        """
        body = PostAclAclSets()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_acl_entry_config(self):
        """Test case for post_acl_entry_config

        
        """
        body = PostAclEntryConfig()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}'.format(name='name_example', type='type_example', sequence_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_acl_set_config(self):
        """Test case for post_acl_set_config

        
        """
        body = PostAclSetConfig()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}'.format(name='name_example', type='type_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_actions_config(self):
        """Test case for post_actions_config

        
        """
        body = PostActionsConfig()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/actions'.format(name='name_example', type='type_example', sequence_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_config_forwarding_action(self):
        """Test case for post_config_forwarding_action

        
        """
        body = PostConfigForwardingAction()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/actions/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_config_id(self):
        """Test case for post_config_id

        
        """
        body = PostConfigId()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/config'.format(id='id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_config_interface(self):
        """Test case for post_config_interface

        
        """
        body = PostConfigInterface()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/input-interface/interface-ref/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_config_name(self):
        """Test case for post_config_name

        
        """
        body = PostConfigName()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/config'.format(name='name_example', type='type_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_config_sequence_id(self):
        """Test case for post_config_sequence_id

        
        """
        body = PostConfigSequenceId()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_config_set_name(self):
        """Test case for post_config_set_name

        
        """
        body = PostConfigSetName()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}/config'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_config_source_address(self):
        """Test case for post_config_source_address

        
        """
        body = PostConfigSourceAddress()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_config_source_mac(self):
        """Test case for post_config_source_mac

        
        """
        body = PostConfigSourceMac()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_config_source_port(self):
        """Test case for post_config_source_port

        
        """
        body = PostConfigSourcePort()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/transport/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_egress_acl_set_config(self):
        """Test case for post_egress_acl_set_config

        
        """
        body = PostEgressAclSetConfig()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_egress_acl_set_config_set_name(self):
        """Test case for post_egress_acl_set_config_set_name

        
        """
        body = PostEgressAclSetConfigSetName()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}/config'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_ingress_acl_set_config(self):
        """Test case for post_ingress_acl_set_config

        
        """
        body = PostIngressAclSetConfig()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_input_interface_interface_ref(self):
        """Test case for post_input_interface_interface_ref

        
        """
        body = PostInputInterfaceInterfaceRef()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/input-interface'.format(name='name_example', type='type_example', sequence_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_interface_config(self):
        """Test case for post_interface_config

        
        """
        body = PostInterfaceConfig()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}'.format(id='id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_interface_interface_ref_config(self):
        """Test case for post_interface_interface_ref_config

        
        """
        body = PostInterfaceInterfaceRefConfig()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/interface-ref'.format(id='id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_interface_ref_config(self):
        """Test case for post_interface_ref_config

        
        """
        body = PostInterfaceRefConfig()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/input-interface/interface-ref'.format(name='name_example', type='type_example', sequence_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_interface_ref_config_interface(self):
        """Test case for post_interface_ref_config_interface

        
        """
        body = PostInterfaceRefConfigInterface()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/interface-ref/config'.format(id='id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_ipv4_config(self):
        """Test case for post_ipv4_config

        
        """
        body = PostIpv4Config()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4'.format(name='name_example', type='type_example', sequence_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_ipv6_config(self):
        """Test case for post_ipv6_config

        
        """
        body = PostIpv6Config()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6'.format(name='name_example', type='type_example', sequence_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_ipv6_config_source_address(self):
        """Test case for post_ipv6_config_source_address

        
        """
        body = PostIpv6ConfigSourceAddress()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_l2_config(self):
        """Test case for post_l2_config

        
        """
        body = PostL2Config()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2'.format(name='name_example', type='type_example', sequence_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_list_base_acl_entries_acl_entry(self):
        """Test case for post_list_base_acl_entries_acl_entry

        
        """
        body = PostListBaseAclEntriesAclEntry()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries'.format(name='name_example', type='type_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_list_base_acl_sets_acl_set(self):
        """Test case for post_list_base_acl_sets_acl_set

        
        """
        body = PostListBaseAclSetsAclSet()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_list_base_egress_acl_sets_egress_acl_set(self):
        """Test case for post_list_base_egress_acl_sets_egress_acl_set

        
        """
        body = PostListBaseEgressAclSetsEgressAclSet()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets'.format(id='id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_list_base_ingress_acl_sets_ingress_acl_set(self):
        """Test case for post_list_base_ingress_acl_sets_ingress_acl_set

        
        """
        body = PostListBaseIngressAclSetsIngressAclSet()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets'.format(id='id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_list_base_interfaces_interface(self):
        """Test case for post_list_base_interfaces_interface

        
        """
        body = PostListBaseInterfacesInterface()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_transport_config(self):
        """Test case for post_transport_config

        
        """
        body = PostTransportConfig()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/transport'.format(name='name_example', type='type_example', sequence_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_acl(self):
        """Test case for put_acl

        
        """
        body = PutAcl()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_acl_acl_sets(self):
        """Test case for put_acl_acl_sets

        
        """
        body = PutAclAclSets()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_acl_acl_sets_acl_set(self):
        """Test case for put_acl_acl_sets_acl_set

        
        """
        body = PutAclAclSetsAclSet()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}'.format(name='name_example', type='type_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_acl_entry_actions(self):
        """Test case for put_acl_entry_actions

        
        """
        body = PutAclEntryActions()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/actions'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_acl_entry_config(self):
        """Test case for put_acl_entry_config

        
        """
        body = PutAclEntryConfig()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_acl_entry_config_description(self):
        """Test case for put_acl_entry_config_description

        
        """
        body = PutAclEntryConfigDescription()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/config/description'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_acl_entry_input_interface(self):
        """Test case for put_acl_entry_input_interface

        
        """
        body = PutAclEntryInputInterface()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/input-interface'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_acl_entry_ipv4(self):
        """Test case for put_acl_entry_ipv4

        
        """
        body = PutAclEntryIpv4()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_acl_entry_ipv6(self):
        """Test case for put_acl_entry_ipv6

        
        """
        body = PutAclEntryIpv6()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_acl_entry_l2(self):
        """Test case for put_acl_entry_l2

        
        """
        body = PutAclEntryL2()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_acl_entry_transport(self):
        """Test case for put_acl_entry_transport

        
        """
        body = PutAclEntryTransport()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/transport'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_acl_interfaces(self):
        """Test case for put_acl_interfaces

        
        """
        body = PutAclInterfaces()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_acl_interfaces_interface(self):
        """Test case for put_acl_interfaces_interface

        
        """
        body = PutAclInterfacesInterface()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_acl_set_acl_entries(self):
        """Test case for put_acl_set_acl_entries

        
        """
        body = PutAclSetAclEntries()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries'.format(name='name_example', type='type_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_acl_set_acl_entries_acl_entry(self):
        """Test case for put_acl_set_acl_entries_acl_entry

        
        """
        body = PutAclSetAclEntriesAclEntry()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_acl_set_config(self):
        """Test case for put_acl_set_config

        
        """
        body = PutAclSetConfig()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/config'.format(name='name_example', type='type_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_actions_config(self):
        """Test case for put_actions_config

        
        """
        body = PutActionsConfig()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/actions/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_config_description(self):
        """Test case for put_config_description

        
        """
        body = PutConfigDescription()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/config/description'.format(name='name_example', type='type_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_config_destination_address(self):
        """Test case for put_config_destination_address

        
        """
        body = PutConfigDestinationAddress()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/config/destination-address'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_config_destination_flow_label(self):
        """Test case for put_config_destination_flow_label

        
        """
        body = PutConfigDestinationFlowLabel()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/destination-flow-label'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_config_destination_mac(self):
        """Test case for put_config_destination_mac

        
        """
        body = PutConfigDestinationMac()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/config/destination-mac'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_config_destination_mac_mask(self):
        """Test case for put_config_destination_mac_mask

        
        """
        body = PutConfigDestinationMacMask()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/config/destination-mac-mask'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_config_destination_port(self):
        """Test case for put_config_destination_port

        
        """
        body = PutConfigDestinationPort()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/transport/config/destination-port'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_config_dscp(self):
        """Test case for put_config_dscp

        
        """
        body = PutConfigDscp()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/config/dscp'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_config_ethertype(self):
        """Test case for put_config_ethertype

        
        """
        body = PutConfigEthertype()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/config/ethertype'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_config_forwarding_action(self):
        """Test case for put_config_forwarding_action

        
        """
        body = PutConfigForwardingAction()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/actions/config/forwarding-action'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_config_hop_limit(self):
        """Test case for put_config_hop_limit

        
        """
        body = PutConfigHopLimit()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/config/hop-limit'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_config_id(self):
        """Test case for put_config_id

        
        """
        body = PutConfigId()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/config/id'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_config_interface(self):
        """Test case for put_config_interface

        
        """
        body = PutConfigInterface()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/input-interface/interface-ref/config/interface'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_config_log_action(self):
        """Test case for put_config_log_action

        
        """
        body = PutConfigLogAction()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/actions/config/log-action'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_config_name(self):
        """Test case for put_config_name

        
        """
        body = PutConfigName()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/config/name'.format(name='name_example', type='type_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_config_protocol(self):
        """Test case for put_config_protocol

        
        """
        body = PutConfigProtocol()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/config/protocol'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_config_sequence_id(self):
        """Test case for put_config_sequence_id

        
        """
        body = PutConfigSequenceId()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/config/sequence-id'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_config_set_name(self):
        """Test case for put_config_set_name

        
        """
        body = PutConfigSetName()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}/config/set-name'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_config_source_address(self):
        """Test case for put_config_source_address

        
        """
        body = PutConfigSourceAddress()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/config/source-address'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_config_source_flow_label(self):
        """Test case for put_config_source_flow_label

        
        """
        body = PutConfigSourceFlowLabel()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/source-flow-label'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_config_source_mac(self):
        """Test case for put_config_source_mac

        
        """
        body = PutConfigSourceMac()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/config/source-mac'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_config_source_mac_mask(self):
        """Test case for put_config_source_mac_mask

        
        """
        body = PutConfigSourceMacMask()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/config/source-mac-mask'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_config_source_port(self):
        """Test case for put_config_source_port

        
        """
        body = PutConfigSourcePort()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/transport/config/source-port'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_config_subinterface(self):
        """Test case for put_config_subinterface

        
        """
        body = PutConfigSubinterface()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/input-interface/interface-ref/config/subinterface'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_config_tcp_flags(self):
        """Test case for put_config_tcp_flags

        
        """
        body = PutConfigTcpFlags()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/transport/config/tcp-flags'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_config_type(self):
        """Test case for put_config_type

        
        """
        body = PutConfigType()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/config/type'.format(name='name_example', type='type_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_egress_acl_set_config(self):
        """Test case for put_egress_acl_set_config

        
        """
        body = PutEgressAclSetConfig()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}/config'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_egress_acl_set_config_set_name(self):
        """Test case for put_egress_acl_set_config_set_name

        
        """
        body = PutEgressAclSetConfigSetName()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}/config/set-name'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_egress_acl_set_config_type(self):
        """Test case for put_egress_acl_set_config_type

        
        """
        body = PutEgressAclSetConfigType()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}/config/type'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_ingress_acl_set_config(self):
        """Test case for put_ingress_acl_set_config

        
        """
        body = PutIngressAclSetConfig()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}/config'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_ingress_acl_set_config_type(self):
        """Test case for put_ingress_acl_set_config_type

        
        """
        body = PutIngressAclSetConfigType()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}/config/type'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_input_interface_interface_ref(self):
        """Test case for put_input_interface_interface_ref

        
        """
        body = PutInputInterfaceInterfaceRef()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/input-interface/interface-ref'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_interface_config(self):
        """Test case for put_interface_config

        
        """
        body = PutInterfaceConfig()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/config'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_interface_egress_acl_sets(self):
        """Test case for put_interface_egress_acl_sets

        
        """
        body = PutInterfaceEgressAclSets()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_interface_egress_acl_sets_egress_acl_set(self):
        """Test case for put_interface_egress_acl_sets_egress_acl_set

        
        """
        body = PutInterfaceEgressAclSetsEgressAclSet()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set={set_name},{type}'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_interface_ingress_acl_sets(self):
        """Test case for put_interface_ingress_acl_sets

        
        """
        body = PutInterfaceIngressAclSets()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_interface_ingress_acl_sets_ingress_acl_set(self):
        """Test case for put_interface_ingress_acl_sets_ingress_acl_set

        
        """
        body = PutInterfaceIngressAclSetsIngressAclSet()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set={set_name},{type}'.format(id='id_example', set_name='set_name_example', type='type_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_interface_interface_ref(self):
        """Test case for put_interface_interface_ref

        
        """
        body = PutInterfaceInterfaceRef()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/interface-ref'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_interface_interface_ref_config(self):
        """Test case for put_interface_interface_ref_config

        
        """
        body = PutInterfaceInterfaceRefConfig()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/interface-ref/config'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_interface_ref_config(self):
        """Test case for put_interface_ref_config

        
        """
        body = PutInterfaceRefConfig()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/input-interface/interface-ref/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_interface_ref_config_interface(self):
        """Test case for put_interface_ref_config_interface

        
        """
        body = PutInterfaceRefConfigInterface()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/interface-ref/config/interface'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_interface_ref_config_subinterface(self):
        """Test case for put_interface_ref_config_subinterface

        
        """
        body = PutInterfaceRefConfigSubinterface()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/interface-ref/config/subinterface'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_ipv4_config(self):
        """Test case for put_ipv4_config

        
        """
        body = PutIpv4Config()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv4/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_ipv6_config(self):
        """Test case for put_ipv6_config

        
        """
        body = PutIpv6Config()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_ipv6_config_destination_address(self):
        """Test case for put_ipv6_config_destination_address

        
        """
        body = PutIpv6ConfigDestinationAddress()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/destination-address'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_ipv6_config_dscp(self):
        """Test case for put_ipv6_config_dscp

        
        """
        body = PutIpv6ConfigDscp()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/dscp'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_ipv6_config_hop_limit(self):
        """Test case for put_ipv6_config_hop_limit

        
        """
        body = PutIpv6ConfigHopLimit()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/hop-limit'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_ipv6_config_protocol(self):
        """Test case for put_ipv6_config_protocol

        
        """
        body = PutIpv6ConfigProtocol()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/protocol'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_ipv6_config_source_address(self):
        """Test case for put_ipv6_config_source_address

        
        """
        body = PutIpv6ConfigSourceAddress()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/ipv6/config/source-address'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_l2_config(self):
        """Test case for put_l2_config

        
        """
        body = PutL2Config()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/l2/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_list_base_acl_entries_acl_entry(self):
        """Test case for put_list_base_acl_entries_acl_entry

        
        """
        body = PutListBaseAclEntriesAclEntry()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry'.format(name='name_example', type='type_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_list_base_acl_sets_acl_set(self):
        """Test case for put_list_base_acl_sets_acl_set

        
        """
        body = PutListBaseAclSetsAclSet()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_list_base_egress_acl_sets_egress_acl_set(self):
        """Test case for put_list_base_egress_acl_sets_egress_acl_set

        
        """
        body = PutListBaseEgressAclSetsEgressAclSet()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/egress-acl-sets/egress-acl-set'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_list_base_ingress_acl_sets_ingress_acl_set(self):
        """Test case for put_list_base_ingress_acl_sets_ingress_acl_set

        
        """
        body = PutListBaseIngressAclSetsIngressAclSet()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface={id}/ingress-acl-sets/ingress-acl-set'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_list_base_interfaces_interface(self):
        """Test case for put_list_base_interfaces_interface

        
        """
        body = PutListBaseInterfacesInterface()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/interfaces/interface',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_transport_config(self):
        """Test case for put_transport_config

        
        """
        body = PutTransportConfig()
        response = self.client.open(
            '/v1/restconf/data/openconfig-acl:acl/acl-sets/acl-set={name},{type}/acl-entries/acl-entry={sequence_id}/transport/config'.format(name='name_example', type='type_example', sequence_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
