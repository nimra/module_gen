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

from .A_EarlyStopping.index import EarlyStopping as A_EarlyStopping
from .B_ℓ1and.index import ℓ1and as B_ℓ1and
from .C_Dropout.index import Dropout as C_Dropout
from .D_MaxNormRegularization.index import MaxNormRegularization as D_MaxNormRegularization
from .E_DataAugmentation.index import DataAugmentation as E_DataAugmentation

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                  Download from finelybook www.finelybook.com
# A 2013 paper19 by Andrew Senior et al. compared the performance of some of the
# most popular learning schedules when training deep neural networks for speech rec‐
# ognition using Momentum optimization. The authors concluded that, in this setting,
# both performance scheduling and exponential scheduling performed well, but they
# favored exponential scheduling because it is simpler to implement, is easy to tune,
# and converged slightly faster to the optimal solution.
# Implementing a learning schedule with TensorFlow is fairly straightforward:
#       initial_learning_rate = 0.1
#       decay_steps = 10000
#       decay_rate = 1/10
#       global_step = tf.Variable(0, trainable=False)
#       learning_rate = tf.train.exponential_decay(initial_learning_rate, global_step,
#                                                  decay_steps, decay_rate)
#       optimizer = tf.train.MomentumOptimizer(learning_rate, momentum=0.9)
#       training_op = optimizer.minimize(loss, global_step=global_step)
# After setting the hyperparameter values, we create a nontrainable variable
# global_step (initialized to 0) to keep track of the current training iteration number.
# Then we define an exponentially decaying learning rate (with η0 = 0.1 and r = 10,000)
# using TensorFlow’s exponential_decay() function. Next, we create an optimizer (in
# this example, a MomentumOptimizer) using this decaying learning rate. Finally, we cre‐
# ate the training operation by calling the optimizer’s minimize() method; since we
# pass it the global_step variable, it will kindly take care of incrementing it. That’s it!
# Since AdaGrad, RMSProp, and Adam optimization automatically reduce the learning
# rate during training, it is not necessary to add an extra learning schedule. For other
# optimization algorithms, using exponential decay or performance scheduling can
# considerably speed up convergence.
# 
# Avoiding Overfitting Through Regularization
#       With four parameters I can fit an elephant and with five I can make him wiggle his
#       trunk.
#              —John von Neumann, cited by Enrico Fermi in Nature 427
# 
# Deep neural networks typically have tens of thousands of parameters, sometimes
# even millions. With so many parameters, the network has an incredible amount of
# freedom and can fit a huge variety of complex datasets. But this great flexibility also
# means that it is prone to overfitting the training set.
# 
# 
# 
# 
# 19 “An Empirical Study of Learning Rates in Deep Neural Networks for Speech Recognition,” A. Senior et al.
#    (2013).
# 
# 
# 
# 302   |      Chapter 11: Training Deep Neural Nets
# 
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
            "Avoiding Overfitting Through Regularization",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class AvoidingOverfitting(HierNode):
    def __init__(self):
        super().__init__("Avoiding Overfitting Through Regularization")
        self.add(Content(), "content")
        self.add(A_EarlyStopping())
        self.add(B_ℓ1and())
        self.add(C_Dropout())
        self.add(D_MaxNormRegularization())
        self.add(E_DataAugmentation())

# eof
