#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from math import pi

def move_square():
    rospy.init_node('random', anonymous=True)
    pub=rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate=rospy.Rate(10)
    
    msg=Twist()
    l=0.1
    lspeed=l
    aspeed=0.5
    len=1.0
    ltime=len/lspeed
    while not rospy.is_shutdown():
       msg.linear.x=lspeed
       msg.angular.z=aspeed
       starttime=rospy.Time.now().to_sec()
       while rospy.Time.now().to_sec()-starttime<ltime:
            pub.publish(msg)
            rate.sleep()
       lspeed=lspeed+0.05
   
   

if __name__=='__main__':
    try:
        move_square()
    except rospy.ROSInterruptException:
        pass
