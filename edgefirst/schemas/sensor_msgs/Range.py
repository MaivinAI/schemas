# Single range reading from an active ranger that emits energy and reports
# one range reading that is valid along an arc at the distance measured.
# This message is  not appropriate for laser scanners. See the LaserScan
# message if you are working with a laser scanner.
#
# This message also can represent a fixed-distance (binary) ranger.  This
# sensor will have min_range===max_range===distance of detection.
# These sensors follow REP 117 and will output -Inf if the object is detected
# and +Inf if the object is outside of the detection range.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float32, uint8
from ..std_msgs.Header import Header
from enum import Enum

class RadiationType(Enum):
    # Radiation type enums
    # If you want a value added to this list, send an email to the ros-users list
    ULTRASOUND=0
    INFRARED=1

@dataclass
class Range(IdlStruct, typename='sensor_msgs/Range'):
    header: Header = Header() # timestamp in the header is the time the ranger
                              # returned the distance reading



    radiation_type: uint8 = 0 # the type of radiation used by the sensor
                              # (sound, IR, etc) [enum]

    field_of_view: float32 = 0 # the size of the arc that the distance reading is
                               # valid for [rad]
                               # the object causing the range reading may have
                               # been anywhere within -field_of_view/2 and
                               # field_of_view/2 at the measured range.
                               # 0 angle corresponds to the x-axis of the sensor.

    min_range: float32 = 0 # minimum range value [m]
    max_range: float32 = 0 # maximum range value [m]
                           # Fixed distance rangers require min_range==max_range

    range: float32 = 0 # range data [m]
                       # (Note: values < range_min or > range_max should be discarded)
                       # Fixed distance rangers only output -Inf or +Inf.
                       # -Inf represents a detection within fixed distance.
                       # (Detection too close to the sensor to quantify)
                       # +Inf represents no detection within the fixed distance.
                       # (Object out of range)