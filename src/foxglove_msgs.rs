use crate::{
    builtin_interfaces,
    std_msgs::{self},
};
use serde_derive::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, PartialEq, Clone)]
pub struct FoxgloveCompressedVideo {
    pub header: std_msgs::Header,
    pub data: Vec<u8>,
    pub format: String,
}

#[derive(Serialize, Deserialize, PartialEq, Clone)]
pub struct FoxgloveImageAnnotations {
    pub circles: Vec<FoxgloveCircleAnnotations>,
    pub points: Vec<FoxglovePointAnnotations>,
    pub texts: Vec<FoxgloveTextAnnotations>,
}

#[derive(Serialize, Deserialize, PartialEq, Clone)]
pub struct FoxgloveCircleAnnotations {
    pub timestamp: builtin_interfaces::Time,
    pub position: FoxglovePoint2,
    pub diameter: f64,
    pub thickness: f64,
    pub fill_color: FoxgloveColor,
    pub outline_color: FoxgloveColor,
}

pub mod point_annotation_type {
    pub const UNKNOWN: u8 = 0;

    // Individual points: 0, 1, 2, ...
    pub const POINTS: u8 = 1;

    // Closed polygon: 0-1, 1-2, ..., (n-1)-n, n-0
    pub const LINE_LOOP: u8 = 2;

    // Connected line segments: 0-1, 1-2, ..., (n-1)-n
    pub const LINE_STRIP: u8 = 3;

    // Individual line segments: 0-1, 2-3, 4-5, ...
    pub const LINE_LIST: u8 = 4;
}

#[derive(Serialize, Deserialize, PartialEq, Clone)]
pub struct FoxglovePointAnnotations {
    pub timestamp: builtin_interfaces::Time,
    pub type_: u8,
    pub points: Vec<FoxglovePoint2>,
    pub outline_color: FoxgloveColor,
    pub outline_colors: Vec<FoxgloveColor>,
    pub fill_color: FoxgloveColor,
    pub thickness: f64,
}

#[derive(Serialize, Deserialize, PartialEq, Clone)]
pub struct FoxgloveTextAnnotations {
    pub timestamp: builtin_interfaces::Time,
    pub position: FoxglovePoint2,
    pub text: String,
    pub font_size: f64,
    pub text_color: FoxgloveColor,
    pub background_color: FoxgloveColor,
}

#[derive(Serialize, Deserialize, PartialEq, Clone)]
pub struct FoxglovePoint2 {
    pub x: f64,
    pub y: f64,
}

#[derive(Serialize, Deserialize, PartialEq, Clone)]
pub struct FoxgloveColor {
    pub r: f64,
    pub g: f64,
    pub b: f64,
    pub a: f64,
}
