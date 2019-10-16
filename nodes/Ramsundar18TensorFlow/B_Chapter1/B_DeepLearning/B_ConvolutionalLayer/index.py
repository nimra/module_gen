# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Convolutional Layer
# A convolutional network assumes special spatial structure in its input. In particular, it
# assumes that inputs that are close to each other spatially are semantically related. This
# assumption makes most sense for images, since pixels close to one another are likely
# semantically linked. As a result, convolutional layers have found wide use in deep
# architectures for image processing. This concept is illustrated in Figure 1-2.
# Just like fully connected layers transform lists to lists, convolutional layers transform
# images into images. As a result, convolutional layers can be used to perform complex
# image transformations, such as applying artistic filters to images in photo apps.
# 
# 
# 
# 
# Figure 1-2. A convolutional layer. The red shape on the left represents the input data,
# while the blue shape on the right represents the output. In this particular case, the input
# is of shape (32, 32, 3). That is, the input is a 32-pixel-by-32-pixel image with three RGB
# color channels. The highlighted region in the red input is a “local receptive field,” a group
# of inputs that are processed together to create the highlighted region in the blue output.
# 
# Recurrent Neural Network Layers
# Recurrent neural network (RNN) layers are primitives that allow neural networks to
# learn from sequences of inputs. This layer assumes that the input evolves from step to
# step following a defined update rule that can be learned from data. This update rule
# presents a prediction of the next state in the sequence given all the states that have
# come previously. An RNN is illustrated in Figure 1-3.
# An RNN layer can learn this update rule from data. As a result, RNNs are very useful
# for tasks such as language modeling, where engineers seek to build systems that can
# predict the next word users will type from history.
# 
# 
# 
# 
# 4   |   Chapter 1: Introduction to Deep Learning
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Convolutional Layer",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Convolutional Layer"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ConvolutionalLayer(HierNode):
    def __init__(self):
        super().__init__("Convolutional Layer")
        self.add(Content())

# eof
