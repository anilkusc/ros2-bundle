from rclpy.node import Node
from geometry_msgs.msg import Twist, Vector3 , Pose
from nav_msgs.msg import Odometry
from sensor_msgs.msg import BatteryState

class TugbotNode(Node):

    def __init__(self):
        super().__init__('tugbot_node')
        self.publisher = self.create_publisher(Twist, '/model/tugbot/cmd_vel', 10)
        self.subscription_battery = self.create_subscription(BatteryState, '/model/tugbot/battery/linear_battery/state', self.battery_callback, 10)
        self.subscription_battery # prevent unused variable warning
        self.subscription_odometry = self.create_subscription(Odometry, '/model/tugbot/odometry', self.odometry_callback, 10)
        self.subscription_odometry # prevent unused variable warning
        self.subscription_pose = self.create_subscription(Pose, '/model/tugbot/pose', self.pose_callback, 10)
        self.subscription_pose # prevent unused variable warning
        #self.subscription_tf = self.create_subscription(TransformStamped, '/model/tugbot/tf', self.tf_callback, 10)
        #self.subscription_tf # prevent unused variable warning
        self.linear = Vector3(x=1.0)
        self.angular = Vector3(z=1.0)
        self.timer_period = 1  # seconds
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        #self.tf_pose_position_x = None
        self.odometry_pose_pose_position_x = None
        self.odometry_pose_pose_position_y = None
        self.odometry_pose_pose_orientation_z = None
        self.odometry_pose_pose_orientation_w = None
        self.odometry_twist_twist_linear_x = None
        self.odometry_twist_twist_angular_y = None
        self.pose_position_x = None
        self.pose_position_y = None
        self.pose_position_z = None
        self.pose_orientation_x = None
        self.pose_orientation_y = None
        self.pose_orientation_z = None
        self.pose_orientation_w = None
        self.battery_state = None

    def timer_callback(self):
        twist_msg = Twist()
        twist_msg.linear = self.linear
        twist_msg.angular = self.angular
        #self.publisher.publish(twist_msg)
        #self.get_logger().info('Published: "%s"' % twist_msg)

    #def tf_callback(self, tf_msg):
    #    self.tf_pose_position_x = tf_msg.pose.position.x
        
    def pose_callback(self, pose_msg):
        self.pose_position_x = pose_msg.position.x
        self.pose_position_y = pose_msg.position.y
        self.pose_position_z = pose_msg.position.z
        self.pose_orientation_x = pose_msg.orientation.x
        self.pose_orientation_y = pose_msg.orientation.y
        self.pose_orientation_z = pose_msg.orientation.z
        self.pose_orientation_w = pose_msg.orientation.w

    def odometry_callback(self, odometry_msg):
        self.odometry_pose_pose_position_x = odometry_msg.pose.pose.position.x
        self.odometry_pose_pose_position_y = odometry_msg.pose.pose.position.y
        self.odometry_pose_pose_orientation_z = odometry_msg.pose.pose.orientation.z
        self.odometry_pose_pose_orientation_w = odometry_msg.pose.pose.orientation.w
        self.odometry_twist_twist_linear_x = odometry_msg.twist.twist.linear.x
        self.odometry_twist_twist_angular_y = odometry_msg.twist.twist.angular.y

    def battery_callback(self, battery_state_msg):
        self.battery_state = battery_state_msg.percentage

#gz service -s /world/world_demo/control --reqtype gz.msgs.WorldControl --reptype gz.msgs.Boolean --timeout 3000 --req 'reset: {all: true}'
#gz topic -t /model/tugbot/cmd_vel -m gz.msgs.Twist --pub "linear { x: 1 } angular { z: 0.1 }"
