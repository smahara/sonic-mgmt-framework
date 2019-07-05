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

/*Various Ops hook which can be used by vendors to provide some deviation from usual pddf functionality*/
struct pddf_ops_t
{
    /*Module init ops*/
    int (*pre_init)(void);
    int (*post_init)(void);
    /*probe ops*/
    int (*pre_probe)(struct i2c_client *, const struct i2c_device_id *);
    int (*post_probe)(struct i2c_client *, const struct i2c_device_id *);
    /*remove ops*/
    int (*pre_remove)(struct i2c_client *);
    int (*post_remove)(struct i2c_client *);
    /*Module exit ops*/
    void (*pre_exit)(void);
    void (*post_exit)(void);
};


#define ACCTON_WATCHDOG_STATUS_REG 0x33
#define ACCTON_WATCHDOG_STATUS_MASK 0x01

int pddf_fan_post_probe(struct i2c_client *client, const struct i2c_device_id *dev_id);
extern struct pddf_ops_t pddf_fan_ops;

  
int pddf_fan_post_probe(struct i2c_client *client, const struct i2c_device_id *dev_id)
{
	int status = 0;
	int val = 0;


	/* Disable the wdg timer */
	/*printk(KERN_ERR "Accton Watchdog timer is being disabled ...\n");*/
	status = i2c_smbus_read_byte_data(client, ACCTON_WATCHDOG_STATUS_REG);
	/* Check the value*/
	if (status & ACCTON_WATCHDOG_STATUS_MASK)
	{
		/* Watchdog is enabled -- disable it */
		val = status & (~(status & ACCTON_WATCHDOG_STATUS_MASK));
		status = i2c_smbus_write_byte_data(client, ACCTON_WATCHDOG_STATUS_REG, val);
		if (status<0)
		{
			printk(KERN_ERR "Unable to disable the watchdog timer\n");
			return -1;
		}
		printk(KERN_INFO "Accton FAN watchdog timer is successfully disabled\n");
	}
	else
		printk(KERN_INFO "Accton FAN watchdog timer is already disabled\n");

	return 0;
}
EXPORT_SYMBOL(pddf_fan_post_probe);



static int __init accton_pddf_init(void)
{
	pddf_fan_ops.post_probe = pddf_fan_post_probe;
	/*printk(KERN_ERR "Accton pddf init\n");*/
	return 0;
}

static void __exit accton_pddf_exit(void)
{
	/*printk(KERN_ERR "Accton pddf exit\n");*/
	return;
}

MODULE_AUTHOR("Broadcom");
MODULE_DESCRIPTION("accton pddf fan api");
MODULE_LICENSE("GPL");

module_init(accton_pddf_init);
module_exit(accton_pddf_exit);
