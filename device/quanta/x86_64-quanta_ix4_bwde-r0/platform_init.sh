#!/bin/bash

cat /etc/init.d/opennsl-modules | grep usemsi=1

if [ $? -ne 0 ];then
  echo "Enable msi mode for TH2 SDK driver"
  sed -i 's/modprobe linux-kernel-bde/modprobe linux-kernel-bde usemsi=1/g' /etc/init.d/opennsl-modules
fi

modprobe lpc_ich
modprobe i2c-i801
modprobe i2c-dev
modprobe i2c-mux-pca954x
modprobe gpio-pca953x
modprobe leds-gpio
modprobe optoe
modprobe ipmi_devintf

sleep 1

insmod /lib/modules/$(uname -r)/extra/qci_bwde_cpld.ko
insmod /lib/modules/$(uname -r)/extra/qci_platform_ix4.ko
insmod /lib/modules/$(uname -r)/extra/quanta_hwmon_ipmi.ko

sleep 3

# turn on module power
echo 21 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio21/direction
echo 1 >/sys/class/gpio/gpio21/value

# turn on 100G led by default
i2cset -y 0x10 0x3a 0x04 0x00
i2cset -y 0x11 0x3a 0x04 0x00
i2cset -y 0x12 0x3a 0x04 0x00
i2cset -y 0x13 0x3a 0x04 0x00

# Update System LED
echo 87 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio87/direction
echo 0 >/sys/class/gpio/gpio87/value
echo 88 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio88/direction
echo 1 >/sys/class/gpio/gpio88/value

# QSFP EEPROM
for port in $(seq 1 64); do
    bus=$(expr ${port} + 31)
    echo ${port} >/sys/bus/i2c/devices/${bus}-0050/port_name
done
