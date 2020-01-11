.ONESHELL:
SHELL = /bin/bash
.SHELLFLAGS += -e

MAIN_TARGET = isc-dhcp-relay_$(ISC_DHCP_VERSION)_$(CONFIGURED_ARCH).deb
#DERIVED_TARGETS = isc-dhcp-relay-dbgsym_$(ISC_DHCP_VERSION)_$(CONFIGURED_ARCH).deb

# For non-optimizing builds, use -O1 optimization instead of the default -O0.
ifneq (,$(findstring noopt,$(DEB_BUILD_OPTIONS)))
optlevel = -O1
endif


$(addprefix $(DEST)/, $(MAIN_TARGET)): $(DEST)/% :
	# Remove any stale files
	rm -rf ./isc-dhcp

	# Clone isc-dhcp repo
	git clone https://salsa.debian.org/dhcp-team/isc-dhcp.git
	pushd ./isc-dhcp

	# Reset HEAD to the commit of the proper tag
	# NOTE: Using "git checkout <tag_name>" here detaches our HEAD,
	# which stg doesn't like, so we use this method instead
	git reset --hard debian/$(ISC_DHCP_VERSION)

	# Apply patches
	stg init
	stg import -s ../patch/series

	# Build source and Debian packages
	DEB_CFLAGS_APPEND="$(optlevel)" dpkg-buildpackage -rfakeroot -b -us -uc -j$(SONIC_CONFIG_MAKE_JOBS)
	popd

	# Move the newly-built .deb packages to the destination directory
	#mv $(DERIVED_TARGETS) $* $(DEST)/
	mv $* $(DEST)/

#$(addprefix $(DEST)/, $(DERIVED_TARGETS)): $(DEST)/% : $(DEST)/$(MAIN_TARGET)
