/*
 * Copyright 2019 Broadcom. All rights reserved.
 * The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries.
 *
 * Description of various APIs related to FAN component
 */

#include <linux/module.h>
#include <linux/jiffies.h>
#include <linux/i2c.h>
#include <linux/hwmon.h>
#include <linux/hwmon-sysfs.h>
#include <linux/err.h>
#include <linux/mutex.h>
#include <linux/sysfs.h>
#include <linux/slab.h>
#include <linux/dmi.h>
#include "pddf_fan_defs.h"
#include "pddf_fan_driver.h"

/*#define FAN_DEBUG*/
#ifdef FAN_DEBUG
#define fan_dbg(...) printk(__VA_ARGS__)
#else
#define fan_dbg(...)
#endif

int fan_update_attr(struct device *dev, struct fan_attr_info *info, FAN_DATA_ATTR *udata)
{
    struct i2c_client *client = to_i2c_client(dev);
	FAN_SYSFS_ATTR_DATA *sysfs_attr_data = NULL;


    mutex_lock(&info->update_lock);

    if (time_after(jiffies, info->last_updated + HZ + HZ / 2) || !info->valid) 
	{
        dev_dbg(&client->dev, "Starting pddf_fan update\n");
        info->valid = 0;

		sysfs_attr_data = udata->access_data;
		if (sysfs_attr_data->do_access != NULL)
		{
			(sysfs_attr_data->do_access)(client, udata, info);
		}

		
        info->last_updated = jiffies;
        info->valid = 1;
    }

    mutex_unlock(&info->update_lock);

    return 0;
}


ssize_t fan_show_present_default(struct device *dev, struct device_attribute *da, char *buf)
{
    struct sensor_device_attribute *attr = to_sensor_dev_attr(da);
    struct i2c_client *client = to_i2c_client(dev);
    struct fan_data *data = i2c_get_clientdata(client);
    FAN_PDATA *pdata = (FAN_PDATA *)(client->dev.platform_data);
    FAN_DATA_ATTR *usr_data = NULL;
    struct fan_attr_info *attr_info = NULL;
    int i, status ;


    for (i=0;i<data->num_attr;i++)
    {
		if (strcmp(data->attr_info[i].name, attr->dev_attr.attr.name) == 0 && strcmp(pdata->fan_attrs[i].aname, attr->dev_attr.attr.name) == 0)
        {
            attr_info = &data->attr_info[i];
            usr_data = &pdata->fan_attrs[i];
        }
    }

    if (attr_info==NULL || usr_data==NULL)
        printk(KERN_ERR "%s is not supported attribute for this client\n", usr_data->aname);

    fan_update_attr(dev, attr_info, usr_data);

    status = attr_info->val.intval;
    return sprintf(buf, "%d\n", status);
}

int sonic_i2c_get_fan_present_default(void *client, FAN_DATA_ATTR *udata, void *info)
{
    int status = 0;
    int val = 0;
    struct fan_attr_info *painfo = (struct fan_attr_info *)info;

	val = i2c_smbus_read_byte_data((struct i2c_client *)client, udata->offset);
	painfo->val.intval = ((val & udata->mask) == udata->cmpval);

	/*fan_dbg(KERN_ERR "presence: val:0x%x, mask:0x%x, present_value = 0x%x\n", val, udata->mask, painfo->val.intval);*/

    return status;
}


ssize_t fan_show_rpm_default(struct device *dev, struct device_attribute *da, char *buf)
{
    struct sensor_device_attribute *attr = to_sensor_dev_attr(da);
    struct i2c_client *client = to_i2c_client(dev);
    struct fan_data *data = i2c_get_clientdata(client);
    FAN_PDATA *pdata = (FAN_PDATA *)(client->dev.platform_data);
    FAN_DATA_ATTR *usr_data = NULL;
    struct fan_attr_info *attr_info = NULL;
    int i, status ;


    for (i=0;i<data->num_attr;i++)
    {
		if (strcmp(data->attr_info[i].name, attr->dev_attr.attr.name) == 0 && strcmp(pdata->fan_attrs[i].aname, attr->dev_attr.attr.name) == 0)
        {
            attr_info = &data->attr_info[i];
            usr_data = &pdata->fan_attrs[i];
        }
    }

    if (attr_info==NULL || usr_data==NULL)
        printk(KERN_ERR "%s is not supported attribute for this client\n", usr_data->aname);

    fan_update_attr(dev, attr_info, usr_data);

    status = attr_info->val.intval;
    return sprintf(buf, "%d\n", status);
}

int sonic_i2c_get_fan_rpm_default(void *client, FAN_DATA_ATTR *udata, void *info)
{
    int status = 0;
	uint32_t val = 0;
    struct fan_attr_info *painfo = (struct fan_attr_info *)info;

	if (udata->len == 1)
	{
		val = i2c_smbus_read_byte_data((struct i2c_client *)client, udata->offset);
	}
	else if (udata->len ==2)
	{
		val = i2c_smbus_read_word_swapped((struct i2c_client *)client, udata->offset);
		
	}

	if (udata->is_divisor)
		painfo->val.intval = udata->mult / (val >> 3);
	else
		painfo->val.intval = udata->mult * val;

	return status;
}


