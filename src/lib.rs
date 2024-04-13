/// # Maivin EdgeFirst Schemas
///
/// This library provides the Rust structs for Maivin EdgeFirst messages.
///
/// Common Rust struct for ROS 2 messages used by Maivin EdgeFirst Services with Zenoh.
///
/// Here are some ROS message source:
/// * [common_interface](https://github.com/ros2/common_interfaces): Common-used ROS message
/// * [rcl_interface](https://github.com/ros2/rcl_interfaces): Common interface in RCL
/// * [foxglove_api_msgs](https://github.com/foxglove/schemas/tree/main/ros_foxglove_msgs)
/// * [edgefirst_api_msgs](https://github.com/MaivinAI/schemas): EdgeFirst ROS messages
///

/// EdgeFirst Messages
pub mod edgefirst_msgs;

/// Foxglove Messages
pub mod foxglove_msgs;

/// ROS 2 Common Interfaces
pub mod geometry_msgs;
pub mod sensor_msgs;
pub mod std_msgs;

/// ROS 2 RCL Interfaces
pub mod builtin_interfaces;
pub mod rosgraph_msgs;

pub mod service;
