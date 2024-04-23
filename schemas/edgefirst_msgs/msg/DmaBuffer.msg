# DMA Buffer Message Interface - edgefirst/dma/buffer
#
# The dma interface carries raw camera information 


std_msgs/Header header        # Metadata including timestamp and coordinate frame

uint32 pid        # The process id of the service that created the DMA buffer
int32 fd          # The file descriptor of the DMA buffer
uint32 width      # The width of the image in pixels
uint32 height     # The height of the image in pixels
uint32 stride     # The stride of the image in bytes
uint32 fourcc     # The fourcc code of the image
uint32 length     # The length of the DMA buffer in bytes, used to mmap the buffer
