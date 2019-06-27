/*
 * Copyright 2019 Broadcom. All rights reserved.
 * The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries.
 *
 *  Description of various APIs related to PSU component
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
#include "pddf_psu_defs.h"
#include "pddf_psu_driver.h"


/*#define PSU_DEBUG*/
#ifdef PSU_DEBUG
#define psu_dbg(...) printk(__VA_ARGS__)
#else
#define psu_dbg(...)
#endif


int psu_update_attr(struct device *dev, struct psu_attr_info *data, PSU_DATA_ATTR *udata)
{
    struct i2c_client *client = to_i2c_client(dev);
	PSU_SYSFS_ATTR_DATA *sysfs_attr_data;

    mutex_lock(&data->update_lock);

    if (time_after(jiffies, data->last_updated + HZ + HZ / 2) || !data->valid) 
	{
        dev_dbg(&client->dev, "Starting update for %s\n", data->name);

		/*psu_dbg(KERN_ERR "%s: UPDATING %s ATTR FOR PSU,#### \n", __FUNCTION__, udata->aname );*/
		sysfs_attr_data = udata->access_data;

		if (sysfs_attr_data->do_access != NULL)
		{
			/*psu_dbg(KERN_ERR "Calling access_fptr(0x%x) for %s attr \n", sysfs_attr_data->do_access, udata->aname);*/
			(sysfs_attr_data->do_access)(client, udata, data);
		}
        data->last_updated = jiffies;
        data->valid = 1;
    }

    mutex_unlock(&data->update_lock);
	return 0;
}

ssize_t show_psu_present_default(struct device *dev, struct device_attribute *da, char *buf)
{
    struct sensor_device_attribute *attr = to_sensor_dev_attr(da);
    struct i2c_client *client = to_i2c_client(dev);
    struct psu_data *data = i2c_get_clientdata(client);
    PSU_PDATA *pdata = (PSU_PDATA *)(client->dev.platform_data);
    PSU_DATA_ATTR *usr_data = NULL;
    struct psu_attr_info *sysfs_attr_info = NULL;
    int i, status ;


    for (i=0;i<data->num_attr;i++)
    {
        if (strcmp(data->attr_info[i].name, attr->dev_attr.attr.name) == 0 && strcmp(pdata->psu_attrs[i].aname, attr->dev_attr.attr.name) == 0 )
        {
			/*psu_dbg(KERN_ERR "### ATTR NAME: %s \n", data->attr_info[i].name);*/
			sysfs_attr_info = &data->attr_info[i];
            usr_data = &pdata->psu_attrs[i];
        }
    }

    if (sysfs_attr_info==NULL || usr_data==NULL)
        printk(KERN_ERR "psu_present is not supported attribute for this client\n");

    psu_update_attr(dev, sysfs_attr_info, usr_data);

    status = sysfs_attr_info->val.intval;
    return sprintf(buf, "%d\n", status);
}


int sonic_i2c_get_psu_present_default(void *client, PSU_DATA_ATTR *adata, void *data)
{
	int status = 0;
    int val = 0;
	struct psu_attr_info *padata = (struct psu_attr_info *)data;

	
	if (strncmp(adata->devtype, "cpld", strlen("cpld")) == 0)
	{
		val = board_i2c_cpld_read(adata->devaddr , adata->offset);
		padata->val.intval =  ((val & adata->mask) == adata->cmpval);
		psu_dbg(KERN_ERR "status_value = 0x%x\n", padata->val.intval);
	}

	return status;
}


ssize_t show_psu_power_good_default(struct device *dev, struct device_attribute *da, char *buf)
{
    struct sensor_device_attribute *attr = to_sensor_dev_attr(da);
    struct i2c_client *client = to_i2c_client(dev);
    struct psu_data *data = i2c_get_clientdata(client);
    PSU_PDATA *pdata = (PSU_PDATA *)(client->dev.platform_data);
    PSU_DATA_ATTR *usr_data = NULL;
    struct psu_attr_info *sysfs_attr_info = NULL;
    int i, status;


    for (i=0;i<data->num_attr;i++)
    {
        if (strcmp(data->attr_info[i].name, attr->dev_attr.attr.name) == 0 &&
                strcmp(pdata->psu_attrs[i].aname, attr->dev_attr.attr.name) == 0 )
        {
            sysfs_attr_info = &data->attr_info[i];
            usr_data = &pdata->psu_attrs[i];
        }
    }

    if (sysfs_attr_info==NULL || usr_data==NULL)
        printk(KERN_ERR "psu_present is not supported attribute for this client\n");

    psu_update_attr(dev, sysfs_attr_info, usr_data);

    status = sysfs_attr_info->val.intval;
    return sprintf(buf, "%d\n", status);
}


