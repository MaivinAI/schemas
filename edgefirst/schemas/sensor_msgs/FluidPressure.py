# Single pressure reading.  This message is appropriate for measuring the
# pressure inside of a fluid (air, water, etc).  This also includes
# atmospheric or barometric pressure.
#
# This message is not appropriate for force/pressure contact sensors.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float64
from ..std_msgs.Header import Header

@dataclass
class FluidPressure(IdlStruct, typename='sensor_msgs/FluidPressure'):
    header: Header = Header() # timestamp of the measurement
                            # frame_id is the location of the pressure sensor
    fluid_pressure: float64 = 0 # Absolute pressure reading in Pascals.
    variance: float64 = 0 # 0 is interpreted as variance unknown