###############################################################################
## Presettings
###############################################################################

# Select bash for commands
.ONESHELL:
SHELL = /bin/bash
.SHELLFLAGS += -e
USER = $(shell id -un)
UID = $(shell id -u)
GUID = $(shell id -g)
SONIC_GET_VERSION=$(shell export BUILD_TIMESTAMP=$(BUILD_TIMESTAMP) && export BUILD_NUMBER=$(BUILD_NUMBER) && export BUILD_PRODUCT=$(BUILD_PRODUCT) && . functions.sh && sonic_get_version)

.SECONDEXPANSION:

NULL :=
SPACE := $(NULL) $(NULL)

###############################################################################
## General definitions
###############################################################################

SRC_PATH = src
RULES_PATH = rules
TARGET_PATH = target
DOCKERS_PATH = dockers
ifdef BLDENV
DEBS_PATH = $(TARGET_PATH)/debs/$(BLDENV)
FILES_PATH = $(TARGET_PATH)/files/$(BLDENV)
else
DEBS_PATH = $(TARGET_PATH)/debs
FILES_PATH = $(TARGET_PATH)/files
endif
PYTHON_DEBS_PATH = $(TARGET_PATH)/python-debs
PYTHON_WHEELS_PATH = $(TARGET_PATH)/python-wheels
PROJECT_ROOT = $(shell pwd)
STRETCH_DEBS_PATH = $(TARGET_PATH)/debs/stretch
STRETCH_FILES_PATH = $(TARGET_PATH)/files/stretch
DBG_IMAGE_MARK = dbg

CONFIGURED_PLATFORM := $(shell [ -f .platform ] && cat .platform || echo generic)
PLATFORM_PATH = platform/$(CONFIGURED_PLATFORM)
export BUILD_NUMBER
export BUILD_TIMESTAMP
export BUILD_PRODUCT
export CONFIGURED_PLATFORM

SONIC_MAKEFILE_LIST=slave.mk rules/functions

###############################################################################
## Utility rules
## Define configuration, help etc.
###############################################################################

.platform :
ifneq ($(CONFIGURED_PLATFORM),generic)
	@echo Build system is not configured, please run make configure
	@exit 1
endif

configure :
	@mkdir -p target/debs
	@mkdir -p target/debs/stretch
	@mkdir -p target/files
	@mkdir -p target/files/stretch
	@mkdir -p target/python-debs
	@mkdir -p target/python-wheels
	@echo $(PLATFORM) > .platform

distclean : .platform clean
	@rm -f .platform

list :
	@$(foreach target,$(SONIC_TARGET_LIST),echo $(target);)

# dummy target useful for trying makefile changes
noop :
	@echo "Nothing to do (noop)"

###############################################################################
## Include other rules
###############################################################################

ifeq ($(SONIC_ENABLE_PFCWD_ON_START),y)
ENABLE_PFCWD_ON_START = y
endif

ifeq ($(SONIC_ENABLE_SYSTEM_TELEMETRY),y)
ENABLE_SYSTEM_TELEMETRY = y
endif

ifeq ($(SONIC_ENABLE_SYNCD_RPC),y)
ENABLE_SYNCD_RPC = y
endif

include $(RULES_PATH)/config

ifneq ($(SONIC_INSTALL_DEBUG_TOOLS),)
INSTALL_DEBUG_TOOLS = $(SONIC_INSTALL_DEBUG_TOOLS)
endif

ifneq ($(SONIC_DEBUGGING_ON_PARAM),)
SONIC_DEBUGGING_ON = $(SONIC_DEBUGGING_ON_PARAM)
endif

ifneq ($(SONIC_PROFILING_ON_PARAM),)
SONIC_PROFILING_ON = $(SONIC_PROFILING_ON_PARAM)
endif

ifneq ($(SONIC_COVERAGE_ON_PARAM),)
SONIC_COVERAGE_ON = $(SONIC_COVERAGE_ON_PARAM)
endif

ifeq ($(SONIC_ENABLE_SFLOW),y)
ENABLE_SFLOW = y
endif

