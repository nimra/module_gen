# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                           Chapter 35    Convolutional Neural Networks (CNN)
# 
# 
# 
# 
# Figure 35-3. Colored image with matrix representation
# 
# 
# Local Receptive Fields of the Visual Cortex
# The core concept of convolutional neural networks is built on understanding the
# local receptive fields found in the neurons of the visual cortex – the part of the brain
# responsible for processing visual information.
#      A local receptive field is an area on the neuron that excites or activates that neuron
# to fire information to other neurons. When viewing an image, the neurons in the visual
# cortex react to a small or limited area of the overall image due to the presence of a small
# local receptive field.
#                                                                                           425
# 
# Chapter 35   Convolutional Neural Networks (CNN)
# 
#      Hence, the neurons in the visual cortex do not all sense the entire image at the same
# time, but they are activated by viewing a local area of the image via its local receptive
# field.
#      In Figure 35-4, the local receptive fields overlap to give a collective perspective on
# the entire image. Each neuron in the visual cortex reacts to a different type of visual
# information (e.g., lines with different orientations).
# 
# 
# 
# 
# Figure 35-4. Local receptive field
# 
#     Other neurons have large receptive fields that react to more complex visual patterns
# such as edges, regions, and so on. From here we get the idea that neurons with larger
# receptive field receive information from those with lower receptive fields as they
# progressively learn the visual information of the image.
# 
# 
# 
# Advantages of CNN over MLP
# Suppose we have a 28 x 28 pixel set of image data, a feedforward neural network or
# multilayer perceptron will need 784 input weights plus a bias. By flattening an image as
# you would in MLP, we lose the spatial relationship of the pixels in the image.
#     CNN, on the other hand, can learn complex image features by preserving the spatial
# relationship between the image pixels. It does so by stacking convolutional layers
# whereby the neurons in the higher layers with a larger receptive field receive information
# 
# 426
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Local Receptive Fields of the Visual Cortex",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Local Receptive Fields of the Visual Cortex"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LocalReceptive(HierNode):
    def __init__(self):
        super().__init__("Local Receptive Fields of the Visual Cortex")
        self.add(Content())

# eof
