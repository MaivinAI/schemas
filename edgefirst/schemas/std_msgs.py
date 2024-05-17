from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import (float32, float64, int8, int16, int32,
                          int64, uint8, uint16, uint32, uint64,
                          bounded_str, sequence)
from . import default_field
from .builtin_interfaces import Time

@dataclass
class MultiArrayDimension(IdlStruct, typename='std_msgs/MultiArrayDimension'):
    """
    This was originally provided as an example message.
    It is deprecated as of Foxy
    It is recommended to create your own semantically meaningful message.
    However if you would like to continue using this please use the equivalent in example_msgs.
    """
    label: str = ''
    """
    label of given dimension
    """
    size: uint32 = 0 
    """
    size of given dimension (in type units)
    """
    stride: uint32 = 0 
    """
    stride of given dimension
    """

@dataclass
class MultiArrayLayout(IdlStruct, typename='std_msgs/MultiArrayLayout'):
    """
    This was originally provided as an example message.
    It is deprecated as of Foxy
    It is recommended to create your own semantically meaningful message.
    However if you would like to continue using this please use the equivalent in example_msgs.

    The multiarray declares a generic multi-dimensional array of a
    particular data type.  Dimensions are ordered from outer most
    to inner most.
    
    Accessors should ALWAYS be written in terms of dimension stride
    and specified outer-most dimension first.
    
    multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]
    
    A standard, 3-channel 640x480 image with interleaved color channels
    would be specified as:
    
    dim[0].label  = "height"
    dim[0].size   = 480
    dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)
    dim[1].label  = "width"
    dim[1].size   = 640
    dim[1].stride = 3*640 = 1920
    dim[2].label  = "channel"
    dim[2].size   = 3
    dim[2].stride = 3
    
    multiarray(i,j,k) refers to the ith row, jth column, and kth channel.
    """
    dim: sequence[MultiArrayDimension] = default_field([])
    """
    Array of dimension properties
    """
    data_offset: uint32 = 0
    """
    padding bytes at front of data
    """

@dataclass
class Bool(IdlStruct, typename='std_msgs/Bool'):
    """
    This was originally provided as an example message.
    It is deprecated as of Foxy
    It is recommended to create your own semantically meaningful message.
    However if you would like to continue using this please use the equivalent in example_msgs.
    """
    data: bool = False

@dataclass
class Byte(IdlStruct, typename='std_msgs/Byte'):
    """
    This was originally provided as an example message.
    It is deprecated as of Foxy
    It is recommended to create your own semantically meaningful message.
    However if you would like to continue using this please use the equivalent in example_msgs.
    """
    data: bytes = None

@dataclass
class ByteMultiArray(IdlStruct, typename='std_msgs/ByteMultiArray'):
    """
    This was originally provided as an example message.
    It is deprecated as of Foxy
    It is recommended to create your own semantically meaningful message.
    However if you would like to continue using this please use the equivalent in example_msgs.

    Please look at the MultiArrayLayout message definition for
    documentation on all multiarrays.
    """
    layout: MultiArrayLayout = default_field(MultiArrayLayout)
    """
    specification of data layout
    """
    data: sequence[bytes] = default_field([])
    """
    array of data
    """

@dataclass
class Char(IdlStruct, typename='std_msgs/Char'):
    """
    This was originally provided as an example message.
    It is deprecated as of Foxy
    It is recommended to create your own semantically meaningful message.
    However if you would like to continue using this please use the equivalent in example_msgs.
    """
    data: bounded_str[1] = ''

@dataclass
class ColorRGBA(IdlStruct, typename='std_msgs/ColorRGBA'):
    r: float32 = 0
    g: float32 = 0
    b: float32 = 0
    a: float32 = 0

@dataclass
class Float32(IdlStruct, typename='std_msgs/Float32'):
    """
    This was originally provided as an example message.
    It is deprecated as of Foxy
    It is recommended to create your own semantically meaningful message.
    However if you would like to continue using this please use the equivalent in example_msgs.
    """
    data: float32 = 0

@dataclass
class Float32MultiArray(IdlStruct, typename='std_msgs/Float32MultiArray'):
    """
    This was originally provided as an example message.
    It is deprecated as of Foxy
    It is recommended to create your own semantically meaningful message.
    However if you would like to continue using this please use the equivalent in example_msgs.

    Please look at the MultiArrayLayout message definition for
    documentation on all multiarrays.
    """
    layout: MultiArrayLayout = default_field(MultiArrayLayout)
    """
    specification of data layout
    """
    data: sequence[float32] = default_field([]) 
    """
    array of data
    """

