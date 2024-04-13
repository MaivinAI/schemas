#![doc = include_str!("../README.md")]

/// # Schemas
///
/// Common Rust struct for ROS 2 messages used by Maivin EdgeFirst Services with Zenoh.
///
/// Here are some ROS message source:
/// * [common_interface](https://github.com/ros2/common_interfaces): Common-used ROS message
/// * [rcl_interface](https://github.com/ros2/rcl_interfaces): Common interface in RCL
/// * [foxglove_api_msgs](https://github.com/foxglove/schemas/tree/main/ros_foxglove_msgs)
/// * [edgefirst_api_msgs](https://github.com/MaivinAI/schemas): EdgeFirst ROS messages

pub mod common_interfaces;
pub mod rcl_interfaces;
pub mod foxglove_msgs;
pub mod edgefirst_msgs;
pub mod service;

pub use common_interfaces::*;
pub use rcl_interfaces::*;
pub use foxglove_msgs::*;
pub use edgefirst_msgs::*;
