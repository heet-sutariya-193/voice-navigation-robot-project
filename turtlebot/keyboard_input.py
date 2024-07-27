#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def move_turtlebot():
    rospy.init_node('turtlebot_keyboard_inputs', anonymous=True)
    rospy.loginfo("press keywords as mentioned for turtleBot movements")
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    
    msg = Twist()
    
    while not rospy.is_shutdown():
        key = input("enter commands \n l-left \n r-right \n b-back \n s-stop \n f-forward\n")
        
        if key=='l':
            msg.linear.x=0.0
            msg.angular.z=0.5
        elif key=='r':
            msg.linear.x=0.0
            msg.angular.z=-0.5
        elif key=='b':
            msg.linear.x=-0.1
            msg.angular.z=0.0
        elif key=='s':
            msg.linear.x=0.0
            msg.angular.z=0.0
        elif key=='f':
            msg.linear.x=0.1
            msg.angular.z=0.0
        else:
            rospy.loginfo("enter as per mentioned")
        
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_turtlebot()
    except rospy.ROSInterruptException:
        pass
