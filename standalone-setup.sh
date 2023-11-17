#!/bin/bash
sudo apt update && sudo apt install locales curl software-properties-common -y
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
sudo add-apt-repository universe -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update -y&& sudo apt upgrade -y&& sudo apt install ros-dev-tools ros-iron-desktop ros-iron-ros-base python3-colcon-common-extensions ros-iron-gazebo-ros-pkgs lsb-release wget gnupg python3 python3-pip ros-iron-ros-ign-bridge -y
pip3 install setuptools==58.2.0
source /opt/ros/iron/setup.bash

wget https://packages.osrfoundation.org/gazebo.gpg -O /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null
export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install -y ignition-fortress
