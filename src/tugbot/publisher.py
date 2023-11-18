from rclpy.node import Node
from geometry_msgs.msg import Twist, Vector3

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Twist, '/model/tugbot/cmd_vel', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear = Vector3(x=1.0)
        msg.angular = Vector3(z=1.0)
        self.publisher_.publish(msg)