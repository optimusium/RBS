#!/usr/bin/env python
# works for actual OM ONLY!
# does not work for actual OM_with_TB3

import rospy					#import the python library for ROS
from open_manipulator_msgs.msg import JointPosition	#import JointPosition message from the open_manipulator_msgs package
from open_manipulator_msgs.srv import SetJointPosition
from sensor_msgs.msg import JointState
import math
import time

def callback(msg):				#define a function called 'callback' that receives a parameter named 'msg'
	print msg.name			
	print msg.position	

def talker():
	rospy.init_node('OM_publisher')	#Initiate a Node called 'OM_publisher'
	set_joint_position = rospy.ServiceProxy('/goal_joint_space_path', SetJointPosition)
        set_gripper_position = rospy.ServiceProxy('/goal_tool_control', SetJointPosition)
	
	while not rospy.is_shutdown():
		ii=0
		while ii<50:
			ii+=1
			joint_position = JointPosition()
			joint_position.joint_name = ['joint1','joint2','joint3','joint4']
			#joint_position.position =  [1, 0.2761, 0.4502, -0.3958]		# in radians
			#joint_position.position =  [3.1416, 0.8674, 0.1562, -1.2435]		# in radians
			joint_position.position =  [0.78,  -0.5, 0, 0]		# in radians
			resp1 = set_joint_position('planning_group',joint_position, 3)
			gripper_position = JointPosition()
			gripper_position.joint_name = ['gripper']
			gripper_position.position =  [0.01]	# -0.01 for fully close and 0.01 for fully open
			respg2 = set_gripper_position('planning_group',gripper_position, 3)

			sub_joint_state = rospy.Subscriber('/joint_states', JointState, callback)

		#rospy.sleep(0.1)

		while ii<250:
			ii+=1
			joint_position = JointPosition()
			joint_position.joint_name = ['joint1','joint2','joint3','joint4']
			#joint_position.position =  [1, 0.2761, 0.4502, -0.3958]		# in radians
			#joint_position.position =  [3.1416, 0.8674, 0.1562, -1.2435]		# in radians
			joint_position.position =  [1.5706,  -0.2, 0, 0]		# in radians
			resp1 = set_joint_position('planning_group',joint_position, 3)
			gripper_position = JointPosition()
			gripper_position.joint_name = ['gripper']
			gripper_position.position =  [0.01]	# -0.01 for fully close and 0.01 for fully open
			respg2 = set_gripper_position('planning_group',gripper_position, 3)

			sub_joint_state = rospy.Subscriber('/joint_states', JointState, callback)


		rospy.sleep(0.03)
                ii=0
		while ii<200:
			ii+=1
			joint_position = JointPosition()
			joint_position.joint_name = ['joint1','joint2','joint3','joint4']
			#joint_position.position =  [1, 0.2761, 0.4502, -0.3958]		# in radians
			#joint_position.position =  [1.570, 0.8674, 0.1562, -1.2435]		# in radians
			joint_position.position =  [1.570, 0.7639, 0.2141, -0.9771]		# in radians
			resp1 = set_joint_position('planning_group',joint_position, 3)
			gripper_position = JointPosition()
			gripper_position.joint_name = ['gripper']
			gripper_position.position =  [0.01]	# -0.01 for fully close and 0.01 for fully open
			respg2 = set_gripper_position('planning_group',gripper_position, 3)

			sub_joint_state = rospy.Subscriber('/joint_states', JointState, callback)

		rospy.sleep(0.02)


                ii=0
		while ii<200:
			ii+=1
			joint_position = JointPosition()
			joint_position.joint_name = ['joint1','joint2','joint3','joint4']
			#joint_position.position =  [1, 0.2761, 0.4502, -0.3958]		# in radians
			#joint_position.position =  [1.570, 0.8674, 0.1562, -1.2435]		# in radians
			joint_position.position =  [1.570, 0.7639, 0.2141, -0.9771]		# in radians
			resp1 = set_joint_position('planning_group',joint_position, 3)
			gripper_position = JointPosition()
			gripper_position.joint_name = ['gripper']
			gripper_position.position =  [-0.01]	# -0.01 for fully close and 0.01 for fully open
			respg2 = set_gripper_position('planning_group',gripper_position, 3)

			sub_joint_state = rospy.Subscriber('/joint_states', JointState, callback)

		rospy.sleep(0.01)

		ii=0
		while ii<200:
			ii+=1
			joint_position = JointPosition()
			joint_position.joint_name = ['joint1','joint2','joint3','joint4']
			#joint_position.position =  [1, 0.2761, 0.4502, -0.3958]		# in radians
			joint_position.position =  [1.570, -0.5, 0, 0]		# in radians
			resp1 = set_joint_position('planning_group',joint_position, 3)
			gripper_position = JointPosition()
			gripper_position.joint_name = ['gripper']
			gripper_position.position =  [-0.01]	# -0.01 for fully close and 0.01 for fully open
			respg2 = set_gripper_position('planning_group',gripper_position, 3)

			sub_joint_state = rospy.Subscriber('/joint_states', JointState, callback)

		rospy.sleep(0.001)

		joint_position = JointPosition()
		joint_position.joint_name = ['joint1','joint2','joint3','joint4']
		#joint_position.position =  [1, 0.2761, 0.4502, -0.3958]		# in radians
		joint_position.position =  [0, -0.5, 0, 0]		# in radians
		resp1 = set_joint_position('planning_group',joint_position, 3)
		gripper_position = JointPosition()
		gripper_position.joint_name = ['gripper']
		gripper_position.position =  [-0.01]	# -0.01 for fully close and 0.01 for fully open
		respg2 = set_gripper_position('planning_group',gripper_position, 3)

		sub_joint_state = rospy.Subscriber('/joint_states', JointState, callback)


		rospy.sleep(0.001)
		ii=0
		while ii<100:
			ii+=1
			joint_position = JointPosition()
			joint_position.joint_name = ['joint1','joint2','joint3','joint4']
			#joint_position.position =  [1, 0.2761, 0.4502, -0.3958]		# in radians
			joint_position.position =  [-1.57, -0.5, 0, 0]		# in radians
			resp1 = set_joint_position('planning_group',joint_position, 3)
			gripper_position = JointPosition()
			gripper_position.joint_name = ['gripper']
			gripper_position.position =  [-0.01]	# -0.01 for fully close and 0.01 for fully open
			respg2 = set_gripper_position('planning_group',gripper_position, 3)

			sub_joint_state = rospy.Subscriber('/joint_states', JointState, callback)


		rospy.sleep(0.1)

		ii=0
		while ii<100:
			ii+=1
			joint_position = JointPosition()
			joint_position.joint_name = ['joint1','joint2','joint3','joint4']
			#joint_position.position =  [1, 0.2761, 0.4502, -0.3958]		# in radians
			#joint_position.position =  [-1.57, -0.5, 0, 0]		# in radians
			joint_position.position =  [-1.570, 0.7639, 0.2141, -0.9771]		# in radians
			resp1 = set_joint_position('planning_group',joint_position, 3)
			gripper_position = JointPosition()
			gripper_position.joint_name = ['gripper']
			gripper_position.position =  [-0.01]	# -0.01 for fully close and 0.01 for fully open
			respg2 = set_gripper_position('planning_group',gripper_position, 3)

			sub_joint_state = rospy.Subscriber('/joint_states', JointState, callback)


		rospy.sleep(0.02)
		while 1:
			joint_position = JointPosition()
			joint_position.joint_name = ['joint1','joint2','joint3','joint4']
			#joint_position.position =  [1, 0.2761, 0.4502, -0.3958]		# in radians
			#joint_position.position =  [-1.57, 0.8674, 0.1562, -1.2435]		# in radians
			joint_position.position =  [-1.570, 0.7639, 0.2141, -0.9771]		# in radians
			resp1 = set_joint_position('planning_group',joint_position, 3)
			gripper_position = JointPosition()
			gripper_position.joint_name = ['gripper']
			gripper_position.position =  [0.01]	# -0.01 for fully close and 0.01 for fully open
			respg2 = set_gripper_position('planning_group',gripper_position, 3)

			sub_joint_state = rospy.Subscriber('/joint_states', JointState, callback)


if __name__== '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass