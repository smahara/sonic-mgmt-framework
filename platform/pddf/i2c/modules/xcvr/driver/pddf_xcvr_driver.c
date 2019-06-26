/*
 * Copyright 2019 Broadcom. All rights reserved.
 * The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries.
 *
 * A pddf kernel module for Optic component
 */

#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/jiffies.h>
#include <linux/i2c.h>
#include <linux/hwmon.h>
#include <linux/hwmon-sysfs.h>
#include <linux/err.h>
#include <linux/mutex.h>
#include <linux/sysfs.h>
#include <linux/slab.h>
#include <linux/delay.h>
#include <linux/dmi.h>
#include <linux/kobject.h>
#include "pddf_client_defs.h"
#include "pddf_xcvr_defs.h"
#include "pddf_xcvr_api.h"

enum xcvr_sysfs_attributes {
    XCVR_PRESENT,
	XCVR_RESET,
	XCVR_INTR_STATUS,
	XCVR_LPMODE,
	XCVR_RXLOS,
	XCVR_TXDISABLE,
	XCVR_TXFAULT,
	XCVR_ATTR_MAX
};

/* sysfs attributes  
 */
static SENSOR_DEVICE_ATTR(xcvr_present,	S_IWUSR|S_IRUGO, get_module_presence,	NULL, XCVR_PRESENT);
static SENSOR_DEVICE_ATTR(xcvr_reset,	S_IWUSR|S_IRUGO, get_module_reset, set_module_reset, XCVR_RESET);
static SENSOR_DEVICE_ATTR(xcvr_intr_status,	S_IWUSR|S_IRUGO, get_module_intr_status, NULL, XCVR_INTR_STATUS);
static SENSOR_DEVICE_ATTR(xcvr_lpmode,	S_IWUSR|S_IRUGO, get_module_lpmode, set_module_lpmode, XCVR_LPMODE);
static SENSOR_DEVICE_ATTR(xcvr_rxlos,	S_IWUSR|S_IRUGO, get_module_rxlos, NULL, XCVR_RXLOS);
static SENSOR_DEVICE_ATTR(xcvr_txdisable,	S_IWUSR|S_IRUGO, get_module_txdisable, set_module_txdisable, XCVR_TXDISABLE);
static SENSOR_DEVICE_ATTR(xcvr_txfault,	S_IWUSR|S_IRUGO, get_module_txfault, NULL, XCVR_TXFAULT);

/* List of all the xcvr attribute structures 
 * to get name, use sensor_dev_attr_<>.dev_attr.attr.name
 * to get the id, use sensor_dev_attr_<>.dev_attr.index 
 */
static struct sensor_device_attribute *xcvr_attr_list[MAX_XCVR_ATTRS] = {
	&sensor_dev_attr_xcvr_present,
	&sensor_dev_attr_xcvr_reset,
	&sensor_dev_attr_xcvr_intr_status,
	&sensor_dev_attr_xcvr_lpmode,
	&sensor_dev_attr_xcvr_rxlos,
	&sensor_dev_attr_xcvr_txdisable,
	&sensor_dev_attr_xcvr_txfault,
};

static struct attribute *xcvr_attributes[MAX_XCVR_ATTRS] = {NULL};

static const struct attribute_group xcvr_group = {
    .attrs = xcvr_attributes,
};

