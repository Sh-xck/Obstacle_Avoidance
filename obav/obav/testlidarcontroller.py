import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class LaserReaderNode(Node):

    def __init__(self):
        super().__init__('hLaserReader')
        self.linX = 0.0
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
        min_distance = float('inf')
        min_index = -1

        for index in range(len(laser.ranges)):
            if laser.ranges[index] < min_distance:
                min_distance = laser.ranges[index]
                min_index = index

        if min_distance < 1.0:
            obstacle_detected = True

        if obstacle_detected:
            if min_index < len(laser.ranges) / 2:
                # Obstacle detected on the left side
                self.linX = 0.2
                self.angZ = 0.5  # Rotate right
            else:
                # Obstacle detected on the right side
                self.linX = 0.2
                self.angZ = -0.5  # Rotate left
        else:
            self.linX = 0.4  # Move forward
            self.angZ = 0.0  # No rotation

    def publish_velocity(self):
        msg = Twist()
        msg.linear.x = self.linX
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
