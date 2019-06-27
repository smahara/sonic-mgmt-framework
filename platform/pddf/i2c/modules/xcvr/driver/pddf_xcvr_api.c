/*
 * Copyright 2019 Broadcom. All rights reserved.
 * The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries.
 *
 * Description of various APIs related to transciever component
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
#include "pddf_xcvr_defs.h"

/*#define SFP_DEBUG*/
#ifdef SFP_DEBUG
#define sfp_dbg(...) printk(__VA_ARGS__)
#else
#define sfp_dbg(...)
#endif

int get_xcvr_module_attr_data(struct i2c_client *client, struct device *dev,
                            struct device_attribute *da, XCVR_ATTR *xattr);

ssize_t get_module_presence(struct device *dev, struct device_attribute *da,
             char *buf)
{
    struct sensor_device_attribute *attr = to_sensor_dev_attr(da);
    struct i2c_client *client = to_i2c_client(dev);
    struct xcvr_data *data = i2c_get_clientdata(client);
	XCVR_PDATA *pdata = (XCVR_PDATA *)(client->dev.platform_data);
	XCVR_ATTR *attr_data = NULL;
    uint32_t status = 0, modpres=0, i;

	for (i=0; i<pdata->len; i++)
    {
		attr_data = &pdata->xcvr_attrs[i];
		/*printk(KERN_ERR "\n attr_data->aname: %s, attr->dev_attr.attr.name:%s, attr_data->devtype:%s\n", */
		/*attr_data->aname, attr->dev_attr.attr.name, attr_data->devtype);*/
		if (strcmp(attr_data->aname, attr->dev_attr.attr.name) == 0)
		{
	        mutex_lock(&data->update_lock);
			if (strcmp(attr_data->devtype, "cpld") == 0)
			{
				status = board_i2c_cpld_read(attr_data->devaddr , attr_data->offset);
				modpres = ((status & BIT_INDEX(attr_data->mask)) == attr_data->cmpval) ? 1 : 0;
				sfp_dbg(KERN_ERR "\nMod presence :0x%x, reg_value = 0x%x\n", modpres, status);
			} 
			else if(strcmp(attr_data->devtype, "eeprom") == 0)
			{
				/* get client client for eeprom -  Not Applicable */
			}
	        mutex_unlock(&data->update_lock);
			return sprintf(buf, "%d\n", modpres);
		}
	}
	return sprintf(buf, "%s","");
}

ssize_t get_module_reset(struct device *dev, struct device_attribute *da,
             char *buf)
{
    struct sensor_device_attribute *attr = to_sensor_dev_attr(da);
    struct i2c_client *client = to_i2c_client(dev);
    struct xcvr_data *data = i2c_get_clientdata(client);
	XCVR_PDATA *pdata = (XCVR_PDATA *)(client->dev.platform_data);
	XCVR_ATTR *attr_data = NULL;
    uint32_t status = 0, modreset=0, i;

	for (i=0; i<pdata->len; i++)
    {
		attr_data = &pdata->xcvr_attrs[i];
		if (strcmp(attr_data->aname, attr->dev_attr.attr.name) == 0)
		{
	        mutex_lock(&data->update_lock);
			if (strcmp(attr_data->devtype, "cpld") == 0)
			{
				status = board_i2c_cpld_read(attr_data->devaddr , attr_data->offset);
				modreset = ((status & BIT_INDEX(attr_data->mask)) == attr_data->cmpval) ? 1 : 0;
				sfp_dbg(KERN_ERR "\nMod Reset :0x%x, reg_value = 0x%x\n", modreset, status);
			} 
			else if(strcmp(attr_data->devtype, "eeprom") == 0)
			{
				/* get client client for eeprom -  Not Applicable */
			}
	        mutex_unlock(&data->update_lock);
			return sprintf(buf, "%d\n", modreset);
		}
	}
	return sprintf(buf, "%s","");
}

ssize_t set_module_reset(struct device *dev, struct device_attribute *da, const char *buf, 
		size_t count)
{
	struct sensor_device_attribute *attr = to_sensor_dev_attr(da);
	struct i2c_client *client = to_i2c_client(dev);
	struct xcvr_data *data = i2c_get_clientdata(client);
	XCVR_PDATA *pdata = (XCVR_PDATA *)(client->dev.platform_data);
	XCVR_ATTR *attr_data = NULL;
	int status = 0, i;
	unsigned int set_value, val_mask;
	uint8_t reg;

	for (i=0; i<pdata->len; i++)
	{
		attr_data = &pdata->xcvr_attrs[i];
		if (strcmp(attr_data->aname, attr->dev_attr.attr.name) == 0)
		{
			mutex_lock(&data->update_lock);
			if (strcmp(attr_data->devtype, "cpld") == 0)
			{
				if(kstrtoint(buf, 10, &set_value))
					return -EINVAL;

				if(set_value == 1) { 
					if(attr_data->cmpval == 0)
						val_mask = ~(BIT_INDEX(attr_data->mask));
					else
						val_mask = BIT_INDEX(attr_data->mask);
				}
				else {
					if(attr_data->cmpval == 0)
						val_mask = BIT_INDEX(attr_data->mask);
					else
						val_mask = ~(BIT_INDEX(attr_data->mask));
				}

				reg = board_i2c_cpld_read(attr_data->devaddr , attr_data->offset);
				reg = reg & val_mask;
				status = board_i2c_cpld_write(attr_data->devaddr, attr_data->offset, reg);
			} 
			mutex_unlock(&data->update_lock);
			return count;
		}
	}
	return -EINVAL;
}

