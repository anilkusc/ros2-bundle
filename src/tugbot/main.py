import rclpy
from .tugbot_node import TugbotNode
from std_srvs.srv import Empty

def main(args=None):
    rclpy.init(args=args)
    tugbot_node = TugbotNode()
    rclpy.spin_once(tugbot_node)
    tugbot_node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