ssize_t fan_show_direction_default(struct device *dev, struct device_attribute *da, char *buf)
{
    struct sensor_device_attribute *attr = to_sensor_dev_attr(da);
    struct i2c_client *client = to_i2c_client(dev);
    struct fan_data *data = i2c_get_clientdata(client);
    FAN_PDATA *pdata = (FAN_PDATA *)(client->dev.platform_data);
    FAN_DATA_ATTR *usr_data = NULL;
    struct fan_attr_info *attr_info = NULL;
    int i, status ;


    for (i=0;i<data->num_attr;i++)
    {
		if (strcmp(data->attr_info[i].name, attr->dev_attr.attr.name) == 0 && strcmp(pdata->fan_attrs[i].aname, attr->dev_attr.attr.name) == 0)
        {
            attr_info = &data->attr_info[i];
            usr_data = &pdata->fan_attrs[i];
        }
    }

    if (attr_info==NULL || usr_data==NULL)
        printk(KERN_ERR "%s is not supported attribute for this client\n", usr_data->aname);

    fan_update_attr(dev, attr_info, usr_data);

    status = attr_info->val.intval;
    return sprintf(buf, "%d\n", status);
}

int sonic_i2c_get_fan_direction_default(void *client, FAN_DATA_ATTR *udata, void *info)
{
    int status = 0;
	uint32_t val = 0;
    struct fan_attr_info *painfo = (struct fan_attr_info *)info;

	val = i2c_smbus_read_byte_data((struct i2c_client *)client, udata->offset);
	painfo->val.intval = ((val & udata->mask) == udata->cmpval);
	/*fan_dbg(KERN_ERR "direction: val:0x%x, mask:0x%x, final val:0x%x\n", val, udata->mask, painfo->val.intval);*/

    return status;
}

ssize_t fan_show_pwm_default(struct device *dev, struct device_attribute *da, char *buf)
{
    struct sensor_device_attribute *attr = to_sensor_dev_attr(da);
    struct i2c_client *client = to_i2c_client(dev);
    struct fan_data *data = i2c_get_clientdata(client);
    FAN_PDATA *pdata = (FAN_PDATA *)(client->dev.platform_data);
    FAN_DATA_ATTR *usr_data = NULL;
    struct fan_attr_info *attr_info = NULL;
    int i, status ;


    for (i=0;i<data->num_attr;i++)
    {
		if (strcmp(data->attr_info[i].name, attr->dev_attr.attr.name) == 0 && strcmp(pdata->fan_attrs[i].aname, attr->dev_attr.attr.name) == 0)
        {
            attr_info = &data->attr_info[i];
            usr_data = &pdata->fan_attrs[i];
        }
    }

    if (attr_info==NULL || usr_data==NULL)
        printk(KERN_ERR "%s is not supported attribute for this client\n", usr_data->aname);

    fan_update_attr(dev, attr_info, usr_data);

    status = attr_info->val.intval;
    return sprintf(buf, "%d\n", status);
}

extern ssize_t fan_set_pwm_default(struct device *dev, struct device_attribute *da, const char *buf, size_t count)
{
	struct sensor_device_attribute *attr = to_sensor_dev_attr(da);
	struct i2c_client *client = to_i2c_client(dev);
	struct fan_data *data = i2c_get_clientdata(client);
	FAN_PDATA *pdata = (FAN_PDATA *)(client->dev.platform_data);
    FAN_DATA_ATTR *usr_data = NULL;
    struct fan_attr_info *attr_info = NULL;
    int i, ret ;
	uint32_t val;

	for (i=0;i<data->num_attr;i++)
    {
		if (strcmp(data->attr_info[i].name, attr->dev_attr.attr.name) == 0 && strcmp(pdata->fan_attrs[i].aname, attr->dev_attr.attr.name) == 0)
        {
            attr_info = &data->attr_info[i];
            usr_data = &pdata->fan_attrs[i];
        }
    }

    if (attr_info==NULL || usr_data==NULL) {
		printk(KERN_ERR "fan_pwm is not supported attribute for this client\n");
	}


	ret = kstrtoint(buf, 10, &val);
	if (ret)
	{
	  return ret;
	}

	/*fan_dbg(KERN_ERR "%s: pwm to be set is %d\n", __FUNCTION__, val);*/
	val = val & usr_data->mask;

	if (val > 255)
	{
	  return -EINVAL;
	}

	mutex_lock(&attr_info->update_lock);
	if (usr_data->len == 1)
		i2c_smbus_write_byte_data(client, usr_data->offset, val);
	else if (usr_data->len == 2)
	{
		uint8_t val_lsb = val & 0xFF;
		uint8_t val_hsb = (val >> 8) & 0xFF;
		/* TODO: Check this logic for LE and BE */
		i2c_smbus_write_byte_data(client, usr_data->offset, val_lsb);
		i2c_smbus_write_byte_data(client, usr_data->offset+1, val_hsb);
	}
	else
	{
		printk(KERN_DEBUG "%s: pwm should be of len 1/2 bytes. Not setting the pwm as the length is %d\n", __FUNCTION__, usr_data->len);
	}
	mutex_unlock(&attr_info->update_lock);
	
	return count;
}


int sonic_i2c_get_fan_pwm_default(void *client, FAN_DATA_ATTR *udata, void *info)
{
    int status = 0;
	uint32_t val = 0;
    struct fan_attr_info *painfo = (struct fan_attr_info *)info;

	if (udata->len == 1)
	{
		val = i2c_smbus_read_byte_data((struct i2c_client *)client, udata->offset);
	}
	else if (udata->len ==2)
	{
		val = i2c_smbus_read_word_swapped((struct i2c_client *)client, udata->offset);
		
	}

	val = val & udata->mask;
	painfo->val.intval = val;
    return status;
}



