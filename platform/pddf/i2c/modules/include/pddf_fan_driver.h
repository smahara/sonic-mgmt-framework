/*
 * Copyright 2019 Broadcom. All rights reserved.
 * The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries.
 *
 * Description
 *  FAN driver related data structures
 */
#ifndef __PDDF_FAN_DRIVER_H__
#define __PDDF_FAN_DRIVER_H__

/* Each client has this additional data */
struct fan_attr_info {
	char				name[ATTR_NAME_LEN];
    struct mutex		update_lock;
    char				valid;           /* != 0 if registers are valid */
    unsigned long		last_updated;    /* In jiffies */
	union {
        char strval[STR_ATTR_SIZE];
        int  intval;
        u16  shortval;
        u8   charval;
    }val;
};

struct fan_data {
    struct device			*hwmon_dev;
	int						num_attr;
	struct attribute		*fan_attribute_list[MAX_FAN_ATTRS];
	struct attribute_group	fan_attribute_group;
	struct fan_attr_info	attr_info[MAX_FAN_ATTRS];
};

#endif //__PDDF_FAN_DRIVER_H__