int sonic_i2c_get_psu_power_good_default(void *client, PSU_DATA_ATTR *adata, void *data)
{
	int status = 0;
    int val = 0;
	struct psu_attr_info *padata = (struct psu_attr_info *)data;
	
	if (strncmp(adata->devtype, "cpld", strlen("cpld")) == 0)
	{
		val = board_i2c_cpld_read(adata->devaddr , adata->offset);
		padata->val.intval =  ((val & adata->mask) == adata->cmpval);
		psu_dbg(KERN_ERR "status_value = 0x%x\n", padata->val.intval);
	}

	return status;
}


ssize_t show_psu_model_name_default(struct device *dev, struct device_attribute *da, char *buf)
{
    struct sensor_device_attribute *attr = to_sensor_dev_attr(da);
    struct i2c_client *client = to_i2c_client(dev);
    struct psu_data *data = i2c_get_clientdata(client);
    PSU_PDATA *pdata = (PSU_PDATA *)(client->dev.platform_data);
    PSU_DATA_ATTR *usr_data = NULL;
    struct psu_attr_info *sysfs_attr_info = NULL;
    int i;


    for (i=0;i<data->num_attr;i++)
    {
        if (strcmp(data->attr_info[i].name, attr->dev_attr.attr.name) == 0 &&
                strcmp(pdata->psu_attrs[i].aname, attr->dev_attr.attr.name) == 0 )
        {
            sysfs_attr_info = &data->attr_info[i];
            usr_data = &pdata->psu_attrs[i];
        }
    }

    if (sysfs_attr_info==NULL || usr_data==NULL)
        printk(KERN_ERR "psu_model_name is not supported attribute for this client\n");

    psu_update_attr(dev, sysfs_attr_info, usr_data);

    return sprintf(buf, "%s\n", sysfs_attr_info->val.strval);
}

int sonic_i2c_get_psu_model_name_default(void *client, PSU_DATA_ATTR *adata, void *data)
{
	int status = 0, retry = 10;
	struct psu_attr_info *padata = (struct psu_attr_info *)data;
	uint8_t offset = (uint8_t)adata->offset;
	int data_len = adata->len;

	/*printk(KERN_ERR "###INSIDE GET MODEL NAME. client:0x%x, offset:0x%x, data_len:%d\n", client, offset, data_len);*/
	while (retry)
	{
		status = i2c_smbus_read_i2c_block_data((struct i2c_client *)client, offset, data_len-1, padata->val.strval);
		if (unlikely(status<0))
		{
			msleep(60);
			retry--;
			continue;
		}
		break;
	}

	if (status < 0) 
	{
		padata->val.strval[0] = '\0';
        dev_dbg(&((struct i2c_client *)client)->dev, "unable to read model name from (0x%x)\n", ((struct i2c_client *)client)->addr);
    }
    else 
	{
		padata->val.strval[data_len-1] = '\0';
    }

	psu_dbg(KERN_ERR "status = %d, model_name : %s\n", status, padata->val.strval);
    return 0;
}


ssize_t show_psu_mfr_id_default(struct device *dev, struct device_attribute *da, char *buf)
{
    struct sensor_device_attribute *attr = to_sensor_dev_attr(da);
    struct i2c_client *client = to_i2c_client(dev);
    struct psu_data *data = i2c_get_clientdata(client);
    PSU_PDATA *pdata = (PSU_PDATA *)(client->dev.platform_data);
    PSU_DATA_ATTR *usr_data = NULL;
    struct psu_attr_info *sysfs_attr_info = NULL;
    int i;


    for (i=0;i<data->num_attr;i++)
    {
        if (strcmp(data->attr_info[i].name, attr->dev_attr.attr.name) == 0 &&
                strcmp(pdata->psu_attrs[i].aname, attr->dev_attr.attr.name) == 0 )
        {
            sysfs_attr_info = &data->attr_info[i];
            usr_data = &pdata->psu_attrs[i];
        }
    }

    if (sysfs_attr_info==NULL || usr_data==NULL)
        printk(KERN_ERR "psu_mfr_id is not supported attribute for this client\n");

    psu_update_attr(dev, sysfs_attr_info, usr_data);

    return sprintf(buf, "%s\n", sysfs_attr_info->val.strval);
}

