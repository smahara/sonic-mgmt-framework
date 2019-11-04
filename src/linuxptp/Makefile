SHELL = /bin/bash
.ONESHELL:
.SHELLFLAGS += -e

#http://deb.debian.org/debian/pool/main/l/linuxptp/linuxptp_1.8-1.dsc
#http://deb.debian.org/debian/pool/main/l/linuxptp/linuxptp_1.8.orig.tar.gz
#http://deb.debian.org/debian/pool/main/l/linuxptp/linuxptp_1.8-1.debian.tar.xz

MAIN_TARGET = linuxptp_$(LINUXPTP_VERSION_FULL)_amd64.deb

# $(addprefix $(DEST)/, $(MAIN_TARGET)): $(DEST)/% :
	# rm -rf linuxptp-$(LINUXPTP_VERSION_MAJOR)
	# wget -O linuxptp_$(LINUXPTP_VERSION_MAJOR).orig.tar.gz -N "http://deb.debian.org/debian/pool/main/l/linuxptp/linuxptp_$(LINUXPTP_VERSION_MAJOR).orig.tar.gz"
	# wget -O linuxptp_$(LINUXPTP_VERSION_FULL).dsc -N "http://deb.debian.org/debian/pool/main/l/linuxptp/linuxptp_$(LINUXPTP_VERSION_FULL).dsc"
	# wget -O linuxptp_$(LINUXPTP_VERSION_FULL).debian.tar.xz -N "http://deb.debian.org/debian/pool/main/l/linuxptp/linuxptp_$(LINUXPTP_VERSION_FULL).debian.tar.xz"
	# dpkg-source -x linuxptp_$(LINUXPTP_VERSION_FULL).dsc

	# pushd linuxptp-$(LINUXPTP_VERSION_MAJOR)
	# dpkg-buildpackage -us -uc -b -j$(SONIC_CONFIG_MAKE_JOBS)
	# popd

	# mv $* $(DEST)/

$(addprefix $(DEST)/, $(MAIN_TARGET)): $(DEST)/% :
	rm -rf linuxptp-$(LINUXPTP_VERSION_MAJOR)
	wget -O linuxptp_$(LINUXPTP_VERSION_MAJOR).orig.tar.gz -N "http://artifactory.force10networks.com/sonic-debs/linuxptp/$(LINUXPTP_VERSION_MAJOR).orig.tar.gz"
	wget -O linuxptp_$(LINUXPTP_VERSION_FULL).dsc -N "http://artifactory.force10networks.com/sonic-debs/linuxptp/$(LINUXPTP_VERSION_FULL).dsc"
	wget -O linuxptp_$(LINUXPTP_VERSION_FULL).debian.tar.xz -N "http://artifactory.force10networks.com/sonic-debs/linuxptp/$(LINUXPTP_VERSION_FULL).debian.tar.xz"
	dpkg-source -x linuxptp_$(LINUXPTP_VERSION_FULL).dsc

	pushd linuxptp-$(LINUXPTP_VERSION_MAJOR)
	dpkg-buildpackage -us -uc -b -j$(SONIC_CONFIG_MAKE_JOBS)
	popd

	mv $* $(DEST)/
