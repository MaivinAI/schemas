# Detect Message Interface - edgefirst/detect/boxes2d
#
# The detect interface carries detection information 


std_msgs/Header header        # Metadata including timestamp and coordinate frame

builtin_interfaces/Time input_timestamp # Timestamp of the input data (e.g., from camera)
builtin_interfaces/Time model_time      # Inference duration for the model to process the image
builtin_interfaces/Time output_time     # Timestamp when the message was sent out

edgefirst_msgs/Box[] boxes          # Array of detected object bounding boxes
                                    # Each box includes normalized center point, width, and height