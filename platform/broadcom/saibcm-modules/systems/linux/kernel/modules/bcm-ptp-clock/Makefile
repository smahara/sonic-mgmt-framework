# -*- Makefile -*-
# $Id: Makefile,v 1.3 2012/07/17 07:39:51 mlarsen Exp $
# $Copyright: (c) 2005 Broadcom Corp.
# All Rights Reserved.$
#
LOCALDIR = systems/linux/kernel/modules/bcm-ptp-clock

include ${SDK}/make/Make.config

LIBS = $(LIBDIR)/libkern.a

ifeq ($(kernel_version),2_4)
MODULE = $(LIBDIR)/linux-bcm-ptp-clock.o
else
KERNEL_MODULE_DIR = kernel_module

THIS_MOD_NAME := linux-bcm-ptp-clock
MODULE = $(LIBDIR)/$(THIS_MOD_NAME).o
KMODULE = $(LIBDIR)/$(THIS_MOD_NAME).ko

build: $(MODULE) $(KMODULE)
endif

HOST_BASED_PHC := 1

#KBUILD_EXTRA_SYMBOLS := ${BLDDIR}/../../../../bde/linux/kernel/kernel_module/Module.symvers
KBUILD_EXTRA_SYMBOLS += ${BLDDIR}/../bcm-knet/kernel_module/Module.symvers

# BCM PTP Clock Device

$(MODULE): $(BLDDIR)/.tree $(BOBJS) $(LIBS)
	$(LD) $(MODULE_LDFLAGS) -r -d $(BOBJS) $(LIBS) -o $@
ifneq ($(kernel_version),2_4)
$(KMODULE): $(MODULE)
	rm -fr $(BLDDIR)/$(KERNEL_MODULE_DIR)
	mkdir $(BLDDIR)/$(KERNEL_MODULE_DIR)
	cp ${SDK}/make/Makefile.linux-kmodule $(BLDDIR)/$(KERNEL_MODULE_DIR)/Makefile
	cat ${KBUILD_EXTRA_SYMBOLS} > $(BLDDIR)/$(KERNEL_MODULE_DIR)/Module.symvers
	MOD_NAME=$(THIS_MOD_NAME) $(MAKE) -C $(BLDDIR)/$(KERNEL_MODULE_DIR) $(THIS_MOD_NAME).ko
endif

# Make.depend is before clean:: so that Make.depend's clean:: runs first.

include ${SDK}/make/Make.depend

clean::
	$(RM) $(BLDDIR)/version.c $(BLDDIR)/version.o
	$(RM) $(BOBJS) $(MODULE)

ifneq ($(kernel_version),2_4)
.PHONY: build
endif
