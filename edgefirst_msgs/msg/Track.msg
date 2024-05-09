# Track Message Interface - edgefirst/msg/Track
#
# The Track message has the track attributes

string id           # Unique identifier for the object track (if the object is not tracked then "")
int32 lifetime      # Number of consecutive frames the object has been tracked
builtin_interfaces/Time created       # Time the track was first added