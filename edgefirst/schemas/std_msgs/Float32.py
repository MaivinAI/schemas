# This was originally provided as an example message.
# It is deprecated as of Foxy
# It is recommended to create your own semantically meaningful message.
# However if you would like to continue using this please use the equivalent in example_msgs.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float32

@dataclass
class Float32(IdlStruct, typename='std_msgs/Float32'):
    data: float32 = 0
