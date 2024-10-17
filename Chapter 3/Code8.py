import tensorflow as tf

t = tf.constant([-6.5, -3.5, 3.5, 6.5])
r1 = tf.round(t)
r2 = tf.compat.v1.rint(t)
r3 = tf.compat.v1.ceil(t)
r4 = tf.floor(t)

print(t, "\n", f"\nround r1: {r1}", f"\nrint r2: {r2}", f"\nceil r3: {r3}", f"\nfloor r4: {r4}")


t1 = tf.constant([0, -2, 4, 6])
t2 = tf.constant([[1, 3], [7, 2]])
r1 = tf.argmin(t1)
r2 = tf.argmax(t2)

print(f"t1: {t1}\nt2: {t2}\nargmin r1: {r1}\nargmax r2: {r2}")
