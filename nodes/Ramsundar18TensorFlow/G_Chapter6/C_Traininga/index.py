# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_TheMNIST.index import TheMNIST as A_TheMNIST
from .B_LoadingMNIST.index import LoadingMNIST as B_LoadingMNIST
from .C_TensorFlowConvolutional.index import TensorFlowConvolutional as C_TensorFlowConvolutional
from .D_TheConvolutional.index import TheConvolutional as D_TheConvolutional
from .E_EvaluatingTrained.index import EvaluatingTrained as E_EvaluatingTrained
from .F_Challengefor.index import Challengefor as F_Challengefor

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Figure 6-16. The CycleGAN is capable of performing complex image transformations,
# such as transforming images of horses into those of zebras (and vice versa).
# 
# Unfortunately, generative adversarial networks are still challenging to train in prac‐
# tice. Making generators and discriminators learn reasonable functions requires a
# deep bag of tricks. As a result, while there have been many exciting GAN demonstra‐
# tions, GANs have not yet matured into a state where they can be widely deployed in
# industrial applications.
# 
# Training a Convolutional Network in TensorFlow
# In this section we consider a code sample for training a simple convolutional neural
# network. In particular, our code sample will demonstrate how to train a LeNet-5 con‐
# volutional architecture on the MNIST dataset using TensorFlow. As always, we rec‐
# ommend that you follow along by running the full code sample from the GitHub
# repo associated with the book.
# 
# The MNIST Dataset
# The MNIST dataset consists of images of handwritten digits. The machine learning
# challenge associated with MNIST consists of creating a model trained on the training
# set of digits that generalizes to the validation set. Figure 6-17 shows some images
# drawn from the MNIST dataset.
# 
# 
# 
# 
# 134   |   Chapter 6: Convolutional Neural Networks
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Training a Convolutional Network in TensorFlow",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(mbk("# Training a Convolutional Network in TensorFlow"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Traininga(HierNode):
    def __init__(self):
        super().__init__("Training a Convolutional Network in TensorFlow")
        self.add(Content())
        self.add(A_TheMNIST())
        self.add(B_LoadingMNIST())
        self.add(C_TensorFlowConvolutional())
        self.add(D_TheConvolutional())
        self.add(E_EvaluatingTrained())
        self.add(F_Challengefor())

# eof
