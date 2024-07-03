#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import std_msgs.msg

if _name== 'main_':
    rospy.init_node("circle")
    rospy.loginfo("node started")

    pub=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)

    rate=rospy.Rate(1)
    while not rospy.is_shutdown():
        msg=Twist()
        msg.linear.x=2
        
        pub.publish(msg)
        rate.sleep()
