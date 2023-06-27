from launch import LaunchDescription
from launch_ros.actions import Node 

def generate_launch_description():
    node1 = Node(
        package="obav",
        executable="opencv",
        name="node1"
    )

    node2 = Node(
        package="obav",
        executable="lidar",
        name="node2"
    )

    return LaunchDescription([
        node1,
        node2
    ])