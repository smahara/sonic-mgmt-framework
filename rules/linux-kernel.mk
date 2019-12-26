# linux kernel package

KVERSION_SHORT = 4.9.0-11-2
KVERSION = $(KVERSION_SHORT)-$(CONFIGURED_ARCH)
KERNEL_VERSION = 4.9.189
KERNEL_SUBVERSION = 3+deb9u2
ifeq ($(CONFIGURED_ARCH), armhf)
# Override kernel version for ARMHF as it uses arm MP (multi-platform) for short version
KVERSION = $(KVERSION_SHORT)-armmp
endif

export KVERSION_SHORT KVERSION KERNEL_VERSION KERNEL_SUBVERSION


SMPATH=$(SRC_PATH)/sonic-linux-kernel/
SM_DEP_LIST  := Makefile
SM_DEP_LIST  += patch/*
SM_DEP_LIST  += patch/preconfig/*
SMDEP_LIST   := $(wildcard $(addprefix $(SMPATH),$(SM_DEP_LIST)))

DEP_LIST     := $(SONIC_MAKEFILE_LIST) rules/linux-kernel.mk

DEP_FLAGS := $(SONIC_DPKG_CACHE_METHOD) $(SONIC_DPKG_CACHE_SOURCE) \
	         $(KERNEL_PROCURE_METHOD) $(KERNEL_CACHE_PATH) \
			 $(SONIC_DEBUGGING_ON)

LINUX_HEADERS_COMMON = linux-headers-$(KVERSION_SHORT)-common_$(KERNEL_VERSION)-$(KERNEL_SUBVERSION)_all.deb
$(LINUX_HEADERS_COMMON)_SRC_PATH = $(SRC_PATH)/sonic-linux-kernel
$(LINUX_HEADERS_COMMON)_CACHE_MODE = $(if $(filter $(strip $(KERNEL_PROCURE_METHOD)),$(strip $(SONIC_DPKG_CACHE_METHOD))),GIT_COMMIT_SHA)
$(LINUX_HEADERS_COMMON)_DEP_SOURCE = $(DEP_LIST)
$(LINUX_HEADERS_COMMON)_SMDEP_SOURCE = $(SMDEP_LIST)
$(LINUX_HEADERS_COMMON)_DEP_FLAGS    = $(DEP_FLAGS)
SONIC_MAKE_DEBS += $(LINUX_HEADERS_COMMON)

LINUX_HEADERS = linux-headers-$(KVERSION)_$(KERNEL_VERSION)-$(KERNEL_SUBVERSION)_$(CONFIGURED_ARCH).deb
$(eval $(call add_derived_package,$(LINUX_HEADERS_COMMON),$(LINUX_HEADERS)))

LINUX_KERNEL = linux-image-$(KVERSION)_$(KERNEL_VERSION)-$(KERNEL_SUBVERSION)_$(CONFIGURED_ARCH).deb
$(eval $(call add_derived_package,$(LINUX_HEADERS_COMMON),$(LINUX_KERNEL)))
