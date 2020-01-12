# SONiC ${MAKE} file

NOJESSIE ?= 0

%::
	@echo "+++ --- Making $@ --- +++"
ifeq ($(NOJESSIE), 0)
	EXTRA_JESSIE_TARGETS=$(notdir $@) ${MAKE} -f Makefile.work jessie
endif
	BLDENV=stretch ${MAKE} -f Makefile.work $@
	BLDENV=stretch ${MAKE} -f Makefile.work docker-cleanup

jessie:
	@echo "+++ Making $@ +++"
ifeq ($(NOJESSIE), 0)
	${MAKE} -f Makefile.work jessie
endif

clean reset init configure docker-cleanup showtag sonic-slave-build sonic-slave-bash :
	@echo "+++ Making $@ +++"
ifeq ($(NOJESSIE), 0)
	${MAKE} -f Makefile.work $@
endif
	BLDENV=stretch ${MAKE} -f Makefile.work $@
