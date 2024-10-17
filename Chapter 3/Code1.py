import tensorflow as tf
lin_tensor = tf.linspace(5., 9., 5)
print(lin_tensor)

# unlike, linspace, range does not accept the number of elements in the tensor. Instead, it computes successive elements by adding a value called delta.
range_tensor = tf.range(3., 7., delta=0.5)
print(range_tensor)

# like python's range funciton tensor's also work by taking only one element 'start' parameter.
range_tensor = tf.range(1.5, delta=0.3)
print(range_tensor)


