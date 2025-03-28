#!/usr/bin/env python3
import rospy
from robot_pose_ekf.srv import GetStatus, GetStatusRequest

if __name__ == '__main__':

    rospy.init_node('spawner', anonymous=True)
    # print 'Looking for node robot_pose_ekf...'   ## python2 to python3
    print("Looking for node \"robot_pose_ekf\"...")
    rospy.wait_for_service('robot_pose_ekf/get_status')

    s = rospy.ServiceProxy('robot_pose_ekf/get_status', GetStatus)
    resp = s.call(GetStatusRequest())
    # print resp.status     ## python2 to python3
    print(resp.status)