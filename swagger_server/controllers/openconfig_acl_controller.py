import connexion
import six
from swagger_ext import rest_request_handler

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
from swagger_server import util


def delete_acl():  # noqa: E501
    """delete_acl

    OperationId: delete_acl Top level enclosing container for ACL model config and operational state data # noqa: E501


    :rtype: Acl
    """
    return rest_request_handler.invoke_handler()


def delete_acl_acl_sets():  # noqa: E501
    """delete_acl_acl_sets

    OperationId: delete_acl_acl_sets Access list entries variables enclosing container # noqa: E501


    :rtype: AclAclSets
    """
    return rest_request_handler.invoke_handler()


def delete_acl_acl_sets_acl_set(name, type):  # noqa: E501
    """delete_acl_acl_sets_acl_set

    OperationId: delete_acl_acl_sets_acl_set List of ACL sets, each comprising of a list of ACL entries # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str

    :rtype: AclAclSetsAclSet
    """
    return rest_request_handler.invoke_handler()


def delete_acl_entry_actions(name, type, sequence_id):  # noqa: E501
    """delete_acl_entry_actions

    OperationId: delete_acl_entry_actions Enclosing container for list of ACL actions associated with an entry # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: AclEntryActions
    """
    return rest_request_handler.invoke_handler()


def delete_acl_entry_config(name, type, sequence_id):  # noqa: E501
    """delete_acl_entry_config

    OperationId: delete_acl_entry_config Access list entries config # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: AclEntryConfig
    """
    return rest_request_handler.invoke_handler()


def delete_acl_entry_config_description(name, type, sequence_id):  # noqa: E501
    """delete_acl_entry_config_description

    OperationId: delete_acl_entry_config_description A user-defined description, or comment, for this Access List Entry. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: AclEntryConfigDescription
    """
    return rest_request_handler.invoke_handler()


def delete_acl_entry_input_interface(name, type, sequence_id):  # noqa: E501
    """delete_acl_entry_input_interface

    OperationId: delete_acl_entry_input_interface Input interface container # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: AclEntryInputInterface
    """
    return rest_request_handler.invoke_handler()


def delete_acl_entry_ipv4(name, type, sequence_id):  # noqa: E501
    """delete_acl_entry_ipv4

    OperationId: delete_acl_entry_ipv4 Top level container for IPv4 match field data # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: AclEntryIpv4
    """
    return rest_request_handler.invoke_handler()


def delete_acl_entry_ipv6(name, type, sequence_id):  # noqa: E501
    """delete_acl_entry_ipv6

    OperationId: delete_acl_entry_ipv6 Top-level container for IPv6 match field data # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: AclEntryIpv6
    """
    return rest_request_handler.invoke_handler()


def delete_acl_entry_l2(name, type, sequence_id):  # noqa: E501
    """delete_acl_entry_l2

    OperationId: delete_acl_entry_l2 Ethernet header fields # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: AclEntryL2
    """
    return rest_request_handler.invoke_handler()


def delete_acl_entry_transport(name, type, sequence_id):  # noqa: E501
    """delete_acl_entry_transport

    OperationId: delete_acl_entry_transport Transport fields container # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: AclEntryTransport
    """
    return rest_request_handler.invoke_handler()


def delete_acl_interfaces():  # noqa: E501
    """delete_acl_interfaces

    OperationId: delete_acl_interfaces Enclosing container for the list of interfaces on which ACLs are set # noqa: E501


    :rtype: AclInterfaces
    """
    return rest_request_handler.invoke_handler()


def delete_acl_interfaces_interface(id):  # noqa: E501
    """delete_acl_interfaces_interface

    OperationId: delete_acl_interfaces_interface List of interfaces on which ACLs are set # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str

    :rtype: AclInterfacesInterface
    """
    return rest_request_handler.invoke_handler()


def delete_acl_set_acl_entries(name, type):  # noqa: E501
    """delete_acl_set_acl_entries

    OperationId: delete_acl_set_acl_entries Access list entries container # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str

    :rtype: AclSetAclEntries
    """
    return rest_request_handler.invoke_handler()


def delete_acl_set_acl_entries_acl_entry(name, type, sequence_id):  # noqa: E501
    """delete_acl_set_acl_entries_acl_entry

    OperationId: delete_acl_set_acl_entries_acl_entry List of ACL entries comprising an ACL set # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: AclSetAclEntriesAclEntry
    """
    return rest_request_handler.invoke_handler()


def delete_acl_set_config(name, type):  # noqa: E501
    """delete_acl_set_config

    OperationId: delete_acl_set_config Access list config # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str

    :rtype: AclSetConfig
    """
    return rest_request_handler.invoke_handler()


def delete_actions_config(name, type, sequence_id):  # noqa: E501
    """delete_actions_config

    OperationId: delete_actions_config Config data for ACL actions # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: ActionsConfig
    """
    return rest_request_handler.invoke_handler()


def delete_config_description(name, type):  # noqa: E501
    """delete_config_description

    OperationId: delete_config_description Description, or comment, for the ACL set # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str

    :rtype: ConfigDescription
    """
    return rest_request_handler.invoke_handler()


def delete_config_destination_address(name, type, sequence_id):  # noqa: E501
    """delete_config_destination_address

    OperationId: delete_config_destination_address Destination IPv4 address prefix. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: ConfigDestinationAddress
    """
    return rest_request_handler.invoke_handler()


def delete_config_destination_flow_label(name, type, sequence_id):  # noqa: E501
    """delete_config_destination_flow_label

    OperationId: delete_config_destination_flow_label Destination IPv6 Flow label. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: ConfigDestinationFlowLabel
    """
    return rest_request_handler.invoke_handler()


def delete_config_destination_mac(name, type, sequence_id):  # noqa: E501
    """delete_config_destination_mac

    OperationId: delete_config_destination_mac Destination IEEE 802 MAC address. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: ConfigDestinationMac
    """
    return rest_request_handler.invoke_handler()


def delete_config_destination_mac_mask(name, type, sequence_id):  # noqa: E501
    """delete_config_destination_mac_mask

    OperationId: delete_config_destination_mac_mask Destination IEEE 802 MAC address mask. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: ConfigDestinationMacMask
    """
    return rest_request_handler.invoke_handler()


def delete_config_destination_port(name, type, sequence_id):  # noqa: E501
    """delete_config_destination_port

    OperationId: delete_config_destination_port Destination port or range # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: ConfigDestinationPort
    """
    return rest_request_handler.invoke_handler()


def delete_config_dscp(name, type, sequence_id):  # noqa: E501
    """delete_config_dscp

    OperationId: delete_config_dscp Value of diffserv codepoint. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: ConfigDscp
    """
    return rest_request_handler.invoke_handler()


def delete_config_ethertype(name, type, sequence_id):  # noqa: E501
    """delete_config_ethertype

    OperationId: delete_config_ethertype Ethertype field to match in Ethernet packets # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: ConfigEthertype
    """
    return rest_request_handler.invoke_handler()


def delete_config_forwarding_action(name, type, sequence_id):  # noqa: E501
    """delete_config_forwarding_action

    OperationId: delete_config_forwarding_action Specifies the forwarding action.  One forwarding action must be specified for each ACL entry # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: ConfigForwardingAction
    """
    return rest_request_handler.invoke_handler()


def delete_config_hop_limit(name, type, sequence_id):  # noqa: E501
    """delete_config_hop_limit

    OperationId: delete_config_hop_limit The IP packet&#39;s hop limit -- known as TTL (in hops) in IPv4 packets, and hop limit in IPv6 # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: ConfigHopLimit
    """
    return rest_request_handler.invoke_handler()


def delete_config_id(id):  # noqa: E501
    """delete_config_id

    OperationId: delete_config_id User-defined identifier for the interface -- a common convention could be &#39;&lt;if name&gt;.&lt;subif index&gt;&#39; # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str

    :rtype: ConfigId
    """
    return rest_request_handler.invoke_handler()


def delete_config_interface(name, type, sequence_id):  # noqa: E501
    """delete_config_interface

    OperationId: delete_config_interface Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: ConfigInterface
    """
    return rest_request_handler.invoke_handler()


def delete_config_log_action(name, type, sequence_id):  # noqa: E501
    """delete_config_log_action

    OperationId: delete_config_log_action Specifies the log action and destination for matched packets.  The default is not to log the packet. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: ConfigLogAction
    """
    return rest_request_handler.invoke_handler()


def delete_config_name(name, type):  # noqa: E501
    """delete_config_name

    OperationId: delete_config_name The name of the access-list set # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str

    :rtype: ConfigName
    """
    return rest_request_handler.invoke_handler()


def delete_config_protocol(name, type, sequence_id):  # noqa: E501
    """delete_config_protocol

    OperationId: delete_config_protocol The protocol carried in the IP packet, expressed either as its IP protocol number, or by a defined identity. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: ConfigProtocol
    """
    return rest_request_handler.invoke_handler()


def delete_config_sequence_id(name, type, sequence_id):  # noqa: E501
    """delete_config_sequence_id

    OperationId: delete_config_sequence_id The sequence id determines the order in which ACL entries are applied.  The sequence id must be unique for each entry in an ACL set.  Target devices should apply the ACL entry rules in ascending order determined by sequence id (low to high), rather than the relying only on order in the list. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: ConfigSequenceId
    """
    return rest_request_handler.invoke_handler()


def delete_config_set_name(id, set_name, type):  # noqa: E501
    """delete_config_set_name

    OperationId: delete_config_set_name Reference to the ACL set name applied on ingress # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str

    :rtype: ConfigSetName
    """
    return rest_request_handler.invoke_handler()


def delete_config_source_address(name, type, sequence_id):  # noqa: E501
    """delete_config_source_address

    OperationId: delete_config_source_address Source IPv4 address prefix. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: ConfigSourceAddress
    """
    return rest_request_handler.invoke_handler()


def delete_config_source_flow_label(name, type, sequence_id):  # noqa: E501
    """delete_config_source_flow_label

    OperationId: delete_config_source_flow_label Source IPv6 Flow label. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: ConfigSourceFlowLabel
    """
    return rest_request_handler.invoke_handler()


def delete_config_source_mac(name, type, sequence_id):  # noqa: E501
    """delete_config_source_mac

    OperationId: delete_config_source_mac Source IEEE 802 MAC address. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: ConfigSourceMac
    """
    return rest_request_handler.invoke_handler()


def delete_config_source_mac_mask(name, type, sequence_id):  # noqa: E501
    """delete_config_source_mac_mask

    OperationId: delete_config_source_mac_mask Source IEEE 802 MAC address mask. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: ConfigSourceMacMask
    """
    return rest_request_handler.invoke_handler()


def delete_config_source_port(name, type, sequence_id):  # noqa: E501
    """delete_config_source_port

    OperationId: delete_config_source_port Source port or range # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: ConfigSourcePort
    """
    return rest_request_handler.invoke_handler()


def delete_config_subinterface(name, type, sequence_id):  # noqa: E501
    """delete_config_subinterface

    OperationId: delete_config_subinterface Reference to a subinterface -- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: ConfigSubinterface
    """
    return rest_request_handler.invoke_handler()


def delete_config_tcp_flags(name, type, sequence_id):  # noqa: E501
    """delete_config_tcp_flags

    OperationId: delete_config_tcp_flags List of TCP flags to match # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: ConfigTcpFlags
    """
    return rest_request_handler.invoke_handler()


def delete_config_type(name, type):  # noqa: E501
    """delete_config_type

    OperationId: delete_config_type The type determines the fields allowed in the ACL entries belonging to the ACL set (e.g., IPv4, IPv6, etc.) # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str

    :rtype: ConfigType
    """
    return rest_request_handler.invoke_handler()


def delete_egress_acl_set_config(id, set_name, type):  # noqa: E501
    """delete_egress_acl_set_config

    OperationId: delete_egress_acl_set_config Configuration data  # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str

    :rtype: EgressAclSetConfig
    """
    return rest_request_handler.invoke_handler()


def delete_egress_acl_set_config_set_name(id, set_name, type):  # noqa: E501
    """delete_egress_acl_set_config_set_name

    OperationId: delete_egress_acl_set_config_set_name Reference to the ACL set name applied on egress # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str

    :rtype: EgressAclSetConfigSetName
    """
    return rest_request_handler.invoke_handler()


def delete_egress_acl_set_config_type(id, set_name, type):  # noqa: E501
    """delete_egress_acl_set_config_type

    OperationId: delete_egress_acl_set_config_type Reference to the ACL set type applied on egress. # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str

    :rtype: EgressAclSetConfigType
    """
    return rest_request_handler.invoke_handler()


def delete_ingress_acl_set_config(id, set_name, type):  # noqa: E501
    """delete_ingress_acl_set_config

    OperationId: delete_ingress_acl_set_config Configuration data  # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str

    :rtype: IngressAclSetConfig
    """
    return rest_request_handler.invoke_handler()


