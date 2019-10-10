# sonic_acl_client.SonicAclApi

All URIs are relative to *https://localhost/restconf/data*

Method | HTTP request | Description
------------- | ------------- | -------------
[**del_llist_sonic_acl_sonic_acl_acl_table_acl_table_list_ports**](SonicAclApi.md#del_llist_sonic_acl_sonic_acl_acl_table_acl_table_list_ports) | **DELETE** /sonic-acl:sonic-acl/ACL_TABLE/ACL_TABLE_LIST&#x3D;{aclname}/ports&#x3D;{ports} | 
[**delete_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list**](SonicAclApi.md#delete_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list) | **DELETE** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST | 
[**delete_list_sonic_acl_sonic_acl_acl_table_acl_table_list**](SonicAclApi.md#delete_list_sonic_acl_sonic_acl_acl_table_acl_table_list) | **DELETE** /sonic-acl:sonic-acl/ACL_TABLE/ACL_TABLE_LIST | 
[**delete_sonic_acl_sonic_acl**](SonicAclApi.md#delete_sonic_acl_sonic_acl) | **DELETE** /sonic-acl:sonic-acl | 
[**delete_sonic_acl_sonic_acl_acl_rule**](SonicAclApi.md#delete_sonic_acl_sonic_acl_acl_rule) | **DELETE** /sonic-acl:sonic-acl/ACL_RULE | 
[**delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list**](SonicAclApi.md#delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list) | **DELETE** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename} | 
[**delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp**](SonicAclApi.md#delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp) | **DELETE** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/DSCP | 
[**delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip**](SonicAclApi.md#delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip) | **DELETE** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/DST_IP | 
[**delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6**](SonicAclApi.md#delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6) | **DELETE** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/DST_IPV6 | 
[**delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type**](SonicAclApi.md#delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type) | **DELETE** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/ETHER_TYPE | 
[**delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol**](SonicAclApi.md#delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol) | **DELETE** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/IP_PROTOCOL | 
[**delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type**](SonicAclApi.md#delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type) | **DELETE** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/IP_TYPE | 
[**delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port**](SonicAclApi.md#delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port) | **DELETE** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/L4_DST_PORT | 
[**delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range**](SonicAclApi.md#delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range) | **DELETE** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/L4_DST_PORT_RANGE | 
[**delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port**](SonicAclApi.md#delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port) | **DELETE** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/L4_SRC_PORT | 
[**delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range**](SonicAclApi.md#delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range) | **DELETE** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/L4_SRC_PORT_RANGE | 
[**delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action**](SonicAclApi.md#delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action) | **DELETE** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/MIRROR_ACTION | 
[**delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action**](SonicAclApi.md#delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action) | **DELETE** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/PACKET_ACTION | 
[**delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority**](SonicAclApi.md#delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority) | **DELETE** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/PRIORITY | 
[**delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description**](SonicAclApi.md#delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description) | **DELETE** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/RULE_DESCRIPTION | 
[**delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip**](SonicAclApi.md#delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip) | **DELETE** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/SRC_IP | 
[**delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6**](SonicAclApi.md#delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6) | **DELETE** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/SRC_IPV6 | 
[**delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags**](SonicAclApi.md#delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags) | **DELETE** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/TCP_FLAGS | 
[**delete_sonic_acl_sonic_acl_acl_table**](SonicAclApi.md#delete_sonic_acl_sonic_acl_acl_table) | **DELETE** /sonic-acl:sonic-acl/ACL_TABLE | 
[**delete_sonic_acl_sonic_acl_acl_table_acl_table_list**](SonicAclApi.md#delete_sonic_acl_sonic_acl_acl_table_acl_table_list) | **DELETE** /sonic-acl:sonic-acl/ACL_TABLE/ACL_TABLE_LIST&#x3D;{aclname} | 
[**delete_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc**](SonicAclApi.md#delete_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc) | **DELETE** /sonic-acl:sonic-acl/ACL_TABLE/ACL_TABLE_LIST&#x3D;{aclname}/policy_desc | 
[**delete_sonic_acl_sonic_acl_acl_table_acl_table_list_ports**](SonicAclApi.md#delete_sonic_acl_sonic_acl_acl_table_acl_table_list_ports) | **DELETE** /sonic-acl:sonic-acl/ACL_TABLE/ACL_TABLE_LIST&#x3D;{aclname}/ports | 
[**delete_sonic_acl_sonic_acl_acl_table_acl_table_list_stage**](SonicAclApi.md#delete_sonic_acl_sonic_acl_acl_table_acl_table_list_stage) | **DELETE** /sonic-acl:sonic-acl/ACL_TABLE/ACL_TABLE_LIST&#x3D;{aclname}/stage | 
[**delete_sonic_acl_sonic_acl_acl_table_acl_table_list_type**](SonicAclApi.md#delete_sonic_acl_sonic_acl_acl_table_acl_table_list_type) | **DELETE** /sonic-acl:sonic-acl/ACL_TABLE/ACL_TABLE_LIST&#x3D;{aclname}/type | 
[**get_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list**](SonicAclApi.md#get_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list) | **GET** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST | 
[**get_list_sonic_acl_sonic_acl_acl_table_acl_table_list**](SonicAclApi.md#get_list_sonic_acl_sonic_acl_acl_table_acl_table_list) | **GET** /sonic-acl:sonic-acl/ACL_TABLE/ACL_TABLE_LIST | 
[**get_llist_sonic_acl_sonic_acl_acl_table_acl_table_list_ports**](SonicAclApi.md#get_llist_sonic_acl_sonic_acl_acl_table_acl_table_list_ports) | **GET** /sonic-acl:sonic-acl/ACL_TABLE/ACL_TABLE_LIST&#x3D;{aclname}/ports&#x3D;{ports} | 
[**get_sonic_acl_sonic_acl**](SonicAclApi.md#get_sonic_acl_sonic_acl) | **GET** /sonic-acl:sonic-acl | 
[**get_sonic_acl_sonic_acl_acl_rule**](SonicAclApi.md#get_sonic_acl_sonic_acl_acl_rule) | **GET** /sonic-acl:sonic-acl/ACL_RULE | 
[**get_sonic_acl_sonic_acl_acl_rule_acl_rule_list**](SonicAclApi.md#get_sonic_acl_sonic_acl_acl_rule_acl_rule_list) | **GET** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename} | 
[**get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp**](SonicAclApi.md#get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp) | **GET** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/DSCP | 
[**get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip**](SonicAclApi.md#get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip) | **GET** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/DST_IP | 
[**get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6**](SonicAclApi.md#get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6) | **GET** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/DST_IPV6 | 
[**get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type**](SonicAclApi.md#get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type) | **GET** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/ETHER_TYPE | 
[**get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol**](SonicAclApi.md#get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol) | **GET** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/IP_PROTOCOL | 
[**get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type**](SonicAclApi.md#get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type) | **GET** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/IP_TYPE | 
[**get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port**](SonicAclApi.md#get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port) | **GET** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/L4_DST_PORT | 
[**get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range**](SonicAclApi.md#get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range) | **GET** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/L4_DST_PORT_RANGE | 
[**get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port**](SonicAclApi.md#get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port) | **GET** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/L4_SRC_PORT | 
[**get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range**](SonicAclApi.md#get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range) | **GET** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/L4_SRC_PORT_RANGE | 
[**get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action**](SonicAclApi.md#get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action) | **GET** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/MIRROR_ACTION | 
[**get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action**](SonicAclApi.md#get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action) | **GET** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/PACKET_ACTION | 
[**get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority**](SonicAclApi.md#get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority) | **GET** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/PRIORITY | 
[**get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description**](SonicAclApi.md#get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description) | **GET** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/RULE_DESCRIPTION | 
[**get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip**](SonicAclApi.md#get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip) | **GET** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/SRC_IP | 
[**get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6**](SonicAclApi.md#get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6) | **GET** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/SRC_IPV6 | 
[**get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags**](SonicAclApi.md#get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags) | **GET** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/TCP_FLAGS | 
[**get_sonic_acl_sonic_acl_acl_table**](SonicAclApi.md#get_sonic_acl_sonic_acl_acl_table) | **GET** /sonic-acl:sonic-acl/ACL_TABLE | 
[**get_sonic_acl_sonic_acl_acl_table_acl_table_list**](SonicAclApi.md#get_sonic_acl_sonic_acl_acl_table_acl_table_list) | **GET** /sonic-acl:sonic-acl/ACL_TABLE/ACL_TABLE_LIST&#x3D;{aclname} | 
[**get_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc**](SonicAclApi.md#get_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc) | **GET** /sonic-acl:sonic-acl/ACL_TABLE/ACL_TABLE_LIST&#x3D;{aclname}/policy_desc | 
[**get_sonic_acl_sonic_acl_acl_table_acl_table_list_ports**](SonicAclApi.md#get_sonic_acl_sonic_acl_acl_table_acl_table_list_ports) | **GET** /sonic-acl:sonic-acl/ACL_TABLE/ACL_TABLE_LIST&#x3D;{aclname}/ports | 
[**get_sonic_acl_sonic_acl_acl_table_acl_table_list_stage**](SonicAclApi.md#get_sonic_acl_sonic_acl_acl_table_acl_table_list_stage) | **GET** /sonic-acl:sonic-acl/ACL_TABLE/ACL_TABLE_LIST&#x3D;{aclname}/stage | 
[**get_sonic_acl_sonic_acl_acl_table_acl_table_list_type**](SonicAclApi.md#get_sonic_acl_sonic_acl_acl_table_acl_table_list_type) | **GET** /sonic-acl:sonic-acl/ACL_TABLE/ACL_TABLE_LIST&#x3D;{aclname}/type | 
[**patch_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list**](SonicAclApi.md#patch_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list) | **PATCH** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST | 
[**patch_list_sonic_acl_sonic_acl_acl_table_acl_table_list**](SonicAclApi.md#patch_list_sonic_acl_sonic_acl_acl_table_acl_table_list) | **PATCH** /sonic-acl:sonic-acl/ACL_TABLE/ACL_TABLE_LIST | 
[**patch_sonic_acl_sonic_acl**](SonicAclApi.md#patch_sonic_acl_sonic_acl) | **PATCH** /sonic-acl:sonic-acl | 
[**patch_sonic_acl_sonic_acl_acl_rule**](SonicAclApi.md#patch_sonic_acl_sonic_acl_acl_rule) | **PATCH** /sonic-acl:sonic-acl/ACL_RULE | 
[**patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list**](SonicAclApi.md#patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list) | **PATCH** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename} | 
[**patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp**](SonicAclApi.md#patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp) | **PATCH** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/DSCP | 
[**patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip**](SonicAclApi.md#patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip) | **PATCH** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/DST_IP | 
[**patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6**](SonicAclApi.md#patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6) | **PATCH** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/DST_IPV6 | 
[**patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type**](SonicAclApi.md#patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type) | **PATCH** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/ETHER_TYPE | 
[**patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol**](SonicAclApi.md#patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol) | **PATCH** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/IP_PROTOCOL | 
[**patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type**](SonicAclApi.md#patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type) | **PATCH** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/IP_TYPE | 
[**patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port**](SonicAclApi.md#patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port) | **PATCH** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/L4_DST_PORT | 
[**patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range**](SonicAclApi.md#patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range) | **PATCH** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/L4_DST_PORT_RANGE | 
[**patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port**](SonicAclApi.md#patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port) | **PATCH** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/L4_SRC_PORT | 
[**patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range**](SonicAclApi.md#patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range) | **PATCH** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/L4_SRC_PORT_RANGE | 
[**patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action**](SonicAclApi.md#patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action) | **PATCH** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/MIRROR_ACTION | 
[**patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action**](SonicAclApi.md#patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action) | **PATCH** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/PACKET_ACTION | 
[**patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority**](SonicAclApi.md#patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority) | **PATCH** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/PRIORITY | 
[**patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description**](SonicAclApi.md#patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description) | **PATCH** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/RULE_DESCRIPTION | 
[**patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip**](SonicAclApi.md#patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip) | **PATCH** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/SRC_IP | 
[**patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6**](SonicAclApi.md#patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6) | **PATCH** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/SRC_IPV6 | 
[**patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags**](SonicAclApi.md#patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags) | **PATCH** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/TCP_FLAGS | 
[**patch_sonic_acl_sonic_acl_acl_table**](SonicAclApi.md#patch_sonic_acl_sonic_acl_acl_table) | **PATCH** /sonic-acl:sonic-acl/ACL_TABLE | 
[**patch_sonic_acl_sonic_acl_acl_table_acl_table_list**](SonicAclApi.md#patch_sonic_acl_sonic_acl_acl_table_acl_table_list) | **PATCH** /sonic-acl:sonic-acl/ACL_TABLE/ACL_TABLE_LIST&#x3D;{aclname} | 
[**patch_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc**](SonicAclApi.md#patch_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc) | **PATCH** /sonic-acl:sonic-acl/ACL_TABLE/ACL_TABLE_LIST&#x3D;{aclname}/policy_desc | 
[**patch_sonic_acl_sonic_acl_acl_table_acl_table_list_ports**](SonicAclApi.md#patch_sonic_acl_sonic_acl_acl_table_acl_table_list_ports) | **PATCH** /sonic-acl:sonic-acl/ACL_TABLE/ACL_TABLE_LIST&#x3D;{aclname}/ports | 
[**patch_sonic_acl_sonic_acl_acl_table_acl_table_list_stage**](SonicAclApi.md#patch_sonic_acl_sonic_acl_acl_table_acl_table_list_stage) | **PATCH** /sonic-acl:sonic-acl/ACL_TABLE/ACL_TABLE_LIST&#x3D;{aclname}/stage | 
[**patch_sonic_acl_sonic_acl_acl_table_acl_table_list_type**](SonicAclApi.md#patch_sonic_acl_sonic_acl_acl_table_acl_table_list_type) | **PATCH** /sonic-acl:sonic-acl/ACL_TABLE/ACL_TABLE_LIST&#x3D;{aclname}/type | 
[**post_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list**](SonicAclApi.md#post_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list) | **POST** /sonic-acl:sonic-acl/ACL_RULE | 
[**post_list_sonic_acl_sonic_acl_acl_table_acl_table_list**](SonicAclApi.md#post_list_sonic_acl_sonic_acl_acl_table_acl_table_list) | **POST** /sonic-acl:sonic-acl/ACL_TABLE | 
[**post_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority**](SonicAclApi.md#post_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority) | **POST** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename} | 
[**post_sonic_acl_sonic_acl_acl_table**](SonicAclApi.md#post_sonic_acl_sonic_acl_acl_table) | **POST** /sonic-acl:sonic-acl | 
[**post_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc**](SonicAclApi.md#post_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc) | **POST** /sonic-acl:sonic-acl/ACL_TABLE/ACL_TABLE_LIST&#x3D;{aclname} | 
[**put_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list**](SonicAclApi.md#put_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list) | **PUT** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST | 
[**put_list_sonic_acl_sonic_acl_acl_table_acl_table_list**](SonicAclApi.md#put_list_sonic_acl_sonic_acl_acl_table_acl_table_list) | **PUT** /sonic-acl:sonic-acl/ACL_TABLE/ACL_TABLE_LIST | 
[**put_sonic_acl_sonic_acl**](SonicAclApi.md#put_sonic_acl_sonic_acl) | **PUT** /sonic-acl:sonic-acl | 
[**put_sonic_acl_sonic_acl_acl_rule**](SonicAclApi.md#put_sonic_acl_sonic_acl_acl_rule) | **PUT** /sonic-acl:sonic-acl/ACL_RULE | 
[**put_sonic_acl_sonic_acl_acl_rule_acl_rule_list**](SonicAclApi.md#put_sonic_acl_sonic_acl_acl_rule_acl_rule_list) | **PUT** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename} | 
[**put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp**](SonicAclApi.md#put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp) | **PUT** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/DSCP | 
[**put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip**](SonicAclApi.md#put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip) | **PUT** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/DST_IP | 
[**put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6**](SonicAclApi.md#put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6) | **PUT** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/DST_IPV6 | 
[**put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type**](SonicAclApi.md#put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type) | **PUT** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/ETHER_TYPE | 
[**put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol**](SonicAclApi.md#put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol) | **PUT** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/IP_PROTOCOL | 
[**put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type**](SonicAclApi.md#put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type) | **PUT** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/IP_TYPE | 
[**put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port**](SonicAclApi.md#put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port) | **PUT** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/L4_DST_PORT | 
[**put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range**](SonicAclApi.md#put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range) | **PUT** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/L4_DST_PORT_RANGE | 
[**put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port**](SonicAclApi.md#put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port) | **PUT** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/L4_SRC_PORT | 
[**put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range**](SonicAclApi.md#put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range) | **PUT** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/L4_SRC_PORT_RANGE | 
[**put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action**](SonicAclApi.md#put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action) | **PUT** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/MIRROR_ACTION | 
[**put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action**](SonicAclApi.md#put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action) | **PUT** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/PACKET_ACTION | 
[**put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority**](SonicAclApi.md#put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority) | **PUT** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/PRIORITY | 
[**put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description**](SonicAclApi.md#put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description) | **PUT** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/RULE_DESCRIPTION | 
[**put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip**](SonicAclApi.md#put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip) | **PUT** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/SRC_IP | 
[**put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6**](SonicAclApi.md#put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6) | **PUT** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/SRC_IPV6 | 
[**put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags**](SonicAclApi.md#put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags) | **PUT** /sonic-acl:sonic-acl/ACL_RULE/ACL_RULE_LIST&#x3D;{aclname},{rulename}/TCP_FLAGS | 
[**put_sonic_acl_sonic_acl_acl_table**](SonicAclApi.md#put_sonic_acl_sonic_acl_acl_table) | **PUT** /sonic-acl:sonic-acl/ACL_TABLE | 
[**put_sonic_acl_sonic_acl_acl_table_acl_table_list**](SonicAclApi.md#put_sonic_acl_sonic_acl_acl_table_acl_table_list) | **PUT** /sonic-acl:sonic-acl/ACL_TABLE/ACL_TABLE_LIST&#x3D;{aclname} | 
[**put_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc**](SonicAclApi.md#put_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc) | **PUT** /sonic-acl:sonic-acl/ACL_TABLE/ACL_TABLE_LIST&#x3D;{aclname}/policy_desc | 
[**put_sonic_acl_sonic_acl_acl_table_acl_table_list_ports**](SonicAclApi.md#put_sonic_acl_sonic_acl_acl_table_acl_table_list_ports) | **PUT** /sonic-acl:sonic-acl/ACL_TABLE/ACL_TABLE_LIST&#x3D;{aclname}/ports | 
[**put_sonic_acl_sonic_acl_acl_table_acl_table_list_stage**](SonicAclApi.md#put_sonic_acl_sonic_acl_acl_table_acl_table_list_stage) | **PUT** /sonic-acl:sonic-acl/ACL_TABLE/ACL_TABLE_LIST&#x3D;{aclname}/stage | 
[**put_sonic_acl_sonic_acl_acl_table_acl_table_list_type**](SonicAclApi.md#put_sonic_acl_sonic_acl_acl_table_acl_table_list_type) | **PUT** /sonic-acl:sonic-acl/ACL_TABLE/ACL_TABLE_LIST&#x3D;{aclname}/type | 


# **del_llist_sonic_acl_sonic_acl_acl_table_acl_table_list_ports**
> del_llist_sonic_acl_sonic_acl_acl_table_acl_table_list_ports(aclname, ports)



OperationId: del_llist_sonic_acl_sonic_acl_acl_table_acl_table_list_ports 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
ports = 'ports_example' # str | 

try:
    api_instance.del_llist_sonic_acl_sonic_acl_acl_table_acl_table_list_ports(aclname, ports)
except ApiException as e:
    print("Exception when calling SonicAclApi->del_llist_sonic_acl_sonic_acl_acl_table_acl_table_list_ports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **ports** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list**
> delete_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list()



OperationId: delete_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()

try:
    api_instance.delete_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list()
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_list_sonic_acl_sonic_acl_acl_table_acl_table_list**
> delete_list_sonic_acl_sonic_acl_acl_table_acl_table_list()



OperationId: delete_list_sonic_acl_sonic_acl_acl_table_acl_table_list 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()

try:
    api_instance.delete_list_sonic_acl_sonic_acl_acl_table_acl_table_list()
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_list_sonic_acl_sonic_acl_acl_table_acl_table_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonic_acl_sonic_acl**
> delete_sonic_acl_sonic_acl()



OperationId: delete_sonic_acl_sonic_acl 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()

try:
    api_instance.delete_sonic_acl_sonic_acl()
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_sonic_acl_sonic_acl: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonic_acl_sonic_acl_acl_rule**
> delete_sonic_acl_sonic_acl_acl_rule()



OperationId: delete_sonic_acl_sonic_acl_acl_rule 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()

try:
    api_instance.delete_sonic_acl_sonic_acl_acl_rule()
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_sonic_acl_sonic_acl_acl_rule: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list**
> delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list(aclname, rulename)



OperationId: delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_instance.delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list(aclname, rulename)
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp**
> delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp(aclname, rulename)



OperationId: delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_instance.delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp(aclname, rulename)
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip**
> delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip(aclname, rulename)



OperationId: delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_instance.delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip(aclname, rulename)
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6**
> delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6(aclname, rulename)



OperationId: delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_instance.delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6(aclname, rulename)
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type**
> delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type(aclname, rulename)



OperationId: delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_instance.delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type(aclname, rulename)
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol**
> delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol(aclname, rulename)



OperationId: delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_instance.delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol(aclname, rulename)
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type**
> delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type(aclname, rulename)



OperationId: delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_instance.delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type(aclname, rulename)
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port**
> delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port(aclname, rulename)



OperationId: delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_instance.delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port(aclname, rulename)
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range**
> delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range(aclname, rulename)



OperationId: delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_instance.delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range(aclname, rulename)
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port**
> delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port(aclname, rulename)



OperationId: delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_instance.delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port(aclname, rulename)
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range**
> delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range(aclname, rulename)



OperationId: delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_instance.delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range(aclname, rulename)
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action**
> delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action(aclname, rulename)



OperationId: delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_instance.delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action(aclname, rulename)
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action**
> delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action(aclname, rulename)



OperationId: delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_instance.delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action(aclname, rulename)
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority**
> delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority(aclname, rulename)



OperationId: delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_instance.delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority(aclname, rulename)
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description**
> delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description(aclname, rulename)



OperationId: delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_instance.delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description(aclname, rulename)
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip**
> delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip(aclname, rulename)



OperationId: delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_instance.delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip(aclname, rulename)
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6**
> delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6(aclname, rulename)



OperationId: delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_instance.delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6(aclname, rulename)
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags**
> delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags(aclname, rulename)



OperationId: delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_instance.delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags(aclname, rulename)
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonic_acl_sonic_acl_acl_table**
> delete_sonic_acl_sonic_acl_acl_table()



OperationId: delete_sonic_acl_sonic_acl_acl_table 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()

try:
    api_instance.delete_sonic_acl_sonic_acl_acl_table()
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_sonic_acl_sonic_acl_acl_table: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonic_acl_sonic_acl_acl_table_acl_table_list**
> delete_sonic_acl_sonic_acl_acl_table_acl_table_list(aclname)



OperationId: delete_sonic_acl_sonic_acl_acl_table_acl_table_list 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 

try:
    api_instance.delete_sonic_acl_sonic_acl_acl_table_acl_table_list(aclname)
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_sonic_acl_sonic_acl_acl_table_acl_table_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc**
> delete_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc(aclname)



OperationId: delete_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 

try:
    api_instance.delete_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc(aclname)
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonic_acl_sonic_acl_acl_table_acl_table_list_ports**
> delete_sonic_acl_sonic_acl_acl_table_acl_table_list_ports(aclname)



OperationId: delete_sonic_acl_sonic_acl_acl_table_acl_table_list_ports 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 

try:
    api_instance.delete_sonic_acl_sonic_acl_acl_table_acl_table_list_ports(aclname)
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_sonic_acl_sonic_acl_acl_table_acl_table_list_ports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonic_acl_sonic_acl_acl_table_acl_table_list_stage**
> delete_sonic_acl_sonic_acl_acl_table_acl_table_list_stage(aclname)



OperationId: delete_sonic_acl_sonic_acl_acl_table_acl_table_list_stage 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 

try:
    api_instance.delete_sonic_acl_sonic_acl_acl_table_acl_table_list_stage(aclname)
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_sonic_acl_sonic_acl_acl_table_acl_table_list_stage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sonic_acl_sonic_acl_acl_table_acl_table_list_type**
> delete_sonic_acl_sonic_acl_acl_table_acl_table_list_type(aclname)



OperationId: delete_sonic_acl_sonic_acl_acl_table_acl_table_list_type 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 

try:
    api_instance.delete_sonic_acl_sonic_acl_acl_table_acl_table_list_type(aclname)
except ApiException as e:
    print("Exception when calling SonicAclApi->delete_sonic_acl_sonic_acl_acl_table_acl_table_list_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list**
> GetSonicAclSonicAclAclRuleAclRuleList get_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list()



OperationId: get_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()

try:
    api_response = api_instance.get_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSonicAclSonicAclAclRuleAclRuleList**](GetSonicAclSonicAclAclRuleAclRuleList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_sonic_acl_sonic_acl_acl_table_acl_table_list**
> GetSonicAclSonicAclAclTableAclTableList get_list_sonic_acl_sonic_acl_acl_table_acl_table_list()



OperationId: get_list_sonic_acl_sonic_acl_acl_table_acl_table_list 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()

try:
    api_response = api_instance.get_list_sonic_acl_sonic_acl_acl_table_acl_table_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_list_sonic_acl_sonic_acl_acl_table_acl_table_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSonicAclSonicAclAclTableAclTableList**](GetSonicAclSonicAclAclTableAclTableList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_llist_sonic_acl_sonic_acl_acl_table_acl_table_list_ports**
> GetSonicAclSonicAclAclTableAclTableListPorts get_llist_sonic_acl_sonic_acl_acl_table_acl_table_list_ports(aclname, ports)



OperationId: get_llist_sonic_acl_sonic_acl_acl_table_acl_table_list_ports 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
ports = 'ports_example' # str | 

try:
    api_response = api_instance.get_llist_sonic_acl_sonic_acl_acl_table_acl_table_list_ports(aclname, ports)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_llist_sonic_acl_sonic_acl_acl_table_acl_table_list_ports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **ports** | **str**|  | 

### Return type

[**GetSonicAclSonicAclAclTableAclTableListPorts**](GetSonicAclSonicAclAclTableAclTableListPorts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_acl_sonic_acl**
> GetSonicAclSonicAcl get_sonic_acl_sonic_acl()



OperationId: get_sonic_acl_sonic_acl 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()

try:
    api_response = api_instance.get_sonic_acl_sonic_acl()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_sonic_acl_sonic_acl: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSonicAclSonicAcl**](GetSonicAclSonicAcl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_acl_sonic_acl_acl_rule**
> GetSonicAclSonicAclAclRule get_sonic_acl_sonic_acl_acl_rule()



OperationId: get_sonic_acl_sonic_acl_acl_rule 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()

try:
    api_response = api_instance.get_sonic_acl_sonic_acl_acl_rule()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_sonic_acl_sonic_acl_acl_rule: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSonicAclSonicAclAclRule**](GetSonicAclSonicAclAclRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_acl_sonic_acl_acl_rule_acl_rule_list**
> GetSonicAclSonicAclAclRuleAclRuleList get_sonic_acl_sonic_acl_acl_rule_acl_rule_list(aclname, rulename)



OperationId: get_sonic_acl_sonic_acl_acl_rule_acl_rule_list 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_response = api_instance.get_sonic_acl_sonic_acl_acl_rule_acl_rule_list(aclname, rulename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_sonic_acl_sonic_acl_acl_rule_acl_rule_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

[**GetSonicAclSonicAclAclRuleAclRuleList**](GetSonicAclSonicAclAclRuleAclRuleList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp**
> GetSonicAclSonicAclAclRuleAclRuleListDscp get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp(aclname, rulename)



OperationId: get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_response = api_instance.get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp(aclname, rulename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

[**GetSonicAclSonicAclAclRuleAclRuleListDscp**](GetSonicAclSonicAclAclRuleAclRuleListDscp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip**
> GetSonicAclSonicAclAclRuleAclRuleListDstIp get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip(aclname, rulename)



OperationId: get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_response = api_instance.get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip(aclname, rulename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

[**GetSonicAclSonicAclAclRuleAclRuleListDstIp**](GetSonicAclSonicAclAclRuleAclRuleListDstIp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6**
> GetSonicAclSonicAclAclRuleAclRuleListDstIpv6 get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6(aclname, rulename)



OperationId: get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_response = api_instance.get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6(aclname, rulename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

[**GetSonicAclSonicAclAclRuleAclRuleListDstIpv6**](GetSonicAclSonicAclAclRuleAclRuleListDstIpv6.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type**
> GetSonicAclSonicAclAclRuleAclRuleListEtherType get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type(aclname, rulename)



OperationId: get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_response = api_instance.get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type(aclname, rulename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

[**GetSonicAclSonicAclAclRuleAclRuleListEtherType**](GetSonicAclSonicAclAclRuleAclRuleListEtherType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol**
> GetSonicAclSonicAclAclRuleAclRuleListIpProtocol get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol(aclname, rulename)



OperationId: get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_response = api_instance.get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol(aclname, rulename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

[**GetSonicAclSonicAclAclRuleAclRuleListIpProtocol**](GetSonicAclSonicAclAclRuleAclRuleListIpProtocol.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type**
> GetSonicAclSonicAclAclRuleAclRuleListIpType get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type(aclname, rulename)



OperationId: get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_response = api_instance.get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type(aclname, rulename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

[**GetSonicAclSonicAclAclRuleAclRuleListIpType**](GetSonicAclSonicAclAclRuleAclRuleListIpType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port**
> GetSonicAclSonicAclAclRuleAclRuleListL4DstPort get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port(aclname, rulename)



OperationId: get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_response = api_instance.get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port(aclname, rulename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

[**GetSonicAclSonicAclAclRuleAclRuleListL4DstPort**](GetSonicAclSonicAclAclRuleAclRuleListL4DstPort.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range**
> GetSonicAclSonicAclAclRuleAclRuleListL4DstPortRange get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range(aclname, rulename)



OperationId: get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_response = api_instance.get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range(aclname, rulename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

[**GetSonicAclSonicAclAclRuleAclRuleListL4DstPortRange**](GetSonicAclSonicAclAclRuleAclRuleListL4DstPortRange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port**
> GetSonicAclSonicAclAclRuleAclRuleListL4SrcPort get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port(aclname, rulename)



OperationId: get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_response = api_instance.get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port(aclname, rulename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

[**GetSonicAclSonicAclAclRuleAclRuleListL4SrcPort**](GetSonicAclSonicAclAclRuleAclRuleListL4SrcPort.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range**
> GetSonicAclSonicAclAclRuleAclRuleListL4SrcPortRange get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range(aclname, rulename)



OperationId: get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_response = api_instance.get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range(aclname, rulename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

[**GetSonicAclSonicAclAclRuleAclRuleListL4SrcPortRange**](GetSonicAclSonicAclAclRuleAclRuleListL4SrcPortRange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action**
> GetSonicAclSonicAclAclRuleAclRuleListMirrorAction get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action(aclname, rulename)



OperationId: get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_response = api_instance.get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action(aclname, rulename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

[**GetSonicAclSonicAclAclRuleAclRuleListMirrorAction**](GetSonicAclSonicAclAclRuleAclRuleListMirrorAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action**
> GetSonicAclSonicAclAclRuleAclRuleListPacketAction get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action(aclname, rulename)



OperationId: get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_response = api_instance.get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action(aclname, rulename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

[**GetSonicAclSonicAclAclRuleAclRuleListPacketAction**](GetSonicAclSonicAclAclRuleAclRuleListPacketAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority**
> GetSonicAclSonicAclAclRuleAclRuleListPriority get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority(aclname, rulename)



OperationId: get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_response = api_instance.get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority(aclname, rulename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

[**GetSonicAclSonicAclAclRuleAclRuleListPriority**](GetSonicAclSonicAclAclRuleAclRuleListPriority.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description**
> GetSonicAclSonicAclAclRuleAclRuleListRuleDescription get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description(aclname, rulename)



OperationId: get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_response = api_instance.get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description(aclname, rulename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

[**GetSonicAclSonicAclAclRuleAclRuleListRuleDescription**](GetSonicAclSonicAclAclRuleAclRuleListRuleDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip**
> GetSonicAclSonicAclAclRuleAclRuleListSrcIp get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip(aclname, rulename)



OperationId: get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_response = api_instance.get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip(aclname, rulename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

[**GetSonicAclSonicAclAclRuleAclRuleListSrcIp**](GetSonicAclSonicAclAclRuleAclRuleListSrcIp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6**
> GetSonicAclSonicAclAclRuleAclRuleListSrcIpv6 get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6(aclname, rulename)



OperationId: get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_response = api_instance.get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6(aclname, rulename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

[**GetSonicAclSonicAclAclRuleAclRuleListSrcIpv6**](GetSonicAclSonicAclAclRuleAclRuleListSrcIpv6.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags**
> GetSonicAclSonicAclAclRuleAclRuleListTcpFlags get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags(aclname, rulename)



OperationId: get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 

try:
    api_response = api_instance.get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags(aclname, rulename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 

### Return type

[**GetSonicAclSonicAclAclRuleAclRuleListTcpFlags**](GetSonicAclSonicAclAclRuleAclRuleListTcpFlags.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_acl_sonic_acl_acl_table**
> GetSonicAclSonicAclAclTable get_sonic_acl_sonic_acl_acl_table()



OperationId: get_sonic_acl_sonic_acl_acl_table 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()

try:
    api_response = api_instance.get_sonic_acl_sonic_acl_acl_table()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_sonic_acl_sonic_acl_acl_table: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSonicAclSonicAclAclTable**](GetSonicAclSonicAclAclTable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_acl_sonic_acl_acl_table_acl_table_list**
> GetSonicAclSonicAclAclTableAclTableList get_sonic_acl_sonic_acl_acl_table_acl_table_list(aclname)



OperationId: get_sonic_acl_sonic_acl_acl_table_acl_table_list 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 

try:
    api_response = api_instance.get_sonic_acl_sonic_acl_acl_table_acl_table_list(aclname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_sonic_acl_sonic_acl_acl_table_acl_table_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 

### Return type

[**GetSonicAclSonicAclAclTableAclTableList**](GetSonicAclSonicAclAclTableAclTableList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc**
> GetSonicAclSonicAclAclTableAclTableListPolicyDesc get_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc(aclname)



OperationId: get_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 

try:
    api_response = api_instance.get_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc(aclname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 

### Return type

[**GetSonicAclSonicAclAclTableAclTableListPolicyDesc**](GetSonicAclSonicAclAclTableAclTableListPolicyDesc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_acl_sonic_acl_acl_table_acl_table_list_ports**
> GetSonicAclSonicAclAclTableAclTableListPorts get_sonic_acl_sonic_acl_acl_table_acl_table_list_ports(aclname)



OperationId: get_sonic_acl_sonic_acl_acl_table_acl_table_list_ports 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 

try:
    api_response = api_instance.get_sonic_acl_sonic_acl_acl_table_acl_table_list_ports(aclname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_sonic_acl_sonic_acl_acl_table_acl_table_list_ports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 

### Return type

[**GetSonicAclSonicAclAclTableAclTableListPorts**](GetSonicAclSonicAclAclTableAclTableListPorts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_acl_sonic_acl_acl_table_acl_table_list_stage**
> GetSonicAclSonicAclAclTableAclTableListStage get_sonic_acl_sonic_acl_acl_table_acl_table_list_stage(aclname)



OperationId: get_sonic_acl_sonic_acl_acl_table_acl_table_list_stage 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 

try:
    api_response = api_instance.get_sonic_acl_sonic_acl_acl_table_acl_table_list_stage(aclname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_sonic_acl_sonic_acl_acl_table_acl_table_list_stage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 

### Return type

[**GetSonicAclSonicAclAclTableAclTableListStage**](GetSonicAclSonicAclAclTableAclTableListStage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sonic_acl_sonic_acl_acl_table_acl_table_list_type**
> GetSonicAclSonicAclAclTableAclTableListType get_sonic_acl_sonic_acl_acl_table_acl_table_list_type(aclname)



OperationId: get_sonic_acl_sonic_acl_acl_table_acl_table_list_type 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 

try:
    api_response = api_instance.get_sonic_acl_sonic_acl_acl_table_acl_table_list_type(aclname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SonicAclApi->get_sonic_acl_sonic_acl_acl_table_acl_table_list_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 

### Return type

[**GetSonicAclSonicAclAclTableAclTableListType**](GetSonicAclSonicAclAclTableAclTableListType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list**
> patch_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list(body)



OperationId: patch_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
body = sonic_acl_client.PatchListSonicAclSonicAclAclRuleAclRuleList() # PatchListSonicAclSonicAclAclRuleAclRuleList | 

try:
    api_instance.patch_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list(body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchListSonicAclSonicAclAclRuleAclRuleList**](PatchListSonicAclSonicAclAclRuleAclRuleList.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_list_sonic_acl_sonic_acl_acl_table_acl_table_list**
> patch_list_sonic_acl_sonic_acl_acl_table_acl_table_list(body)



OperationId: patch_list_sonic_acl_sonic_acl_acl_table_acl_table_list 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
body = sonic_acl_client.PatchListSonicAclSonicAclAclTableAclTableList() # PatchListSonicAclSonicAclAclTableAclTableList | 

try:
    api_instance.patch_list_sonic_acl_sonic_acl_acl_table_acl_table_list(body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_list_sonic_acl_sonic_acl_acl_table_acl_table_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchListSonicAclSonicAclAclTableAclTableList**](PatchListSonicAclSonicAclAclTableAclTableList.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_acl_sonic_acl**
> patch_sonic_acl_sonic_acl(body)



OperationId: patch_sonic_acl_sonic_acl 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
body = sonic_acl_client.PatchSonicAclSonicAcl() # PatchSonicAclSonicAcl | 

try:
    api_instance.patch_sonic_acl_sonic_acl(body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_sonic_acl_sonic_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchSonicAclSonicAcl**](PatchSonicAclSonicAcl.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_acl_sonic_acl_acl_rule**
> patch_sonic_acl_sonic_acl_acl_rule(body)



OperationId: patch_sonic_acl_sonic_acl_acl_rule 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
body = sonic_acl_client.PatchSonicAclSonicAclAclRule() # PatchSonicAclSonicAclAclRule | 

try:
    api_instance.patch_sonic_acl_sonic_acl_acl_rule(body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_sonic_acl_sonic_acl_acl_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchSonicAclSonicAclAclRule**](PatchSonicAclSonicAclAclRule.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list**
> patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list(aclname, rulename, body)



OperationId: patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PatchSonicAclSonicAclAclRuleAclRuleList() # PatchSonicAclSonicAclAclRuleAclRuleList | 

try:
    api_instance.patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PatchSonicAclSonicAclAclRuleAclRuleList**](PatchSonicAclSonicAclAclRuleAclRuleList.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp**
> patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp(aclname, rulename, body)



OperationId: patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PatchSonicAclSonicAclAclRuleAclRuleListDscp() # PatchSonicAclSonicAclAclRuleAclRuleListDscp | 

try:
    api_instance.patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PatchSonicAclSonicAclAclRuleAclRuleListDscp**](PatchSonicAclSonicAclAclRuleAclRuleListDscp.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip**
> patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip(aclname, rulename, body)



OperationId: patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PatchSonicAclSonicAclAclRuleAclRuleListDstIp() # PatchSonicAclSonicAclAclRuleAclRuleListDstIp | 

try:
    api_instance.patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PatchSonicAclSonicAclAclRuleAclRuleListDstIp**](PatchSonicAclSonicAclAclRuleAclRuleListDstIp.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6**
> patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6(aclname, rulename, body)



OperationId: patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PatchSonicAclSonicAclAclRuleAclRuleListDstIpv6() # PatchSonicAclSonicAclAclRuleAclRuleListDstIpv6 | 

try:
    api_instance.patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PatchSonicAclSonicAclAclRuleAclRuleListDstIpv6**](PatchSonicAclSonicAclAclRuleAclRuleListDstIpv6.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type**
> patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type(aclname, rulename, body)



OperationId: patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PatchSonicAclSonicAclAclRuleAclRuleListEtherType() # PatchSonicAclSonicAclAclRuleAclRuleListEtherType | 

try:
    api_instance.patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PatchSonicAclSonicAclAclRuleAclRuleListEtherType**](PatchSonicAclSonicAclAclRuleAclRuleListEtherType.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol**
> patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol(aclname, rulename, body)



OperationId: patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PatchSonicAclSonicAclAclRuleAclRuleListIpProtocol() # PatchSonicAclSonicAclAclRuleAclRuleListIpProtocol | 

try:
    api_instance.patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PatchSonicAclSonicAclAclRuleAclRuleListIpProtocol**](PatchSonicAclSonicAclAclRuleAclRuleListIpProtocol.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type**
> patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type(aclname, rulename, body)



OperationId: patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PatchSonicAclSonicAclAclRuleAclRuleListIpType() # PatchSonicAclSonicAclAclRuleAclRuleListIpType | 

try:
    api_instance.patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PatchSonicAclSonicAclAclRuleAclRuleListIpType**](PatchSonicAclSonicAclAclRuleAclRuleListIpType.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port**
> patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port(aclname, rulename, body)



OperationId: patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PatchSonicAclSonicAclAclRuleAclRuleListL4DstPort() # PatchSonicAclSonicAclAclRuleAclRuleListL4DstPort | 

try:
    api_instance.patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PatchSonicAclSonicAclAclRuleAclRuleListL4DstPort**](PatchSonicAclSonicAclAclRuleAclRuleListL4DstPort.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range**
> patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range(aclname, rulename, body)



OperationId: patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PatchSonicAclSonicAclAclRuleAclRuleListL4DstPortRange() # PatchSonicAclSonicAclAclRuleAclRuleListL4DstPortRange | 

try:
    api_instance.patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PatchSonicAclSonicAclAclRuleAclRuleListL4DstPortRange**](PatchSonicAclSonicAclAclRuleAclRuleListL4DstPortRange.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port**
> patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port(aclname, rulename, body)



OperationId: patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PatchSonicAclSonicAclAclRuleAclRuleListL4SrcPort() # PatchSonicAclSonicAclAclRuleAclRuleListL4SrcPort | 

try:
    api_instance.patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PatchSonicAclSonicAclAclRuleAclRuleListL4SrcPort**](PatchSonicAclSonicAclAclRuleAclRuleListL4SrcPort.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range**
> patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range(aclname, rulename, body)



OperationId: patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PatchSonicAclSonicAclAclRuleAclRuleListL4SrcPortRange() # PatchSonicAclSonicAclAclRuleAclRuleListL4SrcPortRange | 

try:
    api_instance.patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PatchSonicAclSonicAclAclRuleAclRuleListL4SrcPortRange**](PatchSonicAclSonicAclAclRuleAclRuleListL4SrcPortRange.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action**
> patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action(aclname, rulename, body)



OperationId: patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PatchSonicAclSonicAclAclRuleAclRuleListMirrorAction() # PatchSonicAclSonicAclAclRuleAclRuleListMirrorAction | 

try:
    api_instance.patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PatchSonicAclSonicAclAclRuleAclRuleListMirrorAction**](PatchSonicAclSonicAclAclRuleAclRuleListMirrorAction.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action**
> patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action(aclname, rulename, body)



OperationId: patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PatchSonicAclSonicAclAclRuleAclRuleListPacketAction() # PatchSonicAclSonicAclAclRuleAclRuleListPacketAction | 

try:
    api_instance.patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PatchSonicAclSonicAclAclRuleAclRuleListPacketAction**](PatchSonicAclSonicAclAclRuleAclRuleListPacketAction.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority**
> patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority(aclname, rulename, body)



OperationId: patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PatchSonicAclSonicAclAclRuleAclRuleListPriority() # PatchSonicAclSonicAclAclRuleAclRuleListPriority | 

try:
    api_instance.patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PatchSonicAclSonicAclAclRuleAclRuleListPriority**](PatchSonicAclSonicAclAclRuleAclRuleListPriority.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description**
> patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description(aclname, rulename, body)



OperationId: patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PatchSonicAclSonicAclAclRuleAclRuleListRuleDescription() # PatchSonicAclSonicAclAclRuleAclRuleListRuleDescription | 

try:
    api_instance.patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PatchSonicAclSonicAclAclRuleAclRuleListRuleDescription**](PatchSonicAclSonicAclAclRuleAclRuleListRuleDescription.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip**
> patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip(aclname, rulename, body)



OperationId: patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PatchSonicAclSonicAclAclRuleAclRuleListSrcIp() # PatchSonicAclSonicAclAclRuleAclRuleListSrcIp | 

try:
    api_instance.patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PatchSonicAclSonicAclAclRuleAclRuleListSrcIp**](PatchSonicAclSonicAclAclRuleAclRuleListSrcIp.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6**
> patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6(aclname, rulename, body)



OperationId: patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PatchSonicAclSonicAclAclRuleAclRuleListSrcIpv6() # PatchSonicAclSonicAclAclRuleAclRuleListSrcIpv6 | 

try:
    api_instance.patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PatchSonicAclSonicAclAclRuleAclRuleListSrcIpv6**](PatchSonicAclSonicAclAclRuleAclRuleListSrcIpv6.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags**
> patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags(aclname, rulename, body)



OperationId: patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PatchSonicAclSonicAclAclRuleAclRuleListTcpFlags() # PatchSonicAclSonicAclAclRuleAclRuleListTcpFlags | 

try:
    api_instance.patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PatchSonicAclSonicAclAclRuleAclRuleListTcpFlags**](PatchSonicAclSonicAclAclRuleAclRuleListTcpFlags.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_acl_sonic_acl_acl_table**
> patch_sonic_acl_sonic_acl_acl_table(body)



OperationId: patch_sonic_acl_sonic_acl_acl_table 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
body = sonic_acl_client.PatchSonicAclSonicAclAclTable() # PatchSonicAclSonicAclAclTable | 

try:
    api_instance.patch_sonic_acl_sonic_acl_acl_table(body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_sonic_acl_sonic_acl_acl_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchSonicAclSonicAclAclTable**](PatchSonicAclSonicAclAclTable.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_acl_sonic_acl_acl_table_acl_table_list**
> patch_sonic_acl_sonic_acl_acl_table_acl_table_list(aclname, body)



OperationId: patch_sonic_acl_sonic_acl_acl_table_acl_table_list 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
body = sonic_acl_client.PatchSonicAclSonicAclAclTableAclTableList() # PatchSonicAclSonicAclAclTableAclTableList | 

try:
    api_instance.patch_sonic_acl_sonic_acl_acl_table_acl_table_list(aclname, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_sonic_acl_sonic_acl_acl_table_acl_table_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **body** | [**PatchSonicAclSonicAclAclTableAclTableList**](PatchSonicAclSonicAclAclTableAclTableList.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc**
> patch_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc(aclname, body)



OperationId: patch_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
body = sonic_acl_client.PatchSonicAclSonicAclAclTableAclTableListPolicyDesc() # PatchSonicAclSonicAclAclTableAclTableListPolicyDesc | 

try:
    api_instance.patch_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc(aclname, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **body** | [**PatchSonicAclSonicAclAclTableAclTableListPolicyDesc**](PatchSonicAclSonicAclAclTableAclTableListPolicyDesc.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_acl_sonic_acl_acl_table_acl_table_list_ports**
> patch_sonic_acl_sonic_acl_acl_table_acl_table_list_ports(aclname, body)



OperationId: patch_sonic_acl_sonic_acl_acl_table_acl_table_list_ports 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
body = sonic_acl_client.PatchSonicAclSonicAclAclTableAclTableListPorts() # PatchSonicAclSonicAclAclTableAclTableListPorts | 

try:
    api_instance.patch_sonic_acl_sonic_acl_acl_table_acl_table_list_ports(aclname, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_sonic_acl_sonic_acl_acl_table_acl_table_list_ports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **body** | [**PatchSonicAclSonicAclAclTableAclTableListPorts**](PatchSonicAclSonicAclAclTableAclTableListPorts.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_acl_sonic_acl_acl_table_acl_table_list_stage**
> patch_sonic_acl_sonic_acl_acl_table_acl_table_list_stage(aclname, body)



OperationId: patch_sonic_acl_sonic_acl_acl_table_acl_table_list_stage 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
body = sonic_acl_client.PatchSonicAclSonicAclAclTableAclTableListStage() # PatchSonicAclSonicAclAclTableAclTableListStage | 

try:
    api_instance.patch_sonic_acl_sonic_acl_acl_table_acl_table_list_stage(aclname, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_sonic_acl_sonic_acl_acl_table_acl_table_list_stage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **body** | [**PatchSonicAclSonicAclAclTableAclTableListStage**](PatchSonicAclSonicAclAclTableAclTableListStage.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sonic_acl_sonic_acl_acl_table_acl_table_list_type**
> patch_sonic_acl_sonic_acl_acl_table_acl_table_list_type(aclname, body)



OperationId: patch_sonic_acl_sonic_acl_acl_table_acl_table_list_type 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
body = sonic_acl_client.PatchSonicAclSonicAclAclTableAclTableListType() # PatchSonicAclSonicAclAclTableAclTableListType | 

try:
    api_instance.patch_sonic_acl_sonic_acl_acl_table_acl_table_list_type(aclname, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->patch_sonic_acl_sonic_acl_acl_table_acl_table_list_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **body** | [**PatchSonicAclSonicAclAclTableAclTableListType**](PatchSonicAclSonicAclAclTableAclTableListType.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list**
> post_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list(body)



OperationId: post_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
body = sonic_acl_client.PostListSonicAclSonicAclAclRuleAclRuleList() # PostListSonicAclSonicAclAclRuleAclRuleList | 

try:
    api_instance.post_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list(body)
except ApiException as e:
    print("Exception when calling SonicAclApi->post_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostListSonicAclSonicAclAclRuleAclRuleList**](PostListSonicAclSonicAclAclRuleAclRuleList.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_list_sonic_acl_sonic_acl_acl_table_acl_table_list**
> post_list_sonic_acl_sonic_acl_acl_table_acl_table_list(body)



OperationId: post_list_sonic_acl_sonic_acl_acl_table_acl_table_list 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
body = sonic_acl_client.PostListSonicAclSonicAclAclTableAclTableList() # PostListSonicAclSonicAclAclTableAclTableList | 

try:
    api_instance.post_list_sonic_acl_sonic_acl_acl_table_acl_table_list(body)
except ApiException as e:
    print("Exception when calling SonicAclApi->post_list_sonic_acl_sonic_acl_acl_table_acl_table_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostListSonicAclSonicAclAclTableAclTableList**](PostListSonicAclSonicAclAclTableAclTableList.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority**
> post_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority(aclname, rulename, body)



OperationId: post_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PostSonicAclSonicAclAclRuleAclRuleListPriority() # PostSonicAclSonicAclAclRuleAclRuleListPriority | 

try:
    api_instance.post_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->post_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PostSonicAclSonicAclAclRuleAclRuleListPriority**](PostSonicAclSonicAclAclRuleAclRuleListPriority.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sonic_acl_sonic_acl_acl_table**
> post_sonic_acl_sonic_acl_acl_table(body)



OperationId: post_sonic_acl_sonic_acl_acl_table 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
body = sonic_acl_client.PostSonicAclSonicAclAclTable() # PostSonicAclSonicAclAclTable | 

try:
    api_instance.post_sonic_acl_sonic_acl_acl_table(body)
except ApiException as e:
    print("Exception when calling SonicAclApi->post_sonic_acl_sonic_acl_acl_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostSonicAclSonicAclAclTable**](PostSonicAclSonicAclAclTable.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc**
> post_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc(aclname, body)



OperationId: post_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
body = sonic_acl_client.PostSonicAclSonicAclAclTableAclTableListPolicyDesc() # PostSonicAclSonicAclAclTableAclTableListPolicyDesc | 

try:
    api_instance.post_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc(aclname, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->post_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **body** | [**PostSonicAclSonicAclAclTableAclTableListPolicyDesc**](PostSonicAclSonicAclAclTableAclTableListPolicyDesc.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list**
> put_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list(body)



OperationId: put_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
body = sonic_acl_client.PutListSonicAclSonicAclAclRuleAclRuleList() # PutListSonicAclSonicAclAclRuleAclRuleList | 

try:
    api_instance.put_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list(body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_list_sonic_acl_sonic_acl_acl_rule_acl_rule_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutListSonicAclSonicAclAclRuleAclRuleList**](PutListSonicAclSonicAclAclRuleAclRuleList.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_list_sonic_acl_sonic_acl_acl_table_acl_table_list**
> put_list_sonic_acl_sonic_acl_acl_table_acl_table_list(body)



OperationId: put_list_sonic_acl_sonic_acl_acl_table_acl_table_list 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
body = sonic_acl_client.PutListSonicAclSonicAclAclTableAclTableList() # PutListSonicAclSonicAclAclTableAclTableList | 

try:
    api_instance.put_list_sonic_acl_sonic_acl_acl_table_acl_table_list(body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_list_sonic_acl_sonic_acl_acl_table_acl_table_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutListSonicAclSonicAclAclTableAclTableList**](PutListSonicAclSonicAclAclTableAclTableList.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_acl_sonic_acl**
> put_sonic_acl_sonic_acl(body)



OperationId: put_sonic_acl_sonic_acl 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
body = sonic_acl_client.PutSonicAclSonicAcl() # PutSonicAclSonicAcl | 

try:
    api_instance.put_sonic_acl_sonic_acl(body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_sonic_acl_sonic_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutSonicAclSonicAcl**](PutSonicAclSonicAcl.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_acl_sonic_acl_acl_rule**
> put_sonic_acl_sonic_acl_acl_rule(body)



OperationId: put_sonic_acl_sonic_acl_acl_rule 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
body = sonic_acl_client.PutSonicAclSonicAclAclRule() # PutSonicAclSonicAclAclRule | 

try:
    api_instance.put_sonic_acl_sonic_acl_acl_rule(body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_sonic_acl_sonic_acl_acl_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutSonicAclSonicAclAclRule**](PutSonicAclSonicAclAclRule.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_acl_sonic_acl_acl_rule_acl_rule_list**
> put_sonic_acl_sonic_acl_acl_rule_acl_rule_list(aclname, rulename, body)



OperationId: put_sonic_acl_sonic_acl_acl_rule_acl_rule_list 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PutSonicAclSonicAclAclRuleAclRuleList() # PutSonicAclSonicAclAclRuleAclRuleList | 

try:
    api_instance.put_sonic_acl_sonic_acl_acl_rule_acl_rule_list(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_sonic_acl_sonic_acl_acl_rule_acl_rule_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PutSonicAclSonicAclAclRuleAclRuleList**](PutSonicAclSonicAclAclRuleAclRuleList.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp**
> put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp(aclname, rulename, body)



OperationId: put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PutSonicAclSonicAclAclRuleAclRuleListDscp() # PutSonicAclSonicAclAclRuleAclRuleListDscp | 

try:
    api_instance.put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dscp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PutSonicAclSonicAclAclRuleAclRuleListDscp**](PutSonicAclSonicAclAclRuleAclRuleListDscp.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip**
> put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip(aclname, rulename, body)



OperationId: put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PutSonicAclSonicAclAclRuleAclRuleListDstIp() # PutSonicAclSonicAclAclRuleAclRuleListDstIp | 

try:
    api_instance.put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PutSonicAclSonicAclAclRuleAclRuleListDstIp**](PutSonicAclSonicAclAclRuleAclRuleListDstIp.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6**
> put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6(aclname, rulename, body)



OperationId: put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PutSonicAclSonicAclAclRuleAclRuleListDstIpv6() # PutSonicAclSonicAclAclRuleAclRuleListDstIpv6 | 

try:
    api_instance.put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_dst_ipv6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PutSonicAclSonicAclAclRuleAclRuleListDstIpv6**](PutSonicAclSonicAclAclRuleAclRuleListDstIpv6.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type**
> put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type(aclname, rulename, body)



OperationId: put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PutSonicAclSonicAclAclRuleAclRuleListEtherType() # PutSonicAclSonicAclAclRuleAclRuleListEtherType | 

try:
    api_instance.put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ether_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PutSonicAclSonicAclAclRuleAclRuleListEtherType**](PutSonicAclSonicAclAclRuleAclRuleListEtherType.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol**
> put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol(aclname, rulename, body)



OperationId: put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PutSonicAclSonicAclAclRuleAclRuleListIpProtocol() # PutSonicAclSonicAclAclRuleAclRuleListIpProtocol | 

try:
    api_instance.put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_protocol: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PutSonicAclSonicAclAclRuleAclRuleListIpProtocol**](PutSonicAclSonicAclAclRuleAclRuleListIpProtocol.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type**
> put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type(aclname, rulename, body)



OperationId: put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PutSonicAclSonicAclAclRuleAclRuleListIpType() # PutSonicAclSonicAclAclRuleAclRuleListIpType | 

try:
    api_instance.put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_ip_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PutSonicAclSonicAclAclRuleAclRuleListIpType**](PutSonicAclSonicAclAclRuleAclRuleListIpType.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port**
> put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port(aclname, rulename, body)



OperationId: put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PutSonicAclSonicAclAclRuleAclRuleListL4DstPort() # PutSonicAclSonicAclAclRuleAclRuleListL4DstPort | 

try:
    api_instance.put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PutSonicAclSonicAclAclRuleAclRuleListL4DstPort**](PutSonicAclSonicAclAclRuleAclRuleListL4DstPort.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range**
> put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range(aclname, rulename, body)



OperationId: put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PutSonicAclSonicAclAclRuleAclRuleListL4DstPortRange() # PutSonicAclSonicAclAclRuleAclRuleListL4DstPortRange | 

try:
    api_instance.put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_dst_port_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PutSonicAclSonicAclAclRuleAclRuleListL4DstPortRange**](PutSonicAclSonicAclAclRuleAclRuleListL4DstPortRange.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port**
> put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port(aclname, rulename, body)



OperationId: put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PutSonicAclSonicAclAclRuleAclRuleListL4SrcPort() # PutSonicAclSonicAclAclRuleAclRuleListL4SrcPort | 

try:
    api_instance.put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PutSonicAclSonicAclAclRuleAclRuleListL4SrcPort**](PutSonicAclSonicAclAclRuleAclRuleListL4SrcPort.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range**
> put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range(aclname, rulename, body)



OperationId: put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PutSonicAclSonicAclAclRuleAclRuleListL4SrcPortRange() # PutSonicAclSonicAclAclRuleAclRuleListL4SrcPortRange | 

try:
    api_instance.put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_l4_src_port_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PutSonicAclSonicAclAclRuleAclRuleListL4SrcPortRange**](PutSonicAclSonicAclAclRuleAclRuleListL4SrcPortRange.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action**
> put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action(aclname, rulename, body)



OperationId: put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PutSonicAclSonicAclAclRuleAclRuleListMirrorAction() # PutSonicAclSonicAclAclRuleAclRuleListMirrorAction | 

try:
    api_instance.put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_mirror_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PutSonicAclSonicAclAclRuleAclRuleListMirrorAction**](PutSonicAclSonicAclAclRuleAclRuleListMirrorAction.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action**
> put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action(aclname, rulename, body)



OperationId: put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PutSonicAclSonicAclAclRuleAclRuleListPacketAction() # PutSonicAclSonicAclAclRuleAclRuleListPacketAction | 

try:
    api_instance.put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_packet_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PutSonicAclSonicAclAclRuleAclRuleListPacketAction**](PutSonicAclSonicAclAclRuleAclRuleListPacketAction.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority**
> put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority(aclname, rulename, body)



OperationId: put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PutSonicAclSonicAclAclRuleAclRuleListPriority() # PutSonicAclSonicAclAclRuleAclRuleListPriority | 

try:
    api_instance.put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_priority: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PutSonicAclSonicAclAclRuleAclRuleListPriority**](PutSonicAclSonicAclAclRuleAclRuleListPriority.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description**
> put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description(aclname, rulename, body)



OperationId: put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PutSonicAclSonicAclAclRuleAclRuleListRuleDescription() # PutSonicAclSonicAclAclRuleAclRuleListRuleDescription | 

try:
    api_instance.put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_rule_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PutSonicAclSonicAclAclRuleAclRuleListRuleDescription**](PutSonicAclSonicAclAclRuleAclRuleListRuleDescription.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip**
> put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip(aclname, rulename, body)



OperationId: put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PutSonicAclSonicAclAclRuleAclRuleListSrcIp() # PutSonicAclSonicAclAclRuleAclRuleListSrcIp | 

try:
    api_instance.put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PutSonicAclSonicAclAclRuleAclRuleListSrcIp**](PutSonicAclSonicAclAclRuleAclRuleListSrcIp.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6**
> put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6(aclname, rulename, body)



OperationId: put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PutSonicAclSonicAclAclRuleAclRuleListSrcIpv6() # PutSonicAclSonicAclAclRuleAclRuleListSrcIpv6 | 

try:
    api_instance.put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_src_ipv6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PutSonicAclSonicAclAclRuleAclRuleListSrcIpv6**](PutSonicAclSonicAclAclRuleAclRuleListSrcIpv6.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags**
> put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags(aclname, rulename, body)



OperationId: put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
rulename = 'rulename_example' # str | 
body = sonic_acl_client.PutSonicAclSonicAclAclRuleAclRuleListTcpFlags() # PutSonicAclSonicAclAclRuleAclRuleListTcpFlags | 

try:
    api_instance.put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags(aclname, rulename, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_sonic_acl_sonic_acl_acl_rule_acl_rule_list_tcp_flags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **rulename** | **str**|  | 
 **body** | [**PutSonicAclSonicAclAclRuleAclRuleListTcpFlags**](PutSonicAclSonicAclAclRuleAclRuleListTcpFlags.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_acl_sonic_acl_acl_table**
> put_sonic_acl_sonic_acl_acl_table(body)



OperationId: put_sonic_acl_sonic_acl_acl_table 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
body = sonic_acl_client.PutSonicAclSonicAclAclTable() # PutSonicAclSonicAclAclTable | 

try:
    api_instance.put_sonic_acl_sonic_acl_acl_table(body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_sonic_acl_sonic_acl_acl_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutSonicAclSonicAclAclTable**](PutSonicAclSonicAclAclTable.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_acl_sonic_acl_acl_table_acl_table_list**
> put_sonic_acl_sonic_acl_acl_table_acl_table_list(aclname, body)



OperationId: put_sonic_acl_sonic_acl_acl_table_acl_table_list 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
body = sonic_acl_client.PutSonicAclSonicAclAclTableAclTableList() # PutSonicAclSonicAclAclTableAclTableList | 

try:
    api_instance.put_sonic_acl_sonic_acl_acl_table_acl_table_list(aclname, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_sonic_acl_sonic_acl_acl_table_acl_table_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **body** | [**PutSonicAclSonicAclAclTableAclTableList**](PutSonicAclSonicAclAclTableAclTableList.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc**
> put_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc(aclname, body)



OperationId: put_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
body = sonic_acl_client.PutSonicAclSonicAclAclTableAclTableListPolicyDesc() # PutSonicAclSonicAclAclTableAclTableListPolicyDesc | 

try:
    api_instance.put_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc(aclname, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_sonic_acl_sonic_acl_acl_table_acl_table_list_policy_desc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **body** | [**PutSonicAclSonicAclAclTableAclTableListPolicyDesc**](PutSonicAclSonicAclAclTableAclTableListPolicyDesc.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_acl_sonic_acl_acl_table_acl_table_list_ports**
> put_sonic_acl_sonic_acl_acl_table_acl_table_list_ports(aclname, body)



OperationId: put_sonic_acl_sonic_acl_acl_table_acl_table_list_ports 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
body = sonic_acl_client.PutSonicAclSonicAclAclTableAclTableListPorts() # PutSonicAclSonicAclAclTableAclTableListPorts | 

try:
    api_instance.put_sonic_acl_sonic_acl_acl_table_acl_table_list_ports(aclname, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_sonic_acl_sonic_acl_acl_table_acl_table_list_ports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **body** | [**PutSonicAclSonicAclAclTableAclTableListPorts**](PutSonicAclSonicAclAclTableAclTableListPorts.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_acl_sonic_acl_acl_table_acl_table_list_stage**
> put_sonic_acl_sonic_acl_acl_table_acl_table_list_stage(aclname, body)



OperationId: put_sonic_acl_sonic_acl_acl_table_acl_table_list_stage 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
body = sonic_acl_client.PutSonicAclSonicAclAclTableAclTableListStage() # PutSonicAclSonicAclAclTableAclTableListStage | 

try:
    api_instance.put_sonic_acl_sonic_acl_acl_table_acl_table_list_stage(aclname, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_sonic_acl_sonic_acl_acl_table_acl_table_list_stage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **body** | [**PutSonicAclSonicAclAclTableAclTableListStage**](PutSonicAclSonicAclAclTableAclTableListStage.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sonic_acl_sonic_acl_acl_table_acl_table_list_type**
> put_sonic_acl_sonic_acl_acl_table_acl_table_list_type(aclname, body)



OperationId: put_sonic_acl_sonic_acl_acl_table_acl_table_list_type 

### Example
```python
from __future__ import print_function
import time
import sonic_acl_client
from sonic_acl_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sonic_acl_client.SonicAclApi()
aclname = 'aclname_example' # str | 
body = sonic_acl_client.PutSonicAclSonicAclAclTableAclTableListType() # PutSonicAclSonicAclAclTableAclTableListType | 

try:
    api_instance.put_sonic_acl_sonic_acl_acl_table_acl_table_list_type(aclname, body)
except ApiException as e:
    print("Exception when calling SonicAclApi->put_sonic_acl_sonic_acl_acl_table_acl_table_list_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclname** | **str**|  | 
 **body** | [**PutSonicAclSonicAclAclTableAclTableListType**](PutSonicAclSonicAclAclTableAclTableListType.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yang-data+json
 - **Accept**: application/yang-data+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

