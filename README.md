# Obstacle_Avoidance
![Screenshot from 2023-06-27 18-37-12](https://github.com/Sh-xck/Obstacle_Avoidance/assets/120919844/f1681355-2be5-4658-ac9f-662089006d5e)
## Step 1(Building the package)
Download the files into the src dir of your ros workspace </br>
</br>
  `cd ros2_ws ` </br>
  `colcon build --symlink-install`

## Step 2(Setting up the world)
Navigate to the racetrack folder and export the files into gazebo </br> </br>
`export GAZEBO_MODEL_PATH='pwd'/models `</br>
`gazebo worlds/tracknew.world`
</br>
</br>where pwd is your current working directory </br>
This command will launch gazebo with the world

## Step 3(Launching the main file with the world)
Navigate to the racetrack folder and give the following command 
</br>
</br>`ros2 launch multi_robot robotlaunch.launch.py world:=worlds/tracknew.world`

## Step 4(Launching the obstacle avoidance nodes)
`ros2 launch obav obstacleavoidance.launch.py`


 # About the package 
 This package creates a gazebo simulation using ros2 where 2 robots are spawned in one world 
 </br>
 One robot is equiped with a camera and the other with a lidar and they follow 2 different algorithms
 </br>
 This project showcases the potential of integrating different sensing technologies and utilizing ROS2 for simulating and testing obstacle avoidance algorithms in a racetrack setting.


 # Results
 

file:///home/shxck/Videos/Screencasts/finalvid.webm


