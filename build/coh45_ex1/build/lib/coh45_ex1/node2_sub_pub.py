# this code was referenced from Beginner client library 
# tutorials in the ROS2 wiki
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalSubscriberAndPublisherNode2(Node):

    def __init__(self):
        super().__init__('node_2') #shown in rqt_graph
        # Subscriber part of the node
        self.subscription = self.create_subscription(
            String,
            'topic_1',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        # Publisher part of the node
        self.publisher_ = self.create_publisher(String, 'topic_2', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def listener_callback(self, msg):
        self.get_logger().info('I heard topic_1 : "%s"' % msg.data)

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World published in topic_2: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    node_2 = MinimalSubscriberAndPublisherNode2()

    rclpy.spin(node_2)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node_2.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()