int sonic_i2c_get_psu_mfr_id_default(void *client, PSU_DATA_ATTR *adata, void *data)
{

	int status = 0, retry = 10;
	struct psu_attr_info *padata = (struct psu_attr_info *)data;
	uint8_t offset = (uint8_t)adata->offset;
	int data_len = adata->len;

	/*psu_dbg(KERN_ERR "###INSIDE GET MFR ID. client:0x%x, offset:0x%x, data_len:%d\n", client, offset, data_len);*/
	while (retry)
	{
		status = i2c_smbus_read_i2c_block_data((struct i2c_client *)client, offset, data_len-1, padata->val.strval);
		if (unlikely(status<0))
		{
			msleep(60);
			retry--;
			continue;
		}
		break;
	}

	if (status < 0) 
	{
		padata->val.strval[0] = '\0';
        dev_dbg(&((struct i2c_client *)client)->dev, "unable to read mfr_id from (0x%x)\n", ((struct i2c_client *)client)->addr);
    }
    else 
	{
		padata->val.strval[data_len-1] = '\0';
    }

	psu_dbg(KERN_ERR "status = %d, mfr_id : %s\n", status, padata->val.strval);
    return 0;
}


ssize_t show_psu_serial_num_default(struct device *dev, struct device_attribute *da, char *buf)
{
    struct sensor_device_attribute *attr = to_sensor_dev_attr(da);
    struct i2c_client *client = to_i2c_client(dev);
    struct psu_data *data = i2c_get_clientdata(client);
    PSU_PDATA *pdata = (PSU_PDATA *)(client->dev.platform_data);
    PSU_DATA_ATTR *usr_data = NULL;
    struct psu_attr_info *sysfs_attr_info = NULL;
    int i;


    for (i=0;i<data->num_attr;i++)
    {
        if (strcmp(data->attr_info[i].name, attr->dev_attr.attr.name) == 0 &&
                strcmp(pdata->psu_attrs[i].aname, attr->dev_attr.attr.name) == 0 )
        {
            sysfs_attr_info = &data->attr_info[i];
            usr_data = &pdata->psu_attrs[i];
        }
    }

    if (sysfs_attr_info==NULL || usr_data==NULL)
        printk(KERN_ERR "psu_serial_num is not supported attribute for this client\n");

    psu_update_attr(dev, sysfs_attr_info, usr_data);

    return sprintf(buf, "%s\n", sysfs_attr_info->val.strval);
}


int sonic_i2c_get_psu_serial_num_default(void *client, PSU_DATA_ATTR *adata, void *data)
{

	int status = 0, retry = 10;
	struct psu_attr_info *padata = (struct psu_attr_info *)data;
	uint8_t offset = (uint8_t)adata->offset;
	int data_len = adata->len;

	/*psu_dbg(KERN_ERR "###INSIDE GET SERIAL_NUM. client:0x%x, offset:0x%x, data_len:%d\n", client, offset, data_len);*/
	while (retry)
	{
		status = i2c_smbus_read_i2c_block_data((struct i2c_client *)client, offset, data_len-1, padata->val.strval);
		if (unlikely(status<0))
		{
			msleep(60);
			retry--;
			continue;
		}
		break;
	}

	if (status < 0) 
	{
		padata->val.strval[0] = '\0';
        dev_dbg(&((struct i2c_client *)client)->dev, "unable to read serial num from (0x%x)\n", ((struct i2c_client *)client)->addr);
    }
    else 
	{
		padata->val.strval[data_len-1] = '\0';
    }

	psu_dbg(KERN_ERR "status = %d, serial_num : %s\n", status, padata->val.strval);
    return 0;
}


