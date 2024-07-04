#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from math import pi
if _name=='main_':
    rospy.init_node("spiral")
    rospy.loginfo("node started")

    pub=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)

    rate=rospy.Rate(1)
    l=0.5
    a=3

    while not rospy.is_shutdown():
        mes=Twist()
        mes.linear.x=l
        mes.angular.z=a
        l+=0.5
        

        pub.publish(mes)
        rate.sleep()
