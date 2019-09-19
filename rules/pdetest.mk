# libpdetest package

LIBPDETEST = libpdetest_1.0.0_amd64.deb
$(LIBPDETEST)_SRC_PATH = $(SRC_PATH)/sonic-platform-pde/pde-test-host2/
$(LIBPDETEST)_DEPENDS += $(BRCM_SAI) $(SWIG)

$(LIBSPDETEST)_RDEPENDS += $(BRCM_SAI)

SONIC_DPKG_DEBS += $(LIBPDETEST)

LIBPDETEST_DEV = libpdetest-dev_1.0.0_amd64.deb
$(eval $(call add_derived_package,$(LIBPDETEST),$(LIBPDETEST_DEV)))

PYTHON_PDETEST = python-pdetest_1.0.0_amd64.deb
$(eval $(call add_derived_package,$(LIBPDETEST),$(PYTHON_PDETEST)))

LIBPDETEST_DBG = libpdetest-dbg_1.0.0_amd64.deb
$(LIBPDETEST_DBG)_DEPENDS += $(LIBPDETEST)
$(LIBPDETEST_DBG)_RDEPENDS += $(LIBPDETEST)
$(eval $(call add_derived_package,$(LIBPDETEST),$(LIBPDETEST_DBG)))
