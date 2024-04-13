# Radar Cube Message Interface - edgefirst/msg/RadarCube
#
# The RadarCube interface carries various radar cube reprensentations of the
# Radar FFT before generally being processed by CFAR into a point cloud.  The
# cube coud be R, RD, RAD, RA, and so on where R=Range, D=Dopper, and A=Azimuth.

# Dimensional labels are used to describe the radar cube layout.  Not all cubes
# include every label.  Undefined is used for dimensions not covered by this list.
uint8 UNDEFINED = 0
uint8 RANGE = 1
uint8 DOPPLER = 2
uint8 AZIMUTH = 3
uint8 ELEVATION = 4
uint8 RXCHANNEL = 5
uint8 SEQUENCE = 6

std_msgs/Header header

uint64 timestamp    # Radar frame timestamp generated on the radar module
uint8[] layout      # Radar cube layout provides labels for each dimensions
uint16[] shape      # Radar cube shape provides the shape of each dimensions
float32[] scales    # The scaling factors for the dimensions representing bins
                    # For dimensions taken "as-is" the scale will be 1.0
int16[] cube        # The radar cube data as 16bit integers.  If the is_complex
                    # is true then each element will be pairs of integers with
                    # the first being real and the second being imaginary
bool is_complex     # True if the radar cube is complex in which case the final
                    # dimension will be doubled in size to account for the pair
                    # of int16 elements representing [real,imaginary].