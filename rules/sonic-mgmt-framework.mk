# SONiC mgmt-framework package

MGMT_FRAMEWORK_VERSION = 1.0-01
SONIC_MGMT_FRAMEWORK = sonic-mgmt-framework_$(MGMT_FRAMEWORK_VERSION)_amd64.deb
$(SONIC_MGMT_FRAMEWORK)_SRC_PATH = $(SRC_PATH)/sonic-mgmt-framework
$(SONIC_MGMT_FRAMEWORK)_DEPENDS = $(LIBYANG_DEV) $(LIBYANG)
$(SONIC_MGMT_FRAMEWORK)_RDEPENDS = $(LIBYANG)
SONIC_DPKG_DEBS += $(SONIC_MGMT_FRAMEWORK)

SONIC_HOST_SERVICE = sonic-host-service_$(MGMT_FRAMEWORK_VERSION)_amd64.deb
$(eval $(call add_derived_package,$(SONIC_MGMT_FRAMEWORK),$(SONIC_HOST_SERVICE)))

SONIC_HAMD = sonic-hamd_$(MGMT_FRAMEWORK_VERSION)_amd64.deb
$(eval $(call add_derived_package,$(SONIC_MGMT_FRAMEWORK),$(SONIC_HAMD)))

SONIC_LIBNSS_HAM = sonic-libnss-ham_$(MGMT_FRAMEWORK_VERSION)_amd64.deb
$(eval $(call add_derived_package,$(SONIC_MGMT_FRAMEWORK),$(SONIC_LIBNSS_HAM)))
