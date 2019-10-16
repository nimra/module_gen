# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Filters.index import Filters as A_Filters
from .B_StackingMultiple.index import StackingMultiple as B_StackingMultiple
from .C_TensorFlowImplementation.index import TensorFlowImplementation as C_TensorFlowImplementation
from .D_MemoryRequirements.index import MemoryRequirements as D_MemoryRequirements

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                     Download from finelybook www.finelybook.com
# and Patrick Haffner, which introduced the famous LeNet-5 architecture, widely used
# to recognize handwritten check numbers. This architecture has some building blocks
# that you already know, such as fully connected layers and sigmoid activation func‐
# tions, but it also introduces two new building blocks: convolutional layers and pooling
# layers. Let’s look at them now.
# 
#                    Why not simply use a regular deep neural network with fully con‐
#                    nected layers for image recognition tasks? Unfortunately, although
#                    this works fine for small images (e.g., MNIST), it breaks down for
#                    larger images because of the huge number of parameters it
#                    requires. For example, a 100 × 100 image has 10,000 pixels, and if
#                    the first layer has just 1,000 neurons (which already severely
#                    restricts the amount of information transmitted to the next layer),
#                    this means a total of 10 million connections. And that’s just the first
#                    layer. CNNs solve this problem using partially connected layers.
# 
# 
# Convolutional Layer
# The most important building block of a CNN is the convolutional layer:6 neurons in
# the first convolutional layer are not connected to every single pixel in the input image
# (like they were in previous chapters), but only to pixels in their receptive fields (see
# Figure 13-2). In turn, each neuron in the second convolutional layer is connected
# only to neurons located within a small rectangle in the first layer. This architecture
# allows the network to concentrate on low-level features in the first hidden layer, then
# assemble them into higher-level features in the next hidden layer, and so on. This
# hierarchical structure is common in real-world images, which is one of the reasons
# why CNNs work so well for image recognition.
# 
# 
# 
# 
# 6 A convolution is a mathematical operation that slides one function over another and measures the integral of
#   their pointwise multiplication. It has deep connections with the Fourier transform and the Laplace transform,
#   and is heavily used in signal processing. Convolutional layers actually use cross-correlations, which are very
#   similar to convolutions (see http://goo.gl/HAfxXd for more details).
# 
# 
# 
#                                                                                     Convolutional Layer   |   355
# 
#                        Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 13-2. CNN layers with rectangular local receptive fields
# 
#                     Until now, all multilayer neural networks we looked at had layers
#                     composed of a long line of neurons, and we had to flatten input
#                     images to 1D before feeding them to the neural network. Now each
#                     layer is represented in 2D, which makes it easier to match neurons
#                     with their corresponding inputs.
# 
# A neuron located in row i, column j of a given layer is connected to the outputs of the
# neurons in the previous layer located in rows i to i + fh – 1, columns j to j + fw – 1,
# where fh and fw are the height and width of the receptive field (see Figure 13-3). In
# order for a layer to have the same height and width as the previous layer, it is com‐
# mon to add zeros around the inputs, as shown in the diagram. This is called zero pad‐
# ding.
# 
# 
# 
# 
# Figure 13-3. Connections between layers and zero padding
# 
# 
# 356   |   Chapter 13: Convolutional Neural Networks
# 
#                     Download from finelybook www.finelybook.com
# It is also possible to connect a large input layer to a much smaller layer by spacing out
# the receptive fields, as shown in Figure 13-4. The distance between two consecutive
# receptive fields is called the stride. In the diagram, a 5 × 7 input layer (plus zero pad‐
# ding) is connected to a 3 × 4 layer, using 3 × 3 receptive fields and a stride of 2 (in this
# example the stride is the same in both directions, but it does not have to be so). A
# neuron located in row i, column j in the upper layer is connected to the outputs of the
# neurons in the previous layer located in rows i × sh to i × sh + fh – 1, columns j × sw +
# fw – 1, where sh and sw are the vertical and horizontal strides.
# 
# 
# 
# 
# Figure 13-4. Reducing dimensionality using a stride
# 
# Filters
# A neuron’s weights can be represented as a small image the size of the receptive field.
# For example, Figure 13-5 shows two possible sets of weights, called filters (or convolu‐
# tion kernels). The first one is represented as a black square with a vertical white line in
# the middle (it is a 7 × 7 matrix full of 0s except for the central column, which is full of
# 1s); neurons using these weights will ignore everything in their receptive field except
# for the central vertical line (since all inputs will get multiplied by 0, except for the
# ones located in the central vertical line). The second filter is a black square with a
# horizontal white line in the middle. Once again, neurons using these weights will
# ignore everything in their receptive field except for the central horizontal line.
# Now if all neurons in a layer use the same vertical line filter (and the same bias term),
# and you feed the network the input image shown in Figure 13-5 (bottom image), the
# layer will output the top-left image. Notice that the vertical white lines get enhanced
# while the rest gets blurred. Similarly, the upper-right image is what you get if all neu‐
# rons use the horizontal line filter; notice that the horizontal white lines get enhanced
# while the rest is blurred out. Thus, a layer full of neurons using the same filter gives
# 
# 
# 
#                                                                      Convolutional Layer   |   357
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
        self.add(A_Filters())
        self.add(B_StackingMultiple())
        self.add(C_TensorFlowImplementation())
        self.add(D_MemoryRequirements())

# eof
