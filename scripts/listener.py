#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("I heard %s", msg.data)

rospy.init_node('listener')
rospy.Subscriber('my_chat_topic', String, callback, queue_size=10)
rospy.spin()

"""
import rospy
from std_msgs.msg import String

def callback(message):
	rospy.loginfo("I heard %s", message.data)

def listner():
	rospy.init_node('listner')
	rospy.Subscriber('my_chat_topic', String, callback, queue_size=10)
	#rospy.Subscriber('my_chat_topic', String, callback)
	rospy.spin()

listner()

"""