#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 09:33:50 2017

@author: willowdodger
"""

#yellow - input signals
#green - hidden layer
#red - output layer

#kiekvienas hidden layer turi savo tiksla
#gaves hidden neuronas x y u values, understands, that
#y and u are the ones that he needs and then he calculates output 

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

