#!/usr/bin/env bash

STATE_DB_IDX="6"

PORT_TABLE_PREFIX="PORT_TABLE"
VLAN_TABLE_PREFIX="VLAN_TABLE"
LAG_TABLE_PREFIX="LAG_TABLE"

function wait_until_iface_ready
{
    TABLE_PREFIX=$1
    IFACE=$2

    echo "Waiting until interface $IFACE is ready..."

    # Wait for the interface to come up
    # (i.e., interface is present in STATE_DB and state is "ok")
    while true; do
        RESULT=$(redis-cli -n ${STATE_DB_IDX} HGET "${TABLE_PREFIX}|${IFACE}" "state" 2> /dev/null)
        if [ x"$RESULT" == x"ok" ]; then
            break
        fi

        sleep 1
    done

    echo "Interface ${IFACE} is ready!"
}

function wait_until_ipv4_address_is_assigned
{
    IFACE=$1

    echo "Waiting until interface $IFACE is up..."

    # Wait for the interface to come up (i.e., 'ip link show' returns 0)
    until ip link show dev $IFACE up > /dev/null 2>&1; do
        sleep 1
    done

    echo "Interface $IFACE is up"

    echo "Waiting until interface $IFACE has an IPv4 address..."

    # Wait until the interface gets assigned an IPv4 address
    while true; do
        IP=$(ip -4 addr show dev $IFACE | grep "inet " | awk '{ print $2 }' | cut -d '/' -f1)

        if [ -n "$IP" ]; then
            break
        fi

        sleep 1
    done

    echo "Interface $IFACE is configured with IP $IP"
}



# Wait for all interfaces to be up and ready
wait_until_iface_ready ${VLAN_TABLE_PREFIX} Vlan1000
wait_until_iface_ready ${LAG_TABLE_PREFIX} PortChannel01
wait_until_iface_ready ${LAG_TABLE_PREFIX} PortChannel02
wait_until_iface_ready ${LAG_TABLE_PREFIX} PortChannel03
wait_until_iface_ready ${LAG_TABLE_PREFIX} PortChannel04

# Wait for all IP addresses to be assigned
wait_until_ipv4_address_is_assigned Vlan1000
wait_until_ipv4_address_is_assigned PortChannel01
wait_until_ipv4_address_is_assigned PortChannel01
wait_until_ipv4_address_is_assigned PortChannel02
wait_until_ipv4_address_is_assigned PortChannel02
wait_until_ipv4_address_is_assigned PortChannel03
wait_until_ipv4_address_is_assigned PortChannel03
wait_until_ipv4_address_is_assigned PortChannel04
wait_until_ipv4_address_is_assigned PortChannel04

