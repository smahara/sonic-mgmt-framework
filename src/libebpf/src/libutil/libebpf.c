/*
 * Copyright 2019 Broadcom. All rights reserved. 
 * The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.
 */

#include <stdio.h>
#include <assert.h>
#include <linux/bpf.h>
#include <string.h>
#include <stdlib.h>
#include <stddef.h>
#include <errno.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <linux/if_ether.h>
#include <stddef.h>
#include <linux/if_link.h>
#include <linux/bpf.h>
#include <linux/filter.h>
#include <linux/if_link.h>
#include <linux/rtnetlink.h>
#include <stdbool.h>
#include <unistd.h>
#include <stdint.h>
#include <linux/if_arp.h>
#include <linux/bpf_common.h>
#include "ebpf/libebpf.h"
#include "ebpf/libbpf.h"
#include "ebpf/bpf_load.h"



__attribute__ ((visibility("default"))) int attach_ebpf_filter(int nl_fd, char *filename)
{
	char filectl[128]="";
	sprintf(filectl, "%s.enable",filename);
	if( access( filectl, F_OK ) == -1 )
	{
		printf("Filter %s is disabled\n", filename);
		return 0;
	}

	if (load_bpf_file(filename)) {
		printf("%s", bpf_log_buf);
		return -1;
	}

	assert(setsockopt(nl_fd, SOL_SOCKET, SO_ATTACH_BPF, prog_fd, sizeof(prog_fd[0])) == 0);
	return 0;
}

#ifdef MAIN
int main(int argc, char *argv[])
{
	printf("\n");
	return 0;
}
#endif




