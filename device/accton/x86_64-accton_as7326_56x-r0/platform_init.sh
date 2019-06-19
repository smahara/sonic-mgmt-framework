#!/bin/bash

cat /etc/init.d/opennsl-modules | grep -q usemsi=1
if [ $? -ne 0 ];then
    sed -i '/modprobe[ \t]* linux-kernel-bde/  s/$/ usemsi=1/' /etc/init.d/opennsl-modules
fi

/usr/local/bin/idt_init.sh
/usr/local/bin/accton_as7326_util.py install
