# Navigation Satellite fix status for any Global Navigation Satellite System.
#
# Whether to output an augmented fix is determined by both the fix
# type and the last time differential corrections were received.  A
# fix is valid when status >= STATUS_FIX.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import uint16, int8
from enum import Enum

class GpsStatus(Enum):
    STATUS_NO_FIX =  -1        # unable to fix position
    STATUS_FIX =      0        # unaugmented fix
    STATUS_SBAS_FIX = 1        # with satellite-based augmentation
    STATUS_GBAS_FIX = 2        # with ground-based augmentation

class GpsService(Enum):
    SERVICE_GPS =     1
    SERVICE_GLONASS = 2
    SERVICE_COMPASS = 4      # includes BeiDou.
    SERVICE_GALILEO = 8

@dataclass
class NavSatStatus(IdlStruct, typename='sensor_msgs/NavSatStatus'):
    status: int8 = 0
    # Bits defining which Global Navigation Satellite System signals were
    # used by the receiver.
    service: uint16 = 0