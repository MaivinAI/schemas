# This was originally provided as an example message.
# It is deprecated as of Foxy
# It is recommended to create your own semantically meaningful message.
# However if you would like to continue using this please use the equivalent in example_msgs.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import uint32

@dataclass
class MultiArrayDimension(IdlStruct, typename='std_msgs/MultiArrayDimension'):
    label: str = '' # label of given dimension
    size: uint32 = 0 # size of given dimension (in type units)
    stride: uint32 = 0 # stride of given dimension