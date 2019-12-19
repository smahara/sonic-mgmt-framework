SHELL = /bin/bash
.ONESHELL:
.SHELLFLAGS += -e

export EBPF_VERSION ?= 1.0.0
DEST ?= /sonic/target/debs/stretch/

MAIN_TARGET := libebpf_$(EBPF_VERSION)_amd64.deb

$(addprefix $(DEST)/, $(MAIN_TARGET)): $(DEST)/% :

	pushd src
	[ ! -f ./autogen.sh ] || ./autogen.sh 
	dpkg-buildpackage -us -uc -b -j$(SONIC_CONFIG_MAKE_JOBS)
	popd

	mv $* $(DEST)/
