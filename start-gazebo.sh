#!/bin/bash
#set -xe
world_folders=($(ls worlds))
echo "which world do you want to start?(enter corresponding number.)"
for index in "${!world_folders[@]}"; do
    echo "$index: ${world_folders[index]}"
done
read world_index
world_name="${world_folders[world_index]}"
ign gazebo worlds/$world_name -v4 -r