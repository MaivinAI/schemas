use serde_derive::{Deserialize, Serialize};

const NSEC_IN_SEC: u64 = 1_000_000_000;

#[derive(Serialize, Deserialize, PartialEq, Clone, Debug)]
pub struct Time {
    pub sec: i32,
    pub nanosec: u32,
}

#[derive(Serialize, Deserialize, PartialEq, Clone, Debug)]
pub struct Duration {
    pub sec: i32,
    pub nanosec: u32,
}

impl Time {
    pub fn new(sec: i32, nanosec: u32) -> Self {
        Time { sec, nanosec }
    }

    pub fn from_nanos(nanos: u64) -> Self {
        Time {
            sec: (nanos / NSEC_IN_SEC) as i32,
            nanosec: (nanos % NSEC_IN_SEC) as u32,
        }
    }

    pub fn to_nanos(&self) -> u64 {
        self.sec as u64 * NSEC_IN_SEC + self.nanosec as u64
    }
}

impl From<Time> for u64 {
    fn from(time: Time) -> Self {
        time.to_nanos()
    }
}