def delete_ingress_acl_set_config_type(id, set_name, type):  # noqa: E501
    """delete_ingress_acl_set_config_type

    OperationId: delete_ingress_acl_set_config_type Reference to the ACL set type applied on ingress # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str

    :rtype: IngressAclSetConfigType
    """
    return rest_request_handler.invoke_handler()


def delete_input_interface_interface_ref(name, type, sequence_id):  # noqa: E501
    """delete_input_interface_interface_ref

    OperationId: delete_input_interface_interface_ref Reference to an interface or subinterface # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: InputInterfaceInterfaceRef
    """
    return rest_request_handler.invoke_handler()


def delete_interface_config(id):  # noqa: E501
    """delete_interface_config

    OperationId: delete_interface_config Configuration for ACL per-interface data # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str

    :rtype: InterfaceConfig
    """
    return rest_request_handler.invoke_handler()


def delete_interface_egress_acl_sets(id):  # noqa: E501
    """delete_interface_egress_acl_sets

    OperationId: delete_interface_egress_acl_sets Enclosing container the list of egress ACLs on the interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str

    :rtype: InterfaceEgressAclSets
    """
    return rest_request_handler.invoke_handler()


def delete_interface_egress_acl_sets_egress_acl_set(id, set_name, type):  # noqa: E501
    """delete_interface_egress_acl_sets_egress_acl_set

    OperationId: delete_interface_egress_acl_sets_egress_acl_set List of egress ACLs on the interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str

    :rtype: InterfaceEgressAclSetsEgressAclSet
    """
    return rest_request_handler.invoke_handler()


def delete_interface_ingress_acl_sets(id):  # noqa: E501
    """delete_interface_ingress_acl_sets

    OperationId: delete_interface_ingress_acl_sets Enclosing container the list of ingress ACLs on the interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str

    :rtype: InterfaceIngressAclSets
    """
    return rest_request_handler.invoke_handler()


def delete_interface_ingress_acl_sets_ingress_acl_set(id, set_name, type):  # noqa: E501
    """delete_interface_ingress_acl_sets_ingress_acl_set

    OperationId: delete_interface_ingress_acl_sets_ingress_acl_set List of ingress ACLs on the interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str

    :rtype: InterfaceIngressAclSetsIngressAclSet
    """
    return rest_request_handler.invoke_handler()


def delete_interface_interface_ref(id):  # noqa: E501
    """delete_interface_interface_ref

    OperationId: delete_interface_interface_ref Reference to an interface or subinterface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str

    :rtype: InterfaceInterfaceRef
    """
    return rest_request_handler.invoke_handler()


def delete_interface_interface_ref_config(id):  # noqa: E501
    """delete_interface_interface_ref_config

    OperationId: delete_interface_interface_ref_config Configured reference to interface / subinterface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str

    :rtype: InterfaceInterfaceRefConfig
    """
    return rest_request_handler.invoke_handler()


def delete_interface_ref_config(name, type, sequence_id):  # noqa: E501
    """delete_interface_ref_config

    OperationId: delete_interface_ref_config Configured reference to interface / subinterface # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: InterfaceRefConfig
    """
    return rest_request_handler.invoke_handler()


def delete_interface_ref_config_interface(id):  # noqa: E501
    """delete_interface_ref_config_interface

    OperationId: delete_interface_ref_config_interface Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface. # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str

    :rtype: InterfaceRefConfigInterface
    """
    return rest_request_handler.invoke_handler()


def delete_interface_ref_config_subinterface(id):  # noqa: E501
    """delete_interface_ref_config_subinterface

    OperationId: delete_interface_ref_config_subinterface Reference to a subinterface -- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set. # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str

    :rtype: InterfaceRefConfigSubinterface
    """
    return rest_request_handler.invoke_handler()


def delete_ipv4_config(name, type, sequence_id):  # noqa: E501
    """delete_ipv4_config

    OperationId: delete_ipv4_config Configuration data for IPv4 match fields # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: Ipv4Config
    """
    return rest_request_handler.invoke_handler()


def delete_ipv6_config(name, type, sequence_id):  # noqa: E501
    """delete_ipv6_config

    OperationId: delete_ipv6_config Configuration data for IPv6 match fields # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: Ipv6Config
    """
    return rest_request_handler.invoke_handler()


def delete_ipv6_config_destination_address(name, type, sequence_id):  # noqa: E501
    """delete_ipv6_config_destination_address

    OperationId: delete_ipv6_config_destination_address Destination IPv6 address prefix. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: Ipv6ConfigDestinationAddress
    """
    return rest_request_handler.invoke_handler()


def delete_ipv6_config_dscp(name, type, sequence_id):  # noqa: E501
    """delete_ipv6_config_dscp

    OperationId: delete_ipv6_config_dscp Value of diffserv codepoint. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: Ipv6ConfigDscp
    """
    return rest_request_handler.invoke_handler()


def delete_ipv6_config_hop_limit(name, type, sequence_id):  # noqa: E501
    """delete_ipv6_config_hop_limit

    OperationId: delete_ipv6_config_hop_limit The IP packet&#39;s hop limit -- known as TTL (in hops) in IPv4 packets, and hop limit in IPv6 # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: Ipv6ConfigHopLimit
    """
    return rest_request_handler.invoke_handler()


def delete_ipv6_config_protocol(name, type, sequence_id):  # noqa: E501
    """delete_ipv6_config_protocol

    OperationId: delete_ipv6_config_protocol The protocol carried in the IP packet, expressed either as its IP protocol number, or by a defined identity. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: Ipv6ConfigProtocol
    """
    return rest_request_handler.invoke_handler()


def delete_ipv6_config_source_address(name, type, sequence_id):  # noqa: E501
    """delete_ipv6_config_source_address

    OperationId: delete_ipv6_config_source_address Source IPv6 address prefix. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: Ipv6ConfigSourceAddress
    """
    return rest_request_handler.invoke_handler()


def delete_l2_config(name, type, sequence_id):  # noqa: E501
    """delete_l2_config

    OperationId: delete_l2_config Configuration data # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: L2Config
    """
    return rest_request_handler.invoke_handler()


def delete_list_base_acl_entries_acl_entry(name, type):  # noqa: E501
    """delete_list_base_acl_entries_acl_entry

    OperationId: delete_list_base_acl_entries_acl_entry List of ACL entries comprising an ACL set # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str

    :rtype: ListBaseAclEntriesAclEntry
    """
    return rest_request_handler.invoke_handler()


def delete_list_base_acl_sets_acl_set():  # noqa: E501
    """delete_list_base_acl_sets_acl_set

    OperationId: delete_list_base_acl_sets_acl_set List of ACL sets, each comprising of a list of ACL entries # noqa: E501


    :rtype: ListBaseAclSetsAclSet
    """
    return rest_request_handler.invoke_handler()


def delete_list_base_egress_acl_sets_egress_acl_set(id):  # noqa: E501
    """delete_list_base_egress_acl_sets_egress_acl_set

    OperationId: delete_list_base_egress_acl_sets_egress_acl_set List of egress ACLs on the interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str

    :rtype: ListBaseEgressAclSetsEgressAclSet
    """
    return rest_request_handler.invoke_handler()


def delete_list_base_ingress_acl_sets_ingress_acl_set(id):  # noqa: E501
    """delete_list_base_ingress_acl_sets_ingress_acl_set

    OperationId: delete_list_base_ingress_acl_sets_ingress_acl_set List of ingress ACLs on the interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str

    :rtype: ListBaseIngressAclSetsIngressAclSet
    """
    return rest_request_handler.invoke_handler()


def delete_list_base_interfaces_interface():  # noqa: E501
    """delete_list_base_interfaces_interface

    OperationId: delete_list_base_interfaces_interface List of interfaces on which ACLs are set # noqa: E501


    :rtype: ListBaseInterfacesInterface
    """
    return rest_request_handler.invoke_handler()


def delete_transport_config(name, type, sequence_id):  # noqa: E501
    """delete_transport_config

    OperationId: delete_transport_config Configuration data # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: TransportConfig
    """
    return rest_request_handler.invoke_handler()


def get_acl():  # noqa: E501
    """get_acl

    OperationId: get_acl Top level enclosing container for ACL model config and operational state data # noqa: E501


    :rtype: GetAcl
    """
    return rest_request_handler.invoke_handler()


def get_acl_acl_sets():  # noqa: E501
    """get_acl_acl_sets

    OperationId: get_acl_acl_sets Access list entries variables enclosing container # noqa: E501


    :rtype: GetAclAclSets
    """
    return rest_request_handler.invoke_handler()


def get_acl_acl_sets_acl_set(name, type):  # noqa: E501
    """get_acl_acl_sets_acl_set

    OperationId: get_acl_acl_sets_acl_set List of ACL sets, each comprising of a list of ACL entries # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str

    :rtype: GetAclAclSetsAclSet
    """
    return rest_request_handler.invoke_handler()


def get_acl_entries_acl_entry_state(id, set_name, type, sequence_id):  # noqa: E501
    """get_acl_entries_acl_entry_state

    OperationId: get_acl_entries_acl_entry_state Operational state data for per-interface ACL entries # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param sequence_id: Reference to per-interface acl entry key
    :type sequence_id: int

    :rtype: GetAclEntriesAclEntryState
    """
    return rest_request_handler.invoke_handler()


def get_acl_entries_acl_entry_state_matched_octets(id, set_name, type, sequence_id):  # noqa: E501
    """get_acl_entries_acl_entry_state_matched_octets

    OperationId: get_acl_entries_acl_entry_state_matched_octets Count of the number of octets (bytes) matching the current ACL entry.  An implementation should provide this counter on a per-interface per-ACL-entry if possible.  If an implementation only supports ACL counters per entry (i.e., not broken out per interface), then the value should be equal to the aggregate count across all interfaces.  An implementation that provides counters per entry per interface is not required to also provide an aggregate count, e.g., per entry -- the user is expected to be able implement the required aggregation if such a count is needed. # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param sequence_id: Reference to per-interface acl entry key
    :type sequence_id: int

    :rtype: GetAclEntriesAclEntryStateMatchedOctets
    """
    return rest_request_handler.invoke_handler()


def get_acl_entries_acl_entry_state_matched_packets(id, set_name, type, sequence_id):  # noqa: E501
    """get_acl_entries_acl_entry_state_matched_packets

    OperationId: get_acl_entries_acl_entry_state_matched_packets Count of the number of packets matching the current ACL entry.  An implementation should provide this counter on a per-interface per-ACL-entry if possible.  If an implementation only supports ACL counters per entry (i.e., not broken out per interface), then the value should be equal to the aggregate count across all interfaces.  An implementation that provides counters per entry per interface is not required to also provide an aggregate count, e.g., per entry -- the user is expected to be able implement the required aggregation if such a count is needed. # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param sequence_id: Reference to per-interface acl entry key
    :type sequence_id: int

    :rtype: GetAclEntriesAclEntryStateMatchedPackets
    """
    return rest_request_handler.invoke_handler()


def get_acl_entries_acl_entry_state_sequence_id(id, set_name, type, sequence_id):  # noqa: E501
    """get_acl_entries_acl_entry_state_sequence_id

    OperationId: get_acl_entries_acl_entry_state_sequence_id Reference to an entry in the ACL set applied to an interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param sequence_id: Reference to per-interface acl entry key
    :type sequence_id: int

    :rtype: GetAclEntriesAclEntryStateSequenceId
    """
    return rest_request_handler.invoke_handler()


def get_acl_entry_actions(name, type, sequence_id):  # noqa: E501
    """get_acl_entry_actions

    OperationId: get_acl_entry_actions Enclosing container for list of ACL actions associated with an entry # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetAclEntryActions
    """
    return rest_request_handler.invoke_handler()


def get_acl_entry_config(name, type, sequence_id):  # noqa: E501
    """get_acl_entry_config

    OperationId: get_acl_entry_config Access list entries config # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetAclEntryConfig
    """
    return rest_request_handler.invoke_handler()


def get_acl_entry_config_description(name, type, sequence_id):  # noqa: E501
    """get_acl_entry_config_description

    OperationId: get_acl_entry_config_description A user-defined description, or comment, for this Access List Entry. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetAclEntryConfigDescription
    """
    return rest_request_handler.invoke_handler()


def get_acl_entry_input_interface(name, type, sequence_id):  # noqa: E501
    """get_acl_entry_input_interface

    OperationId: get_acl_entry_input_interface Input interface container # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetAclEntryInputInterface
    """
    return rest_request_handler.invoke_handler()


def get_acl_entry_ipv4(name, type, sequence_id):  # noqa: E501
    """get_acl_entry_ipv4

    OperationId: get_acl_entry_ipv4 Top level container for IPv4 match field data # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetAclEntryIpv4
    """
    return rest_request_handler.invoke_handler()