@dataclass
class Float64(IdlStruct, typename='std_msgs/Float64'):
    """
    This was originally provided as an example message.
    It is deprecated as of Foxy
    It is recommended to create your own semantically meaningful message.
    However if you would like to continue using this please use the equivalent in example_msgs.
    """
    data: float64 = 0

@dataclass
class Float64MultiArray(IdlStruct, typename='std_msgs/Float64MultiArray'):
    """
    This was originally provided as an example message.
    It is deprecated as of Foxy
    It is recommended to create your own semantically meaningful message.
    However if you would like to continue using this please use the equivalent in example_msgs.

    Please look at the MultiArrayLayout message definition for
    documentation on all multiarrays.
    """
    layout: MultiArrayLayout = default_field(MultiArrayLayout)
    """
    specification of data layout
    """
    data: sequence[float64] = default_field([]) 
    """
    array of data
    """

@dataclass
class Header(IdlStruct, typename='std_msgs/Header'):
    """
    Standard metadata for higher-level stamped data types.
    This is generally used to communicate timestamped data
    in a particular coordinate frame.
    """
    stamp: Time = default_field(Time)
    """
    Two-integer timestamp that is expressed as seconds and nanoseconds.
    """
    frame_id: str = '' 
    """
    Transform frame with which this data is associated.
    """

@dataclass
class Int8(IdlStruct, typename='std_msgs/Int8'):
    """
    This was originally provided as an example message.
    It is deprecated as of Foxy
    It is recommended to create your own semantically meaningful message.
    However if you would like to continue using this please use the equivalent in example_msgs.
    """
    data: int8 = 0

@dataclass
class Int8MultiArray(IdlStruct, typename='std_msgs/Int8MultiArray'):
    """
    This was originally provided as an example message.
    It is deprecated as of Foxy
    It is recommended to create your own semantically meaningful message.
    However if you would like to continue using this please use the equivalent in example_msgs.

    Please look at the MultiArrayLayout message definition for
    documentation on all multiarrays.
    """
    layout: MultiArrayLayout = default_field(MultiArrayLayout)
    """
    specification of data layout
    """
    data: sequence[int8] = default_field([]) 
    """
    array of data
    """

@dataclass
class Int16(IdlStruct, typename='std_msgs/Int16'):
    """
    This was originally provided as an example message.
    It is deprecated as of Foxy
    It is recommended to create your own semantically meaningful message.
    However if you would like to continue using this please use the equivalent in example_msgs.
    """
    data: int16 = 0

@dataclass
class Int16MultiArray(IdlStruct, typename='std_msgs/Int16MultiArray'):
    """
    This was originally provided as an example message.
    It is deprecated as of Foxy
    It is recommended to create your own semantically meaningful message.
    However if you would like to continue using this please use the equivalent in example_msgs.

    Please look at the MultiArrayLayout message definition for
    documentation on all multiarrays.
    """
    layout: MultiArrayLayout = default_field(MultiArrayLayout)
    """
    specification of data layout
    """
    data: sequence[int16] = default_field([]) 
    """
    array of data
    """

@dataclass
class Int32(IdlStruct, typename='std_msgs/Int32'):
    """
    This was originally provided as an example message.
    It is deprecated as of Foxy
    It is recommended to create your own semantically meaningful message.
    However if you would like to continue using this please use the equivalent in example_msgs.
    """
    data: int32 = 0

@dataclass
class Int32MultiArray(IdlStruct, typename='std_msgs/Int32MultiArray'):
    """
    This was originally provided as an example message.
    It is deprecated as of Foxy
    It is recommended to create your own semantically meaningful message.
    However if you would like to continue using this please use the equivalent in example_msgs.

    Please look at the MultiArrayLayout message definition for
    documentation on all multiarrays.
    """
    layout: MultiArrayLayout = default_field(MultiArrayLayout)
    """
    specification of data layout
    """
    data: sequence[int32] = default_field([]) 
    """
    array of data
    """

@dataclass
class Int64(IdlStruct, typename='std_msgs/Int64'):
    """
    This was originally provided as an example message.
    It is deprecated as of Foxy
    It is recommended to create your own semantically meaningful message.
    However if you would like to continue using this please use the equivalent in example_msgs.
    """
    data: int64 = 0

