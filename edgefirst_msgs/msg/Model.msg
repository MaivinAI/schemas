# Model Message Interface - edgefirst/msg/Model
#
# The model interface carries model inference results.

std_msgs/Header header        # Metadata including timestamp and coordinate frame

builtin_interfaces/Duration input_time      # Duration to load inputs into the model
builtin_interfaces/Duration model_time      # Duration to run the model, not including input/output/decoding
builtin_interfaces/Duration output_time     # Duration to read outputs from the model
builtin_interfaces/Duration decode_time     # Duration to decode the outputs from the model, including nms and tracking.

edgefirst_msgs/Box[] boxes          # Array of detected object bounding boxes
                                    # Each box includes normalized center point, width, and height
edgefirst_msgs/Mask[] masks         # Segmentation mask from the model.
