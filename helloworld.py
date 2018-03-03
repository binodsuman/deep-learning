
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 18:49:45 2018

@author: binod
"""


import tensorflow as tf

# First create a constant
hello = tf.constant('Hello, Mr. TensorFlow')
sess = tf.Session()
print(sess.run(hello))

