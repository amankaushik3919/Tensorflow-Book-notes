""" Book Code
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

# Creat tensor
msg = tf.string_join(["Hello ", "Tensorflow!"])

# Launch session 
with tf.Session() as sess:
    print(sess.run(msg))


1. Creates a tensor names msg that contains two string elements.
2. Creates a Session names sess and makes it the default session. 
3. Launches the new Session and prints its result.

"""

# Self made code
import tensorflow as tf
tf.compat.v1.disable_eager_execution()
# Create tensor
msg = tf.strings.join(["Hello ", "Tensorflow!"])

with tf.compat.v1.Session() as sess:
    print(sess.run(msg))
