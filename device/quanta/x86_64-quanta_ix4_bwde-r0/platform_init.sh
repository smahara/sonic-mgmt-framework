#!/bin/bash
cat /etc/init.d/opennsl-modules|grep usemsi=1

if [ $? -ne 0 ];then
  echo "Enable msi mode for TH2 SDK driver"
  sed -i 's/modprobe linux-kernel-bde/modprobe linux-kernel-bde usemsi=1/g' /etc/init.d/opennsl-modules
fi

