# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.HierBlock import HierBlock as hbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.ListBlock import ListBlock as lbk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                        Download from finelybook www.finelybook.com
# TensorFlow Implementation
# You can implement a stacked autoencoder very much like a regular deep MLP. In par‐
# ticular, the same techniques we used in Chapter 11 for training deep nets can be
# applied. For example, the following code builds a stacked autoencoder for MNIST,
# using He initialization, the ELU activation function, and ℓ2 regularization. The code
# should look very familiar, except that there are no labels (no y):
#       n_inputs = 28 * 28 # for MNIST
#       n_hidden1 = 300
#       n_hidden2 = 150 # codings
#       n_hidden3 = n_hidden1
#       n_outputs = n_inputs
# 
#       learning_rate = 0.01
#       l2_reg = 0.001
# 
#       X = tf.placeholder(tf.float32, shape=[None, n_inputs])
#       with tf.contrib.framework.arg_scope(
#               [fully_connected],
#               activation_fn=tf.nn.elu,
#               weights_initializer=tf.contrib.layers.variance_scaling_initializer(),
#               weights_regularizer=tf.contrib.layers.l2_regularizer(l2_reg)):
#           hidden1 = fully_connected(X, n_hidden1)
#           hidden2 = fully_connected(hidden1, n_hidden2) # codings
#           hidden3 = fully_connected(hidden2, n_hidden3)
#           outputs = fully_connected(hidden3, n_outputs, activation_fn=None)
# 
#       reconstruction_loss = tf.reduce_mean(tf.square(outputs - X))   # MSE
# 
#       reg_losses = tf.get_collection(tf.GraphKeys.REGULARIZATION_LOSSES)
#       loss = tf.add_n([reconstruction_loss] + reg_losses)
# 
#       optimizer = tf.train.AdamOptimizer(learning_rate)
#       training_op = optimizer.minimize(loss)
# 
#       init = tf.global_variables_initializer()
# 
# You can then train the model normally. Note that the digit labels (y_batch) are
# unused:
#       n_epochs = 5
#       batch_size = 150
# 
#       with tf.Session() as sess:
#           init.run()
#           for epoch in range(n_epochs):
#               n_batches = mnist.train.num_examples // batch_size
#               for iteration in range(n_batches):
#                   X_batch, y_batch = mnist.train.next_batch(batch_size)
#                   sess.run(training_op, feed_dict={X: X_batch})
# 
# 
# 
# 416   |   Chapter 15: Autoencoders
# 
#                      Download from finelybook www.finelybook.com
# Tying Weights
# When an autoencoder is neatly symmetrical, like the one we just built, a common
# technique is to tie the weights of the decoder layers to the weights of the encoder lay‐
# ers. This halves the number of weights in the model, speeding up training and limit‐
# ing the risk of overfitting. Specifically, if the autoencoder has a total of N layers (not
# counting the input layer), and WL represents the connection weights of the Lth layer
#                                                  N
# (e.g., layer 1 is the first hidden layer, layer 2 is the coding layer, and layer N is the
# output layer), then the decoder layer weights can be defined simply as: WN–L+1 = WLT
#                     N
# (with L = 1, 2, ⋯, 2 ).
# 
# Unfortunately, implementing tied weights in TensorFlow using the fully_connec
# ted() function is a bit cumbersome; it’s actually easier to just define the layers man‐
# ually. The code ends up significantly more verbose:
#     activation = tf.nn.elu
#     regularizer = tf.contrib.layers.l2_regularizer(l2_reg)
#     initializer = tf.contrib.layers.variance_scaling_initializer()
# 
#     X = tf.placeholder(tf.float32, shape=[None, n_inputs])
# 
#     weights1_init = initializer([n_inputs, n_hidden1])
#     weights2_init = initializer([n_hidden1, n_hidden2])
# 
#     weights1   =   tf.Variable(weights1_init, dtype=tf.float32, name="weights1")
#     weights2   =   tf.Variable(weights2_init, dtype=tf.float32, name="weights2")
#     weights3   =   tf.transpose(weights2, name="weights3") # tied weights
#     weights4   =   tf.transpose(weights1, name="weights4") # tied weights
# 
#     biases1   =   tf.Variable(tf.zeros(n_hidden1),   name="biases1")
#     biases2   =   tf.Variable(tf.zeros(n_hidden2),   name="biases2")
#     biases3   =   tf.Variable(tf.zeros(n_hidden3),   name="biases3")
#     biases4   =   tf.Variable(tf.zeros(n_outputs),   name="biases4")
# 
#     hidden1   =   activation(tf.matmul(X, weights1) + biases1)
#     hidden2   =   activation(tf.matmul(hidden1, weights2) + biases2)
#     hidden3   =   activation(tf.matmul(hidden2, weights3) + biases3)
#     outputs   =   tf.matmul(hidden3, weights4) + biases4
# 
#     reconstruction_loss = tf.reduce_mean(tf.square(outputs - X))
#     reg_loss = regularizer(weights1) + regularizer(weights2)
#     loss = reconstruction_loss + reg_loss
# 
#     optimizer = tf.train.AdamOptimizer(learning_rate)
#     training_op = optimizer.minimize(loss)
# 
#     init = tf.global_variables_initializer()
# This code is fairly straightforward, but there are a few important things to note:
# 
# 
#                                                                        Stacked Autoencoders   |   417
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "TensorFlow Implementation",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TensorFlowImplementation(HierNode):
    def __init__(self):
        super().__init__("TensorFlow Implementation")
        self.add(Content(), "content")

# eof
