#!/bin/bash
#set -xe
current_bridges=$(ps aux | grep parameter_bridge | awk '{print $2}')
for id in $current_bridges
do
    kill -9 $id
done

export GZ_VERSION=garden
local_path=$(pwd)
pkill -f ros_gz_bridge
rm -fr ros2_ws
source /opt/ros/iron/setup.sh
src_folders=$(ls -d src/*/)
echo "which package do you want to build?(enter corresponding number.)"
for index in "${!src_folders[@]}"; do
    echo "$index: ${src_folders[index]}"
done
read folder_index
package_name=$(echo "${src_folders[folder_index]}" | sed 's/^src\///;s/\/$//g')
bridges=$(cat bridges.txt | tr ',' ' ')
for bridge in $bridges; do
    ros2 run ros_gz_bridge parameter_bridge $bridge & 
done

mkdir -p $local_path/ros2_ws/src
cd $local_path/ros2_ws/src
ros2 pkg create --build-type ament_python $package_name
cd $local_path
cp -fr src/$package_name ros2_ws/src/$package_name
cp src/package.xml ros2_ws/src/$package_name/package.xml
cp src/setup.py ros2_ws/src/$package_name/setup.py
cd $local_path/ros2_ws/src/$package_name
sed -i "s/<package-name>/$package_name/g" package.xml
sed -i "s/<package-name>/$package_name/g" setup.py
pip3 install -r $package_name/requirements.txt
cd $local_path/ros2_ws/
rosdep install -i --from-path src --rosdistro iron -y
colcon build --packages-select $package_name
source install/setup.bash
ros2 run $package_name $package_name