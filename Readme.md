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

4. Up containers
```
  docker-compose up -d --build
```