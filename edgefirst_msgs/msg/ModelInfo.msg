# Message for representing information about a machine learning model
# Typically used to communicate details about a model over ROS
# Define constants for data types

uint8 RAW     = 0
uint8 INT8    = 1
uint8 UINT8   = 2
uint8 INT16   = 3
uint8 UINT16  = 4
uint8 FLOAT16 = 5
uint8 INT32   = 6
uint8 UINT32  = 7
uint8 FLOAT32 = 8
uint8 INT64   = 9
uint8 UINT64  = 10
uint8 FLOAT64 = 11
uint8 STRING  = 12

std_msgs/Header header          # Metadata including timestamp and coordinate frame
uint32[] input_shape     # Shape of the input tensor(s) in the format "height,width,channels" or "height,width,depth,channels"
uint8 input_type      # Data type of the input tensor(s) (e.g., "float32", "uint8")
uint32[] output_shape    # Shape of the output tensor(s) in the format "height,width,channels" or "height,width,depth,channels"
uint8 output_type     # Data type of the output tensor(s) (e.g., "float32", "uint8")
string[] labels        # Array of strings representing the labels used by the model, empty if no labels available
string model_types     # Model tasks/types (e.g., ["object_detection", "classification"])
string model_format    # Format of the model (e.g., "DeepViewRT", "HailoRT", "RKNN", "TensorRT", "TFLite")
string model_name      # Name of the model (if available), otherwise use filename without extension or path
