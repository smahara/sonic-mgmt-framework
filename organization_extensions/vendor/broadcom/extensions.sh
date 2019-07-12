#!/bin/bash
########################################################################
# This script is to perform SONiC build extensions for all Broadcom    #
# branded builds. All customers get these customizations.              #
#                                                                      #
########################################################################
set -e

# Create a holding place for Broadcom customizations
sudo mkdir -p ${FILESYSTEM_ROOT}/usr/share/broadcom_sonic

# Copy supported configuration profiles
sudo cp -R ${VENDOR_EXT_BASE}/config_profiles \
           ${FILESYSTEM_ROOT}/usr/share/broadcom_sonic

# Choose factory default configuration profile to be applied on boot
sudo LANG=C chroot $FILESYSTEM_ROOT /bin/bash -c 'echo "l2" > /usr/share/broadcom_sonic/config_profiles/active'

# Create factory default configuration hooks
sudo mkdir -p ${FILESYSTEM_ROOT}/etc/config-setup/factory-default-hooks.d
for script in $(ls -1 ${VENDOR_EXT_BASE}/config_profiles/common/scripts);
do
    sudo ln -sf /usr/share/broadcom_sonic/config_profiles/common/scripts/$script \
                ${FILESYSTEM_ROOT}/etc/config-setup/factory-default-hooks.d/$script
done

exit 0
