# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                  Download from finelybook www.finelybook.com
# Dynamic Unrolling Through Time
# The dynamic_rnn() function uses a while_loop() operation to run over the cell the
# appropriate number of times, and you can set swap_memory=True if you want it to
# swap the GPU’s memory to the CPU’s memory during backpropagation to avoid
# OOM errors. Conveniently, it also accepts a single tensor for all inputs at every time
# step (shape [None, n_steps, n_inputs]) and it outputs a single tensor for all out‐
# puts at every time step (shape [None, n_steps, n_neurons]); there is no need to
# stack, unstack, or transpose. The following code creates the same RNN as earlier
# using the dynamic_rnn() function. It’s so much nicer!
#     X = tf.placeholder(tf.float32, [None, n_steps, n_inputs])
# 
#     basic_cell = tf.contrib.rnn.BasicRNNCell(num_units=n_neurons)
#     outputs, states = tf.nn.dynamic_rnn(basic_cell, X, dtype=tf.float32)
# 
# 
#                During backpropagation, the while_loop() operation does the
#                appropriate magic: it stores the tensor values for each iteration dur‐
#                ing the forward pass so it can use them to compute gradients dur‐
#                ing the reverse pass.
# 
# 
# Handling Variable Length Input Sequences
# So far we have used only fixed-size input sequences (all exactly two steps long). What
# if the input sequences have variable lengths (e.g., like sentences)? In this case you
# should set the sequence_length parameter when calling the dynamic_rnn() (or
# static_rnn()) function; it must be a 1D tensor indicating the length of the input
# sequence for each instance. For example:
#     seq_length = tf.placeholder(tf.int32, [None])
# 
#     [...]
#     outputs, states = tf.nn.dynamic_rnn(basic_cell, X, dtype=tf.float32,
#                                         sequence_length=seq_length)
# For example, suppose the second input sequence contains only one input instead of
# two. It must be padded with a zero vector in order to fit in the input tensor X (because
# the input tensor’s second dimension is the size of the longest sequence—i.e., 2).
#     X_batch = np.array([
#             # step 0     step 1
#             [[0, 1, 2], [9, 8, 7]],   #   instance   0
#             [[3, 4, 5], [0, 0, 0]],   #   instance   1 (padded with a zero vector)
#             [[6, 7, 8], [6, 5, 4]],   #   instance   2
#             [[9, 0, 1], [3, 2, 1]],   #   instance   3
#         ])
#     seq_length_batch = np.array([2,   1, 2, 2])
# 
# 
# 
#                                                                   Basic RNNs in TensorFlow   |   387
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Dynamic Unrolling Through Time",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Dynamic Unrolling Through Time"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DynamicUnrolling(HierNode):
    def __init__(self):
        super().__init__("Dynamic Unrolling Through Time")
        self.add(Content())

# eof
