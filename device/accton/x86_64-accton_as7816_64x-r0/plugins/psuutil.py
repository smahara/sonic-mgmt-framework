#!/usr/bin/env python

#############################################################################
# Accton
#
# Module contains an implementation of SONiC PSU Base API and
# provides the PSUs status which are available in the platform
#
#############################################################################

import os.path

try:
    from sonic_psu.psu_base import PsuBase
except ImportError as e:
    raise ImportError (str(e) + "- required module not found")

class PsuUtil(PsuBase):
    """Platform-specific PSUutil class"""

    def __init__(self):
        PsuBase.__init__(self)

        self.psu_path = "/sys/bus/i2c/devices/"
        self.psu_presence = "/psu_present"
        self.psu_oper_status = "/psu_power_good"
        self.psu_model_name = "/psu_model_name"
        self.psu_mfr_id = "/psu_mfr_id"
        self.psu_serial_num = "/psu_serial_num"
        self.psu_fan_dir = "/psu_fan_direction"
        self.psu_v_out = "/psu_v_out"
        self.psu_i_out = "/psu_i_out"
        self.psu_p_out = "/psu_p_out"
        self.psu_fan1_speed_rpm = "/psu_fan1_speed_rpm"

        self.psu_mapping_info = {
            1: "10-0053",
            2: "9-0050",
        }

        self.psu_mapping_diag = {
            1: "10-005b",
            2: "9-0058",
        }


    def get_psu_mapping_info(self, index):
        if index is None:
            return False

        for id in self.psu_mapping_info:
            psu_name = str()
            node = self.psu_path + self.psu_mapping_info[id] + "/name"

            try:
                with open(node, 'r') as psu_name_fd:
                    psu_name = psu_name_fd.read()
            except IOError:
                    return False

            if psu_name.find("as7816_64x_psu" + str(index)) != -1:
               return self.psu_mapping_info[id]

        return str()

    def get_psu_mapping_diag(self, index):
        if index is None:
           return False

        for id in self.psu_mapping_diag:
            psu_name = str()
            node = self.psu_path + self.psu_mapping_info[id] + "/name"

            try:
                with open(node, 'r') as psu_name_fd:
                    psu_name = psu_name_fd.read()
            except IOError:
                    return False

            if psu_name.find("as7816_64x_psu" + str(index)) != -1:
               return self.psu_mapping_diag[id]

        return str()


    def get_num_psus(self):
        return len(self.psu_mapping_info)

    def get_psu_status(self, index):
        if index is None:
            return False

        status = 0
        node = self.psu_path + self.get_psu_mapping_info(index)+self.psu_oper_status
        try:
            with open(node, 'r') as power_status:
                status = int(power_status.read())
        except IOError:
            return False

        return status == 1

    def get_psu_presence(self, index):
        if index is None:
            return False

        status = 0
        node = self.psu_path + self.get_psu_mapping_info(index) + self.psu_presence
        try:
            with open(node, 'r') as presence_status:
                status = int(presence_status.read())
        except IOError:
            return False

        return status == 1

    def get_powergood_status(self, index):
        if index is None:
            return False

        status = 0
        node = self.psu_path + self.get_psu_mapping_info(index) + self.psu_oper_status
        try:
            with open(node, 'r') as powergood_status:
                status = int(powergood_status.read())
        except IOError:
            return False

        return status == 1


    def get_model(self, index):
        if index is None:
            return None

        model = ""
        node = self.psu_path + self.get_psu_mapping_info(index) + self.psu_model_name
        try:
            with open(node, 'r') as model_name:
                model = model_name.read()
        except IOError:
            return None

        return model.rstrip()

    def get_mfr_id(self, index):
        if index is None:
            return None

        mfr = ""
        node = self.psu_path + self.get_psu_mapping_diag(index) + self.psu_mfr_id
        try:
            with open(node, 'r') as mfr_id:
                mfr = mfr_id.read()
        except IOError:
            return None

        #pmbus read output's first char needs to be left
        return mfr.rstrip()[1:]

    def get_serial(self, index):
        if index is None:
            return None

        serial = ""
        node = self.psu_path + self.get_psu_mapping_diag(index) + self.psu_serial_num

        try:
            with open(node, 'r') as serial_num:
                serial = serial_num.read()
        except IOError:
            return None

        return serial.rstrip()[1:]  # pmbus read output's first char needs to be left

    def get_direction(self, index):
        if index is None:
            return None

        direction = ""
        node = self.psu_path + self.get_psu_mapping_info(index) + self.psu_fan_dir
        try:
            with open(node, 'r') as fan_dir:
                direction = fan_dir.read()
        except IOError:
            return None

        if 'CR' in direction:
           return "INTAKE"
        elif 'DR' in direction:
           return "EXHAUST"
        else:
           return direction.rstrip()

    def get_output_voltage(self, index):
        if index is None:
            return 0

        vout = 0
        node = self.psu_path + self.get_psu_mapping_diag(index) + self.psu_v_out
        try:
            with open(node, 'r') as v_out:
                vout = int(v_out.read())
        except IOError:
            return 0

        # vout is in milli volts
        return vout

    def get_output_current(self, index):
        if index is None:
            return 0

        iout = 0
        node = self.psu_path + self.get_psu_mapping_diag(index) + self.psu_i_out
        try:
            with open(node, 'r') as i_out:
                iout = int(i_out.read())
        except IOError:
            return 0

        # iout in milli amps
        return iout

    def get_output_power(self, index):
        if index is None:
            return 0

        pout = 0
        node = self.psu_path + self.get_psu_mapping_diag(index) + self.psu_p_out
        try:
            with open(node, 'r') as p_out:
                pout = int(p_out.read())
        except IOError:
            return 0

        # pout should be in micro-watts, CLI is written with conversion
        return (pout*1000)

    def get_fan_rpm(self, index, fan_idx):
        if index is None or fan_idx is None:
            return 0
        if fan_idx!=1:
            return 0

        rpm = 0
        node = self.psu_path + self.get_psu_mapping_diag(index) + self.psu_fan1_speed_rpm

        try:
            with open(node, 'r') as speed_rpm:
                rpm = int(speed_rpm.read())
        except IOError:
            return 0

        return rpm
