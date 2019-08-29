# sonic-fand (SONiC fan daemon) Debian package

SONIC_FAND = python-sonic-fand_1.0-1_all.deb
$(SONIC_FAND)_SRC_PATH = $(SRC_PATH)/sonic-platform-daemons/sonic-fand
SONIC_PYTHON_STDEB_DEBS += $(SONIC_FAND)
