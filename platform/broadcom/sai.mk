BRCM_SAI = libsaibcm_3.6.0.1_amd64.deb
$(BRCM_SAI)_URL = "http://10.59.132.240:9999/projects/csg_sonic/sonicbld/ocp_sai_190522_0300/build/libsaibcm_3.6.0.1_amd64.deb"

BRCM_SAI_DEV = libsaibcm-dev_3.6.0.1_amd64.deb
$(eval $(call add_derived_package,$(BRCM_SAI),$(BRCM_SAI_DEV)))
$(BRCM_SAI_DEV)_URL = "http://10.59.132.240:9999/projects/csg_sonic/sonicbld/ocp_sai_190522_0300/build/libsaibcm-dev_3.6.0.1_amd64.deb"

SONIC_ONLINE_DEBS += $(BRCM_SAI)
$(BRCM_SAI_DEV)_DEPENDS += $(BRCM_SAI)
