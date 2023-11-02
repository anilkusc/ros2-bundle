FROM osrf/ros:iron-desktop-full

SHELL ["/bin/bash", "-c"]

ARG PACKAGE_NAME
ENV PACKAGE_NAME ${PACKAGE_NAME}
WORKDIR /root/ros2_ws/src

RUN source /opt/ros/iron/setup.sh && ros2 pkg create --build-type ament_python $PACKAGE_NAME

WORKDIR /root/ros2_ws/src/$PACKAGE_NAME 

COPY src/$PACKAGE_NAME $PACKAGE_NAME
COPY src/package.xml package.xml
RUN sed -i "s/<package-name>/$PACKAGE_NAME/g" package.xml
COPY src/setup.py setup.py
RUN sed -i "s/<package-name>/$PACKAGE_NAME/g" setup.py

WORKDIR /root/ros2_ws
RUN source /opt/ros/iron/setup.sh && rosdep install -i --from-path src --rosdistro iron -y
RUN source /opt/ros/iron/setup.sh && colcon build --packages-select $PACKAGE_NAME
CMD source install/setup.bash && ros2 run $PACKAGE_NAME $PACKAGE_NAME
