# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_FullyConnected.index import FullyConnected as A_FullyConnected
from .B_ConvolutionalLayer.index import ConvolutionalLayer as B_ConvolutionalLayer
from .C_RecurrentNeural.index import RecurrentNeural as C_RecurrentNeural
from .D_LongShortTerm.index import LongShortTerm as D_LongShortTerm

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Deep Learning Primitives
# Most deep architectures are built by combining and recombining a limited set of
# architectural primitives. Such primitives, typically called neural network layers, are
# the foundational building blocks of deep networks. In the rest of this book, we will
# provide in-depth introductions to such layers. However, in this section, we will pro‐
# vide a brief overview of the common modules that are found in many deep networks.
# This section is not meant to provide a thorough introduction to these modules.
# Rather, we aim to provide a rapid overview of the building blocks of sophisticated
# deep architectures to whet your appetite. The art of deep learning consists of combin‐
# ing and recombining such modules and we want to show you the alphabet of the lan‐
# guage to start you on the path to deep learning expertise.
# 
# Fully Connected Layer
# A fully connected network transforms a list of inputs into a list of outputs. The trans‐
# formation is called fully connected since any input value can affect any output value.
# These layers will have many learnable parameters, even for relatively small inputs, but
# they have the large advantage of assuming no structure in the inputs. This concept is
# illustrated in Figure 1-1.
# 
# 
# 
# 
# Figure 1-1. A fully connected layer. Inbound arrows represent inputs, while outbound
# arrows represent outputs. The thickness of interconnecting lines represents the magnitude
# of learned weights. The fully connected layer transforms inputs into outputs via the
# learned rule.
# 
# 
#                                                                 Deep Learning Primitives   |   3
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Deep Learning Primitives",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Deep Learning Primitives"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DeepLearning(HierNode):
    def __init__(self):
        super().__init__("Deep Learning Primitives")
        self.add(Content())
        self.add(A_FullyConnected())
        self.add(B_ConvolutionalLayer())
        self.add(C_RecurrentNeural())
        self.add(D_LongShortTerm())

# eof
