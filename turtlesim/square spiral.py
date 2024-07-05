#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from math import pi
if _name=='main_':
    rospy.init_node("square_spiral")
    rospy.loginfo("node started")

    pub=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)

    rate=rospy.Rate(1)
    l=0.2
    while not rospy.is_shutdown():
        mes=Twist()
        mes.linear.x=l
        pub.publish(mes)
        rate.sleep()
        l+=0.2

        mes.linear.x=0.0
        mes.angular.z=0.0
        pub.publish(mes)
        rate.sleep()

        mes.angular.z=1.5708
        pub.publish(mes)
        rate.sleep()

        mes.linear.x=0.0
        mes.angular.z=0.0
        pub.publish(mes)
        rate.sleep()
