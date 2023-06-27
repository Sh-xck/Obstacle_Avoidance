import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class LaserReaderNode(Node):

    def __init__(self):
        super().__init__('hLaserReader')
        self.linX = 0.0
        self.angY = 0.0
        self.angZ = 0.0

        self.publisher = self.create_publisher(Twist, 'bot1/cmd_vel', 10)
        self.subscription = self.create_subscription(
            LaserScan,
            '/bot1/scan',
            self.laser_scan_callback,
            1
        )
        self.subscription  

        self.timer = self.create_timer(0.1, self.publish_velocity)

    def laser_scan_callback(self, laser):
        obstacle_detected = False
        for index in range(len(laser.ranges)):
            if 1 < laser.ranges[index] < 3:
                if index > 6:
                    print(index)
                    self.linX = 0.05
                    self.angY = 1.0
                    self.angZ = 1.0
                
                obstacle_detected = True
                break

        if not obstacle_detected:
            print(index)
            self.linX = 0.15
            self.angY = 0.0
            self.angZ = 0.0

    def publish_velocity(self):
        msg = Twist()
        msg.linear.x = self.linX
        msg.angular.y = self.angY
        msg.angular.z = self.angZ

        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = LaserReaderNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
