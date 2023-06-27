import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge
import cv2


class ObstacleAvoidanceNode(Node):
    def __init__(self):
        super().__init__('obstacle_avoidance_node')
        self.subscription = self.create_subscription(
            Image, '/camera/image_raw', self.image_callback, 10)
        self.cv_bridge = CvBridge()
        self.publisher = self.create_publisher(Twist, '/bot2/cmd_vel', 10)
        self.twist = Twist()
        self.obstacle = False
        self.angz = 0

    def image_callback(self, msg):
        try:
            cv_image = self.cv_bridge.imgmsg_to_cv2(msg, 'bgr8')
            gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
            _, binary_image = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if len(contours) > 0:
                self.avoid_obstacle(contours)
            else:
                self.move()

        except Exception as e:
            self.get_logger().error('Error processing image: {0}'.format(str(e)))

    def reroute(self):
        self.twist.linear.x = 0.4
        self.twist.linear.z = -(self.angz)
        self.publisher.publish(self.twist)
        self.obstacle = False

    def move(self):
        self.twist.linear.x = 0.4
        self.twist.angular.z = 0.0
        self.publisher.publish(self.twist)

    def avoid_obstacle(self, contours):
        image_width = 450
        center_x = image_width // 2
        largest_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(largest_contour)
        cx = int(M['m10'] / M['m00'])
        print(cx)
        if(cx == 224):
           self.move()
        
        else:
            deviation = cx - center_x
            max_angular_vel = 1.2
            self.twist.linear.x = 0.2
            self.twist.angular.z = -deviation / center_x * max_angular_vel
            self.publisher.publish(self.twist)
            self.obstacle = True
            self.angz = self.twist.angular.z


def main(args=None):
    rclpy.init(args=args)
    obstacle_avoidance_node = ObstacleAvoidanceNode()
    rclpy.spin(obstacle_avoidance_node)
    obstacle_avoidance_node.destroy_node()
    rclpy.shutdown()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

