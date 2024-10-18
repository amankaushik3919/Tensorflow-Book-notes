import tensorflow as tf

tf.compat.v1.disable_eager_execution()
print()
print()
print()
print()
print()

a = tf.constant([2.5,])
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.INFO)
with tf.compat.v1.Session() as sess:
    output = sess.run(a)
    tf.compat.v1.logging.info('\n\nOutput: %f', output)


