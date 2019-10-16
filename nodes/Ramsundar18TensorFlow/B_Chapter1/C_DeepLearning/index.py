# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_LeNet.index import LeNet as A_LeNet
from .B_AlexNet.index import AlexNet as B_AlexNet
from .C_ResNet.index import ResNet as C_ResNet
from .D_NeuralCaptioning.index import NeuralCaptioning as D_NeuralCaptioning
from .E_GoogleNeural.index import GoogleNeural as E_GoogleNeural
from .F_OneShotModels.index import OneShotModels as F_OneShotModels
from .G_AlphaGo.index import AlphaGo as G_AlphaGo
from .H_GenerativeAdversarial.index import GenerativeAdversarial as H_GenerativeAdversarial
from .I_NeuralTuring.index import NeuralTuring as I_NeuralTuring

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Deep Learning Architectures
# There have been hundreds of different deep learning models that combine the deep
# learning primitives presented in the previous section. Some of these architectures
# have been historically important. Others were the first presentations of novel designs
# that influenced perceptions of what deep learning could do.
# In this section, we present a selection of different deep learning architectures that
# have proven influential for the research community. We want to emphasize that this
# is an episodic history that makes no attempt to be exhaustive. There are certainly
# important models in the literature that have not been presented here.
# 
# LeNet
# The LeNet architecture is arguably the first prominent “deep” convolutional architec‐
# ture. Introduced in 1988, it was used to perform optical character recoginition (OCR)
# for documents. Although it performed its task admirably, the computational cost of
# the LeNet was extreme for the computer hardware available at the time, so the design
# languished in (relative) obscurity for a few decades after its creation. This architec‐
# ture is illustrated in Figure 1-5.
# 
# 
# 
# 
# Figure 1-5. The LeNet architecture for image processing. Introduced in 1988, it was argu‐
# ably the first deep convolutional model for image processing.
# 
# AlexNet
# The ImageNet Large Scale Visual Recognition Challenge (ILSVRC) was first organ‐
# ized in 2010 as a test of the progress made in visual recognition systems. The organiz‐
# ers made use of Amazon Mechanical Turk, an online platform to connect workers to
# requesters, to catalog a large collection of images with associated lists of objects
# present in the image. The use of Mechanical Turk permitted the curation of a collec‐
# tion of data significantly larger than those gathered previously.
# The first two years the challenge ran, more traditional machine-learned systems that
# relied on systems like HOG and SIFT features (hand-tuned visual feature extraction
# methods) triumphed. In 2012, the AlexNet architecture, based on a modification of
# LeNet run on powerful graphics processing units (GPUs), entered and dominated the
# 
# 
# 6   |   Chapter 1: Introduction to Deep Learning
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Deep Learning Architectures",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Deep Learning Architectures"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DeepLearning(HierNode):
    def __init__(self):
        super().__init__("Deep Learning Architectures")
        self.add(Content())
        self.add(A_LeNet())
        self.add(B_AlexNet())
        self.add(C_ResNet())
        self.add(D_NeuralCaptioning())
        self.add(E_GoogleNeural())
        self.add(F_OneShotModels())
        self.add(G_AlphaGo())
        self.add(H_GenerativeAdversarial())
        self.add(I_NeuralTuring())

# eof
