import tensorflow as tf

tf.compat.v1.disable_eager_execution()
# Add two scalars
a = tf.compat.v1.constant(2.5)
b = tf.compat.v1.constant(4.5)
total = a + b

# Create operations that generate summary data
tf.compat.v1.summary.scalar("a", a)
tf.compat.v1.summary.scalar("b", b)
tf.compat.v1.summary.scalar("total", total)

# Merge the operations into a single operation
merged_op = tf.compat.v1.summary.merge_all()

# Create a FileWriter
writer = tf.compat.v1.summary.FileWriter("summary")

with tf.compat.v1.Session() as sess:
    _, summary = sess.run([total, merged_op])
    writer.add_summary(summary=summary)
    writer.close()