ssize_t show_psu_fan_dir_default(struct device *dev, struct device_attribute *da, char *buf)
{
    struct sensor_device_attribute *attr = to_sensor_dev_attr(da);
    struct i2c_client *client = to_i2c_client(dev);
    struct psu_data *data = i2c_get_clientdata(client);
    PSU_PDATA *pdata = (PSU_PDATA *)(client->dev.platform_data);
    PSU_DATA_ATTR *usr_data = NULL;
    struct psu_attr_info *sysfs_attr_info = NULL;
    int i;


    for (i=0;i<data->num_attr;i++)
    {
        if (strcmp(data->attr_info[i].name, attr->dev_attr.attr.name) == 0 &&
                strcmp(pdata->psu_attrs[i].aname, attr->dev_attr.attr.name) == 0 )
        {
            sysfs_attr_info = &data->attr_info[i];
            usr_data = &pdata->psu_attrs[i];
        }
    }

    if (sysfs_attr_info==NULL || usr_data==NULL)
        printk(KERN_ERR "psu_fan_dir is not supported attribute for this client\n");

    psu_update_attr(dev, sysfs_attr_info, usr_data);

    return sprintf(buf, "%s\n", sysfs_attr_info->val.strval);
}


int sonic_i2c_get_psu_fan_dir_default(void *client, PSU_DATA_ATTR *adata, void *data)
{

	int status = 0, retry = 10;
	struct psu_attr_info *padata = (struct psu_attr_info *)data;
	char fan_dir[5] = "";
	uint8_t offset = (uint8_t)adata->offset;
	int data_len = adata->len;

	while (retry)
	{
		status = i2c_smbus_read_i2c_block_data((struct i2c_client *)client, offset, data_len-1, fan_dir);
		if (unlikely(status<0))
		{
			msleep(60);
			retry--;
			continue;
		}
		break;
	}

	if (status < 0) 
	{
		fan_dir[0] = '\0';
        dev_dbg(&((struct i2c_client *)client)->dev, "unable to read fan_dir from (0x%x)\n", ((struct i2c_client *)client)->addr);
    }
    else 
	{
		fan_dir[data_len-1] = '\0';
    }

	if (strncmp(adata->devtype, "pmbus", strlen("pmbus")) == 0)
		strncpy(padata->val.strval, fan_dir+1, data_len-1);
	else
		strncpy(padata->val.strval, fan_dir, data_len);

	psu_dbg(KERN_ERR "status = %d, fan_dir : %s\n", status, padata->val.strval);
    return 0;
}

static int two_complement_to_int(u16 data, u8 valid_bit, int mask)
{
    u16  valid_data  = data & mask;
    bool is_negative = valid_data >> (valid_bit - 1);

    return is_negative ? (-(((~valid_data) & mask) + 1)) : valid_data;
}


ssize_t show_psu_v_out_default(struct device *dev, struct device_attribute *da, char *buf)
{
    struct sensor_device_attribute *attr = to_sensor_dev_attr(da);
    struct i2c_client *client = to_i2c_client(dev);
    struct psu_data *data = i2c_get_clientdata(client);
    PSU_PDATA *pdata = (PSU_PDATA *)(client->dev.platform_data);
    PSU_DATA_ATTR *usr_data = NULL;
    struct psu_attr_info *sysfs_attr_info = NULL;
    int i;
	u16 value = 0;
    int exponent, mantissa;
    int multiplier = 1000;


    for (i=0;i<data->num_attr;i++)
    {
        if (strcmp(data->attr_info[i].name, attr->dev_attr.attr.name) == 0 &&
                strcmp(pdata->psu_attrs[i].aname, attr->dev_attr.attr.name) == 0 )
        {
            sysfs_attr_info = &data->attr_info[i];
            usr_data = &pdata->psu_attrs[i];
        }
    }

    if (sysfs_attr_info==NULL || usr_data==NULL)
        psu_dbg(KERN_ERR "psu_v_out is not supported attribute for this client\n");

    psu_update_attr(dev, sysfs_attr_info, usr_data);

	value = sysfs_attr_info->val.shortval;

	exponent = two_complement_to_int(value >> 11, 5, 0x1f);
    mantissa = two_complement_to_int(value & 0x7ff, 11, 0x7ff);
    if (exponent >= 0)
		return sprintf(buf, "%d\n", (mantissa << exponent) * multiplier);
	else
		return sprintf(buf, "%d\n", (mantissa * multiplier) / (1 << -exponent));

}

