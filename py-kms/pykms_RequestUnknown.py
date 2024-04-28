#!/usr/bin/env python3

import struct
import logging

from pykms_Base import kmsBase
from pykms_Misc import ErrorCodes
from pykms_Format import pretty_printer

#---------------------------------------------------------------------------------------------------------------------------------------------------------

loggersrv = logging.getLogger('logsrv')

class kmsRequestUnknown(kmsBase):
        def executeRequestLogic(self):
                finalResponse = bytearray()
                finalResponse.extend(bytearray(struct.pack('<I', 0)))
                finalResponse.extend(bytearray(struct.pack('<I', 0)))
                finalResponse.extend(bytearray(struct.pack('<I', ErrorCodes['SL_E_VL_KEY_MANAGEMENT_SERVICE_ID_MISMATCH'][0])))
                finalResponse=bytes(finalResponse)
#               finalResponse=finalResponse.decode('utf-8'.encode('utf-8')
                return finalResponse
