import os
import xacro
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from ament_index_python.packages import get_package_share_directory



def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time',default='true')

    # Process the URDF filecol
    pkg_path = os.path.join(get_package_share_directory('multi_robot'))
    xacro_file = os.path.join(pkg_path,'description','robot.urdf.xacro')
    robot_description_config = xacro.process_file(xacro_file)

    pkg_path1 = os.path.join(get_package_share_directory('multi_robot'))
    xacro_file1 = os.path.join(pkg_path1,'description','robot1.urdf.xacro')
    robot_description_config1 = xacro.process_file(xacro_file1)


    entity_name_0 = "bot1"
    entity_name_1 = "bot2"



    return LaunchDescription([

       DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use sim time if true'),

            
        IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
                    
             ),
        
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            namespace= entity_name_0,
            parameters=[{'frame_prefix': entity_name_0+'/', 'use_sim_time': use_sim_time, 'robot_description': robot_description_config.toxml()}],
            output="screen"
        ),

       
        
        Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'bot1/robot_description',
                                   '-entity', 'bot1'],
                        output='screen'),

        

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            namespace=entity_name_1,
            parameters=[{'frame_prefix': entity_name_1+'/', 'use_sim_time': use_sim_time, 'robot_description': robot_description_config1.toxml()}],
            output="screen"
            ),


            Node(package='gazebo_ros', executable='spawn_entity.py',
            arguments=['-topic', 'bot2/robot_description',
            '-entity', 'bot2'],
            output='screen')
                
    ])
