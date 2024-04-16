# Track Message Interface - edgefirst/Track
#
# The Track message has the track attributes

string id           # Unique identifier for the object track
int32 lifetime     # Number of consecutive frames the object has been tracked
builtin_interfaces/Time created       # Time the track was first added