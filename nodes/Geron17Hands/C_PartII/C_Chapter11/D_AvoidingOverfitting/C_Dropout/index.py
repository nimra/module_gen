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
#                weights_regularizer=tf.contrib.layers.l1_regularizer(scale=0.01)):
#            hidden1 = fully_connected(X, n_hidden1, scope="hidden1")
#            hidden2 = fully_connected(hidden1, n_hidden2, scope="hidden2")
#            logits = fully_connected(hidden2, n_outputs, activation_fn=None,scope="out")
# This code creates a neural network with two hidden layers and one output layer, and
# it also creates nodes in the graph to compute the ℓ1 regularization loss corresponding
# to each layer’s weights. TensorFlow automatically adds these nodes to a special collec‐
# tion containing all the regularization losses. You just need to add these regularization
# losses to your overall loss, like this:
#       reg_losses = tf.get_collection(tf.GraphKeys.REGULARIZATION_LOSSES)
#       loss = tf.add_n([base_loss] + reg_losses, name="loss")
# 
#                      Don’t forget to add the regularization losses to your overall loss, or
#                      else they will simply be ignored.
# 
# 
# 
# 
# Dropout
# The most popular regularization technique for deep neural networks is arguably
# dropout. It was proposed20 by G. E. Hinton in 2012 and further detailed in a paper21 by
# Nitish Srivastava et al., and it has proven to be highly successful: even the state-of-
# the-art neural networks got a 1–2% accuracy boost simply by adding dropout. This
# may not sound like a lot, but when a model already has 95% accuracy, getting a 2%
# accuracy boost means dropping the error rate by almost 40% (going from 5% error to
# roughly 3%).
# It is a fairly simple algorithm: at every training step, every neuron (including the
# input neurons but excluding the output neurons) has a probability p of being tem‐
# porarily “dropped out,” meaning it will be entirely ignored during this training step,
# but it may be active during the next step (see Figure 11-9). The hyperparameter p is
# called the dropout rate, and it is typically set to 50%. After training, neurons don’t get
# dropped anymore. And that’s all (except for a technical detail we will discuss momen‐
# tarily).
# 
# 
# 
# 
# 20 “Improving neural networks by preventing co-adaptation of feature detectors,” G. Hinton et al. (2012).
# 21 “Dropout: A Simple Way to Prevent Neural Networks from Overfitting,” N. Srivastava et al. (2014).
# 
# 
# 
# 304   |   Chapter 11: Training Deep Neural Nets
# 
#                  Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 11-9. Dropout regularization
# 
# It is quite surprising at first that this rather brutal technique works at all. Would a
# company perform better if its employees were told to toss a coin every morning to
# decide whether or not to go to work? Well, who knows; perhaps it would! The com‐
# pany would obviously be forced to adapt its organization; it could not rely on any sin‐
# gle person to fill in the coffee machine or perform any other critical tasks, so this
# expertise would have to be spread across several people. Employees would have to
# learn to cooperate with many of their coworkers, not just a handful of them. The
# company would become much more resilient. If one person quit, it wouldn’t make
# much of a difference. It’s unclear whether this idea would actually work for compa‐
# nies, but it certainly does for neural networks. Neurons trained with dropout cannot
# co-adapt with their neighboring neurons; they have to be as useful as possible on
# their own. They also cannot rely excessively on just a few input neurons; they must
# pay attention to each of their input neurons. They end up being less sensitive to slight
# changes in the inputs. In the end you get a more robust network that generalizes bet‐
# ter.
# Another way to understand the power of dropout is to realize that a unique neural
# network is generated at each training step. Since each neuron can be either present or
# absent, there is a total of 2N possible networks (where N is the total number of drop‐
# pable neurons). This is such a huge number that it is virtually impossible for the same
# neural network to be sampled twice. Once you have run a 10,000 training steps, you
# have essentially trained 10,000 different neural networks (each with just one training
# instance). These neural networks are obviously not independent since they share
# many of their weights, but they are nevertheless all different. The resulting neural
# network can be seen as an averaging ensemble of all these smaller neural networks.
# There is one small but important technical detail. Suppose p = 50, in which case dur‐
# ing testing a neuron will be connected to twice as many input neurons as it was (on
# average) during training. To compensate for this fact, we need to multiply each neu‐
# 
# 
#                                                 Avoiding Overfitting Through Regularization   |   305
# 
#                   Download from finelybook www.finelybook.com
# ron’s input connection weights by 0.5 after training. If we don’t, each neuron will get a
# total input signal roughly twice as large as what the network was trained on, and it is
# unlikely to perform well. More generally, we need to multiply each input connection
# weight by the keep probability (1 – p) after training. Alternatively, we can divide each
# neuron’s output by the keep probability during training (these alternatives are not
# perfectly equivalent, but they work equally well).
# To implement dropout using TensorFlow, you can simply apply the dropout() func‐
# tion to the input layer and to the output of every hidden layer. During training, this
# function randomly drops some items (setting them to 0) and divides the remaining
# items by the keep probability. After training, this function does nothing at all. The
# following code applies dropout regularization to our three-layer neural network:
#       from tensorflow.contrib.layers import dropout
# 
#       [...]
#       is_training = tf.placeholder(tf.bool, shape=(), name='is_training')
# 
#       keep_prob = 0.5
#       X_drop = dropout(X, keep_prob, is_training=is_training)
# 
#       hidden1 = fully_connected(X_drop, n_hidden1, scope="hidden1")
#       hidden1_drop = dropout(hidden1, keep_prob, is_training=is_training)
# 
#       hidden2 = fully_connected(hidden1_drop, n_hidden2, scope="hidden2")
#       hidden2_drop = dropout(hidden2, keep_prob, is_training=is_training)
# 
#       logits = fully_connected(hidden2_drop, n_outputs, activation_fn=None,
#                                scope="outputs")
# 
# 
#                      You want to use the dropout() function in tensorflow.con
#                      trib.layers, not the one in tensorflow.nn. The first one turns off
#                      (no-op) when not training, which is what you want, while the sec‐
#                      ond one does not.
# 
# 
# Of course, just like you did earlier for Batch Normalization, you need to set is_train
# ing to True when training, and to False when testing.
# If you observe that the model is overfitting, you can increase the dropout rate (i.e.,
# reduce the keep_prob hyperparameter). Conversely, you should try decreasing the
# dropout rate (i.e., increasing keep_prob) if the model underfits the training set. It can
# also help to increase the dropout rate for large layers, and reduce it for small ones.
# Dropout does tend to significantly slow down convergence, but it usually results in a
# much better model when tuned properly. So, it is generally well worth the extra time
# and effort.
# 
# 
# 
# 306   |   Chapter 11: Training Deep Neural Nets
# 
#                  Download from finelybook www.finelybook.com
#                Dropconnect is a variant of dropout where individual connections
#                are dropped randomly rather than whole neurons. In general drop‐
#                out performs better.
# 
# 
# 
# Max-Norm Regularization
# Another regularization technique that is quite popular for neural networks is called
# max-norm regularization: for each neuron, it constrains the weights w of the incom‐
# ing connections such that ∥ w ∥2 ≤ r, where r is the max-norm hyperparameter and
# ∥ · ∥2 is the ℓ2 norm.
# We typically implement this constraint by computing ∥w∥2 after each training step
#                                   r
# and clipping w if needed (� � ∥ � ∥ ).
#                                        2
# 
# Reducing r increases the amount of regularization and helps reduce overfitting. Max-
# norm regularization can also help alleviate the vanishing/exploding gradients prob‐
# lems (if you are not using Batch Normalization).
# TensorFlow does not provide an off-the-shelf max-norm regularizer, but it is not too
# hard to implement. The following code creates a node clip_weights that will clip the
# weights variable along the second axis so that each row vector has a maximum norm
# of 1.0:
#     threshold = 1.0
#     clipped_weights = tf.clip_by_norm(weights, clip_norm=threshold, axes=1)
#     clip_weights = tf.assign(weights, clipped_weights)
# You would then apply this operation after each training step, like so:
#     with tf.Session() as sess:
#         [...]
#         for epoch in range(n_epochs):
#             [...]
#             for X_batch, y_batch in zip(X_batches, y_batches):
#                 sess.run(training_op, feed_dict={X: X_batch, y: y_batch})
#                 clip_weights.eval()
# 
# You may wonder how to get access to the weights variable of each layer. For this you
# can simply use a variable scope like this:
#     hidden1 = fully_connected(X, n_hidden1, scope="hidden1")
# 
#     with tf.variable_scope("hidden1", reuse=True):
#         weights1 = tf.get_variable("weights")
# Alternatively, you can use the root variable scope:
#     hidden1 = fully_connected(X, n_hidden1, scope="hidden1")
#     hidden2 = fully_connected(hidden1, n_hidden2, scope="hidden2")
# 
# 
#                                                 Avoiding Overfitting Through Regularization   |   307
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Dropout",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Dropout(HierNode):
    def __init__(self):
        super().__init__("Dropout")
        self.add(Content(), "content")

# eof
