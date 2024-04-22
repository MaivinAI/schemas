from dataclasses import dataclass, field
import copy
from pycdr2 import IdlStruct
from pycdr2.types import uint32, int32 

def default_field(obj):
    return field(default_factory=lambda: copy.copy(obj))

@dataclass
class Time(IdlStruct, typename='Time'):
    sec: int32 = 0
    nanosec: uint32 = 0

@dataclass
class Header(IdlStruct, typename='Header'):
    stamp: Time = Time()
    frame_id: str = ''

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

