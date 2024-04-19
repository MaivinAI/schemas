# This was originally provided as an example message.
# It is deprecated as of Foxy
# It is recommended to create your own semantically meaningful message.
# However if you would like to continue using this please use the equivalent in example_msgs.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import uint32

@dataclass
class Uint32(IdlStruct, typename='std_msgs/Uint32'):
    data: uint32 = 0
