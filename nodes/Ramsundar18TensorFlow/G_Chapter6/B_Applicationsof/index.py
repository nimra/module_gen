# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_ObjectDetection.index import ObjectDetection as A_ObjectDetection
from .B_ImageSegmentation.index import ImageSegmentation as B_ImageSegmentation
from .C_GraphConvolutions.index import GraphConvolutions as C_GraphConvolutions
from .D_GeneratingImages.index import GeneratingImages as D_GeneratingImages

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Figure 6-8. A dilated (or atrous) convolution. Gaps are left in the local receptive field for
# each neuron. Diagram (a) depicts a 1-dilated 3 × 3 convolution. Diagram (b) depicts the
# application of a 2-dilated 3 × 3 convolution to (a). Diagram (c) depicts the application of
# a 4-dilated 3 × 3 convolution to (b). Notice that the (a) layer has receptive field of width
# 3, the (b) layer has receptive field of width 7, and the (c) layer has receptive field of width
# 15.
# 
# Applications of Convolutional Networks
# In the previous section, we covered the mechanics of convolutional networks and
# introduced you to many of the components that make up these networks. In this sec‐
# tion, we describe some applications that convolutional architectures enable.
# 
# Object Detection and Localization
# Object detection is the task of detecting the objects (or entities) present in a photo‐
# graph. Object localization is the task of identifying where in the image the objects
# exist and drawing a “bounding box” around each occurrence. Figure 6-9 demon‐
# strates what detection and localization on standard images looks like.
# 
# 
# 
# 
# Figure 6-9. Objects detected and localized with bounding boxes in some example images.
# 
# 
#                                                         Applications of Convolutional Networks   |   127
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Applications of Convolutional Networks",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(mbk("# Applications of Convolutional Networks"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Applicationsof(HierNode):
    def __init__(self):
        super().__init__("Applications of Convolutional Networks")
        self.add(Content())
        self.add(A_ObjectDetection())
        self.add(B_ImageSegmentation())
        self.add(C_GraphConvolutions())
        self.add(D_GeneratingImages())

# eof
