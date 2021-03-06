
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 19:19:01 2018

@author: binod
"""

import os
import tensorflow as tf

#Define computational graph of three Node: X, Y and addition node
#X and Y node directed to Node addition.

# Firest Node name X
X = tf.placeholder(tf.float32, name="X")
# Second Node name Y
Y = tf.placeholder(tf.float32, name="Y")

#Third Node name with additioin which depends on X and Y
addition = tf.add(X,Y, name="addition")

#Create the session to execute the above graph

with tf.Session() as session:
    #Here we are passing value of X and Y.
    result = session.run(addition, feed_dict={X: [1], Y: [4]})
    # To enabled Tensorboard where you can see all graph and node.
    # After run this program, go to command propmot and type
    #(d:\InstalledSoftware\Anaconda3\envs\tensorflow) C:\Users\binod>tensorboard  --logdir=d:/tensorboard
    
# (tensorflow) C:\Users\binod>tensorboard  --logdir=d:/tensorboard
# W0310 20:21:02.517210 Reloader tf_logging.py:114] Found more than one graph event per run, or there was a metagraph containing a graph_def, as well as one or more graph events.  Overwriting the graph with the newest event.
# W0310 20:21:02.532909 Reloader tf_logging.py:114] Found more than one metagraph event per run. Overwriting the metagraph with the newest event.
# TensorBoard 1.5.1 at http://Binod_Dell_Laptop:6006 (Press CTRL+C to quit)
# Open browser and put address http://Binod_Dell_Laptop:6006 (In your case it would be http://your-computer-hostname:6006)


    writer = tf.summary.FileWriter("d:/tensorboard",session.graph)
    print(result)

#This is another way to create session.
sess = tf.Session()

result2 = sess.run(addition, feed_dict={X: [1], Y: [4]})
print("Value of result 2 :",result2)

#Other way to pass constant to any node
a = tf.constant(37, name="a")
b = tf.constant(57, name="b")
c = tf.add(a, b, name="c")

#To execute this graph, it has to pass throuogh the sessioin. It will do nothing without
#passing trhough session.
#If you want to see value of c, you will not get result.
print("C before running inside session :", c)

addresult = sess.run(c)
print("C after execution :",addresult)

