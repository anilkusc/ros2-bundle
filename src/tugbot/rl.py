import os
import rclpy
from geometry_msgs.msg import Vector3
class RL():
    def __init__(self,node) -> None:
        self.state_dim = 1
        self.action_dim = 1
        self.max_action = 1
        self.min_action = 1
        self.node = node
    
    def reset(self):
        os.system("gz service -s /world/world_demo/control --reqtype gz.msgs.WorldControl --reptype gz.msgs.Boolean --timeout 3000 --req 'reset: {all: true}'")

    def step(self,action):
        self.node.linear ,self.node.angular = self.calculate_cmd_vel(action)
        print(self.node.pose_position_z)
        rclpy.spin_once(self.node)
    
    def calculate_cmd_vel(self,action):
        return Vector3(x=1.0) , Vector3(z=1.0)