import tensorflow as tf

t1 = tf.constant([4., 3., 2.])
t2 = tf.constant([3., 2., 1.])

dot = tf.tensordot(t1, t2, 1)
print("\n\n", t1, "\nt2:", t2, "\ndot:", dot)