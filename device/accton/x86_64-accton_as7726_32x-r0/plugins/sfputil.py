# sfputil.py
#
# Platform-specific SFP transceiver interface for SONiC
#

try:
    import time
    from sonic_sfp.sfputilbase import SfpUtilBase
except ImportError as e:
    raise ImportError("%s - required module not found" % str(e))


class SfpUtil(SfpUtilBase):
    """Platform-specific SfpUtil class"""
    
    PORT_START = 0
    PORT_END = 33
    PORTS_IN_BLOCK = 34
    
    BASE_OOM_PATH = "/sys/bus/i2c/devices/{0}-0050/"
    BASE_CPLD_PATH = "/sys/bus/i2c/devices/11-0060/"
    
    _port_to_is_present = {}
    _port_to_lp_mode = {}

    _port_to_eeprom_mapping = {}
    _port_to_i2c_mapping = {
           0: [1, 21],
           1: [2, 22],
           2: [3, 23],
           3: [4, 24],
           4: [5, 26],
           5: [6, 25],
           6: [7, 28],
           7: [8, 27],
           8: [9, 17],
           9: [10, 18],
           10: [11, 19],
           11: [12, 20],
           12: [13, 29],
           13: [14, 30],
           14: [15, 31],
           15: [16, 32],
           16: [17, 33],
           17: [18, 34],
           18: [19, 35],
           19: [20, 36],
           20: [21, 45],
           21: [22, 46],
           22: [23, 47],
           23: [24, 48],
           24: [25, 37],
           25: [26, 38],
           26: [27, 39],
           27: [28, 40],
           28: [29, 41],
           29: [30, 42],
           30: [31, 43],
           31: [32, 44],              
           32: [33, 15], 
           33: [34, 16], 
           }

    @property
    def port_start(self):
        return self.PORT_START

    @property
    def port_end(self):
        return self.PORT_END
   
    @property
    def qsfp_ports(self):
        return range(self.PORT_START, self.PORTS_IN_BLOCK - 2)

    @property
    def port_to_eeprom_mapping(self):
        return self._port_to_eeprom_mapping

    def __init__(self):
        eeprom_path = self.BASE_OOM_PATH + "eeprom"
        
        for x in range(0, self.port_end+1):
            self.port_to_eeprom_mapping[x] = eeprom_path.format(
                self._port_to_i2c_mapping[x][1]
                )

        SfpUtilBase.__init__(self)

    def get_presence(self, port_num):
        # Check for invalid port_num
        if port_num < self.port_start or port_num > self.port_end:
            return False
       
        present_path = self.BASE_CPLD_PATH + "module_present_" + str(port_num+1)
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

    def get_low_power_mode(self, port_num): 
      raise NotImplementedError
        
    def set_low_power_mode(self, port_num, lpmode):
        raise NotImplementedError

    def reset(self, port_num):
        if port_num < self.port_start or port_num > self.port_end:
            return False
            
        mod_rst_path = self.BASE_CPLD_PATH + "module_reset_" + str(port_num+1)
        
        self.__port_to_mod_rst = mod_rst_path
        try:
            reg_file = open(self.__port_to_mod_rst, 'r+')
        except IOError as e:
            print "Error: unable to open file: %s" % str(e)          
            return False

        reg_value = '1'

        reg_file.write(reg_value)
        reg_file.close()
        
        return True

    def get_transceiver_change_event(self):
        """
        TODO: This function need to be implemented
        when decide to support monitoring SFP(Xcvrd)
        on this platform.
        """
        raise NotImplementedError
