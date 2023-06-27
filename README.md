# Obstacle_Avoidance
![image](https://github.com/Sh-xck/Obstacle_Avoidance/assets/120919844/74ef2376-114e-4f09-b173-69b7ae6c085a)

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
 This package creates a gazebo simulation using ros2 where 2 robots are spawned in one world in which
 one robot is equipped with a camera and the other is equipped with a lidar and they follow 2 different algorithms
 </br>
 </br>
 This project showcases the potential of integrating different sensing technologies and comparing the two technologies where we utilize ROS2 for simulating and testing obstacle avoidance algorithms in a racetrack setting.


 # Results

 

https://github.com/Sh-xck/Obstacle_Avoidance/assets/120919844/83019cd6-145a-4221-907f-c74f235981ca








