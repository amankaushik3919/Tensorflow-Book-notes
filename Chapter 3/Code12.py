import tensorflow as tf

m1 = tf.constant([[1, 2], [3, 4]])
m2 = tf.constant([[5, 6], [7, 8]])

e1 = tf.einsum('ij->ji', m1)
e2 = tf.einsum('ij,jk->ik', m1, m2)

print(f"\n\nm1: {m1}\n\nm2: {m2}\n\ne1: {e1}\n\ne2: {e2}\n\n")
# for more info: https://samuelprime.wordpress.com/2015/03/25/einstein-summation-convention
