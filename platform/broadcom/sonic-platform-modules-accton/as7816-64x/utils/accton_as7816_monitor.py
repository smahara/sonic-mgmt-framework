#!/usr/bin/env python
#
# Copyright (C) 2017 Accton Technology Corporation
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# ------------------------------------------------------------------
# HISTORY:
#    mm/dd/yyyy (A.D.)
#    11/13/2017: Polly Hsu, Create
#    1/10/2018: Jostar modify for as7716_32
#    5/02/2019: Roy Lee modify for as7816_64x
#    08/11 2019: Geans Pin
# ------------------------------------------------------------------

try:
    import os
    import sys, getopt
    import subprocess
    import click
    import imp
    import logging
    import logging.config
    import logging.handlers
    import types
    import time  # this is only being used as part of the example
    import traceback
    import signal
    from tabulate import tabulate
    from as7816_64x.fanutil import FanUtil
    from as7816_64x.thermalutil import ThermalUtil
except ImportError as e:
    raise ImportError('%s - required module not found' % str(e))

# Deafults
VERSION = '1.0'
FUNCTION_NAME = 'accton_as7816_monitor'
DUTY_MAX = 100
DUTY_DEF = 40
CRITICAL_TEMP = 70000

global log_console
global log_level
global num_of_working_fans

fan_state=[2, 2, 2, 2, 2, 2, 2]  #init state=2, insert=1, remove=0

def system_powerdown():
    cmd = "i2cset -y -f 14 0x25 0x11 0x08"
    os.system(cmd)


# Make a class we can use to capture stdout and sterr in the log
class accton_as7816_monitor(object):
    syslog = logging.getLogger("["+FUNCTION_NAME+"]")
    num_of_working_fans = 0

    def __init__(self, log_console, log_file, log_level=logging.INFO):
        formatter = logging.Formatter('%(name)s %(message)s')
        sys_handler  = logging.handlers.SysLogHandler(address = '/dev/log')
        sys_handler.setFormatter(formatter)
        sys_handler.ident = 'conmon'
        self.syslog.setLevel(logging.WARNING)
        self.syslog.addHandler(sys_handler)
        #self.syslog.critical('foo syslog message')

        if log_file:
            fh = logging.FileHandler(log_file)
            fh.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)-15s %(name)s %(message)s')
            fh.setFormatter(formatter)
            self.syslog.addHandler(fh)

        if log_console:
            console = logging.StreamHandler()
            console.setLevel(log_level)
            formatter = logging.Formatter('%(asctime)-15s %(name)s %(message)s')
            console.setFormatter(formatter)
            self.syslog.addHandler(console)

    def manage_fans(self):

        global fan_state
        FAN_STATE_REMOVE = 0
        FAN_STATE_INSERT = 1
        fan_status = True

        max_duty = DUTY_MAX
        fan_policy = {
           0: [52, 0,     43000],
           1: [63, 43000, 46000],
           2: [75, 46000, 52000],
           3: [88, 52000, 57000],
           4: [max_duty, 57000, sys.maxsize],
        }

        thermal = ThermalUtil()
        fan = FanUtil()

        for x in range(fan.get_idx_fan_start(), fan.get_num_fans()+1):
            fan_status = fan.get_fan_status(x)
            fan_present = fan.get_fan_present(x)

            if fan_present == 1:
               if fan_state[x]!=1:
                  fan_state[x]=FAN_STATE_INSERT
                  self.syslog.warning("FAN-%d present is detected", x)
                  self.num_of_working_fans += 1
            else:
               if fan_state[x]!=0:
                  fan_state[x]=FAN_STATE_REMOVE
                  self.syslog.warning("Alarm for FAN-%d absent is detected", x)
                  self.num_of_working_fans -= 1

            if fan_status is None:
               self.syslog.error('SET new_perc to %d (FAN stauts is None. fan_num:%d)', max_duty, x)
               fan.set_fan_duty_cycle(max_duty)

            if fan_status is False:
               self.syslog.warning('SET new_perc to %d (FAN fault. fan_num:%d)', max_duty, x)
               fan.set_fan_duty_cycle(max_duty)


        #Find if current duty matched any of define duty
        #If not, set it to highest one
        cur_duty_cycle = fan.get_fan_duty_cycle()
        new_duty_cycle = DUTY_DEF
        for x in range(0, len(fan_policy)):
            if cur_duty_cycle == fan_policy[x][0]:
                break
        if x == len(fan_policy) :
            fan.set_fan_duty_cycle(fan_policy[0][0])
            cur_duty_cycle = max_duty

        #Decide fan duty by if sum of sensors falls into any of fan_policy{}
        get_temp = thermal.get_thermal_temp()
        fan_insert_after_all_fan_removed = 0

        if get_temp > CRITICAL_TEMP:
           self.syslog.warning('SYSTEM Temperature reaching to critical, shutdown the system')
           system_powerdown()

        if self.num_of_working_fans == 0:
           self.syslog.warning('FAN: Number of working fan == 0, shutdown the system in 60 sec')
           time.sleep(60)
           for x in range(fan.get_idx_fan_start(), fan.get_num_fans()+1):
               if fan.get_fan_present(x) == 1:
                  fan_insert_after_all_fan_removed = 1
                  self.syslog.warning('FAN: fan insert detection, ignore the shutdown')

           if fan_insert_after_all_fan_removed != 1:
              system_powerdown()

        for x in range(0, len(fan_policy)):
            y = len(fan_policy) - x -1 #checked from highest
            if get_temp > fan_policy[y][1] and get_temp < fan_policy[y][2] :
                new_duty_cycle = fan_policy[y][0]
                if (new_duty_cycle == max_duty):
                    self.syslog.warning('Full speed on for high temp: %d',get_temp)

                self.syslog.info('INFO. Sum of temp %d > %d , new_duty_cycle=%d', get_temp, fan_policy[y][1], new_duty_cycle)

        self.syslog.info('INFO. Final duty_cycle=%d', new_duty_cycle)

        if(fan_status is True):
           if(new_duty_cycle != cur_duty_cycle):
              fan.set_fan_duty_cycle(new_duty_cycle)

        return True

def sig_handler(signum, frame):
    fan = FanUtil()
    self.syslog.critical('INFO:Cause signal %d, set fan speed max.', signum)
    fan.set_fan_duty_cycle(DUTY_MAX)
    sys.exit(0)

def main(argv):
    log_level = logging.INFO
    log_console = 0
    log_file = ""

    if len(sys.argv) != 1:
        try:
            opts, args = getopt.getopt(argv,'hdl')
        except getopt.GetoptError:
            print 'Usage: %s [-d]' % sys.argv[0]
            return 0
        for opt, arg in opts:
            if opt == '-h':
                print 'Usage: %s [-d] [-l]' % sys.argv[0]
                return 0
            elif opt in ('-d'):
                log_console = 1 
            elif opt in ('-l'):
                log_file = '%s.log' % sys.argv[0]

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)
    monitor = accton_as7816_monitor(log_console, log_file)

    # Loop forever, doing something useful hopefully:
    while True:
        monitor.manage_fans()
        time.sleep(10)

if __name__ == '__main__':
    main(sys.argv[1:])
