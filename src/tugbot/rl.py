import os
import rclpy

class RL():
    def __init__(self,node) -> None:
        self.state_dim = 14
        self.action_dim = 6
        self.max_action = (1.0,1.0,1.0,1.0,1.0,1.0)
        self.min_action = (-1.0,-1.0,-1.0,-1.0,-1.0,-1.0)
        self.node = node
    
    def reset(self):
        os.system("gz service -s /world/world_demo/control --reqtype gz.msgs.WorldControl --reptype gz.msgs.Boolean --timeout 3000 --req 'reset: {all: true}'")
        #self.node.reset()
        
    def step(self,action):        
        self.applyAction(action)
        new_state = self.newState()
        if None in new_state:
            return new_state,0,False
        done,win = self.isDone(new_state)
        reward = self.evaluateReward(done,win,new_state)
        return new_state , reward , done

    def isDone(self,state):
        is_win = False
        is_done = False
        if state[13] < 10: #self.node.input_battery_state < 10:
            is_done = True
        # if position y between 20 23 and x between -23 -27 -> done
        if -27 < float(state[6]) < -23 and 20 < float(state[7]) < 23:
            is_done = True
            is_win = True
        return is_done,is_win
    
    def evaluateReward(self,done,win,state):
        reward = 1
        if done:
            if win:
                reward = 10 * state[13]
            else:
                reward = -1
        return reward

    def newState(self):
        st = self.node
        return(st.input_odometry_pose_pose_position_x,
        st.input_odometry_pose_pose_position_y,
        st.input_odometry_pose_pose_orientation_z,
        st.input_odometry_pose_pose_orientation_w,
        st.input_odometry_twist_twist_linear_x,
        st.input_odometry_twist_twist_angular_y,
        #st.input_pose_position_x,
        #st.input_pose_position_y,
        #st.input_pose_position_z,
        #st.input_pose_orientation_x,
        #st.input_pose_orientation_y,
        #st.input_pose_orientation_z,
        #st.input_pose_orientation_w,
        st.input_tf_position_x,
        st.input_tf_position_y,
        st.input_tf_position_z,
        st.input_tf_orientation_x,
        st.input_tf_orientation_y,
        st.input_tf_orientation_z,
        st.input_tf_orientation_w,
        st.input_battery_state)

    def applyAction(self,action):
        self.node.output_linear_x = action[0]
        self.node.output_linear_y = action[1]
        self.node.output_linear_z = action[2]
        self.node.output_angular_x = action[3]
        self.node.output_angular_y = action[4]
        self.node.output_angular_z = action[5]
        rclpy.spin_once(self.node)