# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_OneNeural.index import OneNeural as A_OneNeural
from .B_InGraphVersus.index import InGraphVersus as B_InGraphVersus
from .C_ModelParallelism.index import ModelParallelism as C_ModelParallelism
from .D_DataParallelism.index import DataParallelism as D_DataParallelism

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                 Download from finelybook www.finelybook.com
#   • Reading inputs efficiently using readers, queue runners, and coordinators
# 
# Now let’s use all of this to parallelize neural networks!
# 
# Parallelizing Neural Networks on a TensorFlow Cluster
# In this section, first we will look at how to parallelize several neural networks by sim‐
# ply placing each one on a different device. Then we will look at the much trickier
# problem of training a single neural network across multiple devices and servers.
# 
# One Neural Network per Device
# The most trivial way to train and run neural networks on a TensorFlow cluster is to
# take the exact same code you would use for a single device on a single machine, and
# specify the master server’s address when creating the session. That’s it—you’re done!
# Your code will be running on the server’s default device. You can change the device
# that will run your graph simply by putting your code’s construction phase within a
# device block.
# By running several client sessions in parallel (in different threads or different pro‐
# cesses), connecting them to different servers, and configuring them to use different
# devices, you can quite easily train or run many neural networks in parallel, across all
# devices and all machines in your cluster (see Figure 12-11). The speedup is almost
# linear.4 Training 100 neural networks across 50 servers with 2 GPUs each will not take
# much longer than training just 1 neural network on 1 GPU.
# 
# 
# 
# 
# Figure 12-11. Training one neural network per device
# 
# 
# 4 Not 100% linear if you wait for all devices to finish, since the total time will be the time taken by the slowest
#   device.
# 
# 
# 
# 342   |     Chapter 12: Distributing TensorFlow Across Devices and Servers
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Parallelizing Neural Networks on a TensorFlow Cluster",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Parallelizing Neural Networks on a TensorFlow Cluster"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ParallelizingNeural(HierNode):
    def __init__(self):
        super().__init__("Parallelizing Neural Networks on a TensorFlow Cluster")
        self.add(Content())
        self.add(A_OneNeural())
        self.add(B_InGraphVersus())
        self.add(C_ModelParallelism())
        self.add(D_DataParallelism())

# eof
