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
#                  Download from finelybook www.finelybook.com
# With millions of parameters you can fit the whole zoo. In this section we will present
# some of the most popular regularization techniques for neural networks, and how to
# implement them with TensorFlow: early stopping, ℓ1 and ℓ2 regularization, dropout,
# max-norm regularization, and data augmentation.
# 
# Early Stopping
# To avoid overfitting the training set, a great solution is early stopping (introduced in
# Chapter 4): just interrupt training when its performance on the validation set starts
# dropping.
# One way to implement this with TensorFlow is to evaluate the model on a validation
# set at regular intervals (e.g., every 50 steps), and save a “winner” snapshot if it outper‐
# forms previous “winner” snapshots. Count the number of steps since the last “win‐
# ner” snapshot was saved, and interrupt training when this number reaches some limit
# (e.g., 2,000 steps). Then restore the last “winner” snapshot.
# Although early stopping works very well in practice, you can usually get much higher
# performance out of your network by combining it with other regularization techni‐
# ques.
# 
# ℓ and ℓ Regularization
#  1        2
# 
# Just like you did in Chapter 4 for simple linear models, you can use ℓ1 and ℓ2 regulari‐
# zation to constrain a neural network’s connection weights (but typically not its bia‐
# ses).
# One way to do this using TensorFlow is to simply add the appropriate regularization
# terms to your cost function. For example, assuming you have just one hidden layer
# with weights weights1 and one output layer with weights weights2, then you can
# apply ℓ1 regularization like this:
#      [...] # construct the neural network
#      base_loss = tf.reduce_mean(xentropy, name="avg_xentropy")
#      reg_losses = tf.reduce_sum(tf.abs(weights1)) + tf.reduce_sum(tf.abs(weights2))
#      loss = tf.add(base_loss, scale * reg_losses, name="loss")
# However, if there are many layers, this approach is not very convenient. Fortunately,
# TensorFlow provides a better option. Many functions that create variables (such as
# get_variable() or fully_connected()) accept a *_regularizer argument for each
# created variable (e.g., weights_regularizer). You can pass any function that takes
# weights as an argument and returns the corresponding regularization loss. The
# l1_regularizer(), l2_regularizer(), and l1_l2_regularizer() functions return
# such functions. The following code puts all this together:
#      with arg_scope(
#              [fully_connected],
# 
# 
# 
#                                                  Avoiding Overfitting Through Regularization   |   303
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Early Stopping",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class EarlyStopping(HierNode):
    def __init__(self):
        super().__init__("Early Stopping")
        self.add(Content(), "content")

# eof
