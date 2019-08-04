# SONiC vrrp package

VRRP_VERSION = 0.0.1
export VRRP_VERSION

VRRP_PKG = vrrp_$(VRRP_VERSION)_amd64.deb
$(VRRP_PKG)_SRC_PATH = $(SRC_PATH)/vrrp
$(VRRP_PKG)_DEPENDS += $(LIBHIREDIS_DEV)
$(VRRP_PKG)_RDEPENDS += $(LIBHIREDIS)
SONIC_MAKE_DEBS += $(VRRP_PKG)

$(eval $(call add_derived_package,$(VRRP_PKG)))

export VRRP_PKG

