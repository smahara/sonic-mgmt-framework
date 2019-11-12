#!/usr/bin/env python

#############################################################################
#
# Module contains an implementation of SONiC Platform Base API and
# provides the SFP management routines
#
#############################################################################

try:
    from sonic_platform_base.sfp_base import SfpBase
except ImportError as e:
    raise ImportError(str(e) + "- required module not found")

class Sfp(SfpBase):
    """Platform-specific Sfp class"""

    def __init__(self, sfp_index):
        SfpBase.__init__(self)
        self.index = sfp_index

    def get_presence(self):
        """
        Retrieves the presence of the device

        Returns:
            bool: True if device is present, False if not
        """
        raise NotImplementedError

    def get_transceiver_info(self):
        """
        Retrieves transceiver info of this SFP

        Returns:
            A dict which contains following keys/values :
        ========================================================================
        keys                       |Value Format   |Information	
        ---------------------------|---------------|----------------------------
        type                       |1*255VCHAR     |type of SFP
        hardwarerev                |1*255VCHAR     |hardware version of SFP
        serialnum                  |1*255VCHAR     |serial number of the SFP
        manufacturename            |1*255VCHAR     |SFP vendor name
        modelname                  |1*255VCHAR     |SFP model name
        Connector                  |1*255VCHAR     |connector information
        encoding                   |1*255VCHAR     |encoding information
        ext_identifier             |1*255VCHAR     |extend identifier
        ext_rateselect_compliance  |1*255VCHAR     |extended rateSelect compliance
        cable_length               |INT            |cable length in m
        mominal_bit_rate           |INT            |nominal bit rate by 100Mbs
        specification_compliance   |1*255VCHAR     |specification compliance
        vendor_date                |1*255VCHAR     |vendor date
        vendor_oui                 |1*255VCHAR     |vendor OUI
        ========================================================================
        """
        raise NotImplementedError

    def get_transceiver_bulk_status(self):
        """
        Retrieves transceiver bulk status of this SFP

        Returns:
            A dict which contains following keys/values :
        ========================================================================
        keys                       |Value Format   |Information	
        ---------------------------|---------------|----------------------------
        RX LOS                     |BOOLEAN        |RX lost-of-signal status,
                                   |               |True if has RX los, False if not.
        TX FAULT                   |BOOLEAN        |TX fault status,
                                   |               |True if has TX fault, False if not.
        Reset status               |BOOLEAN        |reset status,
                                   |               |True if SFP in reset, False if not.
        LP mode                    |BOOLEAN        |low power mode status,
                                   |               |True in lp mode, False if not.
        TX disable                 |BOOLEAN        |TX disable status,
                                   |               |True TX disabled, False if not.
        TX disabled channel        |HEX            |disabled TX channles in hex,
                                   |               |bits 0 to 3 represent channel 0
                                   |               |to channel 3.
        Temperature                |INT            |module temperature in Celsius
        Voltage                    |INT            |supply voltage in mV
        TX bias                    |INT            |TX Bias Current in mA
        RX power                   |INT            |received optical power in mW
        TX power                   |INT            |TX output power in mW
        ========================================================================
        """
        raise NotImplementedError
