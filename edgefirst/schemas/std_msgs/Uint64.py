# This was originally provided as an example message.
# It is deprecated as of Foxy
# It is recommended to create your own semantically meaningful message.
# However if you would like to continue using this please use the equivalent in example_msgs.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import uint64

@dataclass
class Uint64(IdlStruct, typename='std_msgs/Uint64'):
    data: uint64 = 0
