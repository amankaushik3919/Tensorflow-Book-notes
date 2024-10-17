import tensorflow as tf

a = tf.constant([3., 3., 3.])
b = tf.constant([2., 2., 2.])

sum = tf.add(a, b)
diff = tf.subtract(a, b)
prod = tf.multiply(a, b)
quot = tf.divide(a, b)

print(f"\n\nsum:{sum}\ndiff:{diff}\nprod:{prod}\nquot:{quot}")

total = tf.add(a, b)
total2 = a+b

print(f"total: {total}\ntotal2: {total2}")

