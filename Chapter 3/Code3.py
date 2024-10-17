import tensorflow as tf

vec = tf.constant([1., 2., 3., 4.])
print(vec)

mat = tf.reshape(vec, [2, 2])
print(mat)

# In the reverse function the axis parameter identifies one or more dim to be reversed.
mat = tf.constant([[1., 2., 3.], [4., 5., 6.]])
print(mat)
rev_mat = tf.reverse(mat, [0])
print(rev_mat)
rev_mat = tf.reverse(mat, [0, 1])
print(rev_mat)

