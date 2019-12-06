#!/usr/bin/env python

try:
    import os.path
    import sys, traceback
    from pddf_sfp import PddfSfp
except ImportError, e:
    raise ImportError (str(e) + "- required module not found")


class Sfp(PddfSfp):
    """
    PDDF Platform-Specific Sfp class
    """

    def __init__(self, index):
        PddfSfp.__init__(self, index)

    # Provide the functions/variables below for which implementation is to be overwritten
