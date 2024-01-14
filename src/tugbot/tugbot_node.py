from rclpy.node import Node
from geometry_msgs.msg import Twist, Vector3 , Pose , PoseArray 
from nav_msgs.msg import Odometry 
from sensor_msgs.msg import BatteryState
from ros_gz_interfaces.srv import ControlWorld
import rclpy

class TugbotNode(Node):

    def __init__(self):
        super().__init__('tugbot_node')
        self.publisher = self.create_publisher(Twist, '/model/tugbot/cmd_vel', 10)
        self.subscription_battery = self.create_subscription(BatteryState, '/model/tugbot/battery/linear_battery/state', self.battery_callback, 10)
        self.subscription_battery # prevent unused variable warning
        self.subscription_odometry = self.create_subscription(Odometry, '/model/tugbot/odometry', self.odometry_callback, 10)
        self.subscription_odometry # prevent unused variable warning
        #self.subscription_pose = self.create_subscription(Pose, '/model/tugbot/pose', self.pose_callback, 10)
        #self.subscription_pose # prevent unused variable warning
        self.subscription_tf = self.create_subscription(PoseArray, '/model/tugbot/tf', self.tf_callback, 10)
        self.subscription_tf # prevent unused variable warning
        self.timer_period = 0.1  # seconds
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        
        self.input_odometry_pose_pose_position_x = None
        self.input_odometry_pose_pose_position_y = None
        self.input_odometry_pose_pose_orientation_z = None
        self.input_odometry_pose_pose_orientation_w = None
        self.input_odometry_twist_twist_linear_x = None
        self.input_odometry_twist_twist_angular_y = None
        #self.input_pose_position_x = None
        #self.input_pose_position_y = None
        #self.input_pose_position_z = None
        #self.input_pose_orientation_x = None
        #self.input_pose_orientation_y = None
        #self.input_pose_orientation_z = None
        #self.input_pose_orientation_w = None
        self.input_tf_position_x = None
        self.input_tf_position_y = None
        self.input_tf_position_z = None
        self.input_tf_orientation_x = None
        self.input_tf_orientation_y = None
        self.input_tf_orientation_z = None
        self.input_tf_orientation_w = None
        self.input_battery_state = None

        self.output_linear_x = 0.0
        self.output_linear_y = 0.0
        self.output_linear_z = 0.0
        self.output_angular_x = 0.0
        self.output_angular_y = 0.0
        self.output_angular_z = 0.0

        #self.client_world_control = self.create_client(ControlWorld, '/world/world_demo/control')
        #while not self.client_world_control.wait_for_service(timeout_sec=1.0):
        #    self.get_logger().info('Waiting for "world_demo/control" service...')
        #self.request = ControlWorld.Request()

    def timer_callback(self):
        twist_msg = Twist()
        twist_msg.linear = Vector3(x=self.output_linear_x,y=self.output_linear_y,z=self.output_linear_z)
        twist_msg.angular = Vector3(x=self.output_angular_x,y=self.output_angular_y,z=self.output_angular_z)
        self.publisher.publish(twist_msg)
        #self.get_logger().info('Published: "%s"' % twist_msg)

    def tf_callback(self, tf_msg):
        self.input_tf_position_x = tf_msg.poses[0].position.x
        self.input_tf_position_y = tf_msg.poses[0].position.y
        self.input_tf_position_z = tf_msg.poses[0].position.z
        self.input_tf_orientation_x = tf_msg.poses[0].orientation.x
        self.input_tf_orientation_y = tf_msg.poses[0].orientation.y
        self.input_tf_orientation_z = tf_msg.poses[0].orientation.z
        self.input_tf_orientation_w = tf_msg.poses[0].orientation.w
        
    #def pose_callback(self, pose_msg):
    #    self.input_pose_position_x = pose_msg.position.x
    #    self.input_pose_position_y = pose_msg.position.y
    #    self.input_pose_position_z = pose_msg.position.z
    #    self.input_pose_orientation_x = pose_msg.orientation.x
    #    self.input_pose_orientation_y = pose_msg.orientation.y
    #    self.input_pose_orientation_z = pose_msg.orientation.z
    #    self.input_pose_orientation_w = pose_msg.orientation.w

    def odometry_callback(self, odometry_msg):
        self.input_odometry_pose_pose_position_x = odometry_msg.pose.pose.position.x
        self.input_odometry_pose_pose_position_y = odometry_msg.pose.pose.position.y
        self.input_odometry_pose_pose_orientation_z = odometry_msg.pose.pose.orientation.z
        self.input_odometry_pose_pose_orientation_w = odometry_msg.pose.pose.orientation.w
        self.input_odometry_twist_twist_linear_x = odometry_msg.twist.twist.linear.x
        self.input_odometry_twist_twist_angular_y = odometry_msg.twist.twist.angular.y

    def battery_callback(self, battery_state_msg):
        self.input_battery_state = battery_state_msg.percentage
    
    def reset(self):
        self.request.reset.all = True
        future = self.client.call_async(self.request)
        rclpy.spin_until_future_complete(self, future)

    

#gz service -s /world/world_demo/control --reqtype gz.msgs.WorldControl --reptype gz.msgs.Boolean --timeout 3000 --req 'reset: {all: true}'
#gz topic -t /model/tugbot/cmd_vel -m gz.msgs.Twist --pub "linear { x: 1 } angular { z: 0.1 }"
#ros2 service call /world/world_demo/control gz_msgs/srv/WorldControl '{reset: {all: true}}'
