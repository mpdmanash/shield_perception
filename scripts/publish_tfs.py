#!/usr/bin/env python  
import roslib

import rospy
import tf

if __name__ == '__main__':
    rospy.init_node('fixed_tf_broadcaster')
    br = tf.TransformBroadcaster()
    listener = tf.TransformListener()
    rate = rospy.Rate(100.0)
    while not rospy.is_shutdown():

        # br.sendTransform((2.13379277, -0.46097594, 3.15950329),
        #                  (0.08723707, -0.46148218, -0.05824138,  0.88092669),
        #                  rospy.Time.now(),
        #                  "fridge",
        #                  "camera_depth_optical_frame_2")
        

        # br.sendTransform((3.34122123, 0.22481905, 1.55156895),
        #                  (-0.31476341, -0.00454652,  0.94913535,  0.00673822),
        #                  rospy.Time.now(),
        #                  "real_sense",
        #                  "fridge")

        # br.sendTransform((-3.1602231, -1.3308604, 1.79539307),
        #                  (0.38112725, 0.54278027, 0.60266988, 0.44375739),
        #                  rospy.Time.now(),
        #                  "launcher_camera",
        #                  "real_sense")
        
        # br.sendTransform((9.846676994508622, -1.2487195397461164, 0.09432934029041928),
        #                  (0.09820968985817882, 0.5995303993088189, 0.07197420158993295, -0.7910359437617488),
        #                  rospy.Time.now(),
        #                  "launcher_camera_2",
        #                  "base_footprint")
        
        # br.sendTransform((-0.0897972122212618, 0.008121730656646613, 1.5861054037696538),
        #                  ( -0.5365288218513303, 0.5513395064561633, -0.4578609339676863, 0.44556137297765813),
        #                  rospy.Time.now(),
        #                  "camera_depth_optical_frame_2",
        #                  "base_footprint")

        # br.sendTransform((0.288399, 1.601808, 5.61612 ),
        #                  (   0.01532584, -0.0652771,   0.99761252,  0.01653097),
        #                  rospy.Time.now(),
        #                  "launcher_camera", "camera_depth_optical_frame")
        timet = rospy.Time.now()
        br.sendTransform((6.01944448, -0.52128749,  0.55443587),
                         (0.4995405,  0.45499593, 0.51035028, 0.53195919),
                         timet,
                         "launcher_camera", "base_footprint")

        br.sendTransform((6.01944448, -0.52128749,  0.55443587),
                         (0.4995405,  0.45499593, 0.51035028, 0.53195919),
                         timet,
                         "sc_color_frame", "base_footprint")
        # br.sendTransform((0,0,0),
        #                  (0.0784591, 0.0, 0.0, 0.9969173),
        #                  timet,
        #                  "launcher_camera", "launcher_camera_pre")

        # try:
        #     (trans,rot) = listener.lookupTransform('base_footprint','launcher_camera',rospy.Time(0))
        #     print("translation:", trans)
        #     print("rotation:", rot)
        # except:
        #     print("tf not found")

        rate.sleep()


"""
 listener.lookupTransform('base_footprint','sc_depth_camera',rospy.Time(0))
('translation:', [5.574363423212862, -0.40031510516119606, 0.5773170124014723])
('rotation:', [0.4655766643356737, 0.45389416488539236, 0.5152013737223944, 0.5583779664252736])
"""


"""
The output of (trans,rot) = listener.lookupTransform('base_footprint','camera_depth_optical_frame',rospy.Time(0))
('translation:', [-0.0897972122212618, 0.008121730656646613, 1.5861054037696538])
('rotation:', [-0.5365288218513303, 0.5513395064561633, -0.4578609339676863, 0.44556137297765813])
('translation:', [-0.0897972122212618, 0.008121730656646613, 1.5861054037696538])
('rotation:', [-0.5365288218513303, 0.5513395064561633, -0.4578609339676863, 0.44556137297765813])
('translation:', [-0.0897972122212618, 0.008121730656646613, 1.5861054037696538])
('rotation:', [-0.5365288218513303, 0.5513395064561633, -0.4578609339676863, 0.44556137297765813])
('translation:', [-0.0897972122212618, 0.008121730656646613, 1.5861054037696538])
('rotation:', [-0.5365288218513303, 0.5513395064561633, -0.4578609339676863, 0.44556137297765813])
('translation:', [-0.0897972122212618, 0.008121730656646613, 1.5861054037696538])
('rotation:', [-0.5365288218513303, 0.5513395064561633, -0.4578609339676863, 0.44556137297765813])
('translation:', [-0.0897972122212618, 0.008121730656646613, 1.5861054037696538])
('rotation:', [-0.5365288218513303, 0.5513395064561633, -0.4578609339676863, 0.44556137297765813])
('translation:', [-0.0897972122212618, 0.008121730656646613, 1.5861054037696538])
('rotation:', [-0.5365288218513303, 0.5513395064561633, -0.4578609339676863, 0.44556137297765813])
('translation:', [-0.0897972122212618, 0.008121730656646611, 1.5861054037696538])
('rotation:', [-0.5365288218513303, 0.5513395064561633, -0.4578609339676863, 0.44556137297765813])
('translation:', [-0.0897972122212618, 0.008121730656646616, 1.5861054037696538])
('rotation:', [-0.5365288218513303, 0.5513395064561633, -0.4578609339676863, 0.44556137297765813])
('translation:', [-0.0897972122212618, 0.008121730656646613, 1.5861054037696538])
('rotation:', [-0.5365288218513303, 0.5513395064561633, -0.4578609339676863, 0.44556137297765813])
('translation:', [-0.0897972122212618, 0.008121730656646613, 1.5861054037696538])
('rotation:', [-0.5365288218513303, 0.5513395064561633, -0.4578609339676863, 0.44556137297765813])
('translation:', [-0.0897972122212618, 0.008121730656646613, 1.5861054037696538])
('rotation:', [-0.5365288218513303, 0.5513395064561633, -0.4578609339676863, 0.44556137297765813])
('translation:', [-0.0897972122212618, 0.008121730656646616, 1.5861054037696538])
('rotation:', [-0.5365288218513303, 0.5513395064561633, -0.4578609339676863, 0.44556137297765813])
('translation:', [-0.0897972122212618, 0.008121730656646613, 1.5861054037696538])
('rotation:', [-0.5365288218513303, 0.5513395064561633, -0.4578609339676863, 0.44556137297765813])
('translation:', [-0.0897972122212618, 0.008121730656646616, 1.5861054037696538])
('rotation:', [-0.5365288218513303, 0.5513395064561633, -0.4578609339676863, 0.44556137297765813])







('translation:', [5.581131427098616, -0.4004582927483543, 0.6340388742906594])
('rotation:', [0.43799553410960645, 0.42810552905851135, 0.5366945821952076, 0.5803830525763918])
('translation:', [5.581131427098616, -0.4004582927483543, 0.6340388742906595])
('rotation:', [0.43799553410960645, 0.42810552905851135, 0.5366945821952076, 0.5803830525763918])
('translation:', [5.581131427098616, -0.4004582927483543, 0.6340388742906594])
('rotation:', [0.43799553410960645, 0.42810552905851135, 0.5366945821952076, 0.5803830525763918])
('translation:', [5.581131427098616, -0.4004582927483543, 0.6340388742906594])
('rotation:', [0.43799553410960645, 0.42810552905851135, 0.5366945821952076, 0.5803830525763918])
('translation:', [5.581131427098616, -0.4004582927483543, 0.6340388742906594])
('rotation:', [0.43799553410960645, 0.42810552905851135, 0.5366945821952076, 0.5803830525763918])

"""