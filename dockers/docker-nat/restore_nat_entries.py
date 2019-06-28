#!/usr/bin/env python

""""
Description: restore_nat_entries.py -- restoring nat entries table into kernel during system warm reboot.
    The script is started by supervisord in nat docker when the docker is started.
    It does not do anything in case neither system nor nat warm restart is enabled.
    In case nat warm restart enabled only, it sets the stateDB flag so natsyncd can continue
    the reconciation process.
    In case system warm reboot is enabled, it will try to restore the nat entries table into kernel
    , then it sets the stateDB flag for natsyncd to continue the
    reconciliation process.
"""

import sys
import subprocess
import swsssdk

def add_nat_conntrack_entry_in_kernel(ipproto, src-ip, dst-ip, src-port, dst-port, nat-src-ip, nat-dst-ip, nat-src-port, nat-dst-port):
    # pyroute2 doesn't have support for adding conntrack entries via netlink yet. So, invoking the conntrack utility to add the entries.
    ctcmd = 'conntrack -I -n ' + nat-src-ip + ':' + nat-src-port + '-g ' + nat-dst-ip + ':' + nat-dst-port +
                       ' --protonum ' + ipproto + ' --timeout 600 --src ' + src-ip + ' --sport ' + src-port +
                       ' --dst ' + dst-ip + ' --dport ' + dst-port + ' -u ASSURED'
    subprocess.call(ctcmd, shell=True)
    print("Restored conntrack : %s", ctcmd)

# Set the statedb "NAT_RESTORE_TABLE|Flags", so natsyncd can start reconciliation
def set_statedb_nat_restore_done():
    db = swsssdk.SonicV2Connector(host='127.0.0.1')
    db.connect(db.STATE_DB, False)
    db.set(db.STATE_DB, 'NAT_RESTORE_TABLE|Flags', 'restored', 'true')
    db.close(db.STATE_DB)
    return

# This function is to restore the kernel nat entries based on the saved nat entries.
def restore_update_kernel_nat_entries(filename):
    # Read the entries from nat_entries.dump file and add them to kernel
    with open(filename, 'w') as fp:
        for line in fp:
            ctline = re.findall(r'^(\w+)\s+(\d+).*src=([\d.]+).*dst=([\d.]+).*sport=(\d+).*dport=(\d+).*src=([\d.]+).*dst([\d.]+).*sport=(\d+).*dport=(\d+)', line)
            if (ctline[0] != 'tcp' && ctline[0] != 'udp')
                continue
            add_nat_conntrack_entry_in_kernel(ctline[1], ctline[2], ctline[3], ctline[4], ctline[5], ctline[6], ctline[7], ctline[8], ctline[9])

    # Remove the dump file after restoration

def main():

    print("restore_nat_entries service is started")

    # Use warmstart python binding to check warmstart information
    warmstart = swsscommon.WarmStart()
    warmstart.initialize("natsyncd", "nat")
    warmstart.checkWarmStart("natsyncd", "nat", False)

    # if swss or system warm reboot not enabled, don't run
    if not warmstart.isWarmStart():
        print("restore_nat_entries service is skipped as warm restart not enabled")
        return

    # swss restart not system warm reboot, set statedb directly
    if not warmstart.isSystemWarmRebootEnabled():
        set_statedb_nat_restore_done()
        print("restore_nat_entries service is done as system warm reboot not enabled")
        return

    # Program the nat conntrack entries in the kernel by reading the
    # entries from nat_entries.dump
    try:
        restore_update_kernel_nat_entries('/var/warmboot/nat/nat_entries.dump')
    except Exception as e:
        logger.exception(str(e))
        sys.exit(1)

    # set statedb to signal other processes like natsyncd
    set_statedb_nat_restore_done()
    print("restore_nat_entries service is done for system warmreboot")
    return

if __name__ == '__main__':
    main()
