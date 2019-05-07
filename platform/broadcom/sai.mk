BRCM_SAI =  libsaibcm_3.3.5.4m-1_amd64.deb
BRCM_SAI_DEV =  libsaibcm-dev_3.3.5.4m-1_amd64.deb
SAI_LIBS_MOUNT_POINT = /sai_libs

ifneq  ($(LOCAL_SAI_DEBS_PATH),)
override BRCM_SAI = $(shell find $(SAI_LIBS_MOUNT_POINT) -maxdepth 1 -regex '.*libsaibcm_[0-9.]+_amd64\.deb' -printf "%f")
override BRCM_SAI_DEV = $(shell find $(SAI_LIBS_MOUNT_POINT) -maxdepth 1 -regex '.*libsaibcm-dev_[0-9.]+_amd64\.deb' -printf "%f")
endif

#BRCM_SAI
ifeq ($(LOCAL_SAI_DEBS_PATH),)
$(BRCM_SAI)_URL = "http://10.59.132.240:9999/projects/csg_sonic/sonicbld/ocp_sai_190507_0300/build/libsaibcm_3.5.1.2_amd64.deb"
SONIC_ONLINE_DEBS += $(BRCM_SAI)
else
$(BRCM_SAI)_PATH = $(SAI_LIBS_MOUNT_POINT)
SONIC_COPY_DEBS += $(BRCM_SAI)
endif

#BRCM_SAI_DEV
$(eval $(call add_derived_package,$(BRCM_SAI),$(BRCM_SAI_DEV)))
ifeq ($(LOCAL_SAI_DEBS_PATH),)
$(BRCM_SAI_DEV)_URL = "http://10.59.132.240:9999/projects/csg_sonic/sonicbld/ocp_sai_190507_0300/build/libsaibcm-dev_3.5.1.2_amd64.deb"
else
$(BRCM_SAI_DEV)_PATH = $(SAI_LIBS_MOUNT_POINT)
endif

$(BRCM_SAI_DEV)_DEPENDS += $(BRCM_SAI)
