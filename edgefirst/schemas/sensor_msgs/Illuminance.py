# Single photometric illuminance measurement.  Light should be assumed to be
# measured along the sensor's x-axis (the area of detection is the y-z plane).
# The illuminance should have a 0 or positive value and be received with
# the sensor's +X axis pointing toward the light source.
#
# Photometric illuminance is the measure of the human eye's sensitivity of the
# intensity of light encountering or passing through a surface.
#
# All other Photometric and Radiometric measurements should not use this message.
# This message cannot represent:
#  - Luminous intensity (candela/light source output)
#  - Luminance (nits/light output per area)
#  - Irradiance (watt/area), etc.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float64
from ..std_msgs.Header import Header

@dataclass
class Illuminance(IdlStruct, typename='sensor_msgs/Illuminance'):
    header: Header = Header() # timestamp is the time the illuminance was measured
                              # frame_id is the location and direction of the reading
    illuminance: float64 = 0 # Measurement of the Photometric Illuminance in Lux.
    variance: float64 = 0 # 0 is interpreted as variance unknown