include $(RULES_PATH)/config
include $(RULES_PATH)/functions
include $(RULES_PATH)/*.mk
ifneq ($(CONFIGURED_PLATFORM), undefined)
include $(PLATFORM_PATH)/rules.mk
endif

ifeq ($(SONIC_USE_PDDF_FRAMEWORK),y)
PDDF_SUPPORT = y
endif
export PDDF_SUPPORT

ifeq ($(PDDF_SUPPORT), y)
PDDF_DIR = pddf
PLATFORM_PDDF_PATH = platform/$(PDDF_DIR)
include $(PLATFORM_PDDF_PATH)/rules.mk
endif


ifeq ($(USERNAME),)
override USERNAME := $(DEFAULT_USERNAME)
else
$(warning USERNAME given on command line: could be visible to other users)
endif

ifeq ($(PASSWORD),)
override PASSWORD := $(DEFAULT_PASSWORD)
else
$(warning PASSWORD given on command line: could be visible to other users)
endif

ifeq ($(SONIC_DEBUGGING_ON),y)
DEB_BUILD_OPTIONS_GENERIC := nostrip
endif

ifeq ($(SONIC_PROFILING_ON),y)
DEB_BUILD_OPTIONS_GENERIC := nostrip noopt
endif

ifeq ($(SONIC_COVERAGE_ON),y)
DEB_BUILD_OPTIONS_GENERIC := nostrip noopt
export COV_CFLAGS := -O0 -coverage
export COV_CFG_FLAGS := --enable-gcov=yes
export COV_LDFLAGS := -lgcov
export SONIC_COVERAGE_ON := y
endif

ifeq ($(SONIC_BUILD_JOBS),)
override SONIC_BUILD_JOBS := $(SONIC_CONFIG_BUILD_JOBS)
endif

# Allow command line value to override config file definition.
# It's being done this way since several makefiles already
# reference the SONIC_CONFIG_MAKE_JOBS variable.
ifneq ($(SONIC_MAKE_JOBS),)
override SONIC_CONFIG_MAKE_JOBS := $(SONIC_MAKE_JOBS)
endif

# If SONIC_CONFIG_NATIVE_DOCKERD_SHARED is enabled, force
# SONIC_CONFIG_USE_NATIVE_DOCKERD_FOR_BUILD enabled as well.
ifeq ($(strip $(SONIC_CONFIG_NATIVE_DOCKERD_SHARED)),y)
override SONIC_CONFIG_USE_NATIVE_DOCKERD_FOR_BUILD := y
endif

ifeq ($(strip $(SONIC_CONFIG_NATIVE_DOCKERD_SHARED)),y)
DOCKER_IMAGE_REF = $*$(DOCKER_USERNAME):$(DOCKER_USERTAG)
DOCKER_DBG_IMAGE_REF = $*-$(DBG_IMAGE_MARK)$(DOCKER_USERNAME):$(DOCKER_USERTAG)
docker-load-image-get = $(if $(1),$(1)$(DOCKER_USERNAME):$(DOCKER_USERTAG))
else
DOCKER_IMAGE_REF = $*
DOCKER_DBG_IMAGE_REF = $*-$(DBG_IMAGE_MARK)
docker-load-image-get = $(1)
endif

ifeq ($(VS_PREPARE_MEM),)
override VS_PREPARE_MEM := $(DEFAULT_VS_PREPARE_MEM)
endif

ifeq ($(KERNEL_PROCURE_METHOD),)
override KERNEL_PROCURE_METHOD := $(strip $(DEFAULT_KERNEL_PROCURE_METHOD))
endif

ifeq ($(KERNEL_CACHE_PATH),)
override KERNEL_CACHE_PATH := $(strip $(DEFAULT_KERNEL_CACHE_PATH))
endif

ifeq ($(KERNEL_PROCURE_METHOD),cache)
ifeq ($(KERNEL_CACHE_PATH),)
$(error KERNEL_CACHE_PATH must be specified for KERNEL_PROCURE_METHOD=cache)
endif
endif

MAKEFLAGS += -j $(SONIC_BUILD_JOBS)
DEB_BUILD_OPTIONS_GENERIC += "parallel=$(SONIC_CONFIG_MAKE_JOBS)"
export DEB_BUILD_OPTIONS := "$(DEB_BUILD_OPTIONS_GENERIC)"
export SONIC_CONFIG_MAKE_JOBS

ifeq ($(ENABLE_PDE),y)
override ENABLE_ZTP :=
endif

###############################################################################
## Routing stack related exports
###############################################################################

export SONIC_ROUTING_STACK
export FRR_USER_UID
export FRR_USER_GID

###############################################################################
## Dumping key config attributes associated to current building exercise
###############################################################################

$(info SONiC Build System)
$(info )
$(info Build Configuration)
$(info "CONFIGURED_PLATFORM"             : "$(if $(PLATFORM),$(PLATFORM),$(CONFIGURED_PLATFORM))")
$(info "SONIC_CONFIG_PRINT_DEPENDENCIES" : "$(SONIC_CONFIG_PRINT_DEPENDENCIES)")
$(info "SONIC_BUILD_JOBS"                : "$(SONIC_BUILD_JOBS)")
$(info "SONIC_CONFIG_MAKE_JOBS"          : "$(SONIC_CONFIG_MAKE_JOBS)")
$(info "USE_NATIVE_DOCKERD_FOR_BUILD"    : "$(SONIC_CONFIG_USE_NATIVE_DOCKERD_FOR_BUILD)")
$(info "NATIVE_DOCKERD_SHARED"           : "$(SONIC_CONFIG_NATIVE_DOCKERD_SHARED)")
$(info "USERNAME"                        : "$(USERNAME)")
$(info "PASSWORD"                        : "$(PASSWORD)")
$(info "ENABLE_DHCP_GRAPH_SERVICE"       : "$(ENABLE_DHCP_GRAPH_SERVICE)")
$(info "SHUTDOWN_BGP_ON_START"           : "$(SHUTDOWN_BGP_ON_START)")
$(info "ENABLE_PFCWD_ON_START"           : "$(ENABLE_PFCWD_ON_START)")
$(info "INSTALL_DEBUG_TOOLS"             : "$(INSTALL_DEBUG_TOOLS)")
$(info "ROUTING_STACK"                   : "$(SONIC_ROUTING_STACK)")
ifeq ($(SONIC_ROUTING_STACK),frr)
$(info "FRR_USER_UID"                    : "$(FRR_USER_UID)")
$(info "FRR_USER_GID"                    : "$(FRR_USER_GID)")
endif
$(info "ENABLE_SYNCD_RPC"                : "$(ENABLE_SYNCD_RPC)")
$(info "ENABLE_ORGANIZATION_EXTENSIONS"  : "$(ENABLE_ORGANIZATION_EXTENSIONS)")
$(info "HTTP_PROXY"                      : "$(HTTP_PROXY)")
$(info "HTTPS_PROXY"                     : "$(HTTPS_PROXY)")
$(info "ENABLE_SYSTEM_TELEMETRY"         : "$(ENABLE_SYSTEM_TELEMETRY)")
$(info "ENABLE_ZTP"                      : "$(ENABLE_ZTP)")
$(info "ENABLE_PDE"                      : "$(ENABLE_PDE)")
$(info "SONIC_DEBUGGING_ON"              : "$(SONIC_DEBUGGING_ON)")
$(info "SONIC_PROFILING_ON"              : "$(SONIC_PROFILING_ON)")
$(info "SONIC_COVERAGE_ON"               : "$(SONIC_COVERAGE_ON)")
$(info "KERNEL_PROCURE_METHOD"           : "$(KERNEL_PROCURE_METHOD)")
ifeq ($(KERNEL_PROCURE_METHOD),cache)
$(info "KERNEL_CACHE_PATH"               : "$(KERNEL_CACHE_PATH)")
endif
$(info "SONIC_DPKG_CACHE_METHOD"         : "$(SONIC_DPKG_CACHE_METHOD)")
ifeq ($(SONIC_DPKG_CACHE_METHOD),cache)
$(info "DPKG_CACHE_PATH"                 : "$(SONIC_DPKG_CACHE_SOURCE)")
endif
$(info "BUILD_NUMBER"                    : "$(BUILD_NUMBER)")
$(info "BUILD_TIMESTAMP"                 : "$(BUILD_TIMESTAMP)")
$(info "BUILD_PRODUCT"                   : "$(BUILD_PRODUCT)")
$(info "BLDENV"                          : "$(BLDENV)")
$(info "VS_PREPARE_MEM"                  : "$(VS_PREPARE_MEM)")
$(info "VERSION"                         : "$(SONIC_GET_VERSION)")
$(info "PDDF_SUPPORT"                    : "$(PDDF_SUPPORT)")
$(info "ENABLE_SFLOW"                    : "$(ENABLE_SFLOW)")
$(info )

###############################################################################
## Generic rules section
## All rules must go after includes for propper targets expansion
###############################################################################

export kernel_procure_method=$(KERNEL_PROCURE_METHOD)
export kernel_cache_mount:=/kernel_cache
export vs_build_prepare_mem=$(VS_PREPARE_MEM)

###############################################################################
## Canned sequences
###############################################################################

SONIC_DPKG_CACHE_DIR    := /dpkg_cache
MOD_CACHE_LOCK_SUFFIX   := cache_accss
MOD_CACHE_LOCK_TIMEOUT  := 3600

DOCKER_LOCKFILE_SUFFIX  := access
DOCKER_LOCKFILE_TIMEOUT := 1200

# Lock macro for shared file access
# Lock is implemented through flock command with a specified timeout value
# Lock file is created in the specified directory, a separate one for each target file name
# A designated suffix is appended to each target file name, followed by .lock
#
# Parameters:
#  $(1) - target file name (without path)
#  $(2) - lock file path (only)
#  $(3) - designated lock file suffix
#  $(4) - flock timeout (in seconds)
#
# $(call MOD_LOCK,file,path,suffix,timeout)
define MOD_LOCK
	if [[ ! -f $(2)/$(1)_$(3).lock ]]; then
		touch $(2)/$(1)_$(3).lock
		chmod 777 $(2)/$(1)_$(3).lock;
	fi
	$(eval $(1)_lock_fd=$(subst -,_,$(subst +,_,$(subst .,_,$(1)))))
	exec {$($(1)_lock_fd)}<"$(2)/$(1)_$(3).lock";
	if ! flock -x -w $(4) "$${$($(1)_lock_fd)}" ; then
		echo "ERROR: Lock timeout trying to access $(2)/$(1)_$(3).lock";
		exit 1;
	fi
endef

# UnLock macro for shared file access
#
# Parameters:
#  $(1) - target file name (without path)
#
# $(call MOD_UNLOCK,file)
define MOD_UNLOCK
	eval exec "$${$($(1)_lock_fd)}<&-";
endef


# Loads the deb package from debian cache
# Cache file prefix is formed using SHA value
# The SHA value consists of
#   1.  12 byte SHA value from environmental flags
#   2.  48 byte SHA value from one of the keyword type - GIT_COMMIT_SHA or GIT_CONTENT_SHA
#          GIT_COMMIT_SHA   - SHA value of the last git commit id if it is a submodule
#          GIT_CONTENT_SHA  - SHA value is calculated from the target dependency files content.
#   Cache is loaded only when corresponding cache file is present in cache direcory and its dependencies are not changed.
define LOAD_CACHE
	$(eval MOD_SRC_PATH=$($(1)_SRC_PATH))
	$(eval DEP_FLAGS_SHA := $(shell git hash-object $($(1)_DEP_FLAGS_FILE)|awk '{print substr($$1,0,11);}'))
	$(eval MOD_HASH=$(if $(filter GIT_COMMIT_SHA,$($(1)_CACHE_MODE)),$(shell cd $(MOD_SRC_PATH) && git log -1 --format="%H")
		, $(shell git hash-object $($(1)_DEP_FLAGS_FILE) $($(1)_DEP_SOURCE) $($(1)_SMDEP_SOURCE)|sha1sum|awk '{print $$1}')))
	$(eval MOD_CACHE_FILE=$(1)-$(DEP_FLAGS_SHA)-$(MOD_HASH).tgz)
	$(eval $(1)_MOD_CACHE_FILE=$(MOD_CACHE_FILE))
	$(eval DRV_DEB=$(foreach pkg,$(addprefix $(DEBS_PATH)/,$(1) $($(1)_DERIVED_DEBS)),$(if $(wildcard $(pkg)),,$(pkg))))
	$(eval $(1)_FILES_MODIFIED  := $(if $($(1)_DEP_SOURCE),$(shell git status -s $($(1)_DEP_SOURCE))) \
		   $(if $($(1)_SMDEP_SOURCE),$(shell cd $(MOD_SRC_PATH) &&  git status -s $(subst $(MOD_SRC_PATH)/,,$($(1)_SMDEP_SOURCE)))) )
	#$(filter-out $($(1)_DEP_SOURCE),$($(1)_SMDEP_SOURCE), $?)

	$(if $($(1)_FILES_MODIFIED),
		echo "Target $(1) dependencies are modifed - load cache skipped";
		echo "Modified dependencies are : [$($(1)_FILES_MODIFIED)] ";
	    ,
		$(if $(wildcard $(SONIC_DPKG_CACHE_DIR)/$(MOD_CACHE_FILE)),
			$(if $(DRV_DEB), tar -xzvf $(SONIC_DPKG_CACHE_DIR)/$(MOD_CACHE_FILE),echo );
			echo "File $(SONIC_DPKG_CACHE_DIR)/$(MOD_CACHE_FILE) is loaded from cache";
			$(eval $(1)_CACHE_LOADED := Yes)
			,
			echo "File $(SONIC_DPKG_CACHE_DIR)/$(MOD_CACHE_FILE) is not present in cache !";
		 )
	 )
	echo ""
endef

# Saves the deb package into debian cache
# A single tared-zip cache is created for .deb and its derived packages in the cache direcory.
# It saves the .deb into cache only when its dependencies are not changed
# The cache save is protected with lock.
# The SAVE_CACHE macro has dependecy with LOAD_CACHE macro
# 	 The target specific variables -_SRC_PATH, _MOD_CACHE_FILE and _FILES_MODIFIED are
# 	 derived from the LOAD_CACHE macro
define SAVE_CACHE
	$(eval MOD_SRC_PATH=$($(1)_SRC_PATH))
	$(eval MOD_CACHE_FILE=$($(1)_MOD_CACHE_FILE))
	$(call MOD_LOCK,$(1),$(SONIC_DPKG_CACHE_DIR),$(MOD_CACHE_LOCK_SUFFIX),$(MOD_CACHE_LOCK_TIMEOUT))
	$(if $($(1)_FILES_MODIFIED),
		echo "Target $(1) dependencies are modifed - save cache skipped";
	    ,
		tar -czvf $(SONIC_DPKG_CACHE_DIR)/$(MOD_CACHE_FILE) $(2) $(addprefix $(DEBS_PATH)/,$($(1)_DERIVED_DEBS));
		echo "File $(SONIC_DPKG_CACHE_DIR)/$(MOD_CACHE_FILE) saved in cache ";
	 )
	$(call MOD_UNLOCK,$(1))
	echo ""
endef


ifeq ($(strip $(SONIC_CONFIG_NATIVE_DOCKERD_SHARED)),y)
# $(call docker-image-save,from,to)
define docker-image-save
    @echo "Attempting docker image lock for $(1) save" $(LOG)
    $(call MOD_LOCK,$(1),$(DOCKER_LOCKDIR),$(DOCKER_LOCKFILE_SUFFIX),$(DOCKER_LOCKFILE_TIMEOUT))
    @echo "Obtained docker image lock for $(1) save" $(LOG)
    @echo "Tagging docker image $(1)$(DOCKER_USERNAME):$(DOCKER_USERTAG) as $(1):latest" $(LOG)
    docker tag $(1)$(DOCKER_USERNAME):$(DOCKER_USERTAG) $(1):latest $(LOG)
    @echo "Saving docker image $(1):latest" $(LOG)
    docker save $(1):latest | gzip -c > $(2)
    @echo "Removing docker image $(1):latest" $(LOG)
    docker rmi -f $(1):latest $(LOG)
    $(call MOD_UNLOCK,$(1))
    @echo "Released docker image lock for $(1) save" $(LOG)
    @echo "Removing docker image $(1)$(DOCKER_USERNAME):$(DOCKER_USERTAG)" $(LOG)
    docker rmi -f $(1)$(DOCKER_USERNAME):$(DOCKER_USERTAG) $(LOG)
endef
# $(call docker-image-load,from)
define docker-image-load
    @echo "Attempting docker image lock for $(1) load" $(LOG)
    $(call MOD_LOCK,$(1),$(DOCKER_LOCKDIR),$(DOCKER_LOCKFILE_SUFFIX),$(DOCKER_LOCKFILE_TIMEOUT))
    @echo "Obtained docker image lock for $(1) load" $(LOG)
    @echo "Loading docker image $(TARGET_PATH)/$(1).gz" $(LOG)
    docker load -i $(TARGET_PATH)/$(1).gz $(LOG)
    @echo "Tagging docker image $(1):latest as $(1)$(DOCKER_USERNAME):$(DOCKER_USERTAG)" $(LOG)
    docker tag $(1):latest $(1)$(DOCKER_USERNAME):$(DOCKER_USERTAG) $(LOG)
    @echo "Removing docker image $(1):latest" $(LOG)
    docker rmi -f $(1):latest $(LOG)
    $(call MOD_UNLOCK,$(1))
    @echo "Released docker image lock for $(1) load" $(LOG)
endef
else
define docker-image-save
    docker save $(1):latest | gzip -c > $(2)
endef
define docker-image-load
    docker load -i $(TARGET_PATH)/$(1).gz $(LOG)
endef
endif

###############################################################################
## Local targets
###############################################################################

# Copy debian packages from local directory
# Add new package for copy:
#     SOME_NEW_DEB = some_new_deb.deb
#     $(SOME_NEW_DEB)_PATH = path/to/some_new_deb.deb
#     SONIC_COPY_DEBS += $(SOME_NEW_DEB)
$(addprefix $(DEBS_PATH)/, $(SONIC_COPY_DEBS)) : $(DEBS_PATH)/% : .platform
	$(HEADER)
	$(foreach deb,$* $($*_DERIVED_DEBS), \
	    { cp $($(deb)_PATH)/$(deb) $(DEBS_PATH)/ $(LOG) || exit 1 ; } ; )
	$(FOOTER)


SONIC_TARGET_LIST += $(addprefix $(DEBS_PATH)/, $(SONIC_COPY_DEBS))

# Copy regular files from local directory
# Add new package for copy:
#     SOME_NEW_FILE = some_new_file
#     $(SOME_NEW_FILE)_PATH = path/to/some_new_file
#     SONIC_COPY_FILES += $(SOME_NEW_FILE)
$(addprefix $(FILES_PATH)/, $(SONIC_COPY_FILES)) : $(FILES_PATH)/% : .platform
	$(HEADER)
	cp $($*_PATH)/$* $(FILES_PATH)/ $(LOG) || exit 1
	$(FOOTER)

SONIC_TARGET_LIST += $(addprefix $(FILES_PATH)/, $(SONIC_COPY_FILES))

###############################################################################
## Online targets
###############################################################################

# Download debian packages from online location
# Add new package for download:
#     SOME_NEW_DEB = some_new_deb.deb
#     $(SOME_NEW_DEB)_URL = https://url/to/this/deb.deb
#     SONIC_ONLINE_DEBS += $(SOME_NEW_DEB)
$(addprefix $(DEBS_PATH)/, $(SONIC_ONLINE_DEBS)) : $(DEBS_PATH)/% : .platform
	$(HEADER)
	$(foreach deb,$* $($*_DERIVED_DEBS), \
	    { wget --no-use-server-timestamps -O $(DEBS_PATH)/$(deb) $($(deb)_URL) $(LOG) || exit 1 ; } ; )
	$(FOOTER)

SONIC_TARGET_LIST += $(addprefix $(DEBS_PATH)/, $(SONIC_ONLINE_DEBS))

# Download regular files from online location
# Files are stored in deb packages directory for convenience
# Add new file for download:
#     SOME_NEW_FILE = some_new_file
#     $(SOME_NEW_FILE)_URL = https://url/to/this/file
#     SONIC_ONLINE_FILES += $(SOME_NEW_FILE)
$(addprefix $(FILES_PATH)/, $(SONIC_ONLINE_FILES)) : $(FILES_PATH)/% : .platform
	$(HEADER)
	wget --no-use-server-timestamps -O  $@ $($*_URL) $(LOG)
	$(FOOTER)

SONIC_TARGET_LIST += $(addprefix $(FILES_PATH)/, $(SONIC_ONLINE_FILES))

# Each target defines a optional variable called '_DEP_FLAGS_FILE' that contains  a list of environment flags for that target and
# that indicates that target needs to be rebuilt if  one of the dependent flag is changed
# An environmental dependency flags file is created with the name as ‘<target name>.dep’  for each of the deb targets.
# This file contains the values of target environment flags and gets updated only when there is a change in the flags value.
# This file is added as a dependency to the target, so that any change in the file will trigger the target recompilation.
# For Eg:
#       target/debs/stretch/linux-headers-4.9.0-9-2-common_4.9.168-1+deb9u3_all.deb.dep
#
$(addsuffix .dep,$(addprefix $(DEBS_PATH)/, $(SONIC_MAKE_DEBS) $(SONIC_DPKG_DEBS))) : \
	$(DEBS_PATH)/%.dep : $$(eval $$*_DEP_FLAGS_FILE:=$$@)
	@echo '$($*_DEP_FLAGS)' | cmp -s - $@ || echo '$($*_DEP_FLAGS)' > $@



###############################################################################
## Build targets
###############################################################################

# Build project using build.sh script
# They are essentially a one-time build projects that get sources from some URL
# and compile them
# Add new file for build:
#     SOME_NEW_FILE = some_new_deb.deb
#     $(SOME_NEW_FILE)_SRC_PATH = $(SRC_PATH)/project_name
#     $(SOME_NEW_FILE)_DEPENDS = $(SOME_OTHER_DEB1) $(SOME_OTHER_DEB2) ...
#     SONIC_MAKE_FILES += $(SOME_NEW_FILE)
$(addprefix $(FILES_PATH)/, $(SONIC_MAKE_FILES)) : $(FILES_PATH)/% : .platform $$(addsuffix -install,$$(addprefix $(DEBS_PATH)/,$$($$*_DEPENDS)))
	$(HEADER)
	# Remove target to force rebuild
	rm -f $(addprefix $(FILES_PATH)/, $*)
	# Apply series of patches if exist
	if [ -f $($*_SRC_PATH).patch/series ]; then pushd $($*_SRC_PATH) && QUILT_PATCHES=../$(notdir $($*_SRC_PATH)).patch quilt push -a; popd; fi
	# Build project and take package
	make DEST=$(shell pwd)/$(FILES_PATH) -C $($*_SRC_PATH) $(shell pwd)/$(FILES_PATH)/$* $(LOG)
	# Clean up
	if [ -f $($*_SRC_PATH).patch/series ]; then pushd $($*_SRC_PATH) && quilt pop -a -f; popd; fi
	$(FOOTER)

SONIC_TARGET_LIST += $(addprefix $(FILES_PATH)/, $(SONIC_MAKE_FILES))

###############################################################################
## Debian package related targets
###############################################################################

# Build project using build.sh script
# They are essentially a one-time build projects that get sources from some URL
# and compile them
# Add new package for build:
#     SOME_NEW_DEB = some_new_deb.deb
#     $(SOME_NEW_DEB)_SRC_PATH = $(SRC_PATH)/project_name
#     $(SOME_NEW_DEB)_DEPENDS = $(SOME_OTHER_DEB1) $(SOME_OTHER_DEB2) ...
#     SONIC_MAKE_DEBS += $(SOME_NEW_DEB)
$(addprefix $(DEBS_PATH)/, $(SONIC_MAKE_DEBS)) : $(DEBS_PATH)/% : .platform $$(addsuffix -install,$$(addprefix $(DEBS_PATH)/,$$($$*_DEPENDS))) \
	$$($$*_DEP_SOURCE) $$($$*_SMDEP_SOURCE) | $(DEBS_PATH)/%.dep
	$(HEADER)

	# Load the target deb from DPKG cache
	$(if $(and $(filter-out none,$(SONIC_DPKG_CACHE_METHOD)),$($*_CACHE_MODE)), $(call LOAD_CACHE,$*) )

	# Skip building the target if it is already loaded from cache
	if [ -z '$($*_CACHE_LOADED)' ] ; then

		# Remove target to force rebuild
		rm -f $(addprefix $(DEBS_PATH)/, $* $($*_DERIVED_DEBS) $($*_EXTRA_DEBS))
		# Apply series of patches if exist
		if [ -f $($*_SRC_PATH).patch/series ]; then pushd $($*_SRC_PATH) && QUILT_PATCHES=../$(notdir $($*_SRC_PATH)).patch quilt push -a; popd; fi
		# Build project and take package
		DEB_BUILD_OPTIONS="${DEB_BUILD_OPTIONS_GENERIC}" make DEST=$(shell pwd)/$(DEBS_PATH) -C $($*_SRC_PATH) $(shell pwd)/$(DEBS_PATH)/$* $(LOG)
		# Clean up
		if [ -f $($*_SRC_PATH).patch/series ]; then pushd $($*_SRC_PATH) && quilt pop -a -f; popd; fi

		# Save the target deb into DPKG cache
		$(if $(and $(filter-out none,$(SONIC_DPKG_CACHE_METHOD)),$($*_CACHE_MODE)), $(call SAVE_CACHE,$*,$@))

	fi

	$(FOOTER)

SONIC_TARGET_LIST += $(addprefix $(DEBS_PATH)/, $(SONIC_MAKE_DEBS))

# Build project with dpkg-buildpackage
# Add new package for build:
#     SOME_NEW_DEB = some_new_deb.deb
#     $(SOME_NEW_DEB)_SRC_PATH = $(SRC_PATH)/project_name
#     $(SOME_NEW_DEB)_DEPENDS = $(SOME_OTHER_DEB1) $(SOME_OTHER_DEB2) ...
#     SONIC_DPKG_DEBS += $(SOME_NEW_DEB)
$(addprefix $(DEBS_PATH)/, $(SONIC_DPKG_DEBS)) : $(DEBS_PATH)/% : .platform $$(addsuffix -install,$$(addprefix $(DEBS_PATH)/,$$($$*_DEPENDS))) \
	$$($$*_DEP_SOURCE) $$($$*_SMDEP_SOURCE) | $(DEBS_PATH)/%.dep
	$(HEADER)

	# Load the target deb from DPKG cache
	$(if $(and $(filter-out none,$(SONIC_DPKG_CACHE_METHOD)),$($*_CACHE_MODE)), $(call LOAD_CACHE,$*) )

	# Skip building the target if it is already loaded from cache
	if [ -z '$($*_CACHE_LOADED)' ] ; then

		# Remove old build logs if they exist
		rm -f $($*_SRC_PATH)/debian/*.debhelper.log
		# Apply series of patches if exist
		if [ -f $($*_SRC_PATH).patch/series ]; then pushd $($*_SRC_PATH) && QUILT_PATCHES=../$(notdir $($*_SRC_PATH)).patch quilt push -a; popd; fi
		# Build project
		pushd $($*_SRC_PATH) $(LOG)
		[ ! -f ./autogen.sh ] || ./autogen.sh $(LOG)
		$(if $($*_DPKG_TARGET),
			DEB_BUILD_OPTIONS="${DEB_BUILD_OPTIONS_GENERIC} ${$*_DEB_BUILD_OPTIONS}" dpkg-buildpackage -rfakeroot -b -us -uc -j$(SONIC_CONFIG_MAKE_JOBS) --as-root -T$($*_DPKG_TARGET) $(LOG),
			DEB_BUILD_OPTIONS="${DEB_BUILD_OPTIONS_GENERIC} ${$*_DEB_BUILD_OPTIONS}" dpkg-buildpackage -rfakeroot -b -us -uc -j$(SONIC_CONFIG_MAKE_JOBS) $(LOG)
		)
		popd $(LOG)
		# Clean up
		if [ -f $($*_SRC_PATH).patch/series ]; then pushd $($*_SRC_PATH) && quilt pop -a -f; popd; fi
		# Take built package(s)
		mv $(addprefix $($*_SRC_PATH)/../, $* $($*_DERIVED_DEBS) $($*_EXTRA_DEBS)) $(DEBS_PATH) $(LOG)

		# Save the target deb into DPKG cache
		$(if $(and $(filter-out none,$(SONIC_DPKG_CACHE_METHOD)),$($*_CACHE_MODE)), $(call SAVE_CACHE,$*,$@))
	fi

	$(FOOTER)

SONIC_TARGET_LIST += $(addprefix $(DEBS_PATH)/, $(SONIC_DPKG_DEBS))

# Rules for derived debian packages (dev, dbg, etc.)
# All noise takes place in main deb recipe, so we are just telling that
# we depend on it and move our deb to other targets
# Add new dev package:
#     $(eval $(call add_derived_package,$(ORIGINAL_DEB),derived_deb_file.deb))
$(addprefix $(DEBS_PATH)/, $(SONIC_DERIVED_DEBS)) : $(DEBS_PATH)/% : .platform $$(addsuffix -install,$$(addprefix $(DEBS_PATH)/,$$($$*_DEPENDS)))
	$(HEADER)
	# All noise takes place in main deb recipe, so we are just telling that
	# we depend on it
	# Put newer timestamp
	[ -f $@ ] && touch $@
	$(FOOTER)

SONIC_TARGET_LIST += $(addprefix $(DEBS_PATH)/, $(SONIC_DERIVED_DEBS))

# Rules for extra debian packages
# All noise takes place in main deb recipe, so we are just telling that
# we need to build the main deb and move our deb to other targets
# Add new dev package:
#     $(eval $(call add_extra_package,$(ORIGINAL_DEB),extra_deb_file.deb))
$(addprefix $(DEBS_PATH)/, $(SONIC_EXTRA_DEBS)) : $(DEBS_PATH)/% : .platform $$(addprefix $(DEBS_PATH)/,$$($$*_MAIN_DEB))
	$(HEADER)
	# All noise takes place in main deb recipe, so we are just telling that
	# we depend on it
	# Put newer timestamp
	[ -f $@ ] && touch $@
	$(FOOTER)

SONIC_TARGET_LIST += $(addprefix $(DEBS_PATH)/, $(SONIC_EXTRA_DEBS))

# Targets for installing debian packages prior to build one that depends on them
SONIC_INSTALL_TARGETS = $(addsuffix -install,$(addprefix $(DEBS_PATH)/, \
			$(SONIC_ONLINE_DEBS) \
			$(SONIC_COPY_DEBS) \
			$(SONIC_MAKE_DEBS) \
			$(SONIC_DPKG_DEBS) \
			$(SONIC_PYTHON_STDEB_DEBS) \
			$(SONIC_DERIVED_DEBS) \
			$(SONIC_EXTRA_DEBS)))
$(SONIC_INSTALL_TARGETS) : $(DEBS_PATH)/%-install : .platform $$(addsuffix -install,$$(addprefix $(DEBS_PATH)/,$$($$*_DEPENDS))) $(DEBS_PATH)/$$*
	$(HEADER)
	[ -f $(DEBS_PATH)/$* ] || { echo $(DEBS_PATH)/$* does not exist $(LOG) && false $(LOG) }
	# put a lock here because dpkg does not allow installing packages in parallel
	while true; do
	if mkdir $(DEBS_PATH)/dpkg_lock &> /dev/null; then
	{ sudo dpkg -i $($*_DPKGFLAGS) $(DEBS_PATH)/$* $(LOG) && rm -d $(DEBS_PATH)/dpkg_lock && break; } || { rm -d $(DEBS_PATH)/dpkg_lock && exit 1 ; }
	fi
	done
	$(FOOTER)

###############################################################################
## Python packages
###############################################################################

# Build project with python setup.py --command-packages=stdeb.command
# Add new package for build:
#     SOME_NEW_DEB = some_new_deb.deb
#     $(SOME_NEW_DEB)_SRC_PATH = $(SRC_PATH)/project_name
#     $(SOME_NEW_DEB)_DEPENDS = $(SOME_OTHER_DEB1) $(SOME_OTHER_DEB2) ...
#     SONIC_PYTHON_STDEB_DEBS += $(SOME_NEW_DEB)
$(addprefix $(PYTHON_DEBS_PATH)/, $(SONIC_PYTHON_STDEB_DEBS)) : $(PYTHON_DEBS_PATH)/% : .platform \
		$$(addsuffix -install,$$(addprefix $(PYTHON_DEBS_PATH)/,$$($$*_DEPENDS))) \
		$$(addsuffix -install,$$(addprefix $(PYTHON_WHEELS_PATH)/,$$($$*_WHEEL_DEPENDS)))
	$(HEADER)
	# Apply series of patches if exist
	if [ -f $($*_SRC_PATH).patch/series ]; then pushd $($*_SRC_PATH) && QUILT_PATCHES=../$(notdir $($*_SRC_PATH)).patch quilt push -a; popd; fi
	# Build project
	pushd $($*_SRC_PATH) $(LOG)
	rm -rf deb_dist/* $(LOG)
	python setup.py --command-packages=stdeb.command bdist_deb $(LOG)
	popd $(LOG)
	# Clean up
	if [ -f $($*_SRC_PATH).patch/series ]; then pushd $($*_SRC_PATH) && quilt pop -a -f; popd; fi
	# Take built package(s)
	mv $(addprefix $($*_SRC_PATH)/deb_dist/, $* $($*_DERIVED_DEBS)) $(PYTHON_DEBS_PATH) $(LOG)
	$(FOOTER)

SONIC_TARGET_LIST += $(addprefix $(PYTHON_DEBS_PATH)/, $(SONIC_PYTHON_STDEB_DEBS))

# Build project using python setup.py bdist_wheel
# Projects that generate python wheels
# Add new package for build:
#     SOME_NEW_WHL = some_new_whl.whl
#     $(SOME_NEW_WHL)_SRC_PATH = $(SRC_PATH)/project_name
#     $(SOME_NEW_WHL)_PYTHON_VERSION = 2 (or 3)
#     $(SOME_NEW_WHL)_DEPENDS = $(SOME_OTHER_WHL1) $(SOME_OTHER_WHL2) ...
#     SONIC_PYTHON_WHEELS += $(SOME_NEW_WHL)
$(addprefix $(PYTHON_WHEELS_PATH)/, $(SONIC_PYTHON_WHEELS)) : $(PYTHON_WHEELS_PATH)/% : .platform $$(addsuffix -install,$$(addprefix $(PYTHON_WHEELS_PATH)/,$$($$*_DEPENDS)))
	$(HEADER)
	pushd $($*_SRC_PATH) $(LOG)
	# apply series of patches if exist
	if [ -f ../$(notdir $($*_SRC_PATH)).patch/series ]; then QUILT_PATCHES=../$(notdir $($*_SRC_PATH)).patch quilt push -a; fi
	[ "$($*_TEST)" = "n" ] || python$($*_PYTHON_VERSION) setup.py test $(LOG)
	python$($*_PYTHON_VERSION) setup.py bdist_wheel $(LOG)
	# clean up
	if [ -f ../$(notdir $($*_SRC_PATH)).patch/series ]; then quilt pop -a -f; fi
	popd $(LOG)
	mv $($*_SRC_PATH)/dist/$* $(PYTHON_WHEELS_PATH) $(LOG)
	$(FOOTER)

SONIC_TARGET_LIST += $(addprefix $(PYTHON_WHEELS_PATH)/, $(SONIC_PYTHON_WHEELS))

# Targets for installing python wheels.
# Autogenerated
SONIC_INSTALL_WHEELS = $(addsuffix -install, $(addprefix $(PYTHON_WHEELS_PATH)/, $(SONIC_PYTHON_WHEELS)))
$(SONIC_INSTALL_WHEELS) : $(PYTHON_WHEELS_PATH)/%-install : .platform $$(addsuffix -install,$$(addprefix $(PYTHON_WHEELS_PATH)/,$$($$*_DEPENDS))) $(PYTHON_WHEELS_PATH)/$$*
	$(HEADER)
	[ -f $(PYTHON_WHEELS_PATH)/$* ] || { echo $(PYTHON_WHEELS_PATH)/$* does not exist $(LOG) && exit 1; }
	# put a lock here to avoid race conditions
	while true; do
	if mkdir $(PYTHON_WHEELS_PATH)/pip_lock &> /dev/null; then
	{ sudo -E pip$($*_PYTHON_VERSION) install $(PYTHON_WHEELS_PATH)/$* $(LOG) && rm -d $(PYTHON_WHEELS_PATH)/pip_lock && break; } || { rm -d $(PYTHON_WHEELS_PATH)/pip_lock && exit 1 ; }
	fi
	done
	$(FOOTER)

###############################################################################
## Docker images related targets
###############################################################################

# start docker daemon
docker-start :
	@sudo sed -i '/http_proxy/d' /etc/default/docker
	@sudo bash -c "echo \"export http_proxy=$$http_proxy\" >> /etc/default/docker"
	@test x$(SONIC_CONFIG_USE_NATIVE_DOCKERD_FOR_BUILD) != x"y" && sudo service docker status &> /dev/null || ( sudo service docker start &> /dev/null && sleep 1 )

# targets for building simple docker images that do not depend on any debian packages
$(addprefix $(TARGET_PATH)/, $(SONIC_SIMPLE_DOCKER_IMAGES)) : $(TARGET_PATH)/%.gz : .platform docker-start $$(addsuffix -load,$$(addprefix $(TARGET_PATH)/,$$($$*.gz_LOAD_DOCKERS)))
	$(HEADER)
	# Apply series of patches if exist
	if [ -f $($*.gz_PATH).patch/series ]; then pushd $($*.gz_PATH) && QUILT_PATCHES=../$(notdir $($*.gz_PATH)).patch quilt push -a; popd; fi
	docker info $(LOG)
	docker build --squash --no-cache \
		--build-arg http_proxy=$(HTTP_PROXY) \
		--build-arg https_proxy=$(HTTPS_PROXY) \
		--build-arg user=$(USER) \
		--build-arg uid=$(UID) \
		--build-arg guid=$(GUID) \
		--build-arg docker_container_name=$($*.gz_CONTAINER_NAME) \
		--label Tag=$(SONIC_GET_VERSION) \
		-t $(DOCKER_IMAGE_REF) $($*.gz_PATH) $(LOG)
	$(call docker-image-save,$*,$@)
	# Clean up
	if [ -f $($*.gz_PATH).patch/series ]; then pushd $($*.gz_PATH) && quilt pop -a -f; popd; fi
	$(FOOTER)

SONIC_TARGET_LIST += $(addprefix $(TARGET_PATH)/, $(SONIC_SIMPLE_DOCKER_IMAGES))

# Build jessie docker images only in jessie slave docker,
# jessie docker images only in jessie slave docker
ifeq ($(BLDENV),)
	DOCKER_IMAGES_FOR_INSTALLERS := $(sort $(foreach installer,$(SONIC_INSTALLERS),$($(installer)_DOCKERS)))
	DOCKER_IMAGES := $(SONIC_JESSIE_DOCKERS)
	DOCKER_DBG_IMAGES := $(SONIC_JESSIE_DBG_DOCKERS)
	SONIC_JESSIE_DOCKERS_FOR_INSTALLERS = $(filter $(SONIC_JESSIE_DOCKERS),$(DOCKER_IMAGES_FOR_INSTALLERS) $(EXTRA_JESSIE_TARGETS))
	SONIC_JESSIE_DBG_DOCKERS_FOR_INSTALLERS = $(filter $(SONIC_JESSIE_DBG_DOCKERS), $(patsubst %.gz,%-$(DBG_IMAGE_MARK).gz, $(SONIC_JESSIE_DOCKERS_FOR_INSTALLERS)))
else
	DOCKER_IMAGES := $(filter-out $(SONIC_JESSIE_DOCKERS), $(SONIC_DOCKER_IMAGES))
	DOCKER_DBG_IMAGES := $(filter-out $(SONIC_JESSIE_DBG_DOCKERS), $(SONIC_DOCKER_DBG_IMAGES))
endif

# Targets for building docker images
$(addprefix $(TARGET_PATH)/, $(DOCKER_IMAGES)) : $(TARGET_PATH)/%.gz : .platform docker-start \
		$$(addprefix $(DEBS_PATH)/,$$($$*.gz_DEPENDS)) \
		$$(addprefix $(FILES_PATH)/,$$($$*.gz_FILES)) \
		$$(addprefix $(PYTHON_DEBS_PATH)/,$$($$*.gz_PYTHON_DEBS)) \
		$$(addprefix $(PYTHON_WHEELS_PATH)/,$$($$*.gz_PYTHON_WHEELS)) \
		$$(addsuffix -load,$$(addprefix $(TARGET_PATH)/,$$($$*.gz_LOAD_DOCKERS))) \
		$$($$*.gz_PATH)/Dockerfile.j2
	$(HEADER)
	# Apply series of patches if exist
	if [ -f $($*.gz_PATH).patch/series ]; then pushd $($*.gz_PATH) && QUILT_PATCHES=../$(notdir $($*.gz_PATH)).patch quilt push -a; popd; fi
	mkdir -p $($*.gz_PATH)/debs $(LOG)
	mkdir -p $($*.gz_PATH)/files $(LOG)
	mkdir -p $($*.gz_PATH)/python-debs $(LOG)
	mkdir -p $($*.gz_PATH)/python-wheels $(LOG)
	sudo mount --bind $(DEBS_PATH) $($*.gz_PATH)/debs $(LOG)
	sudo mount --bind $(FILES_PATH) $($*.gz_PATH)/files $(LOG)
	sudo mount --bind $(PYTHON_DEBS_PATH) $($*.gz_PATH)/python-debs $(LOG)
	sudo mount --bind $(PYTHON_WHEELS_PATH) $($*.gz_PATH)/python-wheels $(LOG)
	# Export variables for j2. Use path for unique variable names, e.g. docker_orchagent_debs
	$(eval export $(subst -,_,$(notdir $($*.gz_PATH)))_debs=$(shell printf "$(subst $(SPACE),\n,$(call expand,$($*.gz_DEPENDS),RDEPENDS))\n" | awk '!a[$$0]++'))
	$(eval export $(subst -,_,$(notdir $($*.gz_PATH)))_pydebs=$(shell printf "$(subst $(SPACE),\n,$(call expand,$($*.gz_PYTHON_DEBS)))\n" | awk '!a[$$0]++'))
	$(eval export $(subst -,_,$(notdir $($*.gz_PATH)))_whls=$(shell printf "$(subst $(SPACE),\n,$(call expand,$($*.gz_PYTHON_WHEELS)))\n" | awk '!a[$$0]++'))
	$(eval export $(subst -,_,$(notdir $($*.gz_PATH)))_dbgs=$(shell printf "$(subst $(SPACE),\n,$(call expand,$($*.gz_DBG_PACKAGES)))\n" | awk '!a[$$0]++'))
	$(eval export $(subst -,_,$(notdir $($*.gz_PATH)))_load_image=$(shell printf "$(call docker-load-image-get,$(subst $(SPACE),\n,$(patsubst %.gz,%,$(call expand,$($*.gz_LOAD_DOCKERS)))))\n" | awk '!a[$$0]++'))
	j2 $($*.gz_PATH)/Dockerfile.j2 > $($*.gz_PATH)/Dockerfile
	docker info $(LOG)
	docker build --squash --no-cache \
		--build-arg http_proxy=$(HTTP_PROXY) \
		--build-arg https_proxy=$(HTTPS_PROXY) \
		--build-arg user=$(USER) \
		--build-arg uid=$(UID) \
		--build-arg guid=$(GUID) \
		--build-arg docker_container_name=$($*.gz_CONTAINER_NAME) \
		--build-arg frr_user_uid=$(FRR_USER_UID) \
		--build-arg frr_user_gid=$(FRR_USER_GID) \
		--label Tag=$(SONIC_GET_VERSION) \
		-t $(DOCKER_IMAGE_REF) $($*.gz_PATH) $(LOG)
	$(call docker-image-save,$*,$@)
	# Clean up
	if [ -f $($*.gz_PATH).patch/series ]; then pushd $($*.gz_PATH) && quilt pop -a -f; popd; fi
	$(FOOTER)

SONIC_TARGET_LIST += $(addprefix $(TARGET_PATH)/, $(DOCKER_IMAGES))

# Targets for building docker debug images
$(addprefix $(TARGET_PATH)/, $(DOCKER_DBG_IMAGES)) : $(TARGET_PATH)/%-$(DBG_IMAGE_MARK).gz : .platform docker-start \
		$$(addprefix $(DEBS_PATH)/,$$($$*.gz_DBG_DEPENDS)) \
		$$(addsuffix -load,$$(addprefix $(TARGET_PATH)/,$$*.gz))
	$(HEADER)
	mkdir -p $($*.gz_PATH)/debs $(LOG)
	sudo mount --bind $(DEBS_PATH) $($*.gz_PATH)/debs $(LOG)
	# Export variables for j2. Use path for unique variable names, e.g. docker_orchagent_debs
	$(eval export $(subst -,_,$(notdir $($*.gz_PATH)))_dbg_debs=$(shell printf "$(subst $(SPACE),\n,$(call expand,$($*.gz_DBG_DEPENDS),RDEPENDS))\n" | awk '!a[$$0]++'))
	$(eval export $(subst -,_,$(notdir $($*.gz_PATH)))_image_dbgs=$(shell printf "$(subst $(SPACE),\n,$(call expand,$($*.gz_DBG_IMAGE_PACKAGES)))\n" | awk '!a[$$0]++'))
	./build_debug_docker_j2.sh $(DOCKER_IMAGE_REF) $(subst -,_,$(notdir $($*.gz_PATH)))_dbg_debs $(subst -,_,$(notdir $($*.gz_PATH)))_image_dbgs > $($*.gz_PATH)/Dockerfile-dbg.j2
	j2 $($*.gz_PATH)/Dockerfile-dbg.j2 > $($*.gz_PATH)/Dockerfile-dbg
	docker info $(LOG)
	docker build \
		$(if $($*.gz_DBG_DEPENDS), --squash --no-cache, --no-cache) \
		--build-arg http_proxy=$(HTTP_PROXY) \
		--build-arg https_proxy=$(HTTPS_PROXY) \
		--build-arg docker_container_name=$($*.gz_CONTAINER_NAME) \
		--label Tag=$(SONIC_GET_VERSION) \
		--file $($*.gz_PATH)/Dockerfile-dbg \
		-t $(DOCKER_DBG_IMAGE_REF) $($*.gz_PATH) $(LOG)
	$(call docker-image-save,$*-$(DBG_IMAGE_MARK),$@)
	# Clean up
	@echo "Removing docker image $(DOCKER_IMAGE_REF)" $(LOG)
	docker rmi -f $(DOCKER_IMAGE_REF) &> /dev/null || true
	if [ -f $($*.gz_PATH).patch/series ]; then pushd $($*.gz_PATH) && quilt pop -a -f; popd; fi
	$(FOOTER)

SONIC_TARGET_LIST += $(addprefix $(TARGET_PATH)/, $(DOCKER_DBG_IMAGES))

DOCKER_LOAD_TARGETS = $(addsuffix -load,$(addprefix $(TARGET_PATH)/, \
		      $(SONIC_SIMPLE_DOCKER_IMAGES) \
		      $(DOCKER_IMAGES)))

$(DOCKER_LOAD_TARGETS) : $(TARGET_PATH)/%.gz-load : .platform docker-start $$(TARGET_PATH)/$$*.gz
	$(HEADER)
	$(call docker-image-load,$*)
	$(FOOTER)

.PHONY: $(TARGET_PATH)/fsroot_prep
$(TARGET_PATH)/fsroot_prep:
	$(HEADER)
	USERNAME="$(USERNAME)" \
	PASSWORD="$(PASSWORD)" \
	NUMPROCS="$(SONIC_CONFIG_MAKE_JOBS)" \
		./build_debian.sh 1 $(LOG)
	$(FOOTER)

###############################################################################
## Installers
###############################################################################

# targets for building installers with base image
$(addprefix $(TARGET_PATH)/, $(SONIC_INSTALLERS)) : $(TARGET_PATH)/% : \
        .platform \
        onie-image.conf \
        build_debian.sh \
        build_image.sh \
        $$(addsuffix -install,$$(addprefix $(STRETCH_DEBS_PATH)/,$$($$*_DEPENDS))) \
        $$(addprefix $(STRETCH_DEBS_PATH)/,$$($$*_INSTALLS)) \
        $$(addprefix $(STRETCH_DEBS_PATH)/,$$($$*_LAZY_INSTALLS)) \
        $(addprefix $(STRETCH_DEBS_PATH)/,$(INITRAMFS_TOOLS) \
                $(LINUX_KERNEL) \
                $(SONIC_DEVICE_DATA) \
                $(PYTHON_CLICK) \
                $(IFUPDOWN2) \
                $(HWDIAG) \
                $(NTP) \
                $(LIBPAM_TACPLUS) \
                $(LIBNSS_TACPLUS)) \
        $$(addprefix $(TARGET_PATH)/,$$($$*_DOCKERS)) \
        $$(addprefix $(FILES_PATH)/,$$($$*_FILES)) \
	$(if $(findstring y,$(ENABLE_ZTP)),$(addprefix $(DEBS_PATH)/,$(SONIC_ZTP))) \
        $(addprefix $(STRETCH_FILES_PATH)/,$(IXGBE_DRIVER)) \
        $(addprefix $(PYTHON_DEBS_PATH)/,$(SONIC_UTILS)) \
        $(addprefix $(PYTHON_WHEELS_PATH)/,$(SONIC_CONFIG_ENGINE)) \
        $(addprefix $(PYTHON_WHEELS_PATH)/,$(SONIC_PLATFORM_COMMON_PY2)) \
        $(addprefix $(PYTHON_WHEELS_PATH)/,$(REDIS_DUMP_LOAD_PY2)) \
        | $(TARGET_PATH)/fsroot_prep
	$(HEADER)
	# Pass initramfs and linux kernel explicitly. They are used for all platforms
	export debs_path="$(STRETCH_DEBS_PATH)"
	export files_path="$(FILES_PATH)"
	export python_debs_path="$(PYTHON_DEBS_PATH)" 
	export initramfs_tools="$(STRETCH_DEBS_PATH)/$(INITRAMFS_TOOLS)"
	export linux_kernel="$(STRETCH_DEBS_PATH)/$(LINUX_KERNEL)"
	export onie_recovery_image="$(FILES_PATH)/$(ONIE_RECOVERY_IMAGE)"
	export kversion="$(KVERSION)"
	export image_type="$($*_IMAGE_TYPE)"
	export sonicadmin_user="$(USERNAME)"
	export sonic_asic_platform="$(CONFIGURED_PLATFORM)"
	export enable_organization_extensions="$(ENABLE_ORGANIZATION_EXTENSIONS)"
	export enable_dhcp_graph_service="$(ENABLE_DHCP_GRAPH_SERVICE)"
	export sonic_debugging_on="$(SONIC_DEBUGGING_ON)"
	export enable_ztp="$(ENABLE_ZTP)"
	export enable_pde="$(ENABLE_PDE)"
	export shutdown_bgp_on_start="$(SHUTDOWN_BGP_ON_START)"
	export enable_pfcwd_on_start="$(ENABLE_PFCWD_ON_START)"
	export installer_debs="$(addprefix $(STRETCH_DEBS_PATH)/,$($*_INSTALLS))"
	export lazy_installer_debs="$(foreach deb, $($*_LAZY_INSTALLS),$(foreach device, $($(deb)_PLATFORM),$(addprefix $(device)@, $(STRETCH_DEBS_PATH)/$(deb))))"
	export installer_images="$(addprefix $(TARGET_PATH)/,$($*_DOCKERS))"
	export config_engine_wheel_path="$(addprefix $(PYTHON_WHEELS_PATH)/,$(SONIC_CONFIG_ENGINE))"
	export swsssdk_py2_wheel_path="$(addprefix $(PYTHON_WHEELS_PATH)/,$(SWSSSDK_PY2))"
	export platform_common_py2_wheel_path="$(addprefix $(PYTHON_WHEELS_PATH)/,$(SONIC_PLATFORM_COMMON_PY2))"
	export redis_dump_load_py2_wheel_path="$(addprefix $(PYTHON_WHEELS_PATH)/,$(REDIS_DUMP_LOAD_PY2))"

	$(foreach docker, $($*_DOCKERS),\
		export docker_image="$(docker)"
		export docker_image_name="$(basename $(docker))"
		export docker_container_name="$($(docker:-dbg.gz=.gz)_CONTAINER_NAME)"
		$(eval $(docker:-dbg.gz=.gz)_RUN_OPT += $($(docker:-dbg.gz=.gz)_$($*_IMAGE_TYPE)_RUN_OPT))
		export docker_image_run_opt="$($(docker:-dbg.gz=.gz)_RUN_OPT)"
		j2 files/build_templates/docker_image_ctl.j2 > $($(docker:-dbg.gz=.gz)_CONTAINER_NAME).sh
		if [ -f files/build_templates/$($(docker:-dbg.gz=.gz)_CONTAINER_NAME).service.j2 ]; then
			j2 files/build_templates/$($(docker:-dbg.gz=.gz)_CONTAINER_NAME).service.j2 > $($(docker:-dbg.gz=.gz)_CONTAINER_NAME).service
		fi
		chmod +x $($(docker:-dbg.gz=.gz)_CONTAINER_NAME).sh
	)

	export installer_start_scripts="$(foreach docker, $($*_DOCKERS),$(addsuffix .sh, $($(docker:-dbg.gz=.gz)_CONTAINER_NAME)))"
	export installer_services="$(foreach docker, $($*_DOCKERS),$(addsuffix .service, $($(docker:-dbg.gz=.gz)_CONTAINER_NAME)))"
	export installer_extra_files="$(foreach docker, $($*_DOCKERS), $(foreach file, $($(docker:-dbg.gz=.gz)_BASE_IMAGE_FILES), $($(docker:-dbg.gz=.gz)_PATH)/base_image_files/$(file)))"
	export installer_extra_files+="$(foreach docker, $($*_DOCKERS), $(foreach file, $($(docker:-dbg.gz=.gz)_DERIVED_BASE_IMAGE_FILES), $(file)))"

	j2 -f env files/initramfs-tools/union-mount.j2 onie-image.conf > files/initramfs-tools/union-mount
	j2 -f env files/initramfs-tools/arista-convertfs.j2 onie-image.conf > files/initramfs-tools/arista-convertfs

	j2 files/build_templates/updategraph.service.j2 > updategraph.service
	j2 files/dhcp/dhclient.conf.j2 > files/dhcp/dhclient.conf

	$(if $($*_DOCKERS),
		j2 files/build_templates/sonic_debian_extension.j2 > sonic_debian_extension.sh
		chmod +x sonic_debian_extension.sh,
	)

	BUILD_TARGET="$@" \
	USERNAME="$(USERNAME)" \
	PASSWORD="$(PASSWORD)" \
	NUMPROCS="$(SONIC_CONFIG_MAKE_JOBS)" \
		./build_debian.sh 2 $(LOG)

	USERNAME="$(USERNAME)" \
	PASSWORD="$(PASSWORD)" \
	TARGET_MACHINE=$($*_MACHINE) \
	IMAGE_TYPE=$($*_IMAGE_TYPE) \
	BUILD_TARGET="$@" \
		./build_image.sh $(LOG)

	$(foreach docker, $($*_DOCKERS), \
		rm -f $($(docker:-dbg.gz=.gz)_CONTAINER_NAME).sh
		rm -f $($(docker:-dbg.gz=.gz)_CONTAINER_NAME).service
	)

	$(if $($*_DOCKERS),
		rm sonic_debian_extension.sh,
	)

	chmod a+x $@
	$(FOOTER)

SONIC_TARGET_LIST += $(addprefix $(TARGET_PATH)/, $(SONIC_INSTALLERS))

###############################################################################
## Clean targets
###############################################################################

SONIC_CLEAN_DEBS = $(addsuffix -clean,$(addprefix $(DEBS_PATH)/, \
		   $(SONIC_ONLINE_DEBS) \
		   $(SONIC_COPY_DEBS) \
		   $(SONIC_MAKE_DEBS) \
		   $(SONIC_DPKG_DEBS) \
		   $(SONIC_DERIVED_DEBS) \
		   $(SONIC_EXTRA_DEBS)))

SONIC_CLEAN_FILES = $(addsuffix -clean,$(addprefix $(FILES_PATH)/, \
		   $(SONIC_ONLINE_FILES) \
		   $(SONIC_COPY_FILES) \
		   $(SONIC_MAKE_FILES)))

$(SONIC_CLEAN_DEBS) : $(DEBS_PATH)/%-clean : .platform $$(addsuffix -clean,$$(addprefix $(DEBS_PATH)/,$$($$*_MAIN_DEB))) 
	@# remove derived or extra targets if main one is removed, because we treat them
	@# as part of one package
	@rm -f $(addprefix $(DEBS_PATH)/, $* $($*_DERIVED_DEBS) $($*_EXTRA_DEBS)) $($*_DEP_FLAGS_FILE) 

$(SONIC_CLEAN_FILES) : $(FILES_PATH)/%-clean : .platform
	@rm -f $(FILES_PATH)/$*

SONIC_CLEAN_TARGETS += $(addsuffix -clean,$(addprefix $(TARGET_PATH)/, \
		       $(SONIC_DOCKER_IMAGES) \
		       $(SONIC_DOCKER_DBG_IMAGES) \
		       $(SONIC_SIMPLE_DOCKER_IMAGES) \
		       $(SONIC_INSTALLERS)))
$(SONIC_CLEAN_TARGETS) : $(TARGET_PATH)/%-clean : .platform
	@rm -f $(TARGET_PATH)/$*

SONIC_CLEAN_STDEB_DEBS = $(addsuffix -clean,$(addprefix $(PYTHON_DEBS_PATH)/, \
		     $(SONIC_PYTHON_STDEB_DEBS)))
$(SONIC_CLEAN_STDEB_DEBS) : $(PYTHON_DEBS_PATH)/%-clean : .platform
	@rm -f $(PYTHON_DEBS_PATH)/$*

SONIC_CLEAN_WHEELS = $(addsuffix -clean,$(addprefix $(PYTHON_WHEELS_PATH)/, \
		     $(SONIC_PYTHON_WHEELS)))
$(SONIC_CLEAN_WHEELS) : $(PYTHON_WHEELS_PATH)/%-clean : .platform
	@rm -f $(PYTHON_WHEELS_PATH)/$*

clean-logs : .platform
	@rm -f $(TARGET_PATH)/*.log $(DEBS_PATH)/*.log $(FILES_PATH)/*.log $(PYTHON_DEBS_PATH)/*.log $(PYTHON_WHEELS_PATH)/*.log

clean : .platform clean-logs $$(SONIC_CLEAN_DEBS) $$(SONIC_CLEAN_FILES) $$(SONIC_CLEAN_TARGETS) $$(SONIC_CLEAN_STDEB_DEBS) $$(SONIC_CLEAN_WHEELS)

###############################################################################
## all
###############################################################################

all : .platform $$(addprefix $(TARGET_PATH)/,$$(SONIC_ALL))

stretch : $$(addprefix $(DEBS_PATH)/,$$(SONIC_STRETCH_DEBS)) \
          $$(addprefix $(FILES_PATH)/,$$(SONIC_STRETCH_FILES)) \
          $$(addprefix $(TARGET_PATH)/,$$(SONIC_STRETCH_DOCKERS_FOR_INSTALLERS)) \
          $$(addprefix $(TARGET_PATH)/,$$(SONIC_STRETCH_DBG_DOCKERS_FOR_INSTALLERS))

jessie : $$(addprefix $(TARGET_PATH)/,$$(SONIC_JESSIE_DOCKERS_FOR_INSTALLERS))

###############################################################################
## Standard targets
###############################################################################

.PHONY : $(SONIC_CLEAN_DEBS) $(SONIC_CLEAN_FILES) $(SONIC_CLEAN_TARGETS) $(SONIC_CLEAN_STDEB_DEBS) $(SONIC_CLEAN_WHEELS) $(SONIC_PHONY_TARGETS) clean distclean configure noop

.INTERMEDIATE : $(SONIC_INSTALL_TARGETS) $(SONIC_INSTALL_WHEELS) $(DOCKER_LOAD_TARGETS) docker-start .platform
