# Switch Hardware Diagnostics' package
#

HWDIAG_VERSION = 1.0.0

export HWDIAG_VERSION

HWDIAG = hwdiag_$(HWDIAG_VERSION)_all.deb
$(HWDIAG)_SRC_PATH = $(SRC_PATH)/hwdiag
SONIC_DPKG_DEBS += $(HWDIAG)
#SONIC_STRETCH_DEBS += $(HWDIAG)

export HWDIAG
