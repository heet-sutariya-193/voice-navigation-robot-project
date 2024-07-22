# voice-navigation-robot-project
Hello,myself Heet Sutariya
<br>
This repository is about project of voice navigation robot.
<br>
the tasks and codes related to it will be available here.
<br>
folders are created as per task name.
<br>
Result of tasks will be available in respective tasks folder.
<br>

 ## Documentation 

**Error documentation**:https://docs.google.com/spreadsheets/d/1i_S7HlVXYZfgmwxuODDnaRYfB57gDYzvGEP3C_1o3pE/edit?usp=sharing

->So on 17th of june , i started ubuntu installation on my pc,first downloaded the desktop image for ubuntu ,then downloaded etcher for dual booting.<br>
->Dual booting was done very easily ,but after entering to ubuntu,my screen was repeatedly getting struck or freeze,whenever i was clicking for “try ubuntu”,afterward by install option ,the problem was solved.<br>
->Ubuntu was installed successfully using dual-boot.<br>
->After that on the 18th,I started installing ROS via terminal and that was also done easily and no errors happened while installing.<br>
for ROS installation:https://wiki.ros.org/ROS/Tutorials

->On the 19th and 20th,I saw some videos on ROS tutorials and also implemented commands on terminal as per videos and also implemented  turtle simulation.<br>
 link for tutorials:https://www.youtube.com/playlist?list=PLBbhfIdh4NdgBBkX7q0Y3UukO2_ZoICee  <br>
->On the 21st of June ,our meeting regarding further process in the project was held and we were told to complete the course till 26th of june and also to read the book ”Programming Robots with ROS” side by side as we complete the desired course.<br>


**course link:https://drive.google.com/drive/folders/1w25DNhHX5ni11rzTHJScpawzCPzLkVGt?usp=drive_link**<br>
Book:Programming Robots with ROS<br>
in the course above:<br>
**Ros3**:https://drive.google.com/drive/folders/14lrfbEjSHMYQDmFt4ie6jiwNuaPDv5R-?usp=drive_link<br>
in above folder topics such as creating catkin workspace,basics of ROS commands ,Rostopics,setting up Ros are included.also cheat sheet for command is available.<br>

**ROS4**:https://drive.google.com/drive/folders/1w25DNhHX5ni11rzTHJScpawzCPzLkVGt?usp=drive_link<br>
in above floder topics realted to publisher,subscriber,creating nodes,more about ROStopics,about ros meassages creating ros messages has been included.

**ROS5**:https://drive.google.com/drive/folders/14pIqpt8ZbJyeQpq8MNB3FaD7KQqBI3rw?usp=drive_link<br>
in above folder Ros service is explained in detailed.

## turtlesim
-> after course completion tasks for turtlesim has been given,in which different operation on turtlesim has to be done.files related to turtlesim has been there in
**turtlesim** folder.

## gazebo
in this task basically we have to made a robot from scratch<br>
Requirement: 2 wheels,body,sensor(which can dictact surrounding eg:camera,lidar,etc)<br>
Reference:
1.https://classic.gazebosim.org/tutorials

2.https://youtube.com/playlist?list=PLK0b4e05LnzbHiGDGTgE_FIWpOCvndtYx&si=L_LM5ANOhBSrw9pm

3.https://www.youtube.com/watch?v=_qQAfTmB5wc

4.https://youtube.com/playlist?list=PLNw2RD-1J5YYvFGiMafRD_axHrBUGvuIg&si=H0-WYikt94YpSrh3

Result:<br>
![Screenshot from 2024-07-08 22-07-37](https://github.com/user-attachments/assets/724c62ea-5a24-44ee-8a0e-13f696480c17)

## turtlebot
installation and basics:https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/

some extra code for installation(if error occurs than)<br>
sudo apt-get update<br>
sudo apt-get install ros-noetic-turtlebot3 ros-noetic-turtlebot3-msgs ros-noetic-turtlebot3-simulations

cd ~/catkin_ws/src<br>
git clone https://github.com/ROBOTIS-GIT/turtlebot3.git<br>
git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git<br>
git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git<br>
cd ~/catkin_ws<br>
catkin_make<br>
source devel/setup.bash

also:
Ensure you source the setup file for both your workspace and the ROS installation:<br>
source /opt/ros/noetic/setup.bash<br>
source ~/catkin_ws/devel/setup.bash<br>

RESULT:<br>




https://github.com/user-attachments/assets/93081a56-a075-45ef-9c4d-4fc39979ef47


## voice recognition node
pocketsphinx website:https://pypi.org/project/pocketsphinx/
gstreamer tutorial:https://brettviren.github.io/pygst-tutorial-org/pygst-tutorial.html

installation:<br>
Clone this repo : https://github.com/cmusphinx/pocketsphinx.git<br>
also do not forget to do catkin_make after cloning the repo<br>

sudo apt-get install build-essential bison libasound2-dev python3-dev swig<br>
git clone https://github.com/cmusphinx/sphinxbase.git<br>
cd sphinxbase<br>
./autogen.sh<br>
make,br>
sudo make install<br>


Install dependencies(gstreamer):<br>
sudo apt-get update<br>
sudo apt-get install gstreamer1.0-tools gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly gstreamer1.0-plugins-bad<br>

To verify check the version: gst-launch-1.0 --version

for more plugins:

sudo apt-get update<br>
sudo apt-get install -y build-essential autoconf libtool bison swig python3-dev python3-pip python3-setuptools<br>
sudo apt-get install -y gstreamer1.0-tools gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad<br>
sudo apt-get install -y gstreamer1.0-pocketsphinx<br>

For customisation of lm and dict model file:<br> 
1.Make a dictionary file of the words you want to be recognised and keep it in the same directory as of the current files<br>
2.Go to the official site of CMU pocketsphinx and search for generation of language model , usme ek site khul jayegi usme apni dict. File ko dalke lm file generate Karo and usko bhi usi directory mai rakhna jaha pe dict file hai<br>
link of site:http://www.speech.cs.cmu.edu/tools/lmtool-new.html<br>
3.code mai uska paath dena dhyan se<br>









