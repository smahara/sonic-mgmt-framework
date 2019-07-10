#!/usr/bin/python

import traceback

DEBUG = True
LOG_PFX = "TRANSFORMER"

def log_dbg_msg(filename, msg, dbg_on = DEBUG):
     if DEBUG:
        try:
            print(LOG_PFX + "[" + filename + "]:" + msg)
        except Exception as e :
            msg = "Exception while logging message: "  + str(msg) + ". Exception: " + e.message
            print(msg)

def log_err_msg(filename, msg):
     log_dbg_msg(filename, msg, dbg_on = True)

def log_exception_msg(filename, msg):
    try:
        print(LOG_PFX + "[" + filename + "]:" + msg)
    except Exception as e :
        msg = "Exception while logging message: "  + str(msg) + ". Exception: " + e.message
        print(msg)
    msg+=repr(traceback.format_exc())
    print(msg)