@dataclass
class Int64MultiArray(IdlStruct, typename='std_msgs/Int64MultiArray'):
    """
    This was originally provided as an example message.
    It is deprecated as of Foxy
    It is recommended to create your own semantically meaningful message.
    However if you would like to continue using this please use the equivalent in example_msgs.

    Please look at the MultiArrayLayout message definition for
    documentation on all multiarrays.
    """
    layout: MultiArrayLayout = default_field(MultiArrayLayout)
    """
    specification of data layout
    """
    data: sequence[int64] = default_field([]) 
    """
    array of data
    """

@dataclass
class String(IdlStruct, typename='std_msgs/String'):
    """
    This was originally provided as an example message.
    It is deprecated as of Foxy
    It is recommended to create your own semantically meaningful message.
    However if you would like to continue using this please use the equivalent in example_msgs.
    """
    data: str = ''

@dataclass
class Uint8(IdlStruct, typename='std_msgs/Uint8'):
    """
    This was originally provided as an example message.
    It is deprecated as of Foxy
    It is recommended to create your own semantically meaningful message.
    However if you would like to continue using this please use the equivalent in example_msgs.
    """
    data: uint8 = 0

@dataclass
class Uint8MultiArray(IdlStruct, typename='std_msgs/Uint8MultiArray'):
    """
    This was originally provided as an example message.
    It is deprecated as of Foxy
    It is recommended to create your own semantically meaningful message.
    However if you would like to continue using this please use the equivalent in example_msgs.

    Please look at the MultiArrayLayout message definition for
    documentation on all multiarrays.
    """
    layout: MultiArrayLayout = default_field(MultiArrayLayout)
    """
    specification of data layout
    """
    data: sequence[uint8] = default_field([]) 
    """
    array of data
    """

@dataclass
class Uint16(IdlStruct, typename='std_msgs/Uint16'):
    """
    This was originally provided as an example message.
    It is deprecated as of Foxy
    It is recommended to create your own semantically meaningful message.
    However if you would like to continue using this please use the equivalent in example_msgs.
    """
    data: uint16 = 0

@dataclass
class Uint16MultiArray(IdlStruct, typename='std_msgs/Uint16MultiArray'):
    """
    This was originally provided as an example message.
    It is deprecated as of Foxy
    It is recommended to create your own semantically meaningful message.
    However if you would like to continue using this please use the equivalent in example_msgs.

    Please look at the MultiArrayLayout message definition for
    documentation on all multiarrays.
    """
    layout: MultiArrayLayout = default_field(MultiArrayLayout)
    """
    specification of data layout
    """
    data: sequence[uint16] = default_field([]) 
    """
    array of data
    """

@dataclass
class Uint32(IdlStruct, typename='std_msgs/Uint32'):
    """
    This was originally provided as an example message.
    It is deprecated as of Foxy
    It is recommended to create your own semantically meaningful message.
    However if you would like to continue using this please use the equivalent in example_msgs.
    """
    data: uint32 = 0

@dataclass
class Uint32MultiArray(IdlStruct, typename='std_msgs/Uint32MultiArray'):
    """
    This was originally provided as an example message.
    It is deprecated as of Foxy
    It is recommended to create your own semantically meaningful message.
    However if you would like to continue using this please use the equivalent in example_msgs.

    Please look at the MultiArrayLayout message definition for
    documentation on all multiarrays.
    """
    layout: MultiArrayLayout = default_field(MultiArrayLayout)
    """
    specification of data layout
    """
    data: sequence[uint32] = default_field([]) 
    """
    array of data
    """

@dataclass
class Uint64(IdlStruct, typename='std_msgs/Uint64'):
    """
    This was originally provided as an example message.
    It is deprecated as of Foxy
    It is recommended to create your own semantically meaningful message.
    However if you would like to continue using this please use the equivalent in example_msgs.
    """
    data: uint64 = 0

@dataclass
class Uint64MultiArray(IdlStruct, typename='std_msgs/Uint64MultiArray'):
    """
    This was originally provided as an example message.
    It is deprecated as of Foxy
    It is recommended to create your own semantically meaningful message.
    However if you would like to continue using this please use the equivalent in example_msgs.

    Please look at the MultiArrayLayout message definition for
    documentation on all multiarrays.
    """
    layout: MultiArrayLayout = default_field(MultiArrayLayout)
    """
    specification of data layout
    """
    data: sequence[uint64] = default_field([]) 
    """
    array of data
    """