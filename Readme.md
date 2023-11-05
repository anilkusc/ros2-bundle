# ROS2-BUNDLE


## Quickstart


1. Create your package in src folder.
```
    mkdir -p src/my_package
```

2. Copy publisher or subscriber package contents in you package
```
    cp -fr src/publisher/* src/my_package/
```

3. Add your service to docker-compose.yaml
```
  ros2_node3:
    build:
      context: .
      args:
        PACKAGE_NAME: my_package
    container_name: ros2_node3
```

4. Optional for gazebo 
* Copy your world in gazebo folder
```
  cp my_world.sdf gazebo/
```
* add your world to docker-compose.yaml file
```
  gazebo-server:
    build:
      context: ./gazebo
      args:
        WORLD_NAME: my_world      
    network_mode: "host"
```

5. Up containers
```
  docker-compose up -d --build
```

6. Run gzclient for reach gazebo simulation GUI
```
  GAZEBO_MASTER_URI=localhost:11345 gzclient --verbose
```


## TO-DO
* Make ros2 and gazebo versions compatible.(gzserver 10 , ros2 foxy)
* Extend example as both ros2 and gazebo working together
* Add Web GUI support of gazebo
* Add other simulators like deepbots