def get_acl_entry_ipv6(name, type, sequence_id):  # noqa: E501
    """get_acl_entry_ipv6

    OperationId: get_acl_entry_ipv6 Top-level container for IPv6 match field data # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetAclEntryIpv6
    """
    return rest_request_handler.invoke_handler()


def get_acl_entry_l2(name, type, sequence_id):  # noqa: E501
    """get_acl_entry_l2

    OperationId: get_acl_entry_l2 Ethernet header fields # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetAclEntryL2
    """
    return rest_request_handler.invoke_handler()


def get_acl_entry_state(name, type, sequence_id):  # noqa: E501
    """get_acl_entry_state

    OperationId: get_acl_entry_state State information for ACL entries # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetAclEntryState
    """
    return rest_request_handler.invoke_handler()


def get_acl_entry_state_description(name, type, sequence_id):  # noqa: E501
    """get_acl_entry_state_description

    OperationId: get_acl_entry_state_description A user-defined description, or comment, for this Access List Entry. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetAclEntryStateDescription
    """
    return rest_request_handler.invoke_handler()


def get_acl_entry_state_matched_octets(id, set_name, type, sequence_id):  # noqa: E501
    """get_acl_entry_state_matched_octets

    OperationId: get_acl_entry_state_matched_octets Count of the number of octets (bytes) matching the current ACL entry.  An implementation should provide this counter on a per-interface per-ACL-entry if possible.  If an implementation only supports ACL counters per entry (i.e., not broken out per interface), then the value should be equal to the aggregate count across all interfaces.  An implementation that provides counters per entry per interface is not required to also provide an aggregate count, e.g., per entry -- the user is expected to be able implement the required aggregation if such a count is needed. # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param sequence_id: Reference to per-interface acl entry key
    :type sequence_id: int

    :rtype: GetAclEntryStateMatchedOctets
    """
    return rest_request_handler.invoke_handler()


def get_acl_entry_state_matched_packets(id, set_name, type, sequence_id):  # noqa: E501
    """get_acl_entry_state_matched_packets

    OperationId: get_acl_entry_state_matched_packets Count of the number of packets matching the current ACL entry.  An implementation should provide this counter on a per-interface per-ACL-entry if possible.  If an implementation only supports ACL counters per entry (i.e., not broken out per interface), then the value should be equal to the aggregate count across all interfaces.  An implementation that provides counters per entry per interface is not required to also provide an aggregate count, e.g., per entry -- the user is expected to be able implement the required aggregation if such a count is needed. # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param sequence_id: Reference to per-interface acl entry key
    :type sequence_id: int

    :rtype: GetAclEntryStateMatchedPackets
    """
    return rest_request_handler.invoke_handler()


def get_acl_entry_state_sequence_id(id, set_name, type, sequence_id):  # noqa: E501
    """get_acl_entry_state_sequence_id

    OperationId: get_acl_entry_state_sequence_id Reference to an entry in the ACL set applied to an interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param sequence_id: Reference to per-interface acl entry key
    :type sequence_id: int

    :rtype: GetAclEntryStateSequenceId
    """
    return rest_request_handler.invoke_handler()


def get_acl_entry_transport(name, type, sequence_id):  # noqa: E501
    """get_acl_entry_transport

    OperationId: get_acl_entry_transport Transport fields container # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetAclEntryTransport
    """
    return rest_request_handler.invoke_handler()


def get_acl_interfaces():  # noqa: E501
    """get_acl_interfaces

    OperationId: get_acl_interfaces Enclosing container for the list of interfaces on which ACLs are set # noqa: E501


    :rtype: GetAclInterfaces
    """
    return rest_request_handler.invoke_handler()


def get_acl_interfaces_interface(id):  # noqa: E501
    """get_acl_interfaces_interface

    OperationId: get_acl_interfaces_interface List of interfaces on which ACLs are set # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str

    :rtype: GetAclInterfacesInterface
    """
    return rest_request_handler.invoke_handler()


def get_acl_set_acl_entries(name, type):  # noqa: E501
    """get_acl_set_acl_entries

    OperationId: get_acl_set_acl_entries Access list entries container # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str

    :rtype: GetAclSetAclEntries
    """
    return rest_request_handler.invoke_handler()


def get_acl_set_acl_entries_acl_entry(name, type, sequence_id):  # noqa: E501
    """get_acl_set_acl_entries_acl_entry

    OperationId: get_acl_set_acl_entries_acl_entry List of ACL entries comprising an ACL set # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetAclSetAclEntriesAclEntry
    """
    return rest_request_handler.invoke_handler()


def get_acl_set_config(name, type):  # noqa: E501
    """get_acl_set_config

    OperationId: get_acl_set_config Access list config # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str

    :rtype: GetAclSetConfig
    """
    return rest_request_handler.invoke_handler()


def get_acl_set_state(name, type):  # noqa: E501
    """get_acl_set_state

    OperationId: get_acl_set_state Access list state information # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str

    :rtype: GetAclSetState
    """
    return rest_request_handler.invoke_handler()


def get_acl_state():  # noqa: E501
    """get_acl_state

    OperationId: get_acl_state Global operational state data for ACLs # noqa: E501


    :rtype: GetAclState
    """
    return rest_request_handler.invoke_handler()


def get_actions_config(name, type, sequence_id):  # noqa: E501
    """get_actions_config

    OperationId: get_actions_config Config data for ACL actions # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetActionsConfig
    """
    return rest_request_handler.invoke_handler()


def get_actions_state(name, type, sequence_id):  # noqa: E501
    """get_actions_state

    OperationId: get_actions_state State information for ACL actions # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetActionsState
    """
    return rest_request_handler.invoke_handler()


def get_config_description(name, type):  # noqa: E501
    """get_config_description

    OperationId: get_config_description Description, or comment, for the ACL set # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str

    :rtype: GetConfigDescription
    """
    return rest_request_handler.invoke_handler()


def get_config_destination_address(name, type, sequence_id):  # noqa: E501
    """get_config_destination_address

    OperationId: get_config_destination_address Destination IPv4 address prefix. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetConfigDestinationAddress
    """
    return rest_request_handler.invoke_handler()


def get_config_destination_flow_label(name, type, sequence_id):  # noqa: E501
    """get_config_destination_flow_label

    OperationId: get_config_destination_flow_label Destination IPv6 Flow label. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetConfigDestinationFlowLabel
    """
    return rest_request_handler.invoke_handler()


def get_config_destination_mac(name, type, sequence_id):  # noqa: E501
    """get_config_destination_mac

    OperationId: get_config_destination_mac Destination IEEE 802 MAC address. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetConfigDestinationMac
    """
    return rest_request_handler.invoke_handler()


def get_config_destination_mac_mask(name, type, sequence_id):  # noqa: E501
    """get_config_destination_mac_mask

    OperationId: get_config_destination_mac_mask Destination IEEE 802 MAC address mask. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetConfigDestinationMacMask
    """
    return rest_request_handler.invoke_handler()


def get_config_destination_port(name, type, sequence_id):  # noqa: E501
    """get_config_destination_port

    OperationId: get_config_destination_port Destination port or range # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetConfigDestinationPort
    """
    return rest_request_handler.invoke_handler()


def get_config_dscp(name, type, sequence_id):  # noqa: E501
    """get_config_dscp

    OperationId: get_config_dscp Value of diffserv codepoint. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetConfigDscp
    """
    return rest_request_handler.invoke_handler()


def get_config_ethertype(name, type, sequence_id):  # noqa: E501
    """get_config_ethertype

    OperationId: get_config_ethertype Ethertype field to match in Ethernet packets # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetConfigEthertype
    """
    return rest_request_handler.invoke_handler()


def get_config_forwarding_action(name, type, sequence_id):  # noqa: E501
    """get_config_forwarding_action

    OperationId: get_config_forwarding_action Specifies the forwarding action.  One forwarding action must be specified for each ACL entry # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetConfigForwardingAction
    """
    return rest_request_handler.invoke_handler()


def get_config_hop_limit(name, type, sequence_id):  # noqa: E501
    """get_config_hop_limit

    OperationId: get_config_hop_limit The IP packet&#39;s hop limit -- known as TTL (in hops) in IPv4 packets, and hop limit in IPv6 # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetConfigHopLimit
    """
    return rest_request_handler.invoke_handler()


def get_config_id(id):  # noqa: E501
    """get_config_id

    OperationId: get_config_id User-defined identifier for the interface -- a common convention could be &#39;&lt;if name&gt;.&lt;subif index&gt;&#39; # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str

    :rtype: GetConfigId
    """
    return rest_request_handler.invoke_handler()


def get_config_interface(name, type, sequence_id):  # noqa: E501
    """get_config_interface

    OperationId: get_config_interface Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetConfigInterface
    """
    return rest_request_handler.invoke_handler()


def get_config_log_action(name, type, sequence_id):  # noqa: E501
    """get_config_log_action

    OperationId: get_config_log_action Specifies the log action and destination for matched packets.  The default is not to log the packet. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetConfigLogAction
    """
    return rest_request_handler.invoke_handler()


def get_config_name(name, type):  # noqa: E501
    """get_config_name

    OperationId: get_config_name The name of the access-list set # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str

    :rtype: GetConfigName
    """
    return rest_request_handler.invoke_handler()


def get_config_protocol(name, type, sequence_id):  # noqa: E501
    """get_config_protocol

    OperationId: get_config_protocol The protocol carried in the IP packet, expressed either as its IP protocol number, or by a defined identity. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetConfigProtocol
    """
    return rest_request_handler.invoke_handler()


def get_config_sequence_id(name, type, sequence_id):  # noqa: E501
    """get_config_sequence_id

    OperationId: get_config_sequence_id The sequence id determines the order in which ACL entries are applied.  The sequence id must be unique for each entry in an ACL set.  Target devices should apply the ACL entry rules in ascending order determined by sequence id (low to high), rather than the relying only on order in the list. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetConfigSequenceId
    """
    return rest_request_handler.invoke_handler()


def get_config_set_name(id, set_name, type):  # noqa: E501
    """get_config_set_name

    OperationId: get_config_set_name Reference to the ACL set name applied on ingress # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str

    :rtype: GetConfigSetName
    """
    return rest_request_handler.invoke_handler()


def get_config_source_address(name, type, sequence_id):  # noqa: E501
    """get_config_source_address

    OperationId: get_config_source_address Source IPv4 address prefix. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetConfigSourceAddress
    """
    return rest_request_handler.invoke_handler()


def get_config_source_flow_label(name, type, sequence_id):  # noqa: E501
    """get_config_source_flow_label

    OperationId: get_config_source_flow_label Source IPv6 Flow label. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetConfigSourceFlowLabel
    """
    return rest_request_handler.invoke_handler()


def get_config_source_mac(name, type, sequence_id):  # noqa: E501
    """get_config_source_mac

    OperationId: get_config_source_mac Source IEEE 802 MAC address. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetConfigSourceMac
    """
    return rest_request_handler.invoke_handler()


def get_config_source_mac_mask(name, type, sequence_id):  # noqa: E501
    """get_config_source_mac_mask

    OperationId: get_config_source_mac_mask Source IEEE 802 MAC address mask. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetConfigSourceMacMask
    """
    return rest_request_handler.invoke_handler()


def get_config_source_port(name, type, sequence_id):  # noqa: E501
    """get_config_source_port

    OperationId: get_config_source_port Source port or range # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetConfigSourcePort
    """
    return rest_request_handler.invoke_handler()


def get_config_subinterface(name, type, sequence_id):  # noqa: E501
    """get_config_subinterface

    OperationId: get_config_subinterface Reference to a subinterface -- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetConfigSubinterface
    """
    return rest_request_handler.invoke_handler()


def get_config_tcp_flags(name, type, sequence_id):  # noqa: E501
    """get_config_tcp_flags

    OperationId: get_config_tcp_flags List of TCP flags to match # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetConfigTcpFlags
    """
    return rest_request_handler.invoke_handler()


def get_config_type(name, type):  # noqa: E501
    """get_config_type

    OperationId: get_config_type The type determines the fields allowed in the ACL entries belonging to the ACL set (e.g., IPv4, IPv6, etc.) # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str

    :rtype: GetConfigType
    """
    return rest_request_handler.invoke_handler()


def get_egress_acl_set_acl_entries(id, set_name, type):  # noqa: E501
    """get_egress_acl_set_acl_entries

    OperationId: get_egress_acl_set_acl_entries Enclosing container for list of references to ACLs # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str

    :rtype: GetEgressAclSetAclEntries
    """
    return rest_request_handler.invoke_handler()


def get_egress_acl_set_acl_entries_acl_entry_state(id, set_name, type, sequence_id):  # noqa: E501
    """get_egress_acl_set_acl_entries_acl_entry_state

    OperationId: get_egress_acl_set_acl_entries_acl_entry_state Operational state data for per-interface ACL entries # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param sequence_id: Reference to per-interface acl entry key
    :type sequence_id: int

    :rtype: GetEgressAclSetAclEntriesAclEntryState
    """
    return rest_request_handler.invoke_handler()