int sonic_i2c_get_psu_v_out_default(void *client, PSU_DATA_ATTR *adata, void *data)
{

	int status = 0, retry = 10;
	struct psu_attr_info *padata = (struct psu_attr_info *)data;
	uint8_t offset = (uint8_t)adata->offset;

    while (retry) {
        status = i2c_smbus_read_word_data((struct i2c_client *)client, offset);
        if (unlikely(status < 0)) {
            msleep(60);
            retry--;
            continue;
        }
        break;
    }

	if (status < 0) 
	{
		padata->val.shortval = 0;
        dev_dbg(&((struct i2c_client *)client)->dev, "unable to read v_out from (0x%x)\n", ((struct i2c_client *)client)->addr);
    }
    else 
	{
		padata->val.shortval = status;
    }

	psu_dbg(KERN_ERR "v_out : %d\n", padata->val.shortval);
    return 0;
}


ssize_t show_psu_i_out_default(struct device *dev, struct device_attribute *da, char *buf)
{
    struct sensor_device_attribute *attr = to_sensor_dev_attr(da);
    struct i2c_client *client = to_i2c_client(dev);
    struct psu_data *data = i2c_get_clientdata(client);
    PSU_PDATA *pdata = (PSU_PDATA *)(client->dev.platform_data);
    PSU_DATA_ATTR *usr_data = NULL;
    struct psu_attr_info *sysfs_attr_info = NULL;
    int i;
	u16 value = 0;
    int exponent, mantissa;
    int multiplier = 1000;


    for (i=0;i<data->num_attr;i++)
    {
        if (strcmp(data->attr_info[i].name, attr->dev_attr.attr.name) == 0 &&
                strcmp(pdata->psu_attrs[i].aname, attr->dev_attr.attr.name) == 0 )
        {
            sysfs_attr_info = &data->attr_info[i];
            usr_data = &pdata->psu_attrs[i];
        }
    }

    if (sysfs_attr_info==NULL || usr_data==NULL)
        printk(KERN_ERR "psu_i_out is not supported attribute for this client\n");

    psu_update_attr(dev, sysfs_attr_info, usr_data);

	value = sysfs_attr_info->val.shortval;

	exponent = two_complement_to_int(value >> 11, 5, 0x1f);
    mantissa = two_complement_to_int(value & 0x7ff, 11, 0x7ff);
    if (exponent >= 0)
		return sprintf(buf, "%d\n", (mantissa << exponent) * multiplier);
	else
		return sprintf(buf, "%d\n", (mantissa * multiplier) / (1 << -exponent));
}


int sonic_i2c_get_psu_i_out_default(void *client, PSU_DATA_ATTR *adata, void *data)
{

	int status = 0, retry = 10;
	struct psu_attr_info *padata = (struct psu_attr_info *)data;
	uint8_t offset = (uint8_t)adata->offset;

    while (retry) {
        status = i2c_smbus_read_word_data((struct i2c_client *)client, offset);
        if (unlikely(status < 0)) {
            msleep(60);
            retry--;
            continue;
        }
        break;
    }

	if (status < 0) 
	{
		padata->val.shortval = 0;
        dev_dbg(&((struct i2c_client *)client)->dev, "unable to read i_out from (0x%x)\n", ((struct i2c_client *)client)->addr);
    }
    else 
	{
		padata->val.shortval = status;
    }

	psu_dbg(KERN_ERR "i_out : %d\n", padata->val.shortval);
    return 0;
}


