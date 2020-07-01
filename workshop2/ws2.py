#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import random

def callback(msg):
	print('=========================================')
	print('s1 [0]')
	print msg.ranges[0]

	print('s2 [45]')
	print msg.ranges[45]
	#print('s2 [90]')
	#print msg.ranges[90]

	print('s3 [315]')
	print msg.ranges[315]
	#print('s3 [180]')
	#print msg.ranges[180]

	#print('s4 [270]')
	#print msg.ranges[270]

	#print('s5 [359]')
	#print msg.ranges[359]

	#If obstacle is at least 0.5m in front of the TB3, the TB3 will move forward
	if msg.ranges[0] >= 0.5 and msg.ranges[45] >= 0.5 and msg.ranges[315] >= 0.5:
		print("No obstacle detected")
		if move.angular.z==0: 
			print("START State: Moving Straight\nBased on Markov Chain, deciding the direction\n")
			if random.random()<0.7:
				move.linear.x = 0.4
				move.angular.z = 0.0
				print("END State: Moving Straight")
			elif random.random()<0.9:
				move.linear.x = 0.2
				move.angular.z = -1
				print("END State: Turning Right")
			else:
				move.linear.x = 0.2
				move.angular.z = 1
				print("END State: Turning left")
		elif move.angular.z==1:
			print("START State: Turning Left\nBased on Markov Chain, deciding the direction\n")
			if random.random()<0.2:
				move.linear.x = 0.2
				move.angular.z = 1
				print("END State: Turning left")
			elif random.random()<0.8:
				move.linear.x = 0.4
				move.angular.z = 0
				print("END State: Moving Straight")
			else:
				move.linear.x = 0.2
				move.angular.z = -1
				print("END State: Turning Right")
		elif move.angular.z==-1:
			print("START State: Turning right\nBased on Markov Chain, deciding the direction\n")
			if random.random()<0.4:
				move.linear.x = 0.2
				move.angular.z = -1
				print("END State: Turning Right")
			elif random.random()<0.9:
				move.linear.x = 0.4
				move.angular.z = 0
				print("END State: Moving Straight")
			else:
				move.linear.x = 0.2
				move.angular.z = 1
				print("END State: Turning left")
		else:

			move.linear.x = 0.2
			move.angular.z = 1
	elif msg.ranges[45] < 0.5:
		print("Met obstacle at 45 degree direction\nTurning Left")
		move.linear.x = 0.0
		move.angular.z = -1.04
	elif msg.ranges[315] < 0.5:
		print("Met obstacle at 315 degree direction\nTurning Right")
		move.linear.x = 0.0
		move.angular.z = 1.04
	else:
		print("Met obstacle at front, turn left 90 degree")
		move.linear.x = 0.0
		move.angular.z = 1.571 

	pub.publish(move)

rospy.init_node('obstacle_avoidance')			# Initiate a Node called 'obstacle_avoidance'
sub = rospy.Subscriber('/scan', LaserScan, callback)
pub = rospy.Publisher('/cmd_vel', Twist)
move = Twist()

rospy.spin()