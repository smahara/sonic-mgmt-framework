# SONiC make file

NOJESSIE ?= 0

%::
	@echo "+++ --- Making $@ --- +++"
ifeq ($(NOJESSIE), 0)
	EXTRA_JESSIE_TARGETS=$(notdir $@) make -f Makefile.work jessie
endif
	BLDENV=stretch make -f Makefile.work $@
	BLDENV=stretch make -f Makefile.work docker-cleanup

jessie:
	@echo "+++ Making $@ +++"
ifeq ($(NOJESSIE), 0)
	make -f Makefile.work jessie
endif

ENGOPS_SETUP=git merge --abort 2>/dev/null; git checkout engops_dell_sonic 2>/dev/null && git checkout dell_sonic && git merge --no-commit engops_dell_sonic; git checkout dell_sonic || git checkout master
init:
	@echo "+++ Making $@ +++"
	-BLDENV=stretch ${MAKE} -k -f Makefile.work NOJESSIE=1 PLATFORM=broadcom $@
	#${ENGOPS_SETUP}
	git submodule foreach --recursive "${ENGOPS_SETUP}"

clean reset configure docker-cleanup showtag sonic-slave-build sonic-slave-bash:
	@echo "+++ Making $@ +++"
ifeq ($(NOJESSIE), 0)
	make -f Makefile.work $@
endif
	BLDENV=stretch make -f Makefile.work $@
