#!/bin/bash
###########################################################################
# Copyright 2019 Broadcom. The term "Broadcom" refers to Broadcom Inc.    #
# and/or its subsidiaries.                                                #
#                                                                         #
# Licensed under the Apache License, Version 2.0 (the "License");         #
# you may not use this file except in compliance with the License.        #
# You may obtain a copy of the License at                                 #
#                                                                         #
#   http://www.apache.org/licenses/LICENSE-2.0                            #
#                                                                         #
# Unless required by applicable law or agreed to in writing, software     #
# distributed under the License is distributed on an "AS IS" BASIS,       #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.#
# See the License for the specific language governing permissions and     #
# limitations under the License.                                          #
###########################################################################
# SONiC package creation utility                                          #
#                                                                         #
# This script is used to create a package file to include SONiC installer #
# binary and additional files that need to be used as part of the         #
# installation.                                                           #
#                                                                         #
###########################################################################
set -e

usage() {
    echo "$(basename $0) <sonic-broadcom.bin> [files ..]"
}

NOS_BIN=$1
if [ "$#" -le 1 ] ; then
    usage
    exit 1
fi

if [ ! -e $1 ]; then
    echo "SONiC installer binary $1 not found"
    exit 1
fi

shift 1
EXTRA_FILES=$@

echo "Creating a package file to combine $NOS_BIN and $EXTRA_FILES"
# Name of the target package fle
PKG_NAME="$(basename $NOS_BIN .bin).pkg"

# Create a temporary working directory
PKG_DIR=$(mktemp -d)
sharch=$PKG_DIR/payload.tar
rm -f $PKG_NAME
cp $NOS_BIN $PKG_DIR/nos.bin
mkdir -p $PKG_DIR/installer
cp -R $EXTRA_FILES $PKG_DIR/installer || true

sed -e '/^exit_marker/,$d' $NOS_BIN > $PKG_DIR/head
echo exit_marker  >> $PKG_DIR/head
tar -C $PKG_DIR -cf $sharch installer nos.bin || {
      echo "Error creating payload archive"
      rm -rf $PKG_DIR
      exit 1
}
sha1=$(cat $sharch | sha1sum | awk '{print $1}')
cp -f $PKG_DIR/head $PKG_NAME
chmod +w $PKG_NAME
sed -i "/^payload_sha1/c\payload_sha1=$sha1" $PKG_NAME
cat $sharch >> $PKG_NAME
echo "Successfully created package file: $PKG_NAME"

#Remove temporary files
rm -rf $PKG_DIR
exit 0
