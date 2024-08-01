# this code was referenced from Beginner client library 
# tutorials in the ROS2 wiki
#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    node_1 = Node(
        package='coh45_ex1',
        executable='node_1',
        name='node_1'
    )
    node_2 = Node(
        package='coh45_ex1',
        executable='node_2',
        name='node_2'
    )
    node_3 = Node(
        package='coh45_ex1',
        executable='node_3',
        name='node_3'
    )

    return launch.LaunchDescription([
        node_1,
        node_2,
        node_3
    ])