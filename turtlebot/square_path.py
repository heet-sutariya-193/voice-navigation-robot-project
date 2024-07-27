#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from math import pi

def move_square():
    rospy.init_node('turtlebot_square', anonymous=True)
    pub=rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate=rospy.Rate(10)
    
    msg=Twist()
    lspeed=0.1
    aspeed=3.14159265359/4
    sidelength=1.0
    ltime=sidelength/lspeed
    atime=3.14159265359/(2*aspeed)
    
    for _ in range(10):
       msg.linear.x=lspeed
       msg.angular.z=0
       starttime=rospy.Time.now().to_sec()
       while rospy.Time.now().to_sec()-starttime<ltime:
            pub.publish(msg)
            rate.sleep()

       msg.linear.x=0
       pub.publish(msg)
       rospy.sleep(1)

       msg.angular.z=aspeed
       start_time=rospy.Time.now().to_sec()
       while rospy.Time.now().to_sec()-start_time<atime:
            pub.publish(msg)
            rate.sleep()

       msg.angular.z=0
       pub.publish(msg)
       rospy.sleep(1)

    msg.linear.x = 0
    msg.angular.z = 0
    pub.publish(msg)

if __name__=='__main__':
    try:
        move_square()
    except rospy.ROSInterruptException:
        pass
