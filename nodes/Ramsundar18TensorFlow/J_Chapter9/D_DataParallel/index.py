# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_Downloadingand.index import Downloadingand as A_Downloadingand
from .B_DeepDive.index import DeepDive as B_DeepDive
from .C_Trainingon.index import Trainingon as C_Trainingon
from .D_Challengefor.index import Challengefor as D_Challengefor

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Data Parallel Training with Multiple GPUs on Cifar10
# In this section, we will give you an in-depth walkthrough of how to train a data-
# parallel convolutional network on the Cifar10 benchmark set. Cifar10 consists of
# 60,000 images of size 32 × 32. The Cifar10 dataset is often used to benchmark convo‐
# lutional architectures. Figure 9-7 displays sample images from the Cifar10 dataset.
# 
# 
# 
# 
# Figure 9-7. The Cifar10 dataset consists of 60,000 images drawn from 10 classes. Some
# sample images from various classes are displayed here.
# 
# The architecture we will use in this section loads separate copies of the model archi‐
# tecture on different GPUs and periodically syncs learned weights across cores, as
# Figure 9-8 illustrates.
# 
# 
# 
# 
#                                           Data Parallel Training with Multiple GPUs on Cifar10   |   215
# 
# Figure 9-8. The data parallel architecture you will train in this chapter.
# 
# Downloading and Loading the DATA
# The read_cifar10() method reads and parses the Cifar10 raw data files. Example 9-1
# uses tf.FixedLengthRecordReader to read raw data from the Cifar10 files.
# 
# Example 9-1. This function reads and parses data from Cifar10 raw data files
# 
# def read_cifar10(filename_queue):
#   """Reads and parses examples from CIFAR10 data files.
# 
#   Recommendation: if you want N-way read parallelism, call this function
#   N times. This will give you N independent Readers reading different
#   files & positions within those files, which will give better mixing of
#   examples.
# 
#   Args:
#     filename_queue: A queue of strings with the filenames to read from.
# 
#   Returns:
#     An object representing a single example, with the following fields:
#       height: number of rows in the result (32)
#       width: number of columns in the result (32)
#       depth: number of color channels in the result (3)
# 
# 
# 
# 216   | Chapter 9: Training Large Deep Networks
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Data Parallel Training with Multiple GPUs on Cifar10",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(mbk("# Data Parallel Training with Multiple GPUs on Cifar10"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DataParallel(HierNode):
    def __init__(self):
        super().__init__("Data Parallel Training with Multiple GPUs on Cifar10")
        self.add(Content())
        self.add(A_Downloadingand())
        self.add(B_DeepDive())
        self.add(C_Trainingon())
        self.add(D_Challengefor())

# eof
