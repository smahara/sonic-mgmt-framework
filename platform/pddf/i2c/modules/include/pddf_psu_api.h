/*
 * Copyright 2019 Broadcom. All rights reserved.
 * The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries.
 *
 * Description
 *  PSU driver related api declarations
 */

#ifndef __PDDF_PSU_API_H__
#define __PDDF_PSU_API_H__


extern ssize_t show_psu_present_default(struct device *dev, struct device_attribute *da, char *buf);
extern ssize_t show_psu_power_good_default(struct device *dev, struct device_attribute *da, char *buf);
extern ssize_t show_psu_model_name_default(struct device *dev, struct device_attribute *da, char *buf);
extern ssize_t show_psu_mfr_id_default(struct device *dev, struct device_attribute *da, char *buf);
extern ssize_t show_psu_serial_num_default(struct device *dev, struct device_attribute *da, char *buf);
extern ssize_t show_psu_fan_dir_default(struct device *dev, struct device_attribute *da, char *buf);
extern ssize_t show_psu_v_out_default(struct device *dev, struct device_attribute *da, char *buf);
extern ssize_t show_psu_i_out_default(struct device *dev, struct device_attribute *da, char *buf);
extern ssize_t show_psu_p_out_default(struct device *dev, struct device_attribute *da, char *buf);
extern ssize_t show_psu_fan1_speed_rpm_default(struct device *dev, struct device_attribute *da, char *buf);

extern int sonic_i2c_get_psu_present_default(void *client, PSU_DATA_ATTR *adata, void *data);
extern int sonic_i2c_get_psu_power_good_default(void *client, PSU_DATA_ATTR *adata, void *data);
extern int sonic_i2c_get_psu_model_name_default(void *client, PSU_DATA_ATTR *adata, void *data);
extern int sonic_i2c_get_psu_mfr_id_default(void *client, PSU_DATA_ATTR *adata, void *data);
extern int sonic_i2c_get_psu_serial_num_default(void *client, PSU_DATA_ATTR *adata, void *data);
extern int sonic_i2c_get_psu_fan_dir_default(void *client, PSU_DATA_ATTR *adata, void *data);
extern int sonic_i2c_get_psu_v_out_default(void *client, PSU_DATA_ATTR *adata, void *data);
extern int sonic_i2c_get_psu_i_out_default(void *client, PSU_DATA_ATTR *adata, void *data);
extern int sonic_i2c_get_psu_p_out_default(void *client, PSU_DATA_ATTR *adata, void *data);
extern int sonic_i2c_get_psu_fan1_speed_rpm_default(void *client, PSU_DATA_ATTR *adata, void *data);

/*extern int merge_psu_access_func_list(PSU_ACCESS_FUNC *from, PSU_ACCESS_FUNC *to);*/

/* OLD RETRIEVE FUNCTIONS BASED UPON THE TYPE OF ATTRIBUTE */
/*extern void sonic_i2c_retrieve_psu_status(PSU_DATA_ATTR *attr_data, uint32_t *ret);*/
/*extern int sonic_i2c_retrieve_psu_ascii(void *client, char *data, int data_len, uint8_t offset);*/
/*extern int sonic_i2c_retrieve_psu_linear(void *client, uint8_t offset);*/


#endif //__PDDF_PSU_API_H__
