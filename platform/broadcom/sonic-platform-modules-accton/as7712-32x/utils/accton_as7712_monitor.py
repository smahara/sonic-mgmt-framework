#!/usr/bin/env python
#
# Copyright (C) 2019 Accton Technology Corporation
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
#    05/08/2019: Roy Lee, changed for as7712-54x.
# ------------------------------------------------------------------

try:
    import os
    import sys, getopt
    import commands
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
except ImportError as e:
    raise ImportError('%s - required module not found' % str(e))

# Deafults
VERSION = '1.0'
FUNCTION_NAME = 'accton_as7712_monitor'
DUTY_MAX = 100

global log_file
global log_console

# Make a class we can use to capture stdout and sterr in the log
class accton_as7712_monitor(object):
    FAN_NUM_ON_MAIN_BROAD = 6
    FAN_NUM_1_IDX = 1
    FAN_NODE_PATH = '/sys/bus/i2c/devices/2-0066/fan*{0}_{1}'

    llog = logging.getLogger("["+FUNCTION_NAME+"]")
    def __init__(self, log_console, log_file):
        """Needs a logger and a logger level."""

        formatter = logging.Formatter('%(name)s %(message)s')
        sys_handler  = logging.handlers.SysLogHandler(address = '/dev/log')
        sys_handler.setFormatter(formatter)
        sys_handler.ident = 'common'
        sys_handler.setLevel(logging.WARNING)  #only fatal for syslog
        self.llog.addHandler(sys_handler)
        self.llog.setLevel(logging.INFO)

        if log_file:
            fh = logging.FileHandler(log_file)
            fh.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)-15s %(name)s %(message)s')
            fh.setFormatter(formatter)
            self.llog.addHandler(fh)

        # set up logging to console
        if log_console:
            console = logging.StreamHandler()
            console.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)-15s %(name)s %(message)s')
            console.setFormatter(formatter)
            self.llog.addHandler(console)

    def get_fan_to_device_path(self, fan_num, func):
        return self.FAN_NODE_PATH.format(fan_num, func)

    def _get_fan_node_val(self, fan_num, attr):
        if fan_num < self.FAN_NUM_1_IDX or fan_num > self.FAN_NUM_ON_MAIN_BROAD:
            self.llog.debug('GET. Parameter error. fan_num, %d', fan_num)
            return None

        device_path = self.get_fan_to_device_path(fan_num, attr)
        try:
            status, output = commands.getstatusoutput('cat '+ device_path)
        except IOError as e:
            self.llog.error('GET. unable to open file: %s', str(e))
            return None

        if status:
            self.llog.error('GET. unable to open file,  ret:%d', status)
            return None

        content = output.replace(os.linesep,"")
        if content == '':
            self.llog.error('GET. content is NULL. device_path:%s', device_path)
            return None

        return int(content)

    def log_it(self, idx, attr, val):
        if attr == 'present':
            if val:
                self.llog.warning('Info: FAN-%d present is detected', idx)
            else:
                self.llog.warning('Alarm for FAN-%d absent is detected', idx)
        elif attr == 'fault':
            if val:
                self.llog.warning('Alarm for FAN-%d failed is detected', idx)
            else:
                self.llog.warning('Info: FAN-%d becomes operational', idx)


    data = {'present':[0] * FAN_NUM_ON_MAIN_BROAD, 
            'fault':[0] * FAN_NUM_ON_MAIN_BROAD}
    def check_fans(self):
        attrs = self.data.keys()
        for x in range(self.FAN_NUM_ON_MAIN_BROAD):
            idx = x + 1
            for a in attrs:
                stat = self._get_fan_node_val(idx, a)
                if stat is None or stat is False:
                    self.llog.error('Fan %d is %s', index, a)
                    break
                lst = self.data[a]
                if lst[x] != stat:
                    self.log_it(idx, a, stat)
                    lst[x] = stat
        return True

def main(argv):
    log_file = '%s.log' % FUNCTION_NAME
    log_console = 0
    log_file = ""
    if len(sys.argv) != 1:
        try:
            opts, args = getopt.getopt(argv,'hdl')
        except getopt.GetoptError:
            print 'Usage: %s [-d] [-l]' % sys.argv[0]
            return 0
        for opt, arg in opts:
            if opt == '-h':
                print 'Usage: %s [-d] [-l]' % sys.argv[0]
                return 0
            elif opt in ('-d'):
                log_console = 1
            elif opt in ('-l'):
                log_file = '%s.log' % sys.argv[0]

    monitor = accton_as7712_monitor(log_console, log_file)
    # Loop forever, doing something useful hopefully:
    while True:
        monitor.check_fans()
        time.sleep(10)


if __name__ == '__main__':
    main(sys.argv[1:])
