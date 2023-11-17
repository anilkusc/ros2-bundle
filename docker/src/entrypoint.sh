#!/bin/bash
#set -xe
source /opt/ros/iron/setup.bash
bridges=$(echo $1 | tr ',' ' ')
for bridge in $bridges; do
    ros2 run ros_gz_bridge parameter_bridge $bridge &
done
source install/setup.bash
ros2 run $2 $2 &
ign gazebo $3 -v4 -s -r --headless-rendering --record