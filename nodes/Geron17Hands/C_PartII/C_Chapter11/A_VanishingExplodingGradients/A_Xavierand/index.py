# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                       Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 11-1. Logistic activation function saturation
# 
# Xavier and He Initialization
# In their paper, Glorot and Bengio propose a way to significantly alleviate this prob‐
# lem. We need the signal to flow properly in both directions: in the forward direction
# when making predictions, and in the reverse direction when backpropagating gradi‐
# ents. We don’t want the signal to die out, nor do we want it to explode and saturate.
# For the signal to flow properly, the authors argue that we need the variance of the
# outputs of each layer to be equal to the variance of its inputs,2 and we also need the
# gradients to have equal variance before and after flowing through a layer in the
# reverse direction (please check out the paper if you are interested in the mathematical
# details). It is actually not possible to guarantee both unless the layer has an equal
# number of input and output connections, but they proposed a good compromise that
# has proven to work very well in practice: the connection weights must be initialized
# randomly as described in Equation 11-1, where ninputs and noutputs are the number of
# input and output connections for the layer whose weights are being initialized (also
# called fan-in and fan-out). This initialization strategy is often called Xavier initializa‐
# tion (after the author’s first name), or sometimes Glorot initialization.
# 
# 
# 
# 
# 2 Here’s an analogy: if you set a microphone amplifier’s knob too close to zero, people won’t hear your voice, but
#   if you set it too close to the max, your voice will be saturated and people won’t understand what you are say‐
#   ing. Now imagine a chain of such amplifiers: they all need to be set properly in order for your voice to come
#   out loud and clear at the end of the chain. Your voice has to come out of each amplifier at the same amplitude
#   as it came in.
# 
# 
# 
#                                                                  Vanishing/Exploding Gradients Problems    |   277
# 
#                    Download from finelybook www.finelybook.com
#       Equation 11-1. Xavier initialization (when using the logistic activation function)
#                                                                                                   2
#        Normal distribution with mean 0 and standard deviation σ =
#                                                                                           ninputs + noutputs
#                                                                                            6
#        Or a uniform distribution between ‐r and +r, with r =
#                                                                                    ninputs + noutputs
# 
# When the number of input connections is roughly equal to the number of output
# connections, you get simpler equations (e.g., σ = 1/ ninputs or r = 3/ ninputs). We
# used this simplified strategy in Chapter 10.3
# Using the Xavier initialization strategy can speed up training considerably, and it is
# one of the tricks that led to the current success of Deep Learning. Some recent papers4
# have provided similar strategies for different activation functions, as shown in
# Table 11-1. The initialization strategy for the ReLU activation function (and its var‐
# iants, including the ELU activation described shortly) is sometimes called He initiali‐
# zation (after the last name of its author).
# 
# Table 11-1. Initialization parameters for each type of activation function
# Activation function       Uniform distribution [–r, r] Normal distribution
# Logistic                                 6                            2
#                           r=                          σ=
#                                 ninputs + noutputs           ninputs + noutputs
# Hyperbolic tangent                        6                            2
#                           r=4                         σ=4
#                                  ninputs + noutputs           ninputs + noutputs
# ReLU (and its variants)                     6                       2
#                           r= 2                        σ= 2
#                                    ninputs + noutputs      ninputs + noutputs
# 
# 
# By default, the fully_connected() function (introduced in Chapter 10) uses Xavier
# initialization (with a uniform distribution). You can change this to He initialization
# by using the variance_scaling_initializer() function like this:
#       he_init = tf.contrib.layers.variance_scaling_initializer()
#       hidden1 = fully_connected(X, n_hidden1, weights_initializer=he_init, scope="h1")
# 
# 
# 
# 
# 3 This simplified strategy was actually already proposed much earlier—for example, in the 1998 book Neural
#   Networks: Tricks of the Trade by Genevieve Orr and Klaus-Robert Müller (Springer).
# 4 Such as “Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification,” K.
#   He et al. (2015).
# 
# 
# 
# 278    |   Chapter 11: Training Deep Neural Nets
# 
#                      Download from finelybook www.finelybook.com
#                    He initialization considers only the fan-in, not the average between
#                    fan-in and fan-out like in Xavier initialization. This is also the
#                    default for the variance_scaling_initializer() function, but
#                    you can change this by setting the argument mode="FAN_AVG".
# 
# 
# Nonsaturating Activation Functions
# One of the insights in the 2010 paper by Glorot and Bengio was that the vanishing/
# exploding gradients problems were in part due to a poor choice of activation func‐
# tion. Until then most people had assumed that if Mother Nature had chosen to use
# roughly sigmoid activation functions in biological neurons, they must be an excellent
# choice. But it turns out that other activation functions behave much better in deep
# neural networks, in particular the ReLU activation function, mostly because it does
# not saturate for positive values (and also because it is quite fast to compute).
# Unfortunately, the ReLU activation function is not perfect. It suffers from a problem
# known as the dying ReLUs: during training, some neurons effectively die, meaning
# they stop outputting anything other than 0. In some cases, you may find that half of
# your network’s neurons are dead, especially if you used a large learning rate. During
# training, if a neuron’s weights get updated such that the weighted sum of the neuron’s
# inputs is negative, it will start outputting 0. When this happen, the neuron is unlikely
# to come back to life since the gradient of the ReLU function is 0 when its input is
# negative.
# To solve this problem, you may want to use a variant of the ReLU function, such as
# the leaky ReLU. This function is defined as LeakyReLUα(z) = max(αz, z) (see
# Figure 11-2). The hyperparameter α defines how much the function “leaks”: it is the
# slope of the function for z < 0, and is typically set to 0.01. This small slope ensures
# that leaky ReLUs never die; they can go into a long coma, but they have a chance to
# eventually wake up. A recent paper5 compared several variants of the ReLU activation
# function and one of its conclusions was that the leaky variants always outperformed
# the strict ReLU activation function. In fact, setting α = 0.2 (huge leak) seemed to
# result in better performance than α = 0.01 (small leak). They also evaluated the
# randomized leaky ReLU (RReLU), where α is picked randomly in a given range during
# training, and it is fixed to an average value during testing. It also performed fairly well
# and seemed to act as a regularizer (reducing the risk of overfitting the training set).
# Finally, they also evaluated the parametric leaky ReLU (PReLU), where α is authorized
# to be learned during training (instead of being a hyperparameter, it becomes a
# parameter that can be modified by backpropagation like any other parameter). This
# 
# 
# 
# 
# 5 “Empirical Evaluation of Rectified Activations in Convolution Network,” B. Xu et al. (2015).
# 
# 
# 
#                                                                  Vanishing/Exploding Gradients Problems   |   279
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Xavier and He Initialization",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Xavier and He Initialization"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Xavierand(HierNode):
    def __init__(self):
        super().__init__("Xavier and He Initialization")
        self.add(Content())

# eof
