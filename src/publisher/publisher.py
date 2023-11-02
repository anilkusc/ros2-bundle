import rclpy
from std_msgs.msg import String

def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('publisher_node')
    publisher = node.create_publisher(String, 'topic1', 10)

    msg = String()

    i = 0
    while rclpy.ok():
        msg.data = 'Hello ROS 2: %d' % i
        node.get_logger().info('Publishing: "%s"' % msg.data)
        publisher.publish(msg)
        i += 1
        rclpy.spin_once(node)

    node.destroy_node()
    rclpy.shutdown()