ssize_t get_module_intr_status(struct device *dev, struct device_attribute *da,
             char *buf)
{
    struct sensor_device_attribute *attr = to_sensor_dev_attr(da);
    struct i2c_client *client = to_i2c_client(dev);
    struct xcvr_data *data = i2c_get_clientdata(client);
	XCVR_PDATA *pdata = (XCVR_PDATA *)(client->dev.platform_data);
	XCVR_ATTR *attr_data = NULL;
    uint32_t status = 0, mod_intr=0, i;

	for (i=0; i<pdata->len; i++)
    {
		attr_data = &pdata->xcvr_attrs[i];
		if (strcmp(attr_data->aname, attr->dev_attr.attr.name) == 0)
		{
	        mutex_lock(&data->update_lock);
			if (strcmp(attr_data->devtype, "cpld") == 0)
			{
				status = board_i2c_cpld_read(attr_data->devaddr , attr_data->offset);
				mod_intr = ((status & BIT_INDEX(attr_data->mask)) == attr_data->cmpval) ? 1 : 0;
				sfp_dbg(KERN_ERR "\nModule Interrupt :0x%x, reg_value = 0x%x\n", mod_intr, status);
			} 
			else if(strcmp(attr_data->devtype, "eeprom") == 0)
			{
				/* get client client for eeprom -  Not Applicable */
			}
	        mutex_unlock(&data->update_lock);
			return sprintf(buf, "%d\n", mod_intr);
		}
	}
	return sprintf(buf, "%s","");
}

int get_xcvr_module_attr_data(struct i2c_client *client, struct device *dev, 
							struct device_attribute *da, XCVR_ATTR *xattr)
{
    struct sensor_device_attribute *attr = to_sensor_dev_attr(da);
	XCVR_PDATA *pdata = (XCVR_PDATA *)(client->dev.platform_data);
	XCVR_ATTR *attr_data = NULL;
	int i;

	for (i=0; i < pdata->len; i++)
    {
		attr_data = &pdata->xcvr_attrs[i];
		if (strcmp(attr_data->aname, attr->dev_attr.attr.name) == 0)
		{
			xattr = attr_data;
			return 1;
		}
	}
	return 0;
}

ssize_t get_module_lpmode(struct device *dev, struct device_attribute *da, char *buf)
{
    struct i2c_client *client = to_i2c_client(dev);
    struct xcvr_data *data = i2c_get_clientdata(client);
	XCVR_ATTR *attr_data = NULL;
    unsigned int status = 0, lpmode=0;

	if(get_xcvr_module_attr_data(client, dev, da, attr_data) && (attr_data != NULL))
	{
		mutex_lock(&data->update_lock);
		if (strcmp(attr_data->devtype, "cpld") == 0)
		{
			status = board_i2c_cpld_read(attr_data->devaddr , attr_data->offset);
			lpmode = ((status & BIT_INDEX(attr_data->mask)) == attr_data->cmpval) ? 1 : 0;
			sfp_dbg(KERN_ERR "\nModule LPmode :0x%x, reg_value = 0x%x\n", lpmode, status);
		} 
	    mutex_unlock(&data->update_lock);
		return sprintf(buf, "%d\n", lpmode);
	}
	else
		return sprintf(buf,"%s","");
}

ssize_t set_module_lpmode(struct device *dev, struct device_attribute *da, const char *buf, 
		size_t count)
{
    struct i2c_client *client = to_i2c_client(dev);
    struct xcvr_data *data = i2c_get_clientdata(client);
	unsigned int status = 0, set_value, val_mask;
	uint8_t reg;
	XCVR_ATTR *attr_data = NULL;

	if(get_xcvr_module_attr_data(client, dev, da, attr_data) && (attr_data != NULL))
	{
		mutex_lock(&data->update_lock);
		if (strcmp(attr_data->devtype, "cpld") == 0)
		{
			if(kstrtoint(buf, 10, &set_value))
				return -EINVAL;

			if(set_value == 1) { 
				if(attr_data->cmpval == 0)
					val_mask = ~(BIT_INDEX(attr_data->mask));
				else
					val_mask = BIT_INDEX(attr_data->mask);
			}
			else {
				if(attr_data->cmpval == 0)
					val_mask = BIT_INDEX(attr_data->mask);
				else
					val_mask = ~(BIT_INDEX(attr_data->mask));
			}

			reg = board_i2c_cpld_read(attr_data->devaddr , attr_data->offset);
			reg = reg & val_mask;
			status = board_i2c_cpld_write(attr_data->devaddr, attr_data->offset, reg);
		} 
	    mutex_unlock(&data->update_lock);
	}
	return count;
}

