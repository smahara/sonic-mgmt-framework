BRCM_SAI = libsaibcm_3.255.6.4_amd64.deb
BRCM_SAI_DEV = libsaibcm-dev_3.255.6.4_amd64.deb
BRCM_SAI_DIAG = libsaibcm-diag_3.255.6.4_amd64.deb
SAI_LIBS_MOUNT_POINT = /sai_libs

ifneq  ($(LOCAL_SAI_DEBS_PATH),)
override BRCM_SAI = $(shell find $(SAI_LIBS_MOUNT_POINT) -maxdepth 1 -regex '.*libsaibcm_[0-9.]+_amd64\.deb' -printf "%f")
override BRCM_SAI_DEV = $(shell find $(SAI_LIBS_MOUNT_POINT) -maxdepth 1 -regex '.*libsaibcm-dev_[0-9.]+_amd64\.deb' -printf "%f")
override BRCM_SAI_DIAG = $(shell find $(SAI_LIBS_MOUNT_POINT) -maxdepth 1 -regex '.*libsaibcm-diag_[0-9.]+_amd64\.deb' -printf "%f")
endif

#BRCM_SAI
ifeq ($(LOCAL_SAI_DEBS_PATH),)
$(BRCM_SAI)_URL = "http://artifactory.force10networks.com/sonic-debs/$(BRCM_SAI)"
SONIC_ONLINE_DEBS += $(BRCM_SAI)
else
$(BRCM_SAI)_PATH = $(SAI_LIBS_MOUNT_POINT)
SONIC_COPY_DEBS += $(BRCM_SAI)
endif

#BRCM_SAI_DEV
$(eval $(call add_derived_package,$(BRCM_SAI),$(BRCM_SAI_DEV)))
ifeq ($(LOCAL_SAI_DEBS_PATH),)
$(BRCM_SAI_DEV)_URL = "http://artifactory.force10networks.com/sonic-debs/$(BRCM_SAI_DEV)"
else
$(BRCM_SAI_DEV)_PATH = $(SAI_LIBS_MOUNT_POINT)
endif

$(BRCM_SAI_DEV)_DEPENDS += $(BRCM_SAI)

#BRCM_SAI_DIAG
ifeq ($(LOCAL_SAI_DEBS_PATH),)
$(BRCM_SAI_DIAG)_URL = "http://artifactory.force10networks.com/sonic-debs/$(BRCM_SAI_DIAG)"
SONIC_ONLINE_DEBS += $(BRCM_SAI_DIAG)
else
$(BRCM_SAI_DIAG)_PATH = $(SAI_LIBS_MOUNT_POINT)
SONIC_COPY_DEBS += $(BRCM_SAI_DIAG)
endif
