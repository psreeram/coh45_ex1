# this code was referenced from Beginner client library 
# tutorials in the ROS2 wiki
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalPublisherNode1(Node):

    def __init__(self):
        super().__init__('node_1')   # this name is shown in rqt_graph
        self.publisher_ = self.create_publisher(String, 'topic_1', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World published to topic_1: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    node_1 = MinimalPublisherNode1()

    rclpy.spin(node_1)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node_1.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()