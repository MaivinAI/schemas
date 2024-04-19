# Single reading from a relative humidity sensor.
# Defines the ratio of partial pressure of water vapor to the saturated vapor
# pressure at a temperature.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float64
from ..std_msgs.Header import Header

@dataclass
class RelativeHumidity(IdlStruct, typename='sensor_msgs/RelativeHumidity'):
    header: Header = Header()      # timestamp of the measurement
                                   # frame_id is the location of the humidity sensor

    relative_humidity: float64 = 0 # Expression of the relative humidity
                                   # from 0.0 to 1.0.
                                   # 0.0 is no partial pressure of water vapor
                                   # 1.0 represents partial pressure of saturation

    variance: float64 = 0          # 0 is interpreted as variance unknown