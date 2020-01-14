# sfputil.py
#
# Platform-specific SFP transceiver interface for SONiC
#
try:
    import time
    import os
    import string
    from ctypes import create_string_buffer
    from sonic_sfp.sfputilbase import SfpUtilBase
except ImportError as e:
    raise ImportError("%s - required module not found" % str(e))

XCVR_EEPROM_TYPE_SFP = 1

#from xcvrd
SFP_STATUS_INSERTED = '1'
SFP_STATUS_REMOVED = '0'


class SfpUtil(SfpUtilBase):
    """Platform-specific SfpUtil class"""

    PORT_START = 0
    PORT_END = 53
    PORTS_IN_BLOCK = 54
    QSFP_PORT_START = 48
    QSFP_PORT_END = 54

    BASE_VAL_PATH = "/sys/class/i2c-adapter/i2c-{0}/{1}-0050/"
    BASE_OOM_PATH = "/sys/bus/i2c/devices/{0}-0050/"
    BASE_CPLD2_PATH = "/sys/bus/i2c/devices/{0}-0061/"
    BASE_CPLD3_PATH = "/sys/bus/i2c/devices/{0}-0062/"
    I2C_BUS_ORDER = -1

    #The sidebands of QSFP is different. 
    qsfp_sb_map = [1, 3, 5, 2, 4, 6]

    _port_to_is_present = {}
    _port_to_lp_mode = {}

    _port_to_eeprom_mapping = {}
    _port_to_i2c_mapping = {
           0: [1, 2],
           1: [2, 3],
           2: [3, 4],
           3: [4, 5],
           4: [5, 6],
           5: [6, 7],
           6: [7, 8],
           7: [8, 9],
           8: [9, 10],
           9: [10, 11],
           10: [11, 12],
           11: [12, 13],
           12: [13, 14],
           13: [14, 15],
           14: [15, 16],
           15: [16, 17],
           16: [17, 18],
           17: [18, 19],
           18: [19, 20],
           19: [20, 21],
           20: [21, 22],
           21: [22, 23],
           22: [23, 24],
           23: [24, 25],
           24: [25, 26],
           25: [26, 27],
           26: [27, 28],
           27: [28, 29],
           28: [29, 30],
           29: [30, 31],
           30: [31, 32],
           31: [32, 33],
           32: [33, 34],
           33: [34, 35],
           34: [35, 36],
           35: [36, 37],
           36: [37, 38],
           37: [38, 39],
           38: [39, 40],
           39: [40, 41],
           40: [41, 42],
           41: [42, 43],
           42: [43, 44],
           43: [44, 45],
           44: [45, 46],
           45: [46, 47],
           46: [47, 48],
           47: [48, 49],
           48: [49, 50],#QSFP49
           49: [51, 52],
           50: [53, 54],
           51: [50, 51],
           52: [52, 53],
           53: [54, 55],#QSFP54
           }

    @property
    def port_start(self):
        return self.PORT_START

    @property
    def port_end(self):
        return self.PORT_END

    @property
    def qsfp_port_start(self):
        return self.QSFP_PORT_START

    @property
    def qsfp_port_end(self):
        return self.QSFP_PORT_END
    
    @property
    def qsfp_ports(self):
        return range(self.QSFP_PORT_START, self.PORTS_IN_BLOCK + 1)

    @property
    def port_to_eeprom_mapping(self):
        return self._port_to_eeprom_mapping

    #Two i2c buses might get flipped order, check them both.
    def update_i2c_order(self):
        if self.I2C_BUS_ORDER < 0:
            eeprom_path = "/sys/bus/i2c/devices/1-0057/eeprom"
            if os.path.exists(eeprom_path):
                self.I2C_BUS_ORDER = 0
            eeprom_path = "/sys/bus/i2c/devices/0-0057/eeprom"
            if os.path.exists(eeprom_path):
                self.I2C_BUS_ORDER = 1
        return self.I2C_BUS_ORDER 

    def get_presence(self, port_num):
        # Check for invalid port_num
        if port_num < self.port_start or port_num > self.port_end:
            return False

        order = self.update_i2c_order()
        if port_num < 24:
            present_path = self.BASE_CPLD2_PATH.format(order)
        else:
            present_path = self.BASE_CPLD3_PATH.format(order)
        present_path = present_path + "module_present_" + str(self._port_to_i2c_mapping[port_num][0])
        self.__port_to_is_present = present_path

        try:
            val_file = open(self.__port_to_is_present)
        except IOError as e:
            print "Error: unable to open file: %s" % str(e)          
            return False

        content = val_file.readline().rstrip()
        val_file.close()

        # content is a string, either "0" or "1"
        if content == "1":
            return True

        return False

    def qsfp_sb_remap(self, port_num):
        qsfp_start = self.qsfp_port_start
        qsfp_index = self._port_to_i2c_mapping[port_num][0] - qsfp_start
        qsfp_index = self.qsfp_sb_map[qsfp_index-1]
        return qsfp_start+qsfp_index

    def get_low_power_mode_cpld(self, port_num):
        if port_num < self.qsfp_port_start or port_num > self.qsfp_port_end:
            return False
        
        order = self.update_i2c_order()
        lp_mode_path = self.BASE_CPLD3_PATH.format(order)
        lp_mode_path = lp_mode_path + "module_lp_mode_" 
        q = self.qsfp_sb_remap(port_num)
        lp_mode_path = lp_mode_path + str(q)
        
        try:
            val_file = open(lp_mode_path)
        except IOError as e:
            print "Error: unable to open file: %s" % str(e)          
            return False

        content = val_file.readline().rstrip()
        val_file.close()

        # content is a string, either "0" or "1"
        if content == "1":
            return True

        return False

    def get_low_power_mode(self, port_num):
        if port_num < self.qsfp_port_start or port_num > self.qsfp_port_end:
            return False
        
        if not self.get_presence(port_num):
            return self.get_low_power_mode_cpld(port_num)

        try:
            eeprom = None

            eeprom = open(self.port_to_eeprom_mapping[port_num], mode="rb", buffering=0)
            eeprom.seek(93)
            lpmode = ord(eeprom.read(1))

            if not (lpmode & 0x1): # 'Power override' bit is 0
                return self.get_low_power_mode_cpld(port_num)
            else:
                if ((lpmode & 0x2) == 0x2):
                    return True # Low Power Mode if "Power set" bit is 1
                else:
                    return False # High Power Mode if "Power set" bit is 0
        except IOError as err:
            print "Error: unable to open file: %s" % str(err)
            return False
        finally:
            if eeprom is not None:
                eeprom.close()
                time.sleep(0.01)

    def set_low_power_mode(self, port_num, lpmode):
        if port_num < self.qsfp_port_start or port_num > self.qsfp_port_end:
            return False

        try:
            eeprom = None

            if not self.get_presence(port_num):
                return False # Port is not present, unable to set the eeprom

            # Fill in write buffer
            regval = 0x3 if lpmode else 0x1 # 0x3:Low Power Mode, 0x1:High Power Mode
            buffer = create_string_buffer(1)
            buffer[0] = chr(regval)

            # Write to eeprom
            eeprom = open(self.port_to_eeprom_mapping[port_num], mode="r+b", buffering=0)
            eeprom.seek(93)
            eeprom.write(buffer[0])
            return True
        except IOError as err:
            print "Error: unable to open file: %s" % str(err)
            return False
        finally:
            if eeprom is not None:
                eeprom.close()
                time.sleep(0.01)

    def reset(self, port_num):
        if port_num < self.qsfp_port_start or port_num > self.qsfp_port_end:
            return False
         
        order = self.update_i2c_order()
        lp_mode_path = self.BASE_CPLD3_PATH.format(order)
        mod_rst_path = lp_mode_path + "module_reset_" 
        q = self.qsfp_sb_remap(port_num)
        mod_rst_path = mod_rst_path + str(q)
        try:
            reg_file = open(mod_rst_path, 'r+', buffering=0)
        except IOError as e:
            print "Error: unable to open file: %s" % str(e)          
            return False

        #toggle reset
        reg_file.seek(0)
        reg_file.write('0')
        time.sleep(1)
        reg_file.seek(0)
        reg_file.write('1')
        reg_file.close()
        return True

    @property
    def _get_presence_bitmap(self):
	nodes = []
        order = self.update_i2c_order()
        
        present_path = self.BASE_CPLD2_PATH.format(order)
        nodes.append(present_path + "module_present_all")
        present_path = self.BASE_CPLD3_PATH.format(order)
        nodes.append(present_path + "module_present_all")

	bitmap = ""
	for node in nodes: 
            try:
                reg_file = open(node)
    
            except IOError as e:
                print "Error: unable to open file: %s" % str(e)
                return False
            bitmap += reg_file.readline().rstrip() + " "
            reg_file.close()

        rev = bitmap.split(" ")
        rev = "".join(rev[::-1])
        return int(rev,16)
   

    data = {'valid':0, 'last':0, 'present':0} 
    def get_transceiver_change_event(self, timeout=2000):
        now = time.time()
        port_dict = {}
        port = 0

        if timeout < 1000:
            timeout = 1000
        timeout = (timeout) / float(1000) # Convert to secs


        if now < (self.data['last'] + timeout) and self.data['valid']:
            return True, {}

        reg_value = self._get_presence_bitmap
        changed_ports = self.data['present'] ^ reg_value
        if changed_ports:
            for port in range (self.port_start, self.port_end+1):
                # Mask off the bit corresponding to our port
                fp_port = self._port_to_i2c_mapping[port][0]
                mask = (1 << (fp_port - 1))
                if changed_ports & mask:

                    if (reg_value & mask) == 0:
                        port_dict[port] = SFP_STATUS_REMOVED
                    else:
                        port_dict[port] = SFP_STATUS_INSERTED

            # Update cache 
            self.data['present'] = reg_value
            self.data['last'] = now
            self.data['valid'] = 1

            return True, port_dict
        else:
            return True, {}
        return False, {}


    def is_media_type_set_required(self, port_num):
        etype = self.get_eeprom_type(port_num)
        # Set for SFP ports only
        if etype == XCVR_EEPROM_TYPE_SFP:
            return True
        else:
            return False

    def __init__(self):
        eeprom_path = self.BASE_OOM_PATH + "eeprom"

        for x in range(self.port_start, self.port_end+1):
            self.port_to_eeprom_mapping[x] = eeprom_path.format(
                self._port_to_i2c_mapping[x][1]
                )

        SfpUtilBase.__init__(self)

