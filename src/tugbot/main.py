import rclpy
from .tugbot_node import TugbotNode
from .rl import RL
import time
import random

def main(args=None):
    rclpy.init(args=args)
    env = RL(TugbotNode())
    env.reset()
    while True:
        action = (random.uniform(-1, 1),random.uniform(-1, 1),random.uniform(-1, 1),random.uniform(-1, 1),random.uniform(-1, 1),random.uniform(-1, 1))
        env.step(action)
        time.sleep(env.node.timer_period)
    
    #rclpy.spin_once(tugbot_node)
    #rclpy.spin_once(tugbot_node)
    #rclpy.spin_once(tugbot_node)
    #tugbot_node.destroy_node()
    #rclpy.shutdown()
    #os.system("gz service -s /world/world_demo/control --reqtype gz.msgs.WorldControl --reptype gz.msgs.Boolean --timeout 3000 --req 'reset: {all: true}'")

if __name__ == '__main__':
    main()
