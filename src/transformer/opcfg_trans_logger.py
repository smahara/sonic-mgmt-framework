#!/usr/bin/python

import traceback

LOG_PFX = "TRANSFORMER"

import logging
logging.basicConfig(filename='/tmp/transformer.log', level=logging.DEBUG)

def log_dbg_msg(filename, msg):
    try:
	    logging.debug(LOG_PFX + "[" + filename + "]:" + msg)
    except Exception as e :
	    msg = "Exception while logging message: "  + str(msg) + ". Exception: " + e.message
	    logging.exception(msg)

def log_err_msg(filename, msg):
    try:
	    logging.error(LOG_PFX + "[" + filename + "]:" + msg)
    except Exception as e :
 	    msg = "Exception while logging message: "  + str(msg) + ". Exception: " + e.message
	    logging.exception(msg)

def log_exception_msg(filename, msg):
    try:
        logging.error(LOG_PFX + "[" + filename + "]:" + msg)
    except Exception as e :
        msg = "Exception while logging message: "  + str(msg) + ". Exception: " + e.message
        logging.exception(msg)
    # msg+=repr(traceback.format_exc())
    # print(msg)
