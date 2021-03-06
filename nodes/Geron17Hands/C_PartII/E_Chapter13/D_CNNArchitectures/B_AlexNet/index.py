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
#                 Download from finelybook www.finelybook.com
#   • Most neurons in C3 maps are connected to neurons in only three or four S2
#     maps (instead of all six S2 maps). See table 1 in the original paper for details.
#   • The output layer is a bit special: instead of computing the dot product of the
#     inputs and the weight vector, each neuron outputs the square of the Euclidian
#     distance between its input vector and its weight vector. Each output measures
#     how much the image belongs to a particular digit class. The cross entropy cost
#     function is now preferred, as it penalizes bad predictions much more, producing
#     larger gradients and thus converging faster.
# 
# Yann LeCun’s website (“LENET” section) features great demos of LeNet-5 classifying
# digits.
# 
# AlexNet
# The AlexNet CNN architecture9 won the 2012 ImageNet ILSVRC challenge by a large
# margin: it achieved 17% top-5 error rate while the second best achieved only 26%! It
# was developed by Alex Krizhevsky (hence the name), Ilya Sutskever, and Geoffrey
# Hinton. It is quite similar to LeNet-5, only much larger and deeper, and it was the
# first to stack convolutional layers directly on top of each other, instead of stacking a
# pooling layer on top of each convolutional layer. Table 13-2 presents this architecture.
# 
# Table 13-2. AlexNet architecture
# Layer Type          Maps        Size       Kernel size Stride Padding Activation
# Out Fully Connected –           1,000      –           –      –       Softmax
# F9     Fully Connected –        4,096      –           –      –         ReLU
# F8     Fully Connected –        4,096      –           –      –         ReLU
# C7     Convolution     256      13 × 13    3×3         1      SAME      ReLU
# C6     Convolution     384      13 × 13    3×3         1      SAME      ReLU
# C5     Convolution     384      13 × 13    3×3         1      SAME      ReLU
# S4     Max Pooling     256      13 × 13    3×3         2      VALID     –
# C3     Convolution     256      27 × 27    5×5         1      SAME      ReLU
# S2     Max Pooling     96       27 × 27    3×3         2      VALID     –
# C1     Convolution     96       55 × 55    11 × 11     4      SAME      ReLU
# In     Input           3 (RGB) 224 × 224 –             –      –         –
# 
# To reduce overfitting, the authors used two regularization techniques we discussed in
# previous chapters: first they applied dropout (with a 50% dropout rate) during train‐
# ing to the outputs of layers F8 and F9. Second, they performed data augmentation by
# 
# 
# 
# 9 “ImageNet Classification with Deep Convolutional Neural Networks,” A. Krizhevsky et al. (2012).
# 
# 
# 
#                                                                                    CNN Architectures   |   367
# 
#                 Download from finelybook www.finelybook.com
# randomly shifting the training images by various offsets, flipping them horizontally,
# and changing the lighting conditions.
# AlexNet also uses a competitive normalization step immediately after the ReLU step
# of layers C1 and C3, called local response normalization. This form of normalization
# makes the neurons that most strongly activate inhibit neurons at the same location
# but in neighboring feature maps (such competitive activation has been observed in
# biological neurons). This encourages different feature maps to specialize, pushing
# them apart and forcing them to explore a wider range of features, ultimately improv‐
# ing generalization. Equation 13-2 shows how to apply LRN.
# 
#       Equation 13-2. Local response normalization
#                                         −β                        r
#                        jhigh                      jhigh = min i + , f n − 1
#                                                                   2
#       bi = ai k + α     ∑
#                       j = jlow
#                                  a j2        with
#                                                                     r
#                                                   jlow = max 0, i −
#                                                                     2
# 
# 
#    • bi is the normalized output of the neuron located in feature map i, at some row u
#      and column v (note that in this equation we consider only neurons located at this
#      row and column, so u and v are not shown).
#    • ai is the activation of that neuron after the ReLU step, but before normalization.
#    • k, α, β, and r are hyperparameters. k is called the bias, and r is called the depth
#      radius.
#    • fn is the number of feature maps.
# 
# For example, if r = 2 and a neuron has a strong activation, it will inhibit the activation
# of the neurons located in the feature maps immediately above and below its own.
# In AlexNet, the hyperparameters are set as follows: r = 2, α = 0.00002, β = 0.75, and k
# = 1. This step can be implemented using TensorFlow’s local_response_normaliza
# tion() operation.
# A variant of AlexNet called ZF Net was developed by Matthew Zeiler and Rob Fergus
# and won the 2013 ILSVRC challenge. It is essentially AlexNet with a few tweaked
# hyperparameters (number of feature maps, kernel size, stride, etc.).
# 
# GoogLeNet
# The GoogLeNet architecture was developed by Christian Szegedy et al. from Google
# Research,10 and it won the ILSVRC 2014 challenge by pushing the top-5 error rate
# 
# 
# 10 “Going Deeper with Convolutions,” C. Szegedy et al. (2015).
# 
# 
# 
# 368    |   Chapter 13: Convolutional Neural Networks
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "AlexNet",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class AlexNet(HierNode):
    def __init__(self):
        super().__init__("AlexNet")
        self.add(Content(), "content")

# eof
