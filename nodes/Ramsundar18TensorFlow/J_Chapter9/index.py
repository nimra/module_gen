# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_CustomHardware.index import CustomHardware as A_CustomHardware
from .B_CPUTraining.index import CPUTraining as B_CPUTraining
from .C_DistributedDeep.index import DistributedDeep as C_DistributedDeep
from .D_DataParallel.index import DataParallel as D_DataParallel
from .E_Review.index import Review as E_Review

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                                                          CHAPTER 9
#                           Training Large Deep Networks
# 
# 
# 
# 
# Thus far, you have seen how to train small models that can be completely trained on a
# good laptop computer. All of these models can be run fruitfully on GPU-equipped
# hardware with notable speed boosts (with the notable exception of reinforcement
# learning models for reasons discussed in the previous chapter). However, training
# larger models still requires considerable sophistication. In this chapter, we will dis‐
# cuss various types of hardware that can be used to train deep networks, including
# graphics processing units (GPUs), tensor processing units (TPUs), and neuromorphic
# chips. We will also briefly cover the principles of distributed training for larger deep
# learning models. We end the chapter with an in-depth case study, adapated from one
# of the TensorFlow tutorials, demonstrating how to train a CIFAR-10 convolutional
# neural network on a server with multiple GPUs. We recommend that you attempt to
# try running this code yourself, but readily acknowledge that gaining access to a multi-
# GPU server is trickier than finding a good laptop. Luckily, access to multi-GPU
# servers on the cloud is becoming possible and is likely the best solution for industrial
# users of TensorFlow seeking to train large models.
# 
# Custom Hardware for Deep Networks
# As you’ve seen throughout the book, deep network training requires chains of tenso‐
# rial operations performed repeatedly on minibatches of data. Tensorial operations are
# commonly transformed into matrix multiplication operations by software, so rapid
# training of deep networks fundamentally depends on the ability to perform matrix
# multiplication operations rapidly. While CPUs are perfectly capable of implementing
# matrix multiplications, the generality of CPU hardware means much effort will be
# wasted on overhead unneeded for mathematical operations.
# 
# 
# 
# 
#                                                                                      205
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 9. Training Large Deep Networks",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(mbk("# Chapter 9. Training Large Deep Networks"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter9(HierNode):
    def __init__(self):
        super().__init__("Chapter 9. Training Large Deep Networks")
        self.add(Content())
        self.add(A_CustomHardware())
        self.add(B_CPUTraining())
        self.add(C_DistributedDeep())
        self.add(D_DataParallel())
        self.add(E_Review())

# eof
