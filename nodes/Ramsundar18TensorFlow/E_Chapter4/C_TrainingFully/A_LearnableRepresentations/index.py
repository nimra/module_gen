# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Training Fully Connected Neural Networks
# As we mentioned previously, the theory of fully connected networks falls short of
# practice. In this section, we will introduce you to a number of empirical observations
# about fully connected networks that aid practitioners. We strongly encourage you to
# use our code (introduced later in the chapter) to check our claims for yourself.
# 
# Learnable Representations
# One way of thinking about fully connected networks is that each fully connected layer
# effects a transformation of the feature space in which the problem resides. The idea of
# transforming the representation of a problem to render it more malleable is a very
# old one in engineering and physics. It follows that deep learning methods are some‐
# times called “representation learning.” (An interesting factoid is that one of the major
# conferences for deep learning is called the “International Conference on Learning
# Representations.”)
# Generations of analysts have used Fourier transforms, Legendre transforms, Laplace
# transforms, and so on in order to simplify complicated equations and functions to
# forms more suitable for handwritten analysis. One way of thinking about deep learn‐
# ing networks is that they effect a data-driven transform suited to the problem at
# hand.
# The ability to perform problem-specific transformations can be immensely powerful.
# Standard transformation techniques couldn’t solve problems of image or speech anal‐
# ysis, while deep networks are capable of solving these problems with relative ease due
# to the inherent flexibility of the learned representations. This flexibility comes with a
# price: the transformations learned by deep architectures tend to be much less general
# than mathematical transforms such as the Fourier transform. Nonetheless, having
# deep transforms in an analytic toolkit can be a powerful problem-solving tool.
# There’s a reasonable argument that deep learning is simply the first representation
# learning method that works. In the future, there may well be alternative representa‐
# tion learning methods that supplant deep learning methods.
# 
# Activations
# We previously introduced the nonlinear function σ as the sigmoidal function. While
# the sigmoidal is the classical nonlinearity in fully connected networks, in recent years
# researchers have found that other activations, notably the rectified linear activation
# (commonly abbreviated ReLU or relu) σ x = max x, 0 work better than the sigmoi‐
# dal unit. This empirical observation may be due to the vanishing gradient problem in
# deep networks. For the sigmoidal function, the slope is zero for almost all values of its
# input. As a result, for deeper networks, the gradient would tend to zero. For the ReLU
# function, the slope is nonzero for a much greater part of input space, allowing non‐
# 
# 
#                                                    Training Fully Connected Neural Networks   |   89
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Learnable Representations",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Learnable Representations"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LearnableRepresentations(HierNode):
    def __init__(self):
        super().__init__("Learnable Representations")
        self.add(Content())

# eof
