import tensorflow as tf

graph = tf.compat.v1.get_default_graph()

"""
An application can create a new `Graph` by calling the constructor without arguments.
Then the application can set the `Graph` as the default `Graph` by calling the `Graph's as_default` method.
"""

#---------Experiment---------
a = tf.constant([12.])
b = tf.constant([13.])

#----------------------------

newgraph = tf.Graph()
with newgraph.as_default():
    newgraph.get()

"now with graph as default is called, Tf will add all new tensors to the `newgraph` not in `graph variable`"

