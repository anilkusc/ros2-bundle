import rclpy
from .tugbot_node import TugbotNode


def main(args=None):
    rclpy.init(args=args)

    tugbot_node = TugbotNode()

    rclpy.spin(tugbot_node)
    tugbot_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
