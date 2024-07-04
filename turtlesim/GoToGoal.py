#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from math import pi,pow,sqrt,atan2
from turtlesim.msg import Pose

cp=Pose() #cp=current pose
def callback(data):
    global cp
    cp.x=round(data.x,4)
    cp.y=round(data.y,4)
    cp.theta=data.theta

def ed(gp):    #ed=euclidean distance
    return sqrt(pow(gp.x-cp.x,2)+pow(gp.y-cp.y,2))

def lv(gp,k=1.2):    #lv=linear velocity
     return k*ed(gp)

def sa(gp):    #sa=steering angle
    return atan2(gp.y-cp.y,gp.x-cp.x)

def av(gp,k=5):    #av=angular velocity
    return k*(sa(gp) -cp.theta)


def movingtogoal(gp):
    rospy.init_node("GoToGoal",anonymous=True)
    pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    sub=rospy.Subscriber('/turtle1/pose',Pose,callback)
    rate=rospy.Rate(10)

    vel=Twist()
    while not rospy.is_shutdown():

        vel.linear.x=lv(gp) #calling linear velocity function
        vel.linear.y=0
        vel.linear.z=0

        vel.angular.x=0
        vel.angular.y=0
        vel.angular.z=av(gp) #calling angular velocity function
        
        pub.publish(vel)

        d=ed(gp)

        if d < 0.1:
           print("reached goal!")
           break

        rate.sleep()



if _name=="main_":
   try: 
    gp=Pose() #gp=goal pose
    gp.x=float(input("enter x goal:"))
    gp.y=float(input("enter y goal:"))
    movingtogoal(gp)
   except rospy.ROSInterruptException:
       pass
