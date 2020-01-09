# SONiC make file

NOJESSIE = 1

%::
	@echo "+++ --- Making $@ --- +++"
ifeq ($(NOJESSIE), 0)
	EXTRA_JESSIE_TARGETS=$(notdir $@) ${MAKE} -k -f Makefile.work jessie
endif
	BLDENV=stretch ${MAKE} -k -f Makefile.work NOJESSIE=1 PLATFORM=broadcom $@
	-BLDENV=stretch ${MAKE} -k -f Makefile.work docker-cleanup

jessie: configure
stretch: configure
target/sonic-broadcom.bin:  stretch

jessie:
	@echo "+++ Making $@ +++"
ifeq ($(NOJESSIE), 0)
	${MAKE} -k -f Makefile.work jessie
endif

LOCAL_SAI_DEBS_PATH=target/files/stretch/private_sonic-binaries
ENGOPS_SETUP=git merge --abort 2>/dev/null; git checkout engops_broadcom_sonic_share 2>/dev/null && git checkout broadcom_sonic_share && git merge --no-commit engops_broadcom_sonic_share; git checkout broadcom_sonic_share || git checkout master
init:
	@echo "+++ Making $@ +++"
	-BLDENV=stretch ${MAKE} -k -f Makefile.work NOJESSIE=1 PLATFORM=broadcom $@
	rm -rf ${LOCAL_SAI_DEBS_PATH}
	mkdir -p `dirname ${LOCAL_SAI_DEBS_PATH}`
	git clone --depth=1 git@github.com:project-arlo/private_sonic-binaries.git ${LOCAL_SAI_DEBS_PATH}
	#${ENGOPS_SETUP}
	git submodule foreach --recursive "${ENGOPS_SETUP}"

clean reset configure docker-cleanup showtag sonic-slave-build sonic-slave-bash:
	@echo "+++ Making $@ +++"
	BLDENV=stretch ${MAKE} -k -f Makefile.work NOJESSIE=1 PLATFORM=broadcom $@
