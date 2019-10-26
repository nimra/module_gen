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
#                   Download from finelybook www.finelybook.com
#     original_w = [...] # Load the weights from the other framework
#     original_b = [...] # Load the biases from the other framework
# 
#     X = tf.placeholder(tf.float32, shape=(None, n_inputs), name="X")
#     hidden1 = fully_connected(X, n_hidden1, scope="hidden1")
#     [...] # # Build the rest of the model
# 
#     # Get a handle on the variables created by fully_connected()
#     with tf.variable_scope("", default_name="", reuse=True): # root scope
#         hidden1_weights = tf.get_variable("hidden1/weights")
#         hidden1_biases = tf.get_variable("hidden1/biases")
# 
#     # Create nodes to assign arbitrary values to the weights and biases
#     original_weights = tf.placeholder(tf.float32, shape=(n_inputs, n_hidden1))
#     original_biases = tf.placeholder(tf.float32, shape=(n_hidden1))
#     assign_hidden1_weights = tf.assign(hidden1_weights, original_weights)
#     assign_hidden1_biases = tf.assign(hidden1_biases, original_biases)
# 
#     init = tf.global_variables_initializer()
# 
#     with tf.Session() as sess:
#         sess.run(init)
#         sess.run(assign_hidden1_weights, feed_dict={original_weights: original_w})
#         sess.run(assign_hidden1_biases, feed_dict={original_biases: original_b})
#         [...] # Train the model on your new task
# 
# 
# Freezing the Lower Layers
# It is likely that the lower layers of the first DNN have learned to detect low-level fea‐
# tures in pictures that will be useful across both image classification tasks, so you can
# just reuse these layers as they are. It is generally a good idea to “freeze” their weights
# when training the new DNN: if the lower-layer weights are fixed, then the higher-
# layer weights will be easier to train (because they won’t have to learn a moving target).
# To freeze the lower layers during training, the simplest solution is to give the opti‐
# mizer the list of variables to train, excluding the variables from the lower layers:
#     train_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES,
#                                    scope="hidden[34]|outputs")
#     training_op = optimizer.minimize(loss, var_list=train_vars)
# The first line gets the list of all trainable variables in hidden layers 3 and 4 and in the
# output layer. This leaves out the variables in the hidden layers 1 and 2. Next we pro‐
# vide this restricted list of trainable variables to the optimizer’s minimize() function.
# Ta-da! Layers 1 and 2 are now frozen: they will not budge during training (these are
# often called frozen layers).
# 
# 
# 
# 
#                                                                Reusing Pretrained Layers   |   289
# 
#                        Download from finelybook www.finelybook.com
# Caching the Frozen Layers
# Since the frozen layers won’t change, it is possible to cache the output of the topmost
# frozen layer for each training instance. Since training goes through the whole dataset
# many times, this will give you a huge speed boost as you will only need to go through
# the frozen layers once per training instance (instead of once per epoch). For example,
# you could first run the whole training set through the lower layers (assuming you
# have enough RAM):
#       hidden2_outputs = sess.run(hidden2, feed_dict={X: X_train})
# Then during training, instead of building batches of training instances, you would
# build batches of outputs from hidden layer 2 and feed them to the training operation:
#       import numpy as np
# 
#       n_epochs = 100
#       n_batches = 500
# 
#       for epoch in range(n_epochs):
#           shuffled_idx = rnd.permutation(len(hidden2_outputs))
#           hidden2_batches = np.array_split(hidden2_outputs[shuffled_idx], n_batches)
#           y_batches = np.array_split(y_train[shuffled_idx], n_batches)
#           for hidden2_batch, y_batch in zip(hidden2_batches, y_batches):
#               sess.run(training_op, feed_dict={hidden2: hidden2_batch, y: y_batch})
# The last line runs the training operation defined earlier (which freezes layers 1 and 2),
# and feeds it a batch of outputs from the second hidden layer (as well as the targets for
# that batch). Since we give TensorFlow the output of hidden layer 2, it does not try to
# evaluate it (or any node it depends on).
# 
# Tweaking, Dropping, or Replacing the Upper Layers
# The output layer of the original model should usually be replaced since it is most
# likely not useful at all for the new task, and it may not even have the right number of
# outputs for the new task.
# Similarly, the upper hidden layers of the original model are less likely to be as useful
# as the lower layers, since the high-level features that are most useful for the new task
# may differ significantly from the ones that were most useful for the original task. You
# want to find the right number of layers to reuse.
# Try freezing all the copied layers first, then train your model and see how it performs.
# Then try unfreezing one or two of the top hidden layers to let backpropagation tweak
# them and see if performance improves. The more training data you have, the more
# layers you can unfreeze.
# If you still cannot get good performance, and you have little training data, try drop‐
# ping the top hidden layer(s) and freeze all remaining hidden layers again. You can
# 
# 
# 290   |   Chapter 11: Training Deep Neural Nets
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Freezing the Lower Layers",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Freezingthe(HierNode):
    def __init__(self):
        super().__init__("Freezing the Lower Layers")
        self.add(Content(), "content")

# eof
