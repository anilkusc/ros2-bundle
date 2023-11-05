FROM osrf/ros:foxy-desktop

SHELL ["/bin/bash", "-c"]

ARG PACKAGE_NAME
ENV PACKAGE_NAME ${PACKAGE_NAME}

RUN apt update && apt install python3-pip -y
#apt install ros-foxy-ros-core ros-foxy-geometry2

WORKDIR /root/ros2_ws/src

RUN source /opt/ros/foxy/setup.sh && ros2 pkg create --build-type ament_python $PACKAGE_NAME

WORKDIR /root/ros2_ws/src/$PACKAGE_NAME 

COPY $PACKAGE_NAME $PACKAGE_NAME

RUN pip3 install -r $PACKAGE_NAME/requirements.txt
COPY package.xml package.xml
RUN sed -i "s/<package-name>/$PACKAGE_NAME/g" package.xml
COPY setup.py setup.py
RUN sed -i "s/<package-name>/$PACKAGE_NAME/g" setup.py

WORKDIR /root/ros2_ws
RUN source /opt/ros/foxy/setup.sh && rosdep install -i --from-path src --rosdistro foxy -y
RUN source /opt/ros/foxy/setup.sh && colcon build --packages-select $PACKAGE_NAME
CMD source install/setup.bash && ros2 run $PACKAGE_NAME $PACKAGE_NAME