ssize_t show_psu_p_out_default(struct device *dev, struct device_attribute *da, char *buf)
{
    struct sensor_device_attribute *attr = to_sensor_dev_attr(da);
    struct i2c_client *client = to_i2c_client(dev);
    struct psu_data *data = i2c_get_clientdata(client);
    PSU_PDATA *pdata = (PSU_PDATA *)(client->dev.platform_data);
    PSU_DATA_ATTR *usr_data = NULL;
    struct psu_attr_info *sysfs_attr_info = NULL;
    int i;
	u16 value = 0;
    int exponent, mantissa;
    int multiplier = 1000;


    for (i=0;i<data->num_attr;i++)
    {
        if (strcmp(data->attr_info[i].name, attr->dev_attr.attr.name) == 0 &&
                strcmp(pdata->psu_attrs[i].aname, attr->dev_attr.attr.name) == 0 )
        {
            sysfs_attr_info = &data->attr_info[i];
            usr_data = &pdata->psu_attrs[i];
        }
    }

    if (sysfs_attr_info==NULL || usr_data==NULL)
        psu_dbg(KERN_ERR "psu_p_out is not supported attribute for this client\n");

    psu_update_attr(dev, sysfs_attr_info, usr_data);

	value = sysfs_attr_info->val.shortval;

	exponent = two_complement_to_int(value >> 11, 5, 0x1f);
    mantissa = two_complement_to_int(value & 0x7ff, 11, 0x7ff);
 
	if (exponent >= 0)
		return sprintf(buf, "%d\n", (mantissa << exponent) * multiplier);
	else
		return sprintf(buf, "%d\n", (mantissa * multiplier) / (1 << -exponent));
}


int sonic_i2c_get_psu_p_out_default(void *client, PSU_DATA_ATTR *adata, void *data)
{

	int status = 0, retry = 10;
	struct psu_attr_info *padata = (struct psu_attr_info *)data;
	uint8_t offset = (uint8_t)adata->offset;

    while (retry) {
        status = i2c_smbus_read_word_data((struct i2c_client *)client, offset);
        if (unlikely(status < 0)) {
            msleep(60);
            retry--;
            continue;
        }
        break;
    }

	if (status < 0) 
	{
		padata->val.shortval = 0;
        dev_dbg(&((struct i2c_client *)client)->dev, "unable to read p_out from (0x%x)\n", ((struct i2c_client *)client)->addr);
    }
    else 
	{
		padata->val.shortval = status;
    }

	psu_dbg(KERN_ERR "p_out : %d\n", padata->val.shortval);
    return 0;
}


ssize_t show_psu_fan1_speed_rpm_default(struct device *dev, struct device_attribute *da, char *buf)
{
    struct sensor_device_attribute *attr = to_sensor_dev_attr(da);
    struct i2c_client *client = to_i2c_client(dev);
    struct psu_data *data = i2c_get_clientdata(client);
    PSU_PDATA *pdata = (PSU_PDATA *)(client->dev.platform_data);
    PSU_DATA_ATTR *usr_data = NULL;
    struct psu_attr_info *sysfs_attr_info = NULL;
    int i;
	u16 value = 0;
    int exponent, mantissa;
    int multiplier = 1;


    for (i=0;i<data->num_attr;i++)
    {
        if (strcmp(data->attr_info[i].name, attr->dev_attr.attr.name) == 0 &&
                strcmp(pdata->psu_attrs[i].aname, attr->dev_attr.attr.name) == 0 )
        {
            sysfs_attr_info = &data->attr_info[i];
            usr_data = &pdata->psu_attrs[i];
        }
    }

    if (sysfs_attr_info==NULL || usr_data==NULL)
        printk(KERN_ERR "%s is not supported attribute for this client\n", attr->dev_attr.attr.name);

    psu_update_attr(dev, sysfs_attr_info, usr_data);

	value = sysfs_attr_info->val.shortval;

	exponent = two_complement_to_int(value >> 11, 5, 0x1f);
    mantissa = two_complement_to_int(value & 0x7ff, 11, 0x7ff);
 
	if (exponent >= 0)
		return sprintf(buf, "%d\n", (mantissa << exponent) * multiplier);
	else
		return sprintf(buf, "%d\n", (mantissa * multiplier) / (1 << -exponent));
}


