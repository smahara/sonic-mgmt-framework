
KBUILD_PATH ?= /lib/modules/$(KVERSION)/build
KBUILD_SRC_PATH ?= /lib/modules/$(KVERSION)/source


INCLUDES = -I$(KBUILD_SRC_PATH)/include/uapi -I$(KBUILD_SRC_PATH)/include
INCLUDES += -I $(top_srcdir)/utils

nobase_include_HEADERS = ebpf/bpf_load.h ebpf/bpf_helpers.h ebpf/libebpf.h ebpf/libbpf.h 
lib_LIBRARIES = libebpf.a

if DEBUG
DBGFLAGS = -ggdb -DDEBUG
else
DBGFLAGS = -g -DNDEBUG
endif

libebpf_a_CFLAGS = -Wno-unused-variable -D__EXPORTED_HEADERS__ $(COV_CFLAGS) $(ASAN_CFLAGS)
libebpf_a_SOURCES =  bpf_load.c libbpf.c libebpf.c
