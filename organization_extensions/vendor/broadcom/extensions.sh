#!/bin/bash
########################################################################
# This script is to perform SONiC build extensions for all Broadcom    #
# branded builds. All customers get these customizations.              #
#                                                                      #
########################################################################
set -e

# Create a holding place for Broadcom customizations
sudo mkdir -p ${FILESYSTEM_ROOT}/usr/share/broadcom_sonic

########### Begin - Config Profiles feature ###################################

# Copy supported configuration profiles
sudo cp -R ${VENDOR_EXT_BASE}/config_profiles \
           ${FILESYSTEM_ROOT}/usr/share/broadcom_sonic

sudo cp -R ${VENDOR_EXT_BASE}/scripts \
           ${FILESYSTEM_ROOT}/usr/share/broadcom_sonic

# Choose factory default configuration profile to be applied on boot
sudo LANG=C chroot $FILESYSTEM_ROOT /bin/bash -c 'echo "l3" > /usr/share/broadcom_sonic/config_profiles/active'

# Create factory default configuration hooks
sudo mkdir -p ${FILESYSTEM_ROOT}/etc/config-setup/factory-default-hooks.d
for script in $(ls -1 ${VENDOR_EXT_BASE}/scripts/factory-default-hooks);
do
    sudo ln -sf /usr/share/broadcom_sonic/scripts/factory-default-hooks/$script \
                ${FILESYSTEM_ROOT}/etc/config-setup/factory-default-hooks.d/$script
done

sudo mkdir -p ${FILESYSTEM_ROOT}/etc/config-setup/config-migration-pre-hooks.d
sudo ln -sf /usr/share/broadcom_sonic/scripts/config-profile-migration-hooks/08-config-profile-backup \
            ${FILESYSTEM_ROOT}/etc/config-setup/config-migration-pre-hooks.d/08-config-profile-backup

sudo mkdir -p ${FILESYSTEM_ROOT}/etc/config-setup/config-migration-post-hooks.d
sudo ln -sf /usr/share/broadcom_sonic/scripts/config-profile-migration-hooks/08-config-profile-migrate \
            ${FILESYSTEM_ROOT}/etc/config-setup/config-migration-post-hooks.d/08-config-profile-migrate
sudo ln -sf /usr/share/broadcom_sonic/scripts/factory-default-hooks/09-swap-bcm-config \
            ${FILESYSTEM_ROOT}/etc/config-setup/config-migration-post-hooks.d/09-swap-bcm-config

# Config profiles management tool
sudo cp ${VENDOR_EXT_BASE}/scripts/config-profiles ${FILESYSTEM_ROOT}/usr/bin

########### End - Config Profiles feature  ###################################

if [ -e ${SONIC_BASE}/src/broadcom-exclusive/files/scripts/build_extensions.sh ]; then
    ${SONIC_BASE}/src/broadcom-exclusive/files/scripts/build_extensions.sh
fi

exit 0
