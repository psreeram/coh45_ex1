# this code was referenced from Beginner client library 
# tutorials in the ROS2 wiki
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalSubscriberNode3(Node):

    def __init__(self):
        super().__init__('node_3') #shown in rqt_graph
        self.subscription = self.create_subscription(
            String,
            'topic_2',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard topic_2 : "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)

    node_3 = MinimalSubscriberNode3()

    rclpy.spin(node_3)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node_3.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()