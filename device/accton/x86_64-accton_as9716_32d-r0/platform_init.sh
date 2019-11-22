#!/bin/bash

# driver_install
depmod -a
modprobe i2c-ismt
modprobe i2c-i801
modprobe i2c_dev
modprobe i2c_mux_pca954x force_deselect_on_exit=1
#modprobe accton_i2c_psu
modprobe accton_as9716_32d_cpld
modprobe accton_as9716_32d_fan
modprobe accton_as9716_32d_leds
modprobe accton_as9716_32d_psu
modprobe at24
modprobe optoe
modprobe lm75

# cpld_reset_stop
i2cset -y 0 0x65 0x3 0x0

# device_install
echo pca9548 0x77 > /sys/bus/i2c/devices/i2c-0/new_device
echo pca9548 0x72 > /sys/bus/i2c/devices/i2c-1/new_device
echo pca9548 0x76 > /sys/bus/i2c/devices/i2c-1/new_device
echo pca9548 0x72 > /sys/bus/i2c/devices/i2c-2/new_device
echo pca9548 0x73 > /sys/bus/i2c/devices/i2c-2/new_device
echo pca9548 0x74 > /sys/bus/i2c/devices/i2c-2/new_device
echo pca9548 0x75 > /sys/bus/i2c/devices/i2c-2/new_device
echo pca9548 0x76 > /sys/bus/i2c/devices/i2c-2/new_device

echo as9716_32d_fpga 0x60 > /sys/bus/i2c/devices/i2c-19/new_device
echo as9716_32d_cpld1 0x61 > /sys/bus/i2c/devices/i2c-20/new_device
echo as9716_32d_cpld2 0x62 > /sys/bus/i2c/devices/i2c-21/new_device
echo as9716_32d_cpld_cpu 0x65 > /sys/bus/i2c/devices/i2c-0/new_device

echo as9716_32d_fan 0x66 > /sys/bus/i2c/devices/i2c-17/new_device

echo lm75 0x48 > /sys/bus/i2c/devices/i2c-18/new_device
echo lm75 0x49 > /sys/bus/i2c/devices/i2c-18/new_device
echo lm75 0x4a > /sys/bus/i2c/devices/i2c-18/new_device
echo lm75 0x4b > /sys/bus/i2c/devices/i2c-18/new_device
echo lm75 0x4c > /sys/bus/i2c/devices/i2c-18/new_device
echo lm75 0x4e > /sys/bus/i2c/devices/i2c-18/new_device
echo lm75 0x4f > /sys/bus/i2c/devices/i2c-18/new_device

# PSU-1
echo as9716_32d_psu1 0x50 > /sys/bus/i2c/devices/i2c-9/new_device
echo acbel_fsh082    0x58 > /sys/bus/i2c/devices/i2c-9/new_device

# PSU-2
echo as9716_32d_psu2 0x51 > /sys/bus/i2c/devices/i2c-10/new_device
echo acbel_fsh082    0x59 > /sys/bus/i2c/devices/i2c-10/new_device

# System EERPOM
echo 24c02 0x56 > /sys/bus/i2c/devices/i2c-0/new_device

# QSFPDD EEPROM
SFP_MAP=
SFP_MAP+="25 26 27 28 29 30 31 32 "
SFP_MAP+="33 34 35 36 37 38 39 40 "
SFP_MAP+="41 42 43 44 45 46 47 48 "
SFP_MAP+="49 50 51 52 53 54 55 56 "
SFP_MAP+="57 58"

idx=0
for port in ${SFP_MAP}; do
    if [ ${idx} -lt 32 ]; then
        echo optoe1 0x50 > /sys/bus/i2c/devices/i2c-${port}/new_device
    else
        echo optoe2 0x50 > /sys/bus/i2c/devices/i2c-${port}/new_device
    fi
    echo port${idx} > /sys/bus/i2c/devices/${port}-0050/port_name
    idx=$(expr ${idx} + 1)
done

# Diag LED: Boot successfully (SOLID GREEN)
i2cset -f -y 19 0x60 0x64 4

