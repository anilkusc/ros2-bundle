FROM osrf/ros:iron-desktop-full

ARG BRIDGES
ENV BRIDGES ${BRIDGES}

ARG PACKAGE_NAME
ENV PACKAGE_NAME ${PACKAGE_NAME}

ARG GAZEBO_WORLD
ENV GAZEBO_WORLD ${GAZEBO_WORLD}

RUN apt update && apt install ros-iron-gazebo-ros-pkgs lsb-release wget gnupg python3-pip -y
RUN wget https://packages.osrfoundation.org/gazebo.gpg -O /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null
RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get install -y ignition-fortress

WORKDIR /root/ros2_ws/src

RUN . /opt/ros/iron/setup.sh && ros2 pkg create --build-type ament_python $PACKAGE_NAME

WORKDIR /root/ros2_ws/src/$PACKAGE_NAME 

RUN pip3 install setuptools==58.2.0

COPY $PACKAGE_NAME $PACKAGE_NAME
RUN pip3 install -r $PACKAGE_NAME/requirements.txt
COPY package.xml package.xml
RUN sed -i "s/<package-name>/$PACKAGE_NAME/g" package.xml
COPY setup.py setup.py
RUN sed -i "s/<package-name>/$PACKAGE_NAME/g" setup.py

WORKDIR /root/ros2_ws
RUN . /opt/ros/iron/setup.sh && rosdep install -i --from-path src --rosdistro iron -y
RUN . /opt/ros/iron/setup.sh && colcon build --packages-select $PACKAGE_NAME
COPY entrypoint.sh .
COPY worlds/ .
RUN chmod 777 entrypoint.sh
CMD ./entrypoint.sh ${BRIDGES} ${PACKAGE_NAME} ${GAZEBO_WORLD}
