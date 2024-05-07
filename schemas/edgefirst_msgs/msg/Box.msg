# Box Message Interface - edgefirst/msg/Box
#
# The Box message has the box attributes

float32 center_x   # Normalized x-coordinate of the center
float32 center_y   # Normalized y-coordinate of the center
float32 width      # Normalized width of the box
float32 height     # Normalized height of the box
string label       # object label
float32 score      # confidence score for detection
float32 distance   # Distance of object (if known)
float32 speed      # Speed of object (if known)
edgefirst_msgs/Track track       # object tracking, each track includes ID and lifetime information