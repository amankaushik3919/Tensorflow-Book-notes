-  Installation

To avoid the message "The tensorflow library was not compiled to use XYZ instructions, but these are available on you machine and could speed up CPU computations." To turn off this message.

environment Variable name `TF_CPP_MIN_LOG_LEVEL` and set its value to 3.

---

# Exploring the Tensorflow Installation

- Directory name `Tensorflow` that contains a wide variety of files and folders.
- `Core` Directory contains the Primary packages and modules.
- The `Contrib` Directory contains secondary packages that may later be merged into core Tensorflow.

---

Package | Content
--|--
tensorflow | Central Package of the Tensorflow framework, Commonly accessed as tf
tf.train | Optimizers and other classes related to training
tf.nn | Neural Network classes and related math operations.
tf.layers | Functions related to multilayer neural Networks
tf.contrib | Volatile or experimental code
tf.image | Image-processing functions
tf.estimator | High-level tools for training and evaluation
tf.logging | Functions that write data to a log
tf.summary | classes needed to generate summary data
tf.metrics | Functions for measuring the outcome of ML.
tf.contrib.keras | Makes it possible to interface Tensorflow using the keras interface
tf.contrib.ffmpeg | Enables audio processing through the open-source FFMPEG toolset
tf.contrib.bayesflow | contains modules related to Baysian Learning
tf.contrib.integrate | Provides the odeint function, which integrates ordinary differential equations.

---

# Tensor

A tensor instance is an n-dimensional array that contains numeric or string data. Tensors play a central role in Tensorflow development.

```python
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

```

---

