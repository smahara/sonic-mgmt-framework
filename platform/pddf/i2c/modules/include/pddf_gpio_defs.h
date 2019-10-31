/*
 * Copyright 2019 Broadcom. All rights reserved.
 * The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries.
 *
 * Description:
 *  Platform GPIO defines/structures header file
 */

#ifndef __PAL_GPIO_DEFS_H__
#define __PAL_GPIO_DEFS_H__

#include <linux/platform_data/pca953x.h>
/* GPIO CLIENT DATA*/
typedef struct GPIO_DATA
{
    int gpio_base;      // base bus number of the gpio pins
}GPIO_DATA;

#endif //__PAL_GPIO_DEFS_H__
