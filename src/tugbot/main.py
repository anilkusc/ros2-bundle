import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Vector3,Pose,Point  # Import Vector3 message

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Twist, '/model/tugbot/cmd_vel', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Twist()
        msg.linear = Vector3(x=10.0)
        msg.angular = Vector3(z=1.0)
        self.publisher_.publish(msg)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)   
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