def get_egress_acl_set_config(id, set_name, type):  # noqa: E501
    """get_egress_acl_set_config

    OperationId: get_egress_acl_set_config Configuration data  # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str

    :rtype: GetEgressAclSetConfig
    """
    return rest_request_handler.invoke_handler()


def get_egress_acl_set_config_set_name(id, set_name, type):  # noqa: E501
    """get_egress_acl_set_config_set_name

    OperationId: get_egress_acl_set_config_set_name Reference to the ACL set name applied on egress # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str

    :rtype: GetEgressAclSetConfigSetName
    """
    return rest_request_handler.invoke_handler()


def get_egress_acl_set_config_type(id, set_name, type):  # noqa: E501
    """get_egress_acl_set_config_type

    OperationId: get_egress_acl_set_config_type Reference to the ACL set type applied on egress. # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str

    :rtype: GetEgressAclSetConfigType
    """
    return rest_request_handler.invoke_handler()


def get_egress_acl_set_state(id, set_name, type):  # noqa: E501
    """get_egress_acl_set_state

    OperationId: get_egress_acl_set_state Operational state data for interface egress ACLs # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str

    :rtype: GetEgressAclSetState
    """
    return rest_request_handler.invoke_handler()


def get_egress_acl_set_state_set_name(id, set_name, type):  # noqa: E501
    """get_egress_acl_set_state_set_name

    OperationId: get_egress_acl_set_state_set_name Reference to the ACL set name applied on egress # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str

    :rtype: GetEgressAclSetStateSetName
    """
    return rest_request_handler.invoke_handler()


def get_egress_acl_set_state_type(id, set_name, type):  # noqa: E501
    """get_egress_acl_set_state_type

    OperationId: get_egress_acl_set_state_type Reference to the ACL set type applied on egress. # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str

    :rtype: GetEgressAclSetStateType
    """
    return rest_request_handler.invoke_handler()


def get_egress_acl_sets_egress_acl_set_acl_entries_acl_entry(id, set_name, type, sequence_id):  # noqa: E501
    """get_egress_acl_sets_egress_acl_set_acl_entries_acl_entry

    OperationId: get_egress_acl_sets_egress_acl_set_acl_entries_acl_entry List of ACL entries assigned to an interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param sequence_id: Reference to per-interface acl entry key
    :type sequence_id: int

    :rtype: GetEgressAclSetsEgressAclSetAclEntriesAclEntry
    """
    return rest_request_handler.invoke_handler()


def get_ingress_acl_set_acl_entries(id, set_name, type):  # noqa: E501
    """get_ingress_acl_set_acl_entries

    OperationId: get_ingress_acl_set_acl_entries Enclosing container for list of references to ACLs # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str

    :rtype: GetIngressAclSetAclEntries
    """
    return rest_request_handler.invoke_handler()


def get_ingress_acl_set_config(id, set_name, type):  # noqa: E501
    """get_ingress_acl_set_config

    OperationId: get_ingress_acl_set_config Configuration data  # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str

    :rtype: GetIngressAclSetConfig
    """
    return rest_request_handler.invoke_handler()


def get_ingress_acl_set_config_type(id, set_name, type):  # noqa: E501
    """get_ingress_acl_set_config_type

    OperationId: get_ingress_acl_set_config_type Reference to the ACL set type applied on ingress # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str

    :rtype: GetIngressAclSetConfigType
    """
    return rest_request_handler.invoke_handler()


def get_ingress_acl_set_state(id, set_name, type):  # noqa: E501
    """get_ingress_acl_set_state

    OperationId: get_ingress_acl_set_state Operational state data for interface ingress ACLs # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str

    :rtype: GetIngressAclSetState
    """
    return rest_request_handler.invoke_handler()


def get_ingress_acl_set_state_type(id, set_name, type):  # noqa: E501
    """get_ingress_acl_set_state_type

    OperationId: get_ingress_acl_set_state_type Reference to the ACL set type applied on ingress # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str

    :rtype: GetIngressAclSetStateType
    """
    return rest_request_handler.invoke_handler()


def get_ingress_acl_sets_ingress_acl_set_acl_entries_acl_entry(id, set_name, type, sequence_id):  # noqa: E501
    """get_ingress_acl_sets_ingress_acl_set_acl_entries_acl_entry

    OperationId: get_ingress_acl_sets_ingress_acl_set_acl_entries_acl_entry List of ACL entries assigned to an interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param sequence_id: Reference to per-interface acl entry key
    :type sequence_id: int

    :rtype: GetIngressAclSetsIngressAclSetAclEntriesAclEntry
    """
    return rest_request_handler.invoke_handler()


def get_input_interface_interface_ref(name, type, sequence_id):  # noqa: E501
    """get_input_interface_interface_ref

    OperationId: get_input_interface_interface_ref Reference to an interface or subinterface # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetInputInterfaceInterfaceRef
    """
    return rest_request_handler.invoke_handler()


def get_interface_config(id):  # noqa: E501
    """get_interface_config

    OperationId: get_interface_config Configuration for ACL per-interface data # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str

    :rtype: GetInterfaceConfig
    """
    return rest_request_handler.invoke_handler()


def get_interface_egress_acl_sets(id):  # noqa: E501
    """get_interface_egress_acl_sets

    OperationId: get_interface_egress_acl_sets Enclosing container the list of egress ACLs on the interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str

    :rtype: GetInterfaceEgressAclSets
    """
    return rest_request_handler.invoke_handler()


def get_interface_egress_acl_sets_egress_acl_set(id, set_name, type):  # noqa: E501
    """get_interface_egress_acl_sets_egress_acl_set

    OperationId: get_interface_egress_acl_sets_egress_acl_set List of egress ACLs on the interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str

    :rtype: GetInterfaceEgressAclSetsEgressAclSet
    """
    return rest_request_handler.invoke_handler()


def get_interface_ingress_acl_sets(id):  # noqa: E501
    """get_interface_ingress_acl_sets

    OperationId: get_interface_ingress_acl_sets Enclosing container the list of ingress ACLs on the interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str

    :rtype: GetInterfaceIngressAclSets
    """
    return rest_request_handler.invoke_handler()


def get_interface_ingress_acl_sets_ingress_acl_set(id, set_name, type):  # noqa: E501
    """get_interface_ingress_acl_sets_ingress_acl_set

    OperationId: get_interface_ingress_acl_sets_ingress_acl_set List of ingress ACLs on the interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str

    :rtype: GetInterfaceIngressAclSetsIngressAclSet
    """
    return rest_request_handler.invoke_handler()


def get_interface_interface_ref(id):  # noqa: E501
    """get_interface_interface_ref

    OperationId: get_interface_interface_ref Reference to an interface or subinterface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str

    :rtype: GetInterfaceInterfaceRef
    """
    return rest_request_handler.invoke_handler()


def get_interface_interface_ref_config(id):  # noqa: E501
    """get_interface_interface_ref_config

    OperationId: get_interface_interface_ref_config Configured reference to interface / subinterface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str

    :rtype: GetInterfaceInterfaceRefConfig
    """
    return rest_request_handler.invoke_handler()


def get_interface_interface_ref_state(id):  # noqa: E501
    """get_interface_interface_ref_state

    OperationId: get_interface_interface_ref_state Operational state for interface-ref # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str

    :rtype: GetInterfaceInterfaceRefState
    """
    return rest_request_handler.invoke_handler()


def get_interface_ref_config(name, type, sequence_id):  # noqa: E501
    """get_interface_ref_config

    OperationId: get_interface_ref_config Configured reference to interface / subinterface # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetInterfaceRefConfig
    """
    return rest_request_handler.invoke_handler()


def get_interface_ref_config_interface(id):  # noqa: E501
    """get_interface_ref_config_interface

    OperationId: get_interface_ref_config_interface Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface. # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str

    :rtype: GetInterfaceRefConfigInterface
    """
    return rest_request_handler.invoke_handler()


def get_interface_ref_config_subinterface(id):  # noqa: E501
    """get_interface_ref_config_subinterface

    OperationId: get_interface_ref_config_subinterface Reference to a subinterface -- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set. # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str

    :rtype: GetInterfaceRefConfigSubinterface
    """
    return rest_request_handler.invoke_handler()


def get_interface_ref_state(name, type, sequence_id):  # noqa: E501
    """get_interface_ref_state

    OperationId: get_interface_ref_state Operational state for interface-ref # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetInterfaceRefState
    """
    return rest_request_handler.invoke_handler()


def get_interface_ref_state_interface(id):  # noqa: E501
    """get_interface_ref_state_interface

    OperationId: get_interface_ref_state_interface Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface. # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str

    :rtype: GetInterfaceRefStateInterface
    """
    return rest_request_handler.invoke_handler()


def get_interface_ref_state_subinterface(id):  # noqa: E501
    """get_interface_ref_state_subinterface

    OperationId: get_interface_ref_state_subinterface Reference to a subinterface -- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set. # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str

    :rtype: GetInterfaceRefStateSubinterface
    """
    return rest_request_handler.invoke_handler()


def get_interface_state(id):  # noqa: E501
    """get_interface_state

    OperationId: get_interface_state Operational state for ACL per-interface data # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str

    :rtype: GetInterfaceState
    """
    return rest_request_handler.invoke_handler()


def get_ipv4_config(name, type, sequence_id):  # noqa: E501
    """get_ipv4_config

    OperationId: get_ipv4_config Configuration data for IPv4 match fields # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetIpv4Config
    """
    return rest_request_handler.invoke_handler()


def get_ipv4_state(name, type, sequence_id):  # noqa: E501
    """get_ipv4_state

    OperationId: get_ipv4_state State information for IPv4 match fields # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetIpv4State
    """
    return rest_request_handler.invoke_handler()


def get_ipv6_config(name, type, sequence_id):  # noqa: E501
    """get_ipv6_config

    OperationId: get_ipv6_config Configuration data for IPv6 match fields # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetIpv6Config
    """
    return rest_request_handler.invoke_handler()


def get_ipv6_config_destination_address(name, type, sequence_id):  # noqa: E501
    """get_ipv6_config_destination_address

    OperationId: get_ipv6_config_destination_address Destination IPv6 address prefix. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetIpv6ConfigDestinationAddress
    """
    return rest_request_handler.invoke_handler()


def get_ipv6_config_dscp(name, type, sequence_id):  # noqa: E501
    """get_ipv6_config_dscp

    OperationId: get_ipv6_config_dscp Value of diffserv codepoint. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetIpv6ConfigDscp
    """
    return rest_request_handler.invoke_handler()


def get_ipv6_config_hop_limit(name, type, sequence_id):  # noqa: E501
    """get_ipv6_config_hop_limit

    OperationId: get_ipv6_config_hop_limit The IP packet&#39;s hop limit -- known as TTL (in hops) in IPv4 packets, and hop limit in IPv6 # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetIpv6ConfigHopLimit
    """
    return rest_request_handler.invoke_handler()


def get_ipv6_config_protocol(name, type, sequence_id):  # noqa: E501
    """get_ipv6_config_protocol

    OperationId: get_ipv6_config_protocol The protocol carried in the IP packet, expressed either as its IP protocol number, or by a defined identity. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetIpv6ConfigProtocol
    """
    return rest_request_handler.invoke_handler()


def get_ipv6_config_source_address(name, type, sequence_id):  # noqa: E501
    """get_ipv6_config_source_address

    OperationId: get_ipv6_config_source_address Source IPv6 address prefix. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetIpv6ConfigSourceAddress
    """
    return rest_request_handler.invoke_handler()


def get_ipv6_state(name, type, sequence_id):  # noqa: E501
    """get_ipv6_state

    OperationId: get_ipv6_state Operational state data for IPv6 match fields # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetIpv6State
    """
    return rest_request_handler.invoke_handler()


def get_ipv6_state_destination_address(name, type, sequence_id):  # noqa: E501
    """get_ipv6_state_destination_address

    OperationId: get_ipv6_state_destination_address Destination IPv6 address prefix. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetIpv6StateDestinationAddress
    """
    return rest_request_handler.invoke_handler()


def get_ipv6_state_dscp(name, type, sequence_id):  # noqa: E501
    """get_ipv6_state_dscp

    OperationId: get_ipv6_state_dscp Value of diffserv codepoint. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetIpv6StateDscp
    """
    return rest_request_handler.invoke_handler()


def get_ipv6_state_hop_limit(name, type, sequence_id):  # noqa: E501
    """get_ipv6_state_hop_limit

    OperationId: get_ipv6_state_hop_limit The IP packet&#39;s hop limit -- known as TTL (in hops) in IPv4 packets, and hop limit in IPv6 # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetIpv6StateHopLimit
    """
    return rest_request_handler.invoke_handler()


