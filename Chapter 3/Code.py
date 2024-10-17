import tensorflow as tf

# The list provided in the constant funciton will create a 1D tensor.
t1 = tf.constant([1.5, 2.5, 3.5])

# Multi-dimensional arrays use similar notaion. The code creates a 2-x-2 matrix and sets each of its elements to the letter b:
t2 = tf.constant([['b', 'b'], ['b', 'b']])

# if we set the last argument, `verify_shape`, to True, TensorFlow will verify that the 2 shapes are equal.
# t3 = tf.compat.v1.constant(value=[4, 2], dtype=tf.int16, shape=[3], name='Constant', verify_shape=True)
# print(t3)
# Error: TypeError: Expected Tensor [4 2] (converted from [4, 2]) with shape (3,), but got shape (2,).

# The function zeros, ones, and fill create tensors whose elements all have the same value. For zeros, and ones, the only required argument is `Shape`, which identifies the shape of teh desired tensor.
zero_tensor = tf.zeros(shape=[3])
print(zero_tensor)

# The code creates 4-x-4 matrix whose elements equal to 1.0:
one_tensor = tf.ones([4, 4])
print(one_tensor)

# the fill function requires a value parameter which sets the value of the tensor's elements.
fill_tensor = tf.fill(dims=[1, 2, 3], value=81.0)
print(fill_tensor)

