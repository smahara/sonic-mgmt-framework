#!/bin/bash
########################################################################
# This script is to automate Organization specific extensions for     #
# Broadcom distributed images. It may involve Configuration & Scripts  #
# for features like AAA, ZTP, etc. to include in ONIE installer image  #
#                                                                      #
########################################################################
set -e

# Initialize the arguments to default values.
# The values get updated to user provided value, if supplied
SONIC_BASE=/sonic
if [ "$SONIC_VENDOR" = "" ]; then
    SONIC_VENDOR=broadcom
fi

# Export variables to be used in extension scripts
export SONIC_BASE
export FILESYSTEM_ROOT
export SONIC_CUSTOMER
export SONIC_VENDOR
export VENDOR_EXT_BASE=${SONIC_BASE}/organization_extensions/vendor/${SONIC_VENDOR}
export CUSTOMER_EXT_BASE=${SONIC_BASE}/organization_extensions/customer/${SONIC_CUSTOMER}

# Vendor specific extensions
[ -n $SONIC_VENDOR ] && \
    [ -e ${VENDOR_EXT_BASE}/extensions.sh ] && \
    ${VENDOR_EXT_BASE}/extensions.sh

# Customer specific extensions
[ -n $SONIC_CUSTOMER ] && \
    [ -e ${CUSTOMER_EXT_BASE}/extensions.sh ] && \
    ${CUSTOMER_EXT_BASE}/extensions.sh

exit 0
