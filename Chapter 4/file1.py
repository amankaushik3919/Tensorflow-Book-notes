import tensorflow as tf


tf.compat.v1.disable_eager_execution()

a = tf.constant(2.5, name='first_val')
b = tf.constant(4.5, name='second_val')

sum = a+b
print(tf.compat.v1.get_default_graph().get_operations())
print()
print(tf.compat.v1.get_default_graph().get_tensor_by_name('first_val:0'))

# The first `print` statement calls `get_operations` to obtain a list of the graph's operations.
