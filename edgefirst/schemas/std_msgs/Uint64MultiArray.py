# This was originally provided as an example message.
# It is deprecated as of Foxy
# It is recommended to create your own semantically meaningful message.
# However if you would like to continue using this please use the equivalent in example_msgs.

# Please look at the MultiArrayLayout message definition for
# documentation on all multiarrays.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import uint64, sequence
from .MultiArrayLayout import MultiArrayLayout
from .. import default_field

@dataclass
class Uint64MultiArray(IdlStruct, typename='std_msgs/Uint64MultiArray'):
    layout: MultiArrayLayout = MultiArrayLayout() # specification of data layout
    data: sequence[uint64] = default_field([])          # array of data