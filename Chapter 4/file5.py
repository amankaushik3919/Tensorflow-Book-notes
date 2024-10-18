import tensorflow as tf

# Disable eager execution to use TensorFlow 1.x graph mode
tf.compat.v1.disable_eager_execution()

# Define a constant tensor
a = tf.constant(2.5)

# Create a session to evaluate the tensor
with tf.compat.v1.Session() as sess:
    # Run the session to get the value of 'a'
    output_value = sess.run(a)
    
    # Log the output value if the condition (output_value > 0) is true
    tf.compat.v1.logging.log_if(
        level=tf.compat.v1.logging.INFO,
        msg='Output: %f' % output_value, 
        condition=(output_value > 0)
    )
