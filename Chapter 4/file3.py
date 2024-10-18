import tensorflow as tf

tf.compat.v1.disable_eager_execution()
t1 = tf.constant(1.2)
t2 = tf.constant(3.5)

prod = tf.compat.v1.multiply(t1, t2)
with tf.compat.v1.Session() as sess:
    print("\n\nProduct: ", sess.run(prod))

# with interactive session
print()
print()
print()
t1 = tf.constant(1.2)
t2 = tf.constant(3.5)
prod = tf.compat.v1.multiply(t1, t2)
sess = tf.compat.v1.InteractiveSession()
print("Product: ", prod.eval())
