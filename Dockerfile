FROM osrf/ros:iron-desktop-full

SHELL ["/bin/bash", "-c"]

ARG PACKAGE_NAME

WORKDIR /root/ros2_ws/src

RUN source /opt/ros/iron/setup.sh && ros2 pkg create --build-type ament_python $PACKAGE_NAME

COPY src/$PACKAGE_NAME $PACKAGE_NAME/$PACKAGE_NAME
COPY src/package.xml $PACKAGE_NAME/package.xml
COPY src/setup.py $PACKAGE_NAME/setup.py
WORKDIR /root/ros2_ws
RUN source /opt/ros/iron/setup.sh && rosdep install -i --from-path src --rosdistro iron -y
RUN source /opt/ros/iron/setup.sh && colcon build --packages-select $PACKAGE_NAME
RUN source install/setup.bash
CMD sleep infinity
