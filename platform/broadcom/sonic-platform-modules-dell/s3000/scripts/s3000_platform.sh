#!/bin/bash

#platform init script for Dell S3000

source dell_i2c_utils.sh

init_devnum() {
    found=0
    for devnum in 0 1; do
        devname=`cat /sys/bus/i2c/devices/i2c-${devnum}/name`
        # iSMT adapter can be at either dffd0000 or dfff0000
        if [[ $devname == 'SMBus iSMT adapter at '* ]]; then
            found=1
            break
        fi
    done

    [[ $found -eq 0 ]] && echo "cannot find iSMT" && exit 1
}

# Attach/Detach CPU board mux @ 0x70
cpu_board_mux() {
    case $1 in
        "new_device")    i2c_mux_create pca9548 0x73 $devnum 2 
                         ;;
        "delete_device") i2c_mux_delete 0x73 $devnum
                         ;;
        *)               echo "s3000_platform: cpu_board_mux: invalid command !"
                         ;;
    esac
}

# Attach/Detach Switchboard MUX @ 0x71
main_board_mux() {
    case $1 in
        "new_device")    i2c_mux_create pca9548 0x71 8 10
                         i2c_mux_create pca9548 0x72 8 18
                         ;;
        "delete_device") i2c_mux_delete 0x71 8
                         i2c_mux_delete 0x72 8
                         ;;
        *)               echo "s3000_platform: main_board_mux : invalid command !"
                         ;;
    esac
}


#Attach/Detach the system devices
sys_devices() {
    case $1 in
        "new_device")    #Attach syseeprom
                         i2c_config "echo 24lc64t 0x50 > /sys/bus/i2c/devices/i2c-2/$1"
                         #Attach temperature monitor
                         i2c_config "echo max6697 0x1a > /sys/bus/i2c/devices/i2c-3/$1"
                         i2c_config "echo max6697 0x1a > /sys/bus/i2c/devices/i2c-11/$1"
                         #Attach PSU Controller
                         i2c_config "echo dps200 0x5a > /sys/bus/i2c/devices/i2c-12/$1"
                         i2c_config "echo dps200 0x5b > /sys/bus/i2c/devices/i2c-13/$1"
                         #Attach Fan Controller
                         i2c_config "echo emc2305 0x4d > /sys/bus/i2c/devices/i2c-23/$1"
                         ;;
        "delete_device") i2c_config "echo 0x50 > /sys/bus/i2c/devices/i2c-2/$1"
                         i2c_config "echo 0x1a > /sys/bus/i2c/devices/i2c-3/$1"
                         i2c_config "echo 0x1a > /sys/bus/i2c/devices/i2c-11/$1"
                         i2c_config "echo 0x5a > /sys/bus/i2c/devices/i2c-12/$1"
                         i2c_config "echo 0x5b > /sys/bus/i2c/devices/i2c-13/$1"
                         i2c_config "echo 0x4d > /sys/bus/i2c/devices/i2c-23/$1"
                         ;;
        *)               echo "s3000_platform: main_board_mux : invalid command !"
                         ;;
    esac
}

#Attach/Detach the SFP modules on PCA9548_2
switch_board_sfp() {
    case $1 in
        "new_device")    i2c_config "echo sff8436 0x50 > /sys/bus/i2c/devices/i2c-14/$1"
                         i2c_config "echo sff8436 0x50 > /sys/bus/i2c/devices/i2c-15/$1"
                         i2c_config "echo sff8436 0x50 > /sys/bus/i2c/devices/i2c-16/$1"
                         i2c_config "echo sff8436 0x50 > /sys/bus/i2c/devices/i2c-17/$1"
                         ;;
        "delete_device") i2c_config "echo 0x50 > /sys/bus/i2c/devices/i2c-14/$1"
                         i2c_config "echo 0x50 > /sys/bus/i2c/devices/i2c-15/$1"
                         i2c_config "echo 0x50 > /sys/bus/i2c/devices/i2c-16/$1"
                         i2c_config "echo 0x50 > /sys/bus/i2c/devices/i2c-17/$1"
                         ;;
        *)               echo "s3000_platform: switch_board_sfp: invalid command !"
                         ;;
    esac
}

#Forcibly bring quad-port phy out of reset for 48-1G port functionality

platform_firmware_versions() {

FIRMWARE_VERSION_FILE=/var/log/firmware_versions
rm -rf ${FIRMWARE_VERSION_FILE}
# Get BIOS version
echo "BIOS: `dmidecode -s system-version `" > $FIRMWARE_VERSION_FILE
# Get MMC CPLD version
r=`/usr/local/bin/portiocfg.py --get --offset 0x100 | sed 's/reg value //'`
echo "MMC CPLD: $((r >> 4)).$((r & 0xf))" >> $FIRMWARE_VERSION_FILE
# Get SMC CPLD version
r=`/usr/local/bin/portiocfg.py --get --offset 0x200 | sed 's/reg value //'`
echo "SMC CPLD: $((r >> 4)).$((r & 0xf))" >> $FIRMWARE_VERSION_FILE

}


init_devnum

if [[ "$1" == "init" ]]; then
    modprobe i2c-dev
    modprobe i2c-mux-pca954x force_deselect_on_exit=1
    modprobe dell_s3000_lpc_cpld
    modprobe dps200
    modprobe mc24lc64t


    cpu_board_mux "new_device"
    main_board_mux "new_device"
    sys_devices "new_device"
    switch_board_sfp "new_device"

    platform_firmware_versions
elif [[ "$1" == "deinit" ]]; then
    switch_board_sfp "delete_device"
    sysdevices "delete_device"
    main_board_mux "delete_device"
    cpu_board_mux "delete_device"

    modprobe -r mc241c6t
    modprobe -r dps200
    modprobe -r dell_s3000_lpc_cpld
    modprobe -r i2c-mux-pca954x
    modprobe -r i2c-dev
else
     echo "s3000_platform : Invalid option !"
fi
