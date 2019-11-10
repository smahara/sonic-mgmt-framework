# UDLD package
#
UDLD_VERSION = 1.0.0
export UDLD_VERSION

UDLD = udld_$(UDLD_VERSION)_amd64.deb
$(UDLD)_SRC_PATH = $(SRC_PATH)/sonic-udld
$(UDLD)_DEPENDS += $(LIBEVENT)
$(UDLD)_DEPENDS += $(LIBSWSSCOMMON_DEV)
$(UDLD)_RDEPENDS += $(LIBSWSSCOMMON)
SONIC_DPKG_DEBS += $(UDLD)

UDLD_DBG = udld-dbg_1.0.0_amd64.deb
$(UDLD_DBG)_DEPENDS += $(UDLD)
$(UDLD_DBG)_RDEPENDS += $(UDLD)
$(eval $(call add_derived_package,$(UDLD),$(UDLD_DBG)))

export UDLD