def get_ipv6_state_protocol(name, type, sequence_id):  # noqa: E501
    """get_ipv6_state_protocol

    OperationId: get_ipv6_state_protocol The protocol carried in the IP packet, expressed either as its IP protocol number, or by a defined identity. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetIpv6StateProtocol
    """
    return rest_request_handler.invoke_handler()


def get_ipv6_state_source_address(name, type, sequence_id):  # noqa: E501
    """get_ipv6_state_source_address

    OperationId: get_ipv6_state_source_address Source IPv6 address prefix. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetIpv6StateSourceAddress
    """
    return rest_request_handler.invoke_handler()


def get_l2_config(name, type, sequence_id):  # noqa: E501
    """get_l2_config

    OperationId: get_l2_config Configuration data # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetL2Config
    """
    return rest_request_handler.invoke_handler()


def get_l2_state(name, type, sequence_id):  # noqa: E501
    """get_l2_state

    OperationId: get_l2_state State Information. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetL2State
    """
    return rest_request_handler.invoke_handler()


def get_list_base_acl_entries_acl_entry(name, type):  # noqa: E501
    """get_list_base_acl_entries_acl_entry

    OperationId: get_list_base_acl_entries_acl_entry List of ACL entries comprising an ACL set # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str

    :rtype: GetListBaseAclEntriesAclEntry
    """
    return rest_request_handler.invoke_handler()


def get_list_base_acl_sets_acl_set():  # noqa: E501
    """get_list_base_acl_sets_acl_set

    OperationId: get_list_base_acl_sets_acl_set List of ACL sets, each comprising of a list of ACL entries # noqa: E501


    :rtype: GetListBaseAclSetsAclSet
    """
    return rest_request_handler.invoke_handler()


def get_list_base_egress_acl_set_acl_entries_acl_entry(id, set_name, type):  # noqa: E501
    """get_list_base_egress_acl_set_acl_entries_acl_entry

    OperationId: get_list_base_egress_acl_set_acl_entries_acl_entry List of ACL entries assigned to an interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str

    :rtype: GetListBaseEgressAclSetAclEntriesAclEntry
    """
    return rest_request_handler.invoke_handler()


def get_list_base_egress_acl_sets_egress_acl_set(id):  # noqa: E501
    """get_list_base_egress_acl_sets_egress_acl_set

    OperationId: get_list_base_egress_acl_sets_egress_acl_set List of egress ACLs on the interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str

    :rtype: GetListBaseEgressAclSetsEgressAclSet
    """
    return rest_request_handler.invoke_handler()


def get_list_base_ingress_acl_set_acl_entries_acl_entry(id, set_name, type):  # noqa: E501
    """get_list_base_ingress_acl_set_acl_entries_acl_entry

    OperationId: get_list_base_ingress_acl_set_acl_entries_acl_entry List of ACL entries assigned to an interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str

    :rtype: GetListBaseIngressAclSetAclEntriesAclEntry
    """
    return rest_request_handler.invoke_handler()


def get_list_base_ingress_acl_sets_ingress_acl_set(id):  # noqa: E501
    """get_list_base_ingress_acl_sets_ingress_acl_set

    OperationId: get_list_base_ingress_acl_sets_ingress_acl_set List of ingress ACLs on the interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str

    :rtype: GetListBaseIngressAclSetsIngressAclSet
    """
    return rest_request_handler.invoke_handler()


def get_list_base_interfaces_interface():  # noqa: E501
    """get_list_base_interfaces_interface

    OperationId: get_list_base_interfaces_interface List of interfaces on which ACLs are set # noqa: E501


    :rtype: GetListBaseInterfacesInterface
    """
    return rest_request_handler.invoke_handler()


def get_state_counter_capability():  # noqa: E501
    """get_state_counter_capability

    OperationId: get_state_counter_capability System reported indication of how ACL counters are reported by the target # noqa: E501


    :rtype: GetStateCounterCapability
    """
    return rest_request_handler.invoke_handler()


def get_state_description(name, type):  # noqa: E501
    """get_state_description

    OperationId: get_state_description Description, or comment, for the ACL set # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str

    :rtype: GetStateDescription
    """
    return rest_request_handler.invoke_handler()


def get_state_destination_address(name, type, sequence_id):  # noqa: E501
    """get_state_destination_address

    OperationId: get_state_destination_address Destination IPv4 address prefix. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetStateDestinationAddress
    """
    return rest_request_handler.invoke_handler()


def get_state_destination_flow_label(name, type, sequence_id):  # noqa: E501
    """get_state_destination_flow_label

    OperationId: get_state_destination_flow_label Destination IPv6 Flow label. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetStateDestinationFlowLabel
    """
    return rest_request_handler.invoke_handler()


def get_state_destination_mac(name, type, sequence_id):  # noqa: E501
    """get_state_destination_mac

    OperationId: get_state_destination_mac Destination IEEE 802 MAC address. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetStateDestinationMac
    """
    return rest_request_handler.invoke_handler()


def get_state_destination_mac_mask(name, type, sequence_id):  # noqa: E501
    """get_state_destination_mac_mask

    OperationId: get_state_destination_mac_mask Destination IEEE 802 MAC address mask. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetStateDestinationMacMask
    """
    return rest_request_handler.invoke_handler()


def get_state_destination_port(name, type, sequence_id):  # noqa: E501
    """get_state_destination_port

    OperationId: get_state_destination_port Destination port or range # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetStateDestinationPort
    """
    return rest_request_handler.invoke_handler()


def get_state_dscp(name, type, sequence_id):  # noqa: E501
    """get_state_dscp

    OperationId: get_state_dscp Value of diffserv codepoint. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetStateDscp
    """
    return rest_request_handler.invoke_handler()


def get_state_ethertype(name, type, sequence_id):  # noqa: E501
    """get_state_ethertype

    OperationId: get_state_ethertype Ethertype field to match in Ethernet packets # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetStateEthertype
    """
    return rest_request_handler.invoke_handler()


def get_state_forwarding_action(name, type, sequence_id):  # noqa: E501
    """get_state_forwarding_action

    OperationId: get_state_forwarding_action Specifies the forwarding action.  One forwarding action must be specified for each ACL entry # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetStateForwardingAction
    """
    return rest_request_handler.invoke_handler()


def get_state_hop_limit(name, type, sequence_id):  # noqa: E501
    """get_state_hop_limit

    OperationId: get_state_hop_limit The IP packet&#39;s hop limit -- known as TTL (in hops) in IPv4 packets, and hop limit in IPv6 # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetStateHopLimit
    """
    return rest_request_handler.invoke_handler()


def get_state_id(id):  # noqa: E501
    """get_state_id

    OperationId: get_state_id User-defined identifier for the interface -- a common convention could be &#39;&lt;if name&gt;.&lt;subif index&gt;&#39; # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str

    :rtype: GetStateId
    """
    return rest_request_handler.invoke_handler()


def get_state_interface(name, type, sequence_id):  # noqa: E501
    """get_state_interface

    OperationId: get_state_interface Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetStateInterface
    """
    return rest_request_handler.invoke_handler()


def get_state_log_action(name, type, sequence_id):  # noqa: E501
    """get_state_log_action

    OperationId: get_state_log_action Specifies the log action and destination for matched packets.  The default is not to log the packet. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetStateLogAction
    """
    return rest_request_handler.invoke_handler()


def get_state_matched_octets(name, type, sequence_id):  # noqa: E501
    """get_state_matched_octets

    OperationId: get_state_matched_octets Count of the number of octets (bytes) matching the current ACL entry.  An implementation should provide this counter on a per-interface per-ACL-entry if possible.  If an implementation only supports ACL counters per entry (i.e., not broken out per interface), then the value should be equal to the aggregate count across all interfaces.  An implementation that provides counters per entry per interface is not required to also provide an aggregate count, e.g., per entry -- the user is expected to be able implement the required aggregation if such a count is needed. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetStateMatchedOctets
    """
    return rest_request_handler.invoke_handler()


def get_state_matched_packets(name, type, sequence_id):  # noqa: E501
    """get_state_matched_packets

    OperationId: get_state_matched_packets Count of the number of packets matching the current ACL entry.  An implementation should provide this counter on a per-interface per-ACL-entry if possible.  If an implementation only supports ACL counters per entry (i.e., not broken out per interface), then the value should be equal to the aggregate count across all interfaces.  An implementation that provides counters per entry per interface is not required to also provide an aggregate count, e.g., per entry -- the user is expected to be able implement the required aggregation if such a count is needed. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetStateMatchedPackets
    """
    return rest_request_handler.invoke_handler()


def get_state_name(name, type):  # noqa: E501
    """get_state_name

    OperationId: get_state_name The name of the access-list set # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str

    :rtype: GetStateName
    """
    return rest_request_handler.invoke_handler()


def get_state_protocol(name, type, sequence_id):  # noqa: E501
    """get_state_protocol

    OperationId: get_state_protocol The protocol carried in the IP packet, expressed either as its IP protocol number, or by a defined identity. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetStateProtocol
    """
    return rest_request_handler.invoke_handler()


def get_state_sequence_id(name, type, sequence_id):  # noqa: E501
    """get_state_sequence_id

    OperationId: get_state_sequence_id The sequence id determines the order in which ACL entries are applied.  The sequence id must be unique for each entry in an ACL set.  Target devices should apply the ACL entry rules in ascending order determined by sequence id (low to high), rather than the relying only on order in the list. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetStateSequenceId
    """
    return rest_request_handler.invoke_handler()


def get_state_set_name(id, set_name, type):  # noqa: E501
    """get_state_set_name

    OperationId: get_state_set_name Reference to the ACL set name applied on ingress # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str

    :rtype: GetStateSetName
    """
    return rest_request_handler.invoke_handler()


def get_state_source_address(name, type, sequence_id):  # noqa: E501
    """get_state_source_address

    OperationId: get_state_source_address Source IPv4 address prefix. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetStateSourceAddress
    """
    return rest_request_handler.invoke_handler()


def get_state_source_flow_label(name, type, sequence_id):  # noqa: E501
    """get_state_source_flow_label

    OperationId: get_state_source_flow_label Source IPv6 Flow label. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetStateSourceFlowLabel
    """
    return rest_request_handler.invoke_handler()


def get_state_source_mac(name, type, sequence_id):  # noqa: E501
    """get_state_source_mac

    OperationId: get_state_source_mac Source IEEE 802 MAC address. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetStateSourceMac
    """
    return rest_request_handler.invoke_handler()


def get_state_source_mac_mask(name, type, sequence_id):  # noqa: E501
    """get_state_source_mac_mask

    OperationId: get_state_source_mac_mask Source IEEE 802 MAC address mask. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetStateSourceMacMask
    """
    return rest_request_handler.invoke_handler()


def get_state_source_port(name, type, sequence_id):  # noqa: E501
    """get_state_source_port

    OperationId: get_state_source_port Source port or range # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetStateSourcePort
    """
    return rest_request_handler.invoke_handler()


def get_state_subinterface(name, type, sequence_id):  # noqa: E501
    """get_state_subinterface

    OperationId: get_state_subinterface Reference to a subinterface -- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetStateSubinterface
    """
    return rest_request_handler.invoke_handler()


def get_state_tcp_flags(name, type, sequence_id):  # noqa: E501
    """get_state_tcp_flags

    OperationId: get_state_tcp_flags List of TCP flags to match # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetStateTcpFlags
    """
    return rest_request_handler.invoke_handler()


def get_state_type(name, type):  # noqa: E501
    """get_state_type

    OperationId: get_state_type The type determines the fields allowed in the ACL entries belonging to the ACL set (e.g., IPv4, IPv6, etc.) # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str

    :rtype: GetStateType
    """
    return rest_request_handler.invoke_handler()


def get_transport_config(name, type, sequence_id):  # noqa: E501
    """get_transport_config

    OperationId: get_transport_config Configuration data # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetTransportConfig
    """
    return rest_request_handler.invoke_handler()


def get_transport_state(name, type, sequence_id):  # noqa: E501
    """get_transport_state

    OperationId: get_transport_state State data # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int

    :rtype: GetTransportState
    """
    return rest_request_handler.invoke_handler()


