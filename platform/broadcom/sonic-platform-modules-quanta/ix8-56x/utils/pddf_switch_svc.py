#!/usr/bin/env python
# Script to stop and start the respective platforms default services. 
# This will be used while switching the pddf->non-pddf mode and vice versa
import os
import sys
import commands

def check_pddf_support():
    return True

def stop_platform_svc():
    status, output = commands.getstatusoutput("systemctl stop ix8-platform-init.service")
    if status:
        print "Stop ix8-platform-init.service failed %d"%status
        return False
    status, output = commands.getstatusoutput("systemctl disable ix8-platform-init.service")
    if status:
        print "Disable ix8-platform-init.service failed %d"%status
        return False

    # HACK , stop the pddf-platform-init service if it is active
    status, output = commands.getstatusoutput("systemctl stop pddf-platform-init.service")
    if status:
        print "Stop pddf-platform-init.service along with other platform serives failed %d"%status
        return False

    return True
    
def start_platform_svc():
    status, output = commands.getstatusoutput("systemctl enable ix8-platform-init.service")
    if status:
        print "Enable ix8-platform-init.service failed %d"%status
        return False
    status, output = commands.getstatusoutput("systemctl start ix8-platform-init.service")
    if status:
        print "Start ix8-platform-init.service failed %d"%status
        return False

    return True

def start_platform_pddf():
    # Enable PDDF 2.0 object class for IX8
    status, output = commands.getstatusoutput("mkdir /usr/share/sonic/platform/sonic_platform")
    if status:
        print "Unable to create 2.0 object class folder /usr/share/sonic/platform/sonic_platform"
        return False

    status, output = commands.getstatusoutput("systemctl start pddf-platform-init.service")
    if status:
        print "Start pddf-platform-init.service failed %d"%status
        return False
    
    return True

def stop_platform_pddf():
    # Disable PDDF 2.0 object class for IX8
    status, output = commands.getstatusoutput("rm -r /usr/share/sonic/platform/sonic_platform")
    if status:
        print "Unable to delete 2.0 object class folder /usr/share/sonic/platform/sonic_platform"
        return False

    status, output = commands.getstatusoutput("systemctl stop pddf-platform-init.service")
    if status:
        print "Stop pddf-platform-init.service failed %d"%status
        return False

    return True

def main():
    pass

if __name__ == "__main__":
    main()

