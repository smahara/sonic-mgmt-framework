#!/usr/bin/env python

#############################################################################
# Accton
#
# Module contains an implementation of SONiC FAN Base API and
# provides various info about the FANs which are available in the platform
#
#############################################################################

import os.path
import logging

try:
    from sonic_fan.fan_base import FanBase
except ImportError as e:
    raise ImportError (str(e) + "- required module not found")

class FanUtil(FanBase):
    """Platform-specific FANutil class"""

    FAN_NUM_ON_MAIN_BOARD = 6
    FAN_NUM_1_IDX = 1
    FAN_NUM_2_IDX = 2
    FAN_NUM_3_IDX = 3
    FAN_NUM_4_IDX = 4
    FAN_NUM_5_IDX = 5
    FAN_NUM_6_IDX = 6

    BASE_VAL_PATH = '/sys/bus/i2c/devices/11-0066/{0}'
    FAN_DUTY_PATH = '/sys/bus/i2c/devices/11-0066/fan_duty_cycle_percentage'

    logger = logging.getLogger(__name__)

    def __init__(self, log_level=logging.DEBUG):
        FanBase.__init__(self)
        ch = logging.StreamHandler()
        ch.setLevel(log_level)
        self.logger.addHandler(ch)


    def get_num_fans(self):
        return self.FAN_NUM_ON_MAIN_BOARD

    def get_status(self, index):
        if index is None:
            return None

        if index < self.FAN_NUM_1_IDX or index > self.FAN_NUM_ON_MAIN_BOARD:
            self.logger.debug('Invalid FAN index:%d', index)
            return None

        status = 0
        attr_name = 'fan' + str(index) + '_fault'
        node = self.BASE_VAL_PATH.format(attr_name)
        try:
            with open(node, 'r') as fault:
                status = int(fault.read())
        except IOError as e:
            print "Error: %s"%str(e)
            return None

        return False if (status>0) else True

    def get_presence(self, index):
        if index is None:
            return None

        if index < self.FAN_NUM_1_IDX or index > self.FAN_NUM_ON_MAIN_BOARD:
            self.logger.debug('Invalid FAN index:%d', index)
            return None

        status = 0
        attr_name = 'fan' + str(index) + '_present'
        node = self.BASE_VAL_PATH.format(attr_name)
        try:
            with open(node, 'r') as presence_status:
                status = int(presence_status.read())
        except IOError as e:
            print "Error: %s"%str(e)
            return None

        return status == 1

    def get_direction(self, index):
        if index is None:
            return None

        if index < self.FAN_NUM_1_IDX or index > self.FAN_NUM_ON_MAIN_BOARD:
            self.logger.debug('Invalid FAN index:%d', index)
            return None

        direction = ""
        attr_name = 'fan' + str(index) + '_direction'
        node = self.BASE_VAL_PATH.format(attr_name)
        try:
            with open(node, 'r') as fan_dir:
                direction = int(fan_dir.read())
        except IOError as e:
            print "Error: %s"%str(e)
            return None

        if direction==1:
            return "INTAKE"
        else:
            return "EXHAUST"

    def get_speed(self, index):
        if index is None:
            return None

        if index < self.FAN_NUM_1_IDX or index > self.FAN_NUM_ON_MAIN_BOARD:
            self.logger.debug('Invalid FAN index:%d', index)
            return None

        frpm = 0
        attr_name = 'fan' + str(index) + '_front_speed_rpm'
        node = self.BASE_VAL_PATH.format(attr_name)
        try:
            with open(node, 'r') as front_speed:
                frpm = int(front_speed.read())
        except IOError as e:
            print "Error: %s"%str(e)
            return None

        return frpm

    def get_speed_rear(self, index):
        if index is None:
            return None

        if index < self.FAN_NUM_1_IDX or index > self.FAN_NUM_ON_MAIN_BOARD:
            self.logger.debug('Invalid FAN index:%d', index)
            return None

        rrpm = 0
        attr_name = 'fan' + str(index) + '_rear_speed_rpm'
        node = self.BASE_VAL_PATH.format(attr_name)
        try:
            with open(node, 'r') as rear_speed:
                rrpm = int(rear_speed.read())
        except IOError as e:
            print "Error: %s"%str(e)
            return None

        return rrpm

    def set_speed(self, val):
        if val<0 or val>100:
            self.logger.debug('Error: Invalid speed %d. Please provide a valid duty-cycle percentage', val)
            return False

        node = self.FAN_DUTY_PATH
        try:
            with open(node, 'w') as dc:
                dc.write(str(val))
        except IOError:
            return False

        return True
