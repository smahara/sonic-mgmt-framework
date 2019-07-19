#!/usr/bin/env python


# Sample pddf_fanutil file 
# All the supported FAN SysFS aattributes are
#- fan<idx>_present
#- fan<idx>_direction
#- fan<idx>_front_rpm
#- fan<idx>_rear_rpm
#- fan<idx>_pwm
#- fan<idx>_fault
# where idx is in the range [1-8]
#


import os.path
import sys, traceback, time
sys.path.append('/usr/share/sonic/platform/plugins')
import pddfparse
import json

try:
    from sonic_fan.fan_base import FanBase
except ImportError as e:
    raise ImportError (str(e) + "- required module not found")


dirname=os.path.dirname(os.path.realpath(__file__))

with open(dirname+'/../pddf/pd-plugin.json') as pd:
    plugin_data = json.load(pd)


class FanUtil(FanBase):
    """PDDF generic FAN util class"""

    def __init__(self):
        FanBase.__init__(self)

        self.platform = pddfparse.get_platform()

    def get_num_fans(self):
        return self.platform['num_fans']

    def get_fan_presence(self, idx):
        # 1 based fan index
        if idx<1 or idx>self.platform['num_fans']:
            print "Invalid fan index %d\n"%idx
            return False

        attr_name = "fan" + str(idx) + "_present"
        sysfs_path = pddfparse.get_path("FAN-CTRL", attr_name)

        try:
            with open(sysfs_path, 'r') as f:
                presence = int(f.read())
        except IOError:
            return False
        
        #print "FAN-%d is %spresent"%(idx+1, "" if presence==1 else "not ")
        status = (True if presence==1 else False)
        return status

    def get_fan_status(self, idx):
        # 1 based fan index
        if idx<1 or idx>self.platform['num_fans']:
            print "Invalid fan index %d\n"%idx
            return False

        front_speed, rear_speed = self.get_fan_speed(idx)
        status = True if (front_speed != 0 and rear_speed != 0) else False
        return status

    def get_fan_direction(self, idx):
        # 1 based fan index
        if idx<1 or idx>self.platform['num_fans']:
            print "Invalid fan index %d\n"%idx
            return None

        attr = "fan" + str(idx) + "_direction"
        path = pddfparse.get_path("FAN-CTRL", attr)
        #print "%d-%s"%(i,path)
        try:
            with open(path, 'r') as f:
                val = f.read()
        except IOError:
            return None

        vmap = plugin_data['FAN']['direction']['valmap']
        if val.rstrip('\n') in vmap:
            direction = vmap[val.rstrip('\n')]
        else:
            direction = val
        #print "FAN-%d direction is %s"%(i, direction)

        return direction

    def get_direction(self):
        num_fan = self.get_num_fan();

        for i in range(1, num_fan+1):
            attr = "fan" + str(i) + "_direction"
            path = pddfparse.get_path("FAN-CTRL", attr)
            #print "%d-%s"%(i,path)
            try:
                with open(path, 'r') as f:
                    val = int(f.read())
            except IOError:
                return False

            vmap = plugin_data['FAN']['direction']['valmap']
            direction = vmap[str(val)]

            print "FAN-%d direction is %s"%(i, direction)

        return 0

    def get_fan_speed(self, idx):
        # 1 based fan index
        if idx<1 or idx>self.platform['num_fans']:
            print "Invalid fan index %d\n"%idx
            return (0, 0)

        attr1 = "fan" + str(idx) + "_front_rpm"
        attr2 = "fan" + str(idx) + "_rear_rpm"
        path1 = pddfparse.get_path("FAN-CTRL", attr1)
        path2 = pddfparse.get_path("FAN-CTRL", attr2)
        #print %d-%s%(i,path)
        try:
            with open(path1, 'r') as f1:
                frpm = int(f1.read())
            with open(path2, 'r') as f2:
                rrpm = int(f2.read())
        except IOError:
            return (0, 0)
        #ret += "FAN-%d\t\t\t%d\t\t\t%d\n"%(i, frpm, rrpm)

        return (frpm, rrpm)

    def get_speed(self):
        num_fan = self.get_num_fan();
        ret = "FAN_INDEX\t\tFRONT_RPM\t\tREAR_RPM\n"

        for i in range(1, num_fan+1):
            attr1 = "fan" + str(i) + "_front_rpm"
            attr2 = "fan" + str(i) + "_rear_rpm"
            path1 = pddfparse.get_path("FAN-CTRL", attr1)
            path2 = pddfparse.get_path("FAN-CTRL", attr2)
            #print %d-%s%(i,path)
            try:
                with open(path1, 'r') as f1:
                    frpm = int(f1.read())
                with open(path2, 'r') as f2:
                    rrpm = int(f2.read())
            except IOError:
                return False

            ret += "FAN-%d\t\t\t%d\t\t\t%d\n"%(i, frpm, rrpm)

        return ret

    def set_speed(self, val):
        if val<0 or val>100:
            print "Error: Invalid speed %d. Please provide a valid speed percentage"%val
            return False
        
        num_fan = self.platform['num_fans']
        duty_cycle_to_pwm = eval(plugin_data['FAN']['duty_cycle_to_pwm'])
        pwm = duty_cycle_to_pwm(val)
        print "New Speed: %d%% - PWM value to be set is %d\n"%(val,pwm)

        status = 0
        for i in range(1, num_fan+1):
            attr = "fan" + str(i) + "_pwm"
            node = pddfparse.get_path("FAN-CTRL", attr)
            try:
                with open(node, 'w') as f:
                    f.write(str(pwm))
            except IOError:
                return False

        #time.sleep(5)
        #print "Done changing the speed of all the fans ... Reading the speed to crossscheck\n"
        return True

    def dump_sysfs(self):
        return pddfparse.cli_dump_dsysfs('fan')



#if __name__== "__main__":
    #obj=FanUtil()
    ##for i in range(0,6):
        ##obj.get_fan_present(i)

    #obj.get_direction()
    ##print(obj.get_direction())
    #print(obj.get_speed())
    #obj.set_speed(100)
    #print "Chaning the speed back to 50%\n"
    #obj.set_speed(50)
