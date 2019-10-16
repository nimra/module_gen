# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Installation.index import Installation as A_Installation
from .B_Managingthe.index import Managingthe as B_Managingthe
from .C_PlacingOperations.index import PlacingOperations as C_PlacingOperations
from .D_ParallelExecution.index import ParallelExecution as D_ParallelExecution
from .E_ControlDependencies.index import ControlDependencies as E_ControlDependencies

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                    Download from finelybook www.finelybook.com
# TensorFlow’s support of distributed computing is one of its main highlights com‐
# pared to other neural network frameworks. It gives you full control over how to split
# (or replicate) your computation graph across devices and servers, and it lets you par‐
# allelize and synchronize operations in flexible ways so you can choose between all
# sorts of parallelization approaches.
# We will look at some of the most popular approaches to parallelizing the execution
# and training of a neural network. Instead of waiting for weeks for a training algo‐
# rithm to complete, you may end up waiting for just a few hours. Not only does this
# save an enormous amount of time, it also means that you can experiment with vari‐
# ous models much more easily, and frequently retrain your models on fresh data.
# Other great use cases of parallelization include exploring a much larger hyperparame‐
# ter space when fine-tuning your model, and running large ensembles of neural net‐
# works efficiently.
# But we must learn to walk before we can run. Let’s start by parallelizing simple graphs
# across several GPUs on a single machine.
# 
# Multiple Devices on a Single Machine
# You can often get a major performance boost simply by adding GPU cards to a single
# machine. In fact, in many cases this will suffice; you won’t need to use multiple
# machines at all. For example, you can typically train a neural network just as fast
# using 8 GPUs on a single machine rather than 16 GPUs across multiple machines
# (due to the extra delay imposed by network communications in a multimachine
# setup).
# In this section we will look at how to set up your environment so that TensorFlow can
# use multiple GPU cards on one machine. Then we will look at how you can distribute
# operations across available devices and execute them in parallel.
# 
# Installation
# In order to run TensorFlow on multiple GPU cards, you first need to make sure your
# GPU cards have NVidia Compute Capability (greater or equal to 3.0). This includes
# Nvidia’s Titan, Titan X, K20, and K40 cards (if you own another card, you can check
# its compatibility at https://developer.nvidia.com/cuda-gpus).
# 
# 
# 
# 
# 314   |   Chapter 12: Distributing TensorFlow Across Devices and Servers
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Multiple Devices on a Single Machine",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Multiple Devices on a Single Machine"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MultipleDevices(HierNode):
    def __init__(self):
        super().__init__("Multiple Devices on a Single Machine")
        self.add(Content())
        self.add(A_Installation())
        self.add(B_Managingthe())
        self.add(C_PlacingOperations())
        self.add(D_ParallelExecution())
        self.add(E_ControlDependencies())

# eof
