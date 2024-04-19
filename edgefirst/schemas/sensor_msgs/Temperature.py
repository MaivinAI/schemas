# Single temperature reading.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float64
from ..std_msgs.Header import Header

@dataclass
class Temperature(IdlStruct, typename='sensor_msgs/Temperature'):
    header: Header = Header() # timestamp is the time the temperature was measured
                              # frame_id is the location of the temperature reading

    temperature: float64 = 0  # Measurement of the Temperature in Degrees Celsius.

    variance: float64 = 0     # 0 is interpreted as variance unknown.