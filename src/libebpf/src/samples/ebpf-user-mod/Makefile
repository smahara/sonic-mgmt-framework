export KVERSION ?= 4.9.0-11-2-amd64
KBUILD_PATH ?= /lib/modules/$(KVERSION)/build
KBUILD_SRC_PATH ?= /lib/modules/$(KVERSION)/source
LLC ?= llc-6.0
CLANG ?= clang-6.0
LLVM_OBJDUMP ?= llvm-objdump-6.0
INC_FLAGS = -nostdinc -isystem $(shell $(CLANG) -print-file-name=include)
EXTRA_CFLAGS ?= -O2 -g -Wall -emit-llvm

# In case up-to-date headers are not installed locally in /usr/include,
# use source build.

LINUXINCLUDE =	-I../../libutil/ \
		-I$(KBUILD_PATH)/include \
		-I$(KBUILD_PATH)/arch/x86/include \
		-I$(KBUILD_SRC_PATH)/include \
		-I$(KBUILD_SRC_PATH)/arch/x86/include/ \
		-I$(KBUILD_PATH)/include/uapi \
		-I$(KBUILD_SRC_PATH)/include/uapi \
		-I$(KBUILD_SRC_PATH)/arch/x86/include/uapi/ \
		-I$(KBUILD_PATH)/include/generated/uapi \
		-I$(KBUILD_PATH)/arch/x86/include/uapi \
		-I$(KBUILD_PATH)/arch/x86/include/generated/ \
		-I$(KBUILD_PATH)/arch/x86/include/generated/uapi \


KERNELOBJS =	ebpftest.o 
KERNELOBJDUMPS = $(KERNELOBJS:%.o=%.objdump)

prefix ?= $(DESTDIR)
INSTALLPATH = $(prefix)/lib/bpf

all: $(KERNELOBJS)

debug: DEBUG_FLAGS = -DBPFDEBUG
debug: all
	
.PHONY: clean

clean:
	rm -f $(KERNELOBJS) $(KERNELOBJDUMPS)

distclean: clean

test:
	

install_PROGRAM = install
install_DIR = install -dv

$(KERNELOBJS):  %.o:%.c
	$(CLANG) $(INC_FLAGS) \
                -D__KERNEL__ -D__ASM_SYSREG_H \
		$(DEBUG_FLAGS) \
		-Wno-unused-value -Wno-pointer-sign \
                -Wno-compare-distinct-pointer-types \
                -Wno-gnu-variable-sized-type-not-at-end \
                -Wno-address-of-packed-member -Wno-tautological-compare \
                -Wno-unknown-warning-option \
		-I../include $(LINUXINCLUDE) \
		$(EXTRA_CFLAGS) -c $< -o -| $(LLC) -march=bpf -filetype=obj -o $@


$(KERNELOBJDUMPS): %.objdump:%.o
	$(LLVM_OBJDUMP) -S -no-show-raw-insn $< > $@

objdump: $(KERNELOBJDUMPS)
	
install: $(KERNELOBJS)
	$(install_DIR) -d $(INSTALLPATH) ; \
	$(install_PROGRAM) $^ -t $(INSTALLPATH)


uninstall: $(KERNELOBJS)
	rm -rf $(INSTALLPATH)
