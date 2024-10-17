import tensorflow as tf

t1 = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
t2 = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])

dot = tf.matmul(t1, t2)
print("\n\n t1:", t1, "\nt2:", t2, "\ndot:", dot)