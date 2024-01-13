from rclpy.node import Node
from geometry_msgs.msg import Twist, Vector3
from nav_msgs.msg import Odometry
from sensor_msgs.msg import BatteryState
import time 

class TugbotNode(Node):

    def __init__(self):
        super().__init__('tugbot_node')
        self.publisher = self.create_publisher(Twist, '/model/tugbot/cmd_vel', 10)
        self.subscription_battery = self.create_subscription(BatteryState, '/model/tugbot/battery/linear_battery/state', self.battery_callback, 10)
        self.subscription_battery # prevent unused variable warning
        self.subscription_odometry = self.create_subscription(Odometry, '/model/tugbot/odometry', self.odometry_callback, 10)
        self.subscription_odometry # prevent unused variable warning
        self.linear = Vector3(x=1.0)
        self.angular = Vector3(z=1.0)
        self.timer_period = 1  # seconds
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        self.odometry = None
        self.battery_state = None

    def timer_callback(self):
        twist_msg = Twist()
        twist_msg.linear = self.linear
        twist_msg.angular = self.angular
        self.publisher.publish(twist_msg)
        #self.get_logger().info('Published: "%s"' % twist_msg)

    def odometry_callback(self, odometry_msg):
        #self.get_logger().info('Listened: "%s"' % odometry_msg)
        #self.linear = Vector3(x=1.0)
        #self.angular = Vector3(z=1.0)
        self.odometry = odometry_msg
        #time.sleep(self.timer_period)

    def battery_callback(self, battery_state_msg):
        self.battery_state = battery_state_msg

#gz service -s /world/world_demo/control --reqtype gz.msgs.WorldControl --reptype gz.msgs.Boolean --timeout 3000 --req 'reset: {all: true}'
#gz topic -t /model/tugbot/cmd_vel -m gz.msgs.Twist --pub "linear { x: 1 } angular { z: 0.1 }"