#!/usr/bin/env python
from __future__ import print_function
import os
import sys
import rospy
import cv2
import numpy as np
from o3d_ros import o3d_ros
from std_msgs.msg import String
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2
import pycuda.driver as cuda
from pycuda.compiler import SourceModule


def callback(data):

    #pc_o3d = o3d_ros.convertCloudFromRosToOpen3d(data)
    
    #points_array = np.array(list(pc2.read_points(data, skip_nans=True, field_names = ("x", "y", "z"))),dtype=np.float32)
    #x_array = points_array.transpose()[0]  
    cuda.init()
    device = cuda.Device(0)
    print(device)
    mod = SourceModule("""
    __global__ void check_range(float *a)
    {
      int idx = threadIdx.x;
      a[idx] = (*a < 5.0f) ? 1 : 0;
    }
    """)
    ctx = device.make_context()
    x_array = np.random.randn(100).astype(np.float32)  
    x_array_gpu = cuda.mem_alloc(x_array.nbytes)
    cuda.memcpy_htod(x_array_gpu, x_array)

    func = mod.get_function("check_range")
    func(x_array_gpu, block=(400,1,1), grid=(1,1))
    x_bitmap = np.empty_like(x_array)
    cuda.memcpy_dtoh(x_bitmap, x_array_gpu)
    print(x_bitmap)
    ctx.pop()


def main(args):
    rospy.init_node('LidarLeitbakeDetector', anonymous=True)
    image_sub = rospy.Subscriber("/os1_cloud_node/points",PointCloud2,callback,queue_size = 1)
    try:
      rospy.spin()
    except KeyboardInterrupt:
      print("Shutting down")

if __name__ == '__main__':
    main(sys.argv)
