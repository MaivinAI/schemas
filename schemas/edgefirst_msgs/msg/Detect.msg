# Detect Message Interface - edgefirst/detect/boxes2d
#
# The detect interface carries detection information 


std_msgs/Header header        # Metadata including timestamp and coordinate frame

builtin_interfaces/Time input_timestamp # Timestamp of the input data (e.g., from camera)
builtin_interfaces/Time model_time      # Inference duration for the model to process the image
builtin_interfaces/Time output_time     # Timestamp when the message was sent out

edgefirst_msgs/Box[] boxes          # Array of detected object bounding boxes
                     # Each box includes normalized center point, width, and height

================================================================================
# Definition of a bounding box
# Represents a detected object's location in an image
# Normalized coordinates range from 0.0 to 1.0
# (0.0 being the top/left and 1.0 being the bottom/right)
MSG: edgefirst_msgs/Box
float32 center_x   # Normalized x-coordinate of the center
float32 center_y   # Normalized y-coordinate of the center
float32 width      # Normalized width of the box
float32 height     # Normalized height of the box
uint32 label      # object label
float32 score     # confidence score for detection
float32 distance  # Distance of object (if known)
float32 speed     # Speed of object (if known)
bool is_tracked    # Is the object being tracked
edgefirst_msgs/Track track       # object tracking, each track includes ID and lifetime information

================================================================================
# Definition of an object track
# Represents the trajectory and lifetime of a detected object
MSG: edgefirst_msgs/Track
string id           # Unique identifier for the object track
int32 lifetime     # Number of consecutive frames the object has been tracked
builtin_interfaces/Time created       # Time the track was first added

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data
# in a particular coordinate frame.

# Two-integer timestamp that is expressed as seconds and nanoseconds.
builtin_interfaces/Time stamp

# Transform frame with which this data is associated.
string frame_id

================================================================================
MSG: builtin_interfaces/Time
# This message communicates ROS Time defined here:
# https://design.ros2.org/articles/clock_and_time.html

# The seconds component, valid over all int32 values.
int32 sec

# The nanoseconds component, valid in the range [0, 10e9].
uint32 nanosec