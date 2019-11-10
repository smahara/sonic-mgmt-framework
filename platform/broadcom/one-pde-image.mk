# sonic broadcom one image installer

SONIC_ONE_PDE_IMAGE = sonic-broadcom-pde.bin
$(SONIC_ONE_PDE_IMAGE)_MACHINE = broadcom
$(SONIC_ONE_PDE_IMAGE)_IMAGE_TYPE = onie
$(SONIC_ONE_PDE_IMAGE)_INSTALLS += $(BRCM_OPENNSL_KERNEL)
$(SONIC_ONE_PDE_IMAGE)_LAZY_INSTALLS += $(DELL_S6000_PLATFORM_MODULE) \
                               $(DELL_Z9264F_PLATFORM_MODULE) \
                               $(DELL_Z9100_PLATFORM_MODULE) \
                               $(DELL_S6100_PLATFORM_MODULE) \
                               $(INGRASYS_S8900_54XC_PLATFORM_MODULE) \
                               $(INGRASYS_S8900_64XC_PLATFORM_MODULE) \
                               $(INGRASYS_S9100_PLATFORM_MODULE) \
                               $(INGRASYS_S8810_32Q_PLATFORM_MODULE) \
                               $(INGRASYS_S9200_64X_PLATFORM_MODULE) \
                               $(ACCTON_AS7712_32X_PLATFORM_MODULE) \
                               $(ACCTON_AS5712_54X_PLATFORM_MODULE) \
                               $(ACCTON_AS7816_64X_PLATFORM_MODULE) \
                               $(ACCTON_AS7716_32X_PLATFORM_MODULE) \
                               $(ACCTON_AS7312_54X_PLATFORM_MODULE) \
                               $(ACCTON_AS7326_56X_PLATFORM_MODULE) \
                               $(ACCTON_AS7716_32XB_PLATFORM_MODULE) \
                               $(ACCTON_AS6712_32X_PLATFORM_MODULE) \
                               $(ACCTON_AS7726_32X_PLATFORM_MODULE) \
                               $(ACCTON_AS4630_54PE_PLATFORM_MODULE) \
                               $(ACCTON_MINIPACK_PLATFORM_MODULE) \
                               $(ACCTON_AS5812_54X_PLATFORM_MODULE) \
                               $(INVENTEC_D7032Q28B_PLATFORM_MODULE) \
                               $(INVENTEC_D7054Q28B_PLATFORM_MODULE) \
                               $(INVENTEC_D7264Q28B_PLATFORM_MODULE) \
                               $(CEL_DX010_PLATFORM_MODULE) \
                               $(CEL_HALIBURTON_PLATFORM_MODULE) \
                               $(DELTA_AG9032V1_PLATFORM_MODULE) \
                               $(DELTA_AG9064_PLATFORM_MODULE) \
                               $(DELTA_AG5648_PLATFORM_MODULE) \
                               $(DELTA_ET6248BRB_PLATFORM_MODULE) \
                               $(QUANTA_IX1B_32X_PLATFORM_MODULE) \
                               $(QUANTA_IX8_56X_PLATFORM_MODULE) \
                               $(MITAC_LY1200_32X_PLATFORM_MODULE) \
                               $(ALPHANETWORKS_SNH60A0_320FV2_PLATFORM_MODULE) \
                               $(ALPHANETWORKS_SNH60B0_640F_PLATFORM_MODULE) \
                               $(BRCM_XLR_GTS_PLATFORM_MODULE)
$(SONIC_ONE_PDE_IMAGE)_DOCKERS += $(DOCKER_PDE) $(DOCKER_PLATFORM_MONITOR) $(DOCKER_DATABASE)
SONIC_INSTALLERS += $(SONIC_ONE_PDE_IMAGE)
