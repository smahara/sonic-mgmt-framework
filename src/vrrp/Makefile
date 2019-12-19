.ONESHELL:
SHELL = /bin/bash
.SHELLFLAGS += -e

MAIN_TARGET = $(VRRP_PKG)

$(addprefix $(DEST)/, $(MAIN_TARGET)): $(DEST)/% :
	# Remove any stale files
	rm -rf ./keepalived

	# Obtain debian packaging
	git clone https://github.com/formorer/pkg-keepalived.git keepalived 
	pushd ./keepalived

	# Apply patches
	stg init
	stg import -s ../patch/series

	# Build source and Debian packages
	dpkg-buildpackage -rfakeroot -b -us -uc -j$(SONIC_CONFIG_MAKE_JOBS)
	ls -lrt 
	popd

	mv keepalived_1.3.9-1_amd64.deb $*	
	dpkg -c $*	
	
	# Move the newly-built .deb packages to the destination directory
	mv $* $(DEST)/

$(addprefix $(DEST)/, $(DERIVED_TARGETS)): $(DEST)/% : $(DEST)/$(MAIN_TARGET)


