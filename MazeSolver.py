#import list
import rospy
import time as t
from robot_control_class import RobotControl
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

# Radial Move class with assign additional attributes 
# while extending robot control.
# the advantage is to create a dynamic arc that can follow
# a wall to the robots left or right with varied arcing params

class radialMove(RobotControl, object):
    def __init__(self, leftOrRight, angVel, linVel):
        # pull parent attributes
        super(radialMove, self).__init__()
        # Additional arc attributes to be added
        self.direction = leftOrRight
        self.angVel = angVel
        self.linVel = linVel  

    # Funtion to create arc path and measure wall distance
    # to course correct
    def continuousArc(self):
        i = 0
        t = 0.2
        
        while True:
            # Measure distance to wall
            if RobotControl.get_laser(self, 380) < 1:
                RobotControl.turn(self, 'clockwise', 5, 0.5)
            # Set arcing velocities
            else:
                self.cmd.linear.x = 1
                self.cmd.linear.y = 0 
                self.cmd.linear.z = 0
                self.cmd.angular.x = 0
                self.cmd.angular.y = 0
                self.cmd.angular.z = 1.5
            # Publish velocity commands
            RobotControl.publish_once_in_cmd_vel(self)
           
# RadialMove object creation and function call
r1 = radialMove('left', 2, 2)
r1.continuousArc()
