# Date Type Definition

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import uint16, uint8


@dataclass
class Date(IdlStruct, typename='edgefirst_msgs/Date'):
    year: uint16 = 0
    month: uint8 = 0
    day: uint8 = 0
