# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Distributinga.index import Distributinga as A_Distributinga
from .B_ApplyingDropout.index import ApplyingDropout as B_ApplyingDropout
from .C_TheDifficulty.index import TheDifficulty as C_TheDifficulty

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                    Download from finelybook www.finelybook.com
# The rest of the code is the same as earlier. This can provide a significant speed boost
# since there is just one fully connected layer instead of one per time step.
# 
# Creative RNN
# Now that we have a model that can predict the future, we can use it to generate some
# creative sequences, as explained at the beginning of the chapter. All we need is to pro‐
# vide it a seed sequence containing n_steps values (e.g., full of zeros), use the model to
# predict the next value, append this predicted value to the sequence, feed the last
# n_steps values to the model to predict the next value, and so on. This process gener‐
# ates a new sequence that has some resemblance to the original time series (see
# Figure 14-11).
#       sequence = [0.] * n_steps
#       for iteration in range(300):
#           X_batch = np.array(sequence[-n_steps:]).reshape(1, n_steps, 1)
#           y_pred = sess.run(outputs, feed_dict={X: X_batch})
#           sequence.append(y_pred[0, -1, 0])
# 
# 
# 
# 
# Figure 14-11. Creative sequences, seeded with zeros (left) or with an instance (right)
# 
# Now you can try to feed all your John Lennon albums to an RNN and see if it can
# generate the next “Imagine.” However, you will probably need a much more powerful
# RNN, with more neurons, and also much deeper. Let’s look at deep RNNs now.
# 
# Deep RNNs
# It is quite common to stack multiple layers of cells, as shown in Figure 14-12. This
# gives you a deep RNN.
# 
# 
# 
# 
# 396   |   Chapter 14: Recurrent Neural Networks
# 
#                   Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 14-12. Deep RNN (left), unrolled through time (right)
# 
# To implement a deep RNN in TensorFlow, you can create several cells and stack them
# into a MultiRNNCell. In the following code we stack three identical cells (but you
# could very well use various kinds of cells with a different number of neurons):
#     n_neurons = 100
#     n_layers = 3
# 
#     basic_cell = tf.contrib.rnn.BasicRNNCell(num_units=n_neurons)
#     multi_layer_cell = tf.contrib.rnn.MultiRNNCell([basic_cell] * n_layers)
#     outputs, states = tf.nn.dynamic_rnn(multi_layer_cell, X, dtype=tf.float32)
# 
# That’s all there is to it! The states variable is a tuple containing one tensor per layer,
# each representing the final state of that layer’s cell (with shape [batch_size, n_neu
# rons]). If you set state_is_tuple=False when creating the MultiRNNCell, then
# states becomes a single tensor containing the states from every layer, concatenated
# along the column axis (i.e., its shape is [batch_size, n_layers * n_neurons]).
# Note that before TensorFlow 0.11.0, this behavior was the default.
# 
# Distributing a Deep RNN Across Multiple GPUs
# Chapter 12 pointed out that we can efficiently distribute deep RNNs across multiple
# GPUs by pinning each layer to a different GPU (see Figure 12-16). However, if you
# try to create each cell in a different device() block, it will not work:
#     with tf.device("/gpu:0"): # BAD! This is ignored.
#         layer1 = tf.contrib.rnn.BasicRNNCell(num_units=n_neurons)
# 
#     with tf.device("/gpu:1"): # BAD! Ignored again.
#         layer2 = tf.contrib.rnn.BasicRNNCell(num_units=n_neurons)
# 
# This fails because a BasicRNNCell is a cell factory, not a cell per se (as mentioned ear‐
# lier); no cells get created when you create the factory, and thus no variables do either.
# 
# 
#                                                                           Deep RNNs   |   397
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Deep RNNs",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Deep RNNs"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DeepRNNs(HierNode):
    def __init__(self):
        super().__init__("Deep RNNs")
        self.add(Content())
        self.add(A_Distributinga())
        self.add(B_ApplyingDropout())
        self.add(C_TheDifficulty())

# eof
