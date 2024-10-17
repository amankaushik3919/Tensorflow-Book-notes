import tensorflow as tf
t = tf.constant([4.])
t1 = tf.square(t)
t2 = tf.sqrt(t)
t3 = tf.compat.v1.rsqrt(t)

print(f"\nconstant t: {t}\nsquare t1: {t1}\nsqrt t2: {t2}\nrsqrt t3: {t3}")