int sonic_i2c_get_psu_fan1_speed_rpm_default(void *client, PSU_DATA_ATTR *adata, void *data)
{

	int status = 0, retry = 10;
	struct psu_attr_info *padata = (struct psu_attr_info *)data;
	uint8_t offset = (uint8_t)adata->offset;

    while (retry) {
        status = i2c_smbus_read_word_data((struct i2c_client *)client, offset);
        if (unlikely(status < 0)) {
            msleep(60);
            retry--;
            continue;
        }
        break;
    }

	if (status < 0) 
	{
		padata->val.shortval = 0;
        dev_dbg(&((struct i2c_client *)client)->dev, "unable to read fan1_speed_rpm from (0x%x)\n", ((struct i2c_client *)client)->addr);
    }
    else 
	{
		padata->val.shortval = status;
    }

	psu_dbg(KERN_ERR "fan1_speed_rpm : %d\n", padata->val.shortval);
    return 0;
}




#if 0
#define MERGE_ACCESS_OPS(from, to, elem) \
	if (from->elem != NULL) \
	{ \
		to->elem = from->elem; \
	}


int merge_psu_access_func_list(PSU_ACCESS_FUNC *p_from, PSU_ACCESS_FUNC *p_to)
{
    MERGE_ACCESS_OPS(p_from, p_to, get_psu_present);
    MERGE_ACCESS_OPS(p_from, p_to, get_psu_model_name);
    MERGE_ACCESS_OPS(p_from, p_to, get_psu_power_good);
    MERGE_ACCESS_OPS(p_from, p_to, get_psu_mfr_id);
    MERGE_ACCESS_OPS(p_from, p_to, get_psu_serial_num);
    MERGE_ACCESS_OPS(p_from, p_to, get_psu_fan_dir);
    MERGE_ACCESS_OPS(p_from, p_to, get_psu_v_out);
    MERGE_ACCESS_OPS(p_from, p_to, get_psu_i_out);
    MERGE_ACCESS_OPS(p_from, p_to, get_psu_p_out);
    
	return 0;
}
EXPORT_SYMBOL(merge_psu_access_func_list);
#endif


/* OLD DEFAULT GET FUNCTIONS BASED UPON TYPE OF ATTRIBUTE */
void sonic_i2c_retrieve_psu_status(PSU_DATA_ATTR *usr_data, uint32_t *ret)
{
    int val = 0;

    val = board_i2c_cpld_read(usr_data->devaddr , usr_data->offset);
    psu_dbg(KERN_ERR "psu_status value = %x\n", val);
    *ret =  ((val & usr_data->mask) == usr_data->cmpval);
    psu_dbg(KERN_ERR "status_value = 0x%x\n", *ret);

	return;
}

int sonic_i2c_retrieve_psu_ascii(void *client, char *data, int data_len, uint8_t offset)
{
    int status = 0, retry = 10;

	/*status = pre_sonic_i2c_retrieve_psu_mfr_id(client, data, data_len, offset);*/

    psu_dbg(KERN_ERR "Inside sonic_i2c_retrieve_ascii\n");
    psu_dbg(KERN_ERR "client is : %x\n", (int *)client);
    psu_dbg(KERN_ERR "client addr is : %x, offset: 0x%x, data_len:%d\n", ((struct i2c_client *)client)->addr, offset, data_len);

    while (retry) {
        status = i2c_smbus_read_i2c_block_data((struct i2c_client *)client, offset, (data_len), data);
        if (unlikely(status < 0)) {
            msleep(60);
            retry--;
            continue;
        }
        break;
    }
    data[data_len] = '\0';
    psu_dbg(KERN_ERR "status = %d, manufacturer id : %s\n", status, data);

	/*status = post_sonic_i2c_retrieve_psu_mfr_id(data, data_len);*/

    return status;
}


int sonic_i2c_retrieve_psu_linear(void *client, uint8_t offset)
{
    int status = 0, retry = 10;

    psu_dbg(KERN_ERR "Inside sonic_i2c_retrieve_psu_linear\n");
    psu_dbg(KERN_ERR "client is : %x\n", (int *)client);
    psu_dbg(KERN_ERR "client addr is : %x, offset: 0x%x \n", ((struct i2c_client *)client)->addr, offset);

    while (retry) {
        status = i2c_smbus_read_word_data((struct i2c_client *)client, offset);
        if (unlikely(status < 0)) {
            msleep(60);
            retry--;
            continue;
        }
        break;
    }
    psu_dbg(KERN_ERR "status = 0x%x\n", status);
    return status;
}

