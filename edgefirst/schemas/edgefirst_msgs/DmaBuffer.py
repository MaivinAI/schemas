from dataclasses import dataclass
from ..std_msgs import Header
from pycdr2 import IdlStruct
from pycdr2.types import uint32, int32


@dataclass
class DmaBuffer(IdlStruct, typename='DmaBuffer'):
    header: Header = Header() # Metadata including timestamp and coordinate frame
    pid: uint32 = 0 # The process id of the service that created the DMA buffer
    fd: int32 = 0 # The file descriptor of the DMA buffer
    width: uint32 = 0 # The width of the image in pixels
    height: uint32 = 0 # The height of the image in pixels
    stride: uint32 = 0 # The stride of the image in bytes
    fourcc: uint32 = 0 # The fourcc code of the image
    length: uint32 = 0 # The length of the DMA buffer in bytes, used to mmap the buffer

