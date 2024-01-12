from rclpy.node import Node
from geometry_msgs.msg import Twist, Vector3
from nav_msgs.msg import Odometry
import time 

class TugbotNode(Node):

    def __init__(self):
        super().__init__('tugbot_node')
        self.publisher_ = self.create_publisher(Twist, '/model/tugbot/cmd_vel', 10)
        self.subscription = self.create_subscription(Odometry, '/model/tugbot/odometry', self.odometry_callback, 10)
        self.subscription
        self.linear = Vector3(x=0.0)
        self.angular = Vector3(z=0.0)
        self.timer_period = 2  # seconds
        self.timer = self.create_timer(self.timer_period, self.timer_callback)

    def timer_callback(self):
        twist_msg = Twist()
        twist_msg.linear = self.linear
        twist_msg.angular = self.angular
        self.publisher_.publish(twist_msg)
        #self.get_logger().info('Published: "%s"' % twist_msg)

    def odometry_callback(self, odometry_msg):
        #self.get_logger().info('Listened: "%s"' % odometry_msg)
        self.linear = Vector3(x=1.0)
        self.angular = Vector3(z=1.0)
        time.sleep(self.timer_period)

#gz service -s /world/world_demo/control --reqtype gz.msgs.WorldControl --reptype gz.msgs.Boolean --timeout 3000 --req 'reset: {all: true}'