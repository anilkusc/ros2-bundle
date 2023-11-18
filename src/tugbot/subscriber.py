from rclpy.node import Node
from nav_msgs.msg import Odometry


class OdometryListener(Node):

    def __init__(self):
        super().__init__('odometry_listener')
        self.subscription = self.create_subscription(
            Odometry,
            '/model/tugbot/odometry',
            self.odometry_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.get_logger().info('Odometry listener node is ready.')

    def odometry_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg)