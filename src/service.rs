use serde_derive::{Deserialize, Serialize};

/// The struct is used by ROS service.
/// If you want to sent ROS service with Zenoh directly. You should include the header.

#[derive(Serialize, Deserialize, PartialEq, Clone, Debug)]
pub struct ServiceHeader {
    pub guid: i64,
    pub seq: u64,
}
