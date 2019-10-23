#
# fanutil.py
# Platform-specific Fan status interface for SONiC
#

import logging
import os.path

try:
    from sonic_fan.fan_base import FanBase
except ImportError as e:
    raise ImportError (str(e) + "- required module not found")

class FanUtil(FanBase):
    """Platform-specific FANutil class"""

    SYS_FAN_NUM = 3
    HWMON_PATH = '/sys/class/hwmon/hwmon2/'
    FAN_INDEX_START = 76

    logger = logging.getLogger(__name__)

    def __init__(self, log_level=logging.DEBUG):
        FanBase.__init__(self)

    # Get sysfs attribute
    def get_attr_value(self, attr_path):

        retval = 'ERR'
        if (not os.path.isfile(attr_path)):
            return retval

        try:
            with open(attr_path, 'r') as fd:
                retval = fd.read()
        except Exception:
            logging.error("Unable to open ", attr_path, " file !")

        retval = retval.rstrip('\r\n')
        return retval

    def check_fan_index(self, index):
        if index is None:
            return False

        if index < 1 or index > self.SYS_FAN_NUM:
            logging.error("Invalid Fan index:", index)
            return False

        return True

    def get_num_fans(self):
        return self.SYS_FAN_NUM

    def get_status(self, index):
        if self.check_fan_index(index) == False:
            return None

        front_speed_file = 'fan' + str(self.FAN_INDEX_START+2*(index-1)) + '_input'
        rear_speed_file = 'fan' + str(self.FAN_INDEX_START+2*(index-1)+1) + '_input'

        front_speed = self.get_attr_value(self.HWMON_PATH + front_speed_file)
        rear_speed = self.get_attr_value(self.HWMON_PATH + rear_speed_file)

        if front_speed == '0.0' or rear_speed == '0.0':
            return False

        return True

    def get_presence(self, index):
        if self.check_fan_index(index) == False:
            return None

        front_present_file = 'fan' + str(self.FAN_INDEX_START+2*(index-1)) + '_present'
        rear_present_file = 'fan' + str(self.FAN_INDEX_START+2*(index-1)+1) + '_present'

        front_present = self.get_attr_value(self.HWMON_PATH + front_present_file)
        rear_present = self.get_attr_value(self.HWMON_PATH + rear_present_file)

        if front_present == '1' or rear_present == '1':
            return True

        return False

    def get_direction(self, index):
        if self.check_fan_index(index) == False:
            return None

        direction_file = 'fan' + str(self.FAN_INDEX_START+2*(index-1)) + '_direction'
        direction = self.get_attr_value(self.HWMON_PATH + direction_file)

        """
        1: FB 2: BF
        Since the fan is at rear of the switch, FB means Exhaust; BF means Intake
        """
        if direction == '2':
            return "INTAKE"
        else:
            return "EXHAUST"

    def get_speed(self, index):
        if self.check_fan_index(index) == False:
            return None

        speed_file = 'fan' + str(self.FAN_INDEX_START+2*(index-1)) + '_input'
        speed = self.get_attr_value(self.HWMON_PATH + speed_file)

        return int(float(speed))

    def get_speed_rear(self, index):
        if self.check_fan_index(index) == False:
            return None

        speed_file = 'fan' + str(self.FAN_INDEX_START+2*(index-1)+1) + '_input'
        speed = self.get_attr_value(self.HWMON_PATH + speed_file)

        return int(float(speed))

    def set_speed(self, val):
        logging.error("Not allowed to set fan speed!")

        return False
