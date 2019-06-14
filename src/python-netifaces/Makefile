.ONESHELL:
SHELL = /bin/bash
.SHELLFLAGS += -e

PYTHON_NETIFACES_VERSION_ = $(subst .,_,$(PYTHON_NETIFACES_VERSION))

MAIN_TARGET = $(PYTHON_NETIFACES)

$(addprefix $(DEST)/, $(MAIN_TARGET)): $(DEST)/% :
	# Remove any stale files
	rm -rf ./netifaces-release_$(PYTHON_NETIFACES_VERSION_) ./release_$(PYTHON_NETIFACES_VERSION_).tar.gz

	# Get netifaces release archive
	wget --no-check-certificate https://github.com/al45tair/netifaces/archive/release_$(PYTHON_NETIFACES_VERSION_).tar.gz
	tar -z -f release_$(PYTHON_NETIFACES_VERSION_).tar.gz -x
	pushd ./netifaces-release_$(PYTHON_NETIFACES_VERSION_)

	git init
	git add -f *
	git commit -m "unmodified netifaces source"

	# Apply patches
	stg init
	stg import -s ../patch/series

	# Build source and Debian packages
	python$(PYTHON_NETIFACES_PY_VERSION) setup.py --command-packages=stdeb.command bdist_deb

	# Move the newly-built deb to the destination directory
	mv deb_dist/$* $(DEST)/

	popd
