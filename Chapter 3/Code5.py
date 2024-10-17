import tensorflow as tf

t1 = tf.constant([1., 2.])
print(t1)
t2 = tf.constant([3., 4.])
print(t2)

t3 = tf.constant([5., 6.])
print(t3)

t4 = tf.stack([t1, t2, t3])
print(t4)

t4 = tf.stack([t1, t2, t3], axis=1)
print("\n\nt4: ", t4)


print()
# unstack function in doubt cleared
t4 = tf.unstack(t4, axis=0)
print(type(t4[0]))