ssize_t get_module_rxlos(struct device *dev, struct device_attribute *da,
             char *buf)
{
    struct i2c_client *client = to_i2c_client(dev);
    struct xcvr_data *data = i2c_get_clientdata(client);
    unsigned int status = 0, rxlos=0;
	XCVR_ATTR *attr_data = NULL;

	if(get_xcvr_module_attr_data(client, dev, da, attr_data) && (attr_data != NULL))
	{
		mutex_lock(&data->update_lock);
		if (strcmp(attr_data->devtype, "cpld") == 0)
		{
			status = board_i2c_cpld_read(attr_data->devaddr , attr_data->offset);
			rxlos = ((status & BIT_INDEX(attr_data->mask)) == attr_data->cmpval) ? 1 : 0;
			sfp_dbg(KERN_ERR "\nModule RxLOS :0x%x, reg_value = 0x%x\n", rxlos, status);
		} 
	    mutex_unlock(&data->update_lock);
		return sprintf(buf, "%d\n", rxlos);
	}
	else
		return sprintf(buf,"%s","");
}

ssize_t get_module_txdisable(struct device *dev, struct device_attribute *da,
             char *buf)
{
    struct i2c_client *client = to_i2c_client(dev);
    struct xcvr_data *data = i2c_get_clientdata(client);
    unsigned int status = 0, txdis=0;
	XCVR_ATTR *attr_data = NULL;
	
	if(get_xcvr_module_attr_data(client, dev, da, attr_data) && (attr_data != NULL))
	{
		mutex_lock(&data->update_lock);
		if (strcmp(attr_data->devtype, "cpld") == 0)
	{
			status = board_i2c_cpld_read(attr_data->devaddr , attr_data->offset);
			txdis = ((status & BIT_INDEX(attr_data->mask)) == attr_data->cmpval) ? 1 : 0;
			sfp_dbg(KERN_ERR "\nModule TxDisable :0x%x, reg_value = 0x%x\n", txdis, status);
	}
	    mutex_unlock(&data->update_lock);
		return sprintf(buf, "%d\n", txdis);
	}
	else
		return sprintf(buf,"%s","");
}

ssize_t set_module_txdisable(struct device *dev, struct device_attribute *da, const char *buf, 
		size_t count)
{
    struct i2c_client *client = to_i2c_client(dev);
    struct xcvr_data *data = i2c_get_clientdata(client);
	unsigned int status = 0, set_value, val_mask;
	uint8_t reg;
	XCVR_ATTR *attr_data = NULL;

	if(get_xcvr_module_attr_data(client, dev, da, attr_data) && (attr_data != NULL))
	{
		mutex_lock(&data->update_lock);
		if (strcmp(attr_data->devtype, "cpld") == 0)
		{
			if(kstrtoint(buf, 10, &set_value))
				return -EINVAL;

			if(set_value == 1) { 
				if(attr_data->cmpval == 0)
					val_mask = ~(BIT_INDEX(attr_data->mask));
				else
					val_mask = BIT_INDEX(attr_data->mask);
			}
			else {
				if(attr_data->cmpval == 0)
					val_mask = BIT_INDEX(attr_data->mask);
				else
					val_mask = ~(BIT_INDEX(attr_data->mask));
			}

			reg = board_i2c_cpld_read(attr_data->devaddr , attr_data->offset);
			reg = reg & val_mask;
			status = board_i2c_cpld_write(attr_data->devaddr, attr_data->offset, reg);
		} 
	    mutex_unlock(&data->update_lock);
	}
	return count;
}

ssize_t get_module_txfault(struct device *dev, struct device_attribute *da,
             char *buf)
{
    struct i2c_client *client = to_i2c_client(dev);
    struct xcvr_data *data = i2c_get_clientdata(client);
    unsigned int status = 0, txflt=0;
	XCVR_ATTR *attr_data = NULL;

	if(get_xcvr_module_attr_data(client, dev, da, attr_data) && (attr_data != NULL))
	{
		mutex_lock(&data->update_lock);
		if (strcmp(attr_data->devtype, "cpld") == 0)
		{
			status = board_i2c_cpld_read(attr_data->devaddr , attr_data->offset);
			txflt = ((status & BIT_INDEX(attr_data->mask)) == attr_data->cmpval) ? 1 : 0;
			sfp_dbg(KERN_ERR "\nModule TxFault :0x%x, reg_value = 0x%x\n", txflt, status);
		} 
	    mutex_unlock(&data->update_lock);
		return sprintf(buf, "%d\n", txflt);
	}
	return sprintf(buf,"%s","");
}
