import os
import rclpy
import time

class RL():
    def __init__(self,node) -> None:
        self.state_dim = 21
        self.action_dim = 6
        self.max_action = (1.0,1.0,1.0,1.0,1.0,1.0)
        self.min_action = (-1.0,-1.0,-1.0,-1.0,-1.0,-1.0)
        self.node = node
    
    def reset(self):
        os.system("gz service -s /world/world_demo/control --reqtype gz.msgs.WorldControl --reptype gz.msgs.Boolean --timeout 3000 --req 'reset: {all: true}'")
        #rclpy.spin_once(self.node)
        #time.sleep(self.node.timer_period)

    def step(self,action):
        rclpy.spin_once(self.node)
        new_state = self.newState()
        #print(new_state)

    def isDone(self):
        is_done=False
        if self.node.input_battery_state < 10:
            is_done = True
        return is_done
    
    def evaluateReward(self):
        pass

    def newState(self):
        st = self.node
        return(st.input_odometry_pose_pose_position_x,
        st.input_odometry_pose_pose_position_y,
        st.input_odometry_pose_pose_orientation_z,
        st.input_odometry_pose_pose_orientation_w,
        st.input_odometry_twist_twist_linear_x,
        st.input_odometry_twist_twist_angular_y,
        st.input_pose_position_x,
        st.input_pose_position_y,
        st.input_pose_position_z,
        st.input_pose_orientation_x,
        st.input_pose_orientation_y,
        st.input_pose_orientation_z,
        st.input_pose_orientation_w,
        st.input_tf_position_x,
        st.input_tf_position_y,
        st.input_tf_position_z,
        st.input_tf_orientation_x,
        st.input_tf_orientation_y,
        st.input_tf_orientation_z,
        st.input_tf_orientation_w,
        st.input_battery_state)