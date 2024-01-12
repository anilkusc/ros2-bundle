import rclpy
from .tugbot_node import TugbotNode
import os

def main(args=None):
    rclpy.init(args=args)
    tugbot_node = TugbotNode()
    rclpy.spin_once(tugbot_node)
    rclpy.spin_once(tugbot_node)
    rclpy.spin_once(tugbot_node)
    tugbot_node.destroy_node()
    rclpy.shutdown()
    os.system("gz service -s /world/world_demo/control --reqtype gz.msgs.WorldControl --reptype gz.msgs.Boolean --timeout 3000 --req 'reset: {all: true}'")

if __name__ == '__main__':
    main()
