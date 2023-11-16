# ROS2-BUNDLE


## Quickstart


1. Develop your package in src folder.
```
    mkdir -p src/my_package
```

2. Set your package name on docker-compose.yaml
```
  ros2_bundle:
    build:
      context: ./src
      args:
        BRIDGES: /test@std_msgs/msg/Int32@ignition.msgs.Int32,/test2@std_msgs/msg/Int32@ignition.msgs.Int32
        PACKAGE_NAME: my_package        
        GAZEBO_WORLD: empty_world.sdf
```

3. Up containers
```
  docker-compose up -d --build
```

## TO-DO

* Add Web GUI support of gazebo
* Add other simulators like deepbots