static int xcvr_probe(struct i2c_client *client,
            const struct i2c_device_id *dev_id)
{
    struct xcvr_data *data;
    int status =0;
	int i,j,num;
	XCVR_PDATA *xcvr_platform_data;
	XCVR_ATTR *attr_data;

	/* Calling pre_xcvr_probe */
	/*status = pre_xcvr_probe(client, dev_id);*/

	pddf_dbg(KERN_ERR "GENERIC_XCVR_DRIVER Probe called... \n");

	if (client == NULL) {
		pddf_dbg("NULL Client.. \n");
		goto exit;
	}

    if (!i2c_check_functionality(client->adapter, I2C_FUNC_SMBUS_I2C_BLOCK)) {
        status = -EIO;
        goto exit;
    }

    data = kzalloc(sizeof(struct xcvr_data), GFP_KERNEL);
    if (!data) {
        status = -ENOMEM;
        goto exit;
    }

    i2c_set_clientdata(client, data);
    data->valid = 0;
	/*data->index = dev_id->driver_data;*/

    dev_info(&client->dev, "chip found\n");

	/* Take control of the platform data */
	xcvr_platform_data = (XCVR_PDATA *)(client->dev.platform_data);
	num = xcvr_platform_data->len;
	data->index = xcvr_platform_data->idx - 1;
	mutex_init(&data->update_lock);

	/* Add supported attr in the 'attributes' list */
	for (i=0; i<num; i++)
	{
		struct attribute *aptr = NULL;
		attr_data = xcvr_platform_data->xcvr_attrs + i;
		for(j=0;j<XCVR_ATTR_MAX;j++)
		{
			aptr = &xcvr_attr_list[j]->dev_attr.attr;
			/*pddf_dbg(KERN_ERR "i:%d, j:%d, aptr->name: %s, attr_data->name: %s\n", i, j, aptr->name, attr_data->aname);*/

			if (strncmp(aptr->name, attr_data->aname, strlen(attr_data->aname))==0)
				break;
		}
		
		if (j<XCVR_ATTR_MAX)
			xcvr_attributes[i] = &xcvr_attr_list[j]->dev_attr.attr;

	}
	xcvr_attributes[i] = NULL;

    /* Register sysfs hooks */
    status = sysfs_create_group(&client->dev.kobj, &xcvr_group);
    if (status) {
        goto exit_free;
    }

	data->xdev = hwmon_device_register(&client->dev);
	if (IS_ERR(data->xdev)) {
		status = PTR_ERR(data->xdev);
		goto exit_remove;
	}

    dev_info(&client->dev, "%s: xcvr '%s'\n",
         dev_name(data->xdev), client->name);
    
    return 0;

	/* Calling post_xcvr_probe */
	/*status = post_xcvr_probe(client, dev_id);*/

exit_remove:
    sysfs_remove_group(&client->dev.kobj, &xcvr_group);
exit_free:
    kfree(data);
exit:
    
    return status;
}

static int xcvr_remove(struct i2c_client *client)
{
    struct xcvr_data *data = i2c_get_clientdata(client);
	XCVR_PDATA *platdata = (XCVR_PDATA *)client->dev.platform_data;
	XCVR_ATTR *platdata_sub = platdata->xcvr_attrs;

	hwmon_device_unregister(data->xdev);
	sysfs_remove_group(&client->dev.kobj, &xcvr_group);
    kfree(data);

	if (platdata_sub) {
		pddf_dbg(KERN_DEBUG "%s: Freeing platform subdata\n", __FUNCTION__);
		kfree(platdata_sub);
	}
	if (platdata) {
		pddf_dbg(KERN_DEBUG "%s: Freeing platform data\n", __FUNCTION__);
		kfree(platdata);
	}
    
    return 0;
}

enum xcvr_intf 
{
	XCVR_CTRL_INTF,
};

static const struct i2c_device_id xcvr_ids[] = {
	{ "pddf_xcvr", XCVR_CTRL_INTF },
	{}
};

MODULE_DEVICE_TABLE(i2c, xcvr_ids);

static struct i2c_driver xcvr_driver = {
    /*.class        = I2C_CLASS_HWMON,*/
    .driver = {
        .name     = "xcvr",
		.owner    = THIS_MODULE,
    },
    .probe        = xcvr_probe,
    .remove       = xcvr_remove,
    .id_table     = xcvr_ids,
};


/*int __init xcvr_init(void)*/
int xcvr_init(void)
{
	int ret = 0;

	pddf_dbg(KERN_ERR "GENERIC_XCVR_DRIVER.. init Invoked..\n");
    ret = i2c_add_driver(&xcvr_driver);
	
	return ret;
}
EXPORT_SYMBOL(xcvr_init);

void __exit xcvr_exit(void)
{
	pddf_dbg("GENERIC_XCVR_DRIVER.. exit\n");
    i2c_del_driver(&xcvr_driver);
}
EXPORT_SYMBOL(xcvr_exit);

MODULE_AUTHOR("Broadcom");
MODULE_DESCRIPTION("Driver for transceiver operations");
MODULE_LICENSE("GPL");

/*#ifdef SONIC*/
module_init(xcvr_init);
module_exit(xcvr_exit);
/*#endif*/