def patch_acl(body):  # noqa: E501
    """patch_acl

    OperationId: patch_acl Top level enclosing container for ACL model config and operational state data # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchAcl.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_acl_acl_sets(body):  # noqa: E501
    """patch_acl_acl_sets

    OperationId: patch_acl_acl_sets Access list entries variables enclosing container # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchAclAclSets.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_acl_acl_sets_acl_set(name, type, body):  # noqa: E501
    """patch_acl_acl_sets_acl_set

    OperationId: patch_acl_acl_sets_acl_set List of ACL sets, each comprising of a list of ACL entries # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchAclAclSetsAclSet.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_acl_entry_actions(name, type, sequence_id, body):  # noqa: E501
    """patch_acl_entry_actions

    OperationId: patch_acl_entry_actions Enclosing container for list of ACL actions associated with an entry # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchAclEntryActions.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_acl_entry_config(name, type, sequence_id, body):  # noqa: E501
    """patch_acl_entry_config

    OperationId: patch_acl_entry_config Access list entries config # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchAclEntryConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_acl_entry_config_description(name, type, sequence_id, body):  # noqa: E501
    """patch_acl_entry_config_description

    OperationId: patch_acl_entry_config_description A user-defined description, or comment, for this Access List Entry. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchAclEntryConfigDescription.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_acl_entry_input_interface(name, type, sequence_id, body):  # noqa: E501
    """patch_acl_entry_input_interface

    OperationId: patch_acl_entry_input_interface Input interface container # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchAclEntryInputInterface.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_acl_entry_ipv4(name, type, sequence_id, body):  # noqa: E501
    """patch_acl_entry_ipv4

    OperationId: patch_acl_entry_ipv4 Top level container for IPv4 match field data # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchAclEntryIpv4.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_acl_entry_ipv6(name, type, sequence_id, body):  # noqa: E501
    """patch_acl_entry_ipv6

    OperationId: patch_acl_entry_ipv6 Top-level container for IPv6 match field data # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchAclEntryIpv6.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_acl_entry_l2(name, type, sequence_id, body):  # noqa: E501
    """patch_acl_entry_l2

    OperationId: patch_acl_entry_l2 Ethernet header fields # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchAclEntryL2.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_acl_entry_transport(name, type, sequence_id, body):  # noqa: E501
    """patch_acl_entry_transport

    OperationId: patch_acl_entry_transport Transport fields container # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchAclEntryTransport.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_acl_interfaces(body):  # noqa: E501
    """patch_acl_interfaces

    OperationId: patch_acl_interfaces Enclosing container for the list of interfaces on which ACLs are set # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchAclInterfaces.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_acl_interfaces_interface(id, body):  # noqa: E501
    """patch_acl_interfaces_interface

    OperationId: patch_acl_interfaces_interface List of interfaces on which ACLs are set # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchAclInterfacesInterface.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_acl_set_acl_entries(name, type, body):  # noqa: E501
    """patch_acl_set_acl_entries

    OperationId: patch_acl_set_acl_entries Access list entries container # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchAclSetAclEntries.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_acl_set_acl_entries_acl_entry(name, type, sequence_id, body):  # noqa: E501
    """patch_acl_set_acl_entries_acl_entry

    OperationId: patch_acl_set_acl_entries_acl_entry List of ACL entries comprising an ACL set # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchAclSetAclEntriesAclEntry.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_acl_set_config(name, type, body):  # noqa: E501
    """patch_acl_set_config

    OperationId: patch_acl_set_config Access list config # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchAclSetConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_actions_config(name, type, sequence_id, body):  # noqa: E501
    """patch_actions_config

    OperationId: patch_actions_config Config data for ACL actions # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchActionsConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_config_description(name, type, body):  # noqa: E501
    """patch_config_description

    OperationId: patch_config_description Description, or comment, for the ACL set # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchConfigDescription.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_config_destination_address(name, type, sequence_id, body):  # noqa: E501
    """patch_config_destination_address

    OperationId: patch_config_destination_address Destination IPv4 address prefix. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchConfigDestinationAddress.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_config_destination_flow_label(name, type, sequence_id, body):  # noqa: E501
    """patch_config_destination_flow_label

    OperationId: patch_config_destination_flow_label Destination IPv6 Flow label. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchConfigDestinationFlowLabel.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_config_destination_mac(name, type, sequence_id, body):  # noqa: E501
    """patch_config_destination_mac

    OperationId: patch_config_destination_mac Destination IEEE 802 MAC address. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchConfigDestinationMac.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_config_destination_mac_mask(name, type, sequence_id, body):  # noqa: E501
    """patch_config_destination_mac_mask

    OperationId: patch_config_destination_mac_mask Destination IEEE 802 MAC address mask. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchConfigDestinationMacMask.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_config_destination_port(name, type, sequence_id, body):  # noqa: E501
    """patch_config_destination_port

    OperationId: patch_config_destination_port Destination port or range # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchConfigDestinationPort.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_config_dscp(name, type, sequence_id, body):  # noqa: E501
    """patch_config_dscp

    OperationId: patch_config_dscp Value of diffserv codepoint. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchConfigDscp.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_config_ethertype(name, type, sequence_id, body):  # noqa: E501
    """patch_config_ethertype

    OperationId: patch_config_ethertype Ethertype field to match in Ethernet packets # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchConfigEthertype.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_config_forwarding_action(name, type, sequence_id, body):  # noqa: E501
    """patch_config_forwarding_action

    OperationId: patch_config_forwarding_action Specifies the forwarding action.  One forwarding action must be specified for each ACL entry # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchConfigForwardingAction.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_config_hop_limit(name, type, sequence_id, body):  # noqa: E501
    """patch_config_hop_limit

    OperationId: patch_config_hop_limit The IP packet&#39;s hop limit -- known as TTL (in hops) in IPv4 packets, and hop limit in IPv6 # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchConfigHopLimit.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_config_id(id, body):  # noqa: E501
    """patch_config_id

    OperationId: patch_config_id User-defined identifier for the interface -- a common convention could be &#39;&lt;if name&gt;.&lt;subif index&gt;&#39; # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchConfigId.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_config_interface(name, type, sequence_id, body):  # noqa: E501
    """patch_config_interface

    OperationId: patch_config_interface Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchConfigInterface.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_config_log_action(name, type, sequence_id, body):  # noqa: E501
    """patch_config_log_action

    OperationId: patch_config_log_action Specifies the log action and destination for matched packets.  The default is not to log the packet. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchConfigLogAction.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_config_name(name, type, body):  # noqa: E501
    """patch_config_name

    OperationId: patch_config_name The name of the access-list set # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchConfigName.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_config_protocol(name, type, sequence_id, body):  # noqa: E501
    """patch_config_protocol

    OperationId: patch_config_protocol The protocol carried in the IP packet, expressed either as its IP protocol number, or by a defined identity. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchConfigProtocol.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_config_sequence_id(name, type, sequence_id, body):  # noqa: E501
    """patch_config_sequence_id

    OperationId: patch_config_sequence_id The sequence id determines the order in which ACL entries are applied.  The sequence id must be unique for each entry in an ACL set.  Target devices should apply the ACL entry rules in ascending order determined by sequence id (low to high), rather than the relying only on order in the list. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchConfigSequenceId.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_config_set_name(id, set_name, type, body):  # noqa: E501
    """patch_config_set_name

    OperationId: patch_config_set_name Reference to the ACL set name applied on ingress # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchConfigSetName.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_config_source_address(name, type, sequence_id, body):  # noqa: E501
    """patch_config_source_address

    OperationId: patch_config_source_address Source IPv4 address prefix. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchConfigSourceAddress.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_config_source_flow_label(name, type, sequence_id, body):  # noqa: E501
    """patch_config_source_flow_label

    OperationId: patch_config_source_flow_label Source IPv6 Flow label. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchConfigSourceFlowLabel.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_config_source_mac(name, type, sequence_id, body):  # noqa: E501
    """patch_config_source_mac

    OperationId: patch_config_source_mac Source IEEE 802 MAC address. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchConfigSourceMac.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_config_source_mac_mask(name, type, sequence_id, body):  # noqa: E501
    """patch_config_source_mac_mask

    OperationId: patch_config_source_mac_mask Source IEEE 802 MAC address mask. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchConfigSourceMacMask.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_config_source_port(name, type, sequence_id, body):  # noqa: E501
    """patch_config_source_port

    OperationId: patch_config_source_port Source port or range # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchConfigSourcePort.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_config_subinterface(name, type, sequence_id, body):  # noqa: E501
    """patch_config_subinterface

    OperationId: patch_config_subinterface Reference to a subinterface -- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchConfigSubinterface.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_config_tcp_flags(name, type, sequence_id, body):  # noqa: E501
    """patch_config_tcp_flags

    OperationId: patch_config_tcp_flags List of TCP flags to match # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchConfigTcpFlags.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_config_type(name, type, body):  # noqa: E501
    """patch_config_type

    OperationId: patch_config_type The type determines the fields allowed in the ACL entries belonging to the ACL set (e.g., IPv4, IPv6, etc.) # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchConfigType.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_egress_acl_set_config(id, set_name, type, body):  # noqa: E501
    """patch_egress_acl_set_config

    OperationId: patch_egress_acl_set_config Configuration data  # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchEgressAclSetConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_egress_acl_set_config_set_name(id, set_name, type, body):  # noqa: E501
    """patch_egress_acl_set_config_set_name

    OperationId: patch_egress_acl_set_config_set_name Reference to the ACL set name applied on egress # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchEgressAclSetConfigSetName.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_egress_acl_set_config_type(id, set_name, type, body):  # noqa: E501
    """patch_egress_acl_set_config_type

    OperationId: patch_egress_acl_set_config_type Reference to the ACL set type applied on egress. # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchEgressAclSetConfigType.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_ingress_acl_set_config(id, set_name, type, body):  # noqa: E501
    """patch_ingress_acl_set_config

    OperationId: patch_ingress_acl_set_config Configuration data  # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchIngressAclSetConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_ingress_acl_set_config_type(id, set_name, type, body):  # noqa: E501
    """patch_ingress_acl_set_config_type

    OperationId: patch_ingress_acl_set_config_type Reference to the ACL set type applied on ingress # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchIngressAclSetConfigType.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_input_interface_interface_ref(name, type, sequence_id, body):  # noqa: E501
    """patch_input_interface_interface_ref

    OperationId: patch_input_interface_interface_ref Reference to an interface or subinterface # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchInputInterfaceInterfaceRef.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_interface_config(id, body):  # noqa: E501
    """patch_interface_config

    OperationId: patch_interface_config Configuration for ACL per-interface data # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchInterfaceConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_interface_egress_acl_sets(id, body):  # noqa: E501
    """patch_interface_egress_acl_sets

    OperationId: patch_interface_egress_acl_sets Enclosing container the list of egress ACLs on the interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchInterfaceEgressAclSets.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_interface_egress_acl_sets_egress_acl_set(id, set_name, type, body):  # noqa: E501
    """patch_interface_egress_acl_sets_egress_acl_set

    OperationId: patch_interface_egress_acl_sets_egress_acl_set List of egress ACLs on the interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchInterfaceEgressAclSetsEgressAclSet.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_interface_ingress_acl_sets(id, body):  # noqa: E501
    """patch_interface_ingress_acl_sets

    OperationId: patch_interface_ingress_acl_sets Enclosing container the list of ingress ACLs on the interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchInterfaceIngressAclSets.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_interface_ingress_acl_sets_ingress_acl_set(id, set_name, type, body):  # noqa: E501
    """patch_interface_ingress_acl_sets_ingress_acl_set

    OperationId: patch_interface_ingress_acl_sets_ingress_acl_set List of ingress ACLs on the interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchInterfaceIngressAclSetsIngressAclSet.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_interface_interface_ref(id, body):  # noqa: E501
    """patch_interface_interface_ref

    OperationId: patch_interface_interface_ref Reference to an interface or subinterface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchInterfaceInterfaceRef.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_interface_interface_ref_config(id, body):  # noqa: E501
    """patch_interface_interface_ref_config

    OperationId: patch_interface_interface_ref_config Configured reference to interface / subinterface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchInterfaceInterfaceRefConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_interface_ref_config(name, type, sequence_id, body):  # noqa: E501
    """patch_interface_ref_config

    OperationId: patch_interface_ref_config Configured reference to interface / subinterface # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchInterfaceRefConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_interface_ref_config_interface(id, body):  # noqa: E501
    """patch_interface_ref_config_interface

    OperationId: patch_interface_ref_config_interface Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface. # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchInterfaceRefConfigInterface.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_interface_ref_config_subinterface(id, body):  # noqa: E501
    """patch_interface_ref_config_subinterface

    OperationId: patch_interface_ref_config_subinterface Reference to a subinterface -- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set. # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchInterfaceRefConfigSubinterface.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_ipv4_config(name, type, sequence_id, body):  # noqa: E501
    """patch_ipv4_config

    OperationId: patch_ipv4_config Configuration data for IPv4 match fields # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchIpv4Config.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_ipv6_config(name, type, sequence_id, body):  # noqa: E501
    """patch_ipv6_config

    OperationId: patch_ipv6_config Configuration data for IPv6 match fields # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchIpv6Config.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_ipv6_config_destination_address(name, type, sequence_id, body):  # noqa: E501
    """patch_ipv6_config_destination_address

    OperationId: patch_ipv6_config_destination_address Destination IPv6 address prefix. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchIpv6ConfigDestinationAddress.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_ipv6_config_dscp(name, type, sequence_id, body):  # noqa: E501
    """patch_ipv6_config_dscp

    OperationId: patch_ipv6_config_dscp Value of diffserv codepoint. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchIpv6ConfigDscp.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_ipv6_config_hop_limit(name, type, sequence_id, body):  # noqa: E501
    """patch_ipv6_config_hop_limit

    OperationId: patch_ipv6_config_hop_limit The IP packet&#39;s hop limit -- known as TTL (in hops) in IPv4 packets, and hop limit in IPv6 # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchIpv6ConfigHopLimit.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_ipv6_config_protocol(name, type, sequence_id, body):  # noqa: E501
    """patch_ipv6_config_protocol

    OperationId: patch_ipv6_config_protocol The protocol carried in the IP packet, expressed either as its IP protocol number, or by a defined identity. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchIpv6ConfigProtocol.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_ipv6_config_source_address(name, type, sequence_id, body):  # noqa: E501
    """patch_ipv6_config_source_address

    OperationId: patch_ipv6_config_source_address Source IPv6 address prefix. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchIpv6ConfigSourceAddress.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_l2_config(name, type, sequence_id, body):  # noqa: E501
    """patch_l2_config

    OperationId: patch_l2_config Configuration data # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchL2Config.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_list_base_acl_entries_acl_entry(name, type, body):  # noqa: E501
    """patch_list_base_acl_entries_acl_entry

    OperationId: patch_list_base_acl_entries_acl_entry List of ACL entries comprising an ACL set # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchListBaseAclEntriesAclEntry.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_list_base_acl_sets_acl_set(body):  # noqa: E501
    """patch_list_base_acl_sets_acl_set

    OperationId: patch_list_base_acl_sets_acl_set List of ACL sets, each comprising of a list of ACL entries # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchListBaseAclSetsAclSet.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_list_base_egress_acl_sets_egress_acl_set(id, body):  # noqa: E501
    """patch_list_base_egress_acl_sets_egress_acl_set

    OperationId: patch_list_base_egress_acl_sets_egress_acl_set List of egress ACLs on the interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchListBaseEgressAclSetsEgressAclSet.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_list_base_ingress_acl_sets_ingress_acl_set(id, body):  # noqa: E501
    """patch_list_base_ingress_acl_sets_ingress_acl_set

    OperationId: patch_list_base_ingress_acl_sets_ingress_acl_set List of ingress ACLs on the interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchListBaseIngressAclSetsIngressAclSet.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_list_base_interfaces_interface(body):  # noqa: E501
    """patch_list_base_interfaces_interface

    OperationId: patch_list_base_interfaces_interface List of interfaces on which ACLs are set # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchListBaseInterfacesInterface.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def patch_transport_config(name, type, sequence_id, body):  # noqa: E501
    """patch_transport_config

    OperationId: patch_transport_config Configuration data # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PatchTransportConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_acl_acl_sets(body):  # noqa: E501
    """post_acl_acl_sets

    OperationId: post_acl_acl_sets Access list entries variables enclosing container # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostAclAclSets.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_acl_entry_config(name, type, sequence_id, body):  # noqa: E501
    """post_acl_entry_config

    OperationId: post_acl_entry_config Access list entries config # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostAclEntryConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_acl_set_config(name, type, body):  # noqa: E501
    """post_acl_set_config

    OperationId: post_acl_set_config Access list config # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostAclSetConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_actions_config(name, type, sequence_id, body):  # noqa: E501
    """post_actions_config

    OperationId: post_actions_config Config data for ACL actions # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostActionsConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_config_forwarding_action(name, type, sequence_id, body):  # noqa: E501
    """post_config_forwarding_action

    OperationId: post_config_forwarding_action Specifies the forwarding action.  One forwarding action must be specified for each ACL entry # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostConfigForwardingAction.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_config_id(id, body):  # noqa: E501
    """post_config_id

    OperationId: post_config_id User-defined identifier for the interface -- a common convention could be &#39;&lt;if name&gt;.&lt;subif index&gt;&#39; # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostConfigId.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_config_interface(name, type, sequence_id, body):  # noqa: E501
    """post_config_interface

    OperationId: post_config_interface Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostConfigInterface.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_config_name(name, type, body):  # noqa: E501
    """post_config_name

    OperationId: post_config_name The name of the access-list set # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostConfigName.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_config_sequence_id(name, type, sequence_id, body):  # noqa: E501
    """post_config_sequence_id

    OperationId: post_config_sequence_id The sequence id determines the order in which ACL entries are applied.  The sequence id must be unique for each entry in an ACL set.  Target devices should apply the ACL entry rules in ascending order determined by sequence id (low to high), rather than the relying only on order in the list. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostConfigSequenceId.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_config_set_name(id, set_name, type, body):  # noqa: E501
    """post_config_set_name

    OperationId: post_config_set_name Reference to the ACL set name applied on ingress # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostConfigSetName.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_config_source_address(name, type, sequence_id, body):  # noqa: E501
    """post_config_source_address

    OperationId: post_config_source_address Source IPv4 address prefix. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostConfigSourceAddress.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_config_source_mac(name, type, sequence_id, body):  # noqa: E501
    """post_config_source_mac

    OperationId: post_config_source_mac Source IEEE 802 MAC address. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostConfigSourceMac.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_config_source_port(name, type, sequence_id, body):  # noqa: E501
    """post_config_source_port

    OperationId: post_config_source_port Source port or range # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostConfigSourcePort.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_egress_acl_set_config(id, set_name, type, body):  # noqa: E501
    """post_egress_acl_set_config

    OperationId: post_egress_acl_set_config Configuration data  # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostEgressAclSetConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_egress_acl_set_config_set_name(id, set_name, type, body):  # noqa: E501
    """post_egress_acl_set_config_set_name

    OperationId: post_egress_acl_set_config_set_name Reference to the ACL set name applied on egress # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostEgressAclSetConfigSetName.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_ingress_acl_set_config(id, set_name, type, body):  # noqa: E501
    """post_ingress_acl_set_config

    OperationId: post_ingress_acl_set_config Configuration data  # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostIngressAclSetConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_input_interface_interface_ref(name, type, sequence_id, body):  # noqa: E501
    """post_input_interface_interface_ref

    OperationId: post_input_interface_interface_ref Reference to an interface or subinterface # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostInputInterfaceInterfaceRef.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_interface_config(id, body):  # noqa: E501
    """post_interface_config

    OperationId: post_interface_config Configuration for ACL per-interface data # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostInterfaceConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_interface_interface_ref_config(id, body):  # noqa: E501
    """post_interface_interface_ref_config

    OperationId: post_interface_interface_ref_config Configured reference to interface / subinterface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostInterfaceInterfaceRefConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_interface_ref_config(name, type, sequence_id, body):  # noqa: E501
    """post_interface_ref_config

    OperationId: post_interface_ref_config Configured reference to interface / subinterface # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostInterfaceRefConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_interface_ref_config_interface(id, body):  # noqa: E501
    """post_interface_ref_config_interface

    OperationId: post_interface_ref_config_interface Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface. # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostInterfaceRefConfigInterface.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_ipv4_config(name, type, sequence_id, body):  # noqa: E501
    """post_ipv4_config

    OperationId: post_ipv4_config Configuration data for IPv4 match fields # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostIpv4Config.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_ipv6_config(name, type, sequence_id, body):  # noqa: E501
    """post_ipv6_config

    OperationId: post_ipv6_config Configuration data for IPv6 match fields # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostIpv6Config.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_ipv6_config_source_address(name, type, sequence_id, body):  # noqa: E501
    """post_ipv6_config_source_address

    OperationId: post_ipv6_config_source_address Source IPv6 address prefix. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostIpv6ConfigSourceAddress.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_l2_config(name, type, sequence_id, body):  # noqa: E501
    """post_l2_config

    OperationId: post_l2_config Configuration data # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostL2Config.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_list_base_acl_entries_acl_entry(name, type, body):  # noqa: E501
    """post_list_base_acl_entries_acl_entry

    OperationId: post_list_base_acl_entries_acl_entry List of ACL entries comprising an ACL set # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostListBaseAclEntriesAclEntry.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_list_base_acl_sets_acl_set(body):  # noqa: E501
    """post_list_base_acl_sets_acl_set

    OperationId: post_list_base_acl_sets_acl_set List of ACL sets, each comprising of a list of ACL entries # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostListBaseAclSetsAclSet.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_list_base_egress_acl_sets_egress_acl_set(id, body):  # noqa: E501
    """post_list_base_egress_acl_sets_egress_acl_set

    OperationId: post_list_base_egress_acl_sets_egress_acl_set List of egress ACLs on the interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostListBaseEgressAclSetsEgressAclSet.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_list_base_ingress_acl_sets_ingress_acl_set(id, body):  # noqa: E501
    """post_list_base_ingress_acl_sets_ingress_acl_set

    OperationId: post_list_base_ingress_acl_sets_ingress_acl_set List of ingress ACLs on the interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostListBaseIngressAclSetsIngressAclSet.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_list_base_interfaces_interface(body):  # noqa: E501
    """post_list_base_interfaces_interface

    OperationId: post_list_base_interfaces_interface List of interfaces on which ACLs are set # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostListBaseInterfacesInterface.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def post_transport_config(name, type, sequence_id, body):  # noqa: E501
    """post_transport_config

    OperationId: post_transport_config Configuration data # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostTransportConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_acl(body):  # noqa: E501
    """put_acl

    OperationId: put_acl Top level enclosing container for ACL model config and operational state data # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutAcl.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_acl_acl_sets(body):  # noqa: E501
    """put_acl_acl_sets

    OperationId: put_acl_acl_sets Access list entries variables enclosing container # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutAclAclSets.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_acl_acl_sets_acl_set(name, type, body):  # noqa: E501
    """put_acl_acl_sets_acl_set

    OperationId: put_acl_acl_sets_acl_set List of ACL sets, each comprising of a list of ACL entries # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutAclAclSetsAclSet.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_acl_entry_actions(name, type, sequence_id, body):  # noqa: E501
    """put_acl_entry_actions

    OperationId: put_acl_entry_actions Enclosing container for list of ACL actions associated with an entry # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutAclEntryActions.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_acl_entry_config(name, type, sequence_id, body):  # noqa: E501
    """put_acl_entry_config

    OperationId: put_acl_entry_config Access list entries config # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutAclEntryConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_acl_entry_config_description(name, type, sequence_id, body):  # noqa: E501
    """put_acl_entry_config_description

    OperationId: put_acl_entry_config_description A user-defined description, or comment, for this Access List Entry. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutAclEntryConfigDescription.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_acl_entry_input_interface(name, type, sequence_id, body):  # noqa: E501
    """put_acl_entry_input_interface

    OperationId: put_acl_entry_input_interface Input interface container # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutAclEntryInputInterface.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_acl_entry_ipv4(name, type, sequence_id, body):  # noqa: E501
    """put_acl_entry_ipv4

    OperationId: put_acl_entry_ipv4 Top level container for IPv4 match field data # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutAclEntryIpv4.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_acl_entry_ipv6(name, type, sequence_id, body):  # noqa: E501
    """put_acl_entry_ipv6

    OperationId: put_acl_entry_ipv6 Top-level container for IPv6 match field data # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutAclEntryIpv6.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_acl_entry_l2(name, type, sequence_id, body):  # noqa: E501
    """put_acl_entry_l2

    OperationId: put_acl_entry_l2 Ethernet header fields # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutAclEntryL2.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_acl_entry_transport(name, type, sequence_id, body):  # noqa: E501
    """put_acl_entry_transport

    OperationId: put_acl_entry_transport Transport fields container # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutAclEntryTransport.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_acl_interfaces(body):  # noqa: E501
    """put_acl_interfaces

    OperationId: put_acl_interfaces Enclosing container for the list of interfaces on which ACLs are set # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutAclInterfaces.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_acl_interfaces_interface(id, body):  # noqa: E501
    """put_acl_interfaces_interface

    OperationId: put_acl_interfaces_interface List of interfaces on which ACLs are set # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutAclInterfacesInterface.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_acl_set_acl_entries(name, type, body):  # noqa: E501
    """put_acl_set_acl_entries

    OperationId: put_acl_set_acl_entries Access list entries container # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutAclSetAclEntries.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_acl_set_acl_entries_acl_entry(name, type, sequence_id, body):  # noqa: E501
    """put_acl_set_acl_entries_acl_entry

    OperationId: put_acl_set_acl_entries_acl_entry List of ACL entries comprising an ACL set # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutAclSetAclEntriesAclEntry.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_acl_set_config(name, type, body):  # noqa: E501
    """put_acl_set_config

    OperationId: put_acl_set_config Access list config # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutAclSetConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_actions_config(name, type, sequence_id, body):  # noqa: E501
    """put_actions_config

    OperationId: put_actions_config Config data for ACL actions # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutActionsConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_config_description(name, type, body):  # noqa: E501
    """put_config_description

    OperationId: put_config_description Description, or comment, for the ACL set # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutConfigDescription.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_config_destination_address(name, type, sequence_id, body):  # noqa: E501
    """put_config_destination_address

    OperationId: put_config_destination_address Destination IPv4 address prefix. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutConfigDestinationAddress.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_config_destination_flow_label(name, type, sequence_id, body):  # noqa: E501
    """put_config_destination_flow_label

    OperationId: put_config_destination_flow_label Destination IPv6 Flow label. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutConfigDestinationFlowLabel.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_config_destination_mac(name, type, sequence_id, body):  # noqa: E501
    """put_config_destination_mac

    OperationId: put_config_destination_mac Destination IEEE 802 MAC address. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutConfigDestinationMac.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_config_destination_mac_mask(name, type, sequence_id, body):  # noqa: E501
    """put_config_destination_mac_mask

    OperationId: put_config_destination_mac_mask Destination IEEE 802 MAC address mask. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutConfigDestinationMacMask.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_config_destination_port(name, type, sequence_id, body):  # noqa: E501
    """put_config_destination_port

    OperationId: put_config_destination_port Destination port or range # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutConfigDestinationPort.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_config_dscp(name, type, sequence_id, body):  # noqa: E501
    """put_config_dscp

    OperationId: put_config_dscp Value of diffserv codepoint. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutConfigDscp.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_config_ethertype(name, type, sequence_id, body):  # noqa: E501
    """put_config_ethertype

    OperationId: put_config_ethertype Ethertype field to match in Ethernet packets # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutConfigEthertype.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_config_forwarding_action(name, type, sequence_id, body):  # noqa: E501
    """put_config_forwarding_action

    OperationId: put_config_forwarding_action Specifies the forwarding action.  One forwarding action must be specified for each ACL entry # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutConfigForwardingAction.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_config_hop_limit(name, type, sequence_id, body):  # noqa: E501
    """put_config_hop_limit

    OperationId: put_config_hop_limit The IP packet&#39;s hop limit -- known as TTL (in hops) in IPv4 packets, and hop limit in IPv6 # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutConfigHopLimit.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_config_id(id, body):  # noqa: E501
    """put_config_id

    OperationId: put_config_id User-defined identifier for the interface -- a common convention could be &#39;&lt;if name&gt;.&lt;subif index&gt;&#39; # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutConfigId.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_config_interface(name, type, sequence_id, body):  # noqa: E501
    """put_config_interface

    OperationId: put_config_interface Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutConfigInterface.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_config_log_action(name, type, sequence_id, body):  # noqa: E501
    """put_config_log_action

    OperationId: put_config_log_action Specifies the log action and destination for matched packets.  The default is not to log the packet. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutConfigLogAction.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_config_name(name, type, body):  # noqa: E501
    """put_config_name

    OperationId: put_config_name The name of the access-list set # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutConfigName.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_config_protocol(name, type, sequence_id, body):  # noqa: E501
    """put_config_protocol

    OperationId: put_config_protocol The protocol carried in the IP packet, expressed either as its IP protocol number, or by a defined identity. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutConfigProtocol.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_config_sequence_id(name, type, sequence_id, body):  # noqa: E501
    """put_config_sequence_id

    OperationId: put_config_sequence_id The sequence id determines the order in which ACL entries are applied.  The sequence id must be unique for each entry in an ACL set.  Target devices should apply the ACL entry rules in ascending order determined by sequence id (low to high), rather than the relying only on order in the list. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutConfigSequenceId.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_config_set_name(id, set_name, type, body):  # noqa: E501
    """put_config_set_name

    OperationId: put_config_set_name Reference to the ACL set name applied on ingress # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutConfigSetName.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_config_source_address(name, type, sequence_id, body):  # noqa: E501
    """put_config_source_address

    OperationId: put_config_source_address Source IPv4 address prefix. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutConfigSourceAddress.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_config_source_flow_label(name, type, sequence_id, body):  # noqa: E501
    """put_config_source_flow_label

    OperationId: put_config_source_flow_label Source IPv6 Flow label. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutConfigSourceFlowLabel.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_config_source_mac(name, type, sequence_id, body):  # noqa: E501
    """put_config_source_mac

    OperationId: put_config_source_mac Source IEEE 802 MAC address. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutConfigSourceMac.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_config_source_mac_mask(name, type, sequence_id, body):  # noqa: E501
    """put_config_source_mac_mask

    OperationId: put_config_source_mac_mask Source IEEE 802 MAC address mask. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutConfigSourceMacMask.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_config_source_port(name, type, sequence_id, body):  # noqa: E501
    """put_config_source_port

    OperationId: put_config_source_port Source port or range # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutConfigSourcePort.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_config_subinterface(name, type, sequence_id, body):  # noqa: E501
    """put_config_subinterface

    OperationId: put_config_subinterface Reference to a subinterface -- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutConfigSubinterface.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_config_tcp_flags(name, type, sequence_id, body):  # noqa: E501
    """put_config_tcp_flags

    OperationId: put_config_tcp_flags List of TCP flags to match # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutConfigTcpFlags.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_config_type(name, type, body):  # noqa: E501
    """put_config_type

    OperationId: put_config_type The type determines the fields allowed in the ACL entries belonging to the ACL set (e.g., IPv4, IPv6, etc.) # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutConfigType.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_egress_acl_set_config(id, set_name, type, body):  # noqa: E501
    """put_egress_acl_set_config

    OperationId: put_egress_acl_set_config Configuration data  # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutEgressAclSetConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_egress_acl_set_config_set_name(id, set_name, type, body):  # noqa: E501
    """put_egress_acl_set_config_set_name

    OperationId: put_egress_acl_set_config_set_name Reference to the ACL set name applied on egress # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutEgressAclSetConfigSetName.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_egress_acl_set_config_type(id, set_name, type, body):  # noqa: E501
    """put_egress_acl_set_config_type

    OperationId: put_egress_acl_set_config_type Reference to the ACL set type applied on egress. # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutEgressAclSetConfigType.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_ingress_acl_set_config(id, set_name, type, body):  # noqa: E501
    """put_ingress_acl_set_config

    OperationId: put_ingress_acl_set_config Configuration data  # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutIngressAclSetConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_ingress_acl_set_config_type(id, set_name, type, body):  # noqa: E501
    """put_ingress_acl_set_config_type

    OperationId: put_ingress_acl_set_config_type Reference to the ACL set type applied on ingress # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutIngressAclSetConfigType.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_input_interface_interface_ref(name, type, sequence_id, body):  # noqa: E501
    """put_input_interface_interface_ref

    OperationId: put_input_interface_interface_ref Reference to an interface or subinterface # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutInputInterfaceInterfaceRef.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_interface_config(id, body):  # noqa: E501
    """put_interface_config

    OperationId: put_interface_config Configuration for ACL per-interface data # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutInterfaceConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_interface_egress_acl_sets(id, body):  # noqa: E501
    """put_interface_egress_acl_sets

    OperationId: put_interface_egress_acl_sets Enclosing container the list of egress ACLs on the interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutInterfaceEgressAclSets.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_interface_egress_acl_sets_egress_acl_set(id, set_name, type, body):  # noqa: E501
    """put_interface_egress_acl_sets_egress_acl_set

    OperationId: put_interface_egress_acl_sets_egress_acl_set List of egress ACLs on the interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutInterfaceEgressAclSetsEgressAclSet.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_interface_ingress_acl_sets(id, body):  # noqa: E501
    """put_interface_ingress_acl_sets

    OperationId: put_interface_ingress_acl_sets Enclosing container the list of ingress ACLs on the interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutInterfaceIngressAclSets.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_interface_ingress_acl_sets_ingress_acl_set(id, set_name, type, body):  # noqa: E501
    """put_interface_ingress_acl_sets_ingress_acl_set

    OperationId: put_interface_ingress_acl_sets_ingress_acl_set List of ingress ACLs on the interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param set_name: Reference to set name list key
    :type set_name: str
    :param type: Reference to type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutInterfaceIngressAclSetsIngressAclSet.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_interface_interface_ref(id, body):  # noqa: E501
    """put_interface_interface_ref

    OperationId: put_interface_interface_ref Reference to an interface or subinterface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutInterfaceInterfaceRef.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_interface_interface_ref_config(id, body):  # noqa: E501
    """put_interface_interface_ref_config

    OperationId: put_interface_interface_ref_config Configured reference to interface / subinterface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutInterfaceInterfaceRefConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_interface_ref_config(name, type, sequence_id, body):  # noqa: E501
    """put_interface_ref_config

    OperationId: put_interface_ref_config Configured reference to interface / subinterface # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutInterfaceRefConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_interface_ref_config_interface(id, body):  # noqa: E501
    """put_interface_ref_config_interface

    OperationId: put_interface_ref_config_interface Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface. # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutInterfaceRefConfigInterface.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_interface_ref_config_subinterface(id, body):  # noqa: E501
    """put_interface_ref_config_subinterface

    OperationId: put_interface_ref_config_subinterface Reference to a subinterface -- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set. # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutInterfaceRefConfigSubinterface.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_ipv4_config(name, type, sequence_id, body):  # noqa: E501
    """put_ipv4_config

    OperationId: put_ipv4_config Configuration data for IPv4 match fields # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutIpv4Config.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_ipv6_config(name, type, sequence_id, body):  # noqa: E501
    """put_ipv6_config

    OperationId: put_ipv6_config Configuration data for IPv6 match fields # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutIpv6Config.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_ipv6_config_destination_address(name, type, sequence_id, body):  # noqa: E501
    """put_ipv6_config_destination_address

    OperationId: put_ipv6_config_destination_address Destination IPv6 address prefix. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutIpv6ConfigDestinationAddress.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_ipv6_config_dscp(name, type, sequence_id, body):  # noqa: E501
    """put_ipv6_config_dscp

    OperationId: put_ipv6_config_dscp Value of diffserv codepoint. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutIpv6ConfigDscp.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_ipv6_config_hop_limit(name, type, sequence_id, body):  # noqa: E501
    """put_ipv6_config_hop_limit

    OperationId: put_ipv6_config_hop_limit The IP packet&#39;s hop limit -- known as TTL (in hops) in IPv4 packets, and hop limit in IPv6 # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutIpv6ConfigHopLimit.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_ipv6_config_protocol(name, type, sequence_id, body):  # noqa: E501
    """put_ipv6_config_protocol

    OperationId: put_ipv6_config_protocol The protocol carried in the IP packet, expressed either as its IP protocol number, or by a defined identity. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutIpv6ConfigProtocol.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_ipv6_config_source_address(name, type, sequence_id, body):  # noqa: E501
    """put_ipv6_config_source_address

    OperationId: put_ipv6_config_source_address Source IPv6 address prefix. # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutIpv6ConfigSourceAddress.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_l2_config(name, type, sequence_id, body):  # noqa: E501
    """put_l2_config

    OperationId: put_l2_config Configuration data # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutL2Config.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_list_base_acl_entries_acl_entry(name, type, body):  # noqa: E501
    """put_list_base_acl_entries_acl_entry

    OperationId: put_list_base_acl_entries_acl_entry List of ACL entries comprising an ACL set # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutListBaseAclEntriesAclEntry.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_list_base_acl_sets_acl_set(body):  # noqa: E501
    """put_list_base_acl_sets_acl_set

    OperationId: put_list_base_acl_sets_acl_set List of ACL sets, each comprising of a list of ACL entries # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutListBaseAclSetsAclSet.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_list_base_egress_acl_sets_egress_acl_set(id, body):  # noqa: E501
    """put_list_base_egress_acl_sets_egress_acl_set

    OperationId: put_list_base_egress_acl_sets_egress_acl_set List of egress ACLs on the interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutListBaseEgressAclSetsEgressAclSet.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_list_base_ingress_acl_sets_ingress_acl_set(id, body):  # noqa: E501
    """put_list_base_ingress_acl_sets_ingress_acl_set

    OperationId: put_list_base_ingress_acl_sets_ingress_acl_set List of ingress ACLs on the interface # noqa: E501

    :param id: Reference to the interface id list key
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutListBaseIngressAclSetsIngressAclSet.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_list_base_interfaces_interface(body):  # noqa: E501
    """put_list_base_interfaces_interface

    OperationId: put_list_base_interfaces_interface List of interfaces on which ACLs are set # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutListBaseInterfacesInterface.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()


def put_transport_config(name, type, sequence_id, body):  # noqa: E501
    """put_transport_config

    OperationId: put_transport_config Configuration data # noqa: E501

    :param name: Reference to the name list key
    :type name: str
    :param type: Reference to the type list key
    :type type: str
    :param sequence_id: references the list key
    :type sequence_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutTransportConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return rest_request_handler.invoke_handler()
