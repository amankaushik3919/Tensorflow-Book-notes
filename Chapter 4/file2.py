import tensorflow as tf

tf.compat.v1.disable_eager_execution()
tensr = tf.constant([2, 3])
with tf.compat.v1.Session() as sess:
    res = sess.run(fetches=tensr)
    print(res)


#
t1 = tf.constant(7)
t2 = tf.constant(2)
with tf.compat.v1.Session() as sess:
    res = sess.run(t1 + t2)
    print(res)

#
t1 = tf.constant(9)
t2 = tf.constant(5)
with tf.compat.v1.Session() as sess:
    res1, res2 = sess.run([t1, t2])
    print(res1)
    print(res2)

