import rospy
from std_msgs.msg import String

def callback(msg):
	rospy.loginfo("I heard %s", msg.data)

def listner():
	rospy.init_node('listner')
	rospy.Subscriber('my_chat_topic', String, callback)
	rospy.spin()

listner()