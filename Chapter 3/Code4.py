import tensorflow as tf

mat = tf.constant([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]])
print(mat)
slice_mat = tf.slice(mat, [1, 1], [2, 2])
print(slice_mat)