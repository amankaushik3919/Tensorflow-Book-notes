import tensorflow as tf

a = tf.constant([3, 3, 3])
b = tf.constant([2, 2, 2])

div1 = tf.divide(a, b)
div2 = a/b
div3 = tf.compat.v1.div(a, b)
div4 = a//b

print(f"div1:{div1}\ndiv2:{div2}\ndiv3:{div3}\ndiv4:{div4}")
