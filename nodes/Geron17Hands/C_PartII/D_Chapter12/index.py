# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_MultipleDevices.index import MultipleDevices as A_MultipleDevices
from .B_MultipleDevices.index import MultipleDevices as B_MultipleDevices
from .C_ParallelizingNeural.index import ParallelizingNeural as C_ParallelizingNeural
from .D_Exercises.index import Exercises as D_Exercises

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                  Download from finelybook www.finelybook.com
# 
# 
#                                                                         CHAPTER 12
#                          Distributing TensorFlow Across
#                                     Devices and Servers
# 
# 
# 
# 
# In Chapter 11 we discussed several techniques that can considerably speed up train‐
# ing: better weight initialization, Batch Normalization, sophisticated optimizers, and
# so on. However, even with all of these techniques, training a large neural network on
# a single machine with a single CPU can take days or even weeks.
# In this chapter we will see how to use TensorFlow to distribute computations across
# multiple devices (CPUs and GPUs) and run them in parallel (see Figure 12-1). First
# we will distribute computations across multiple devices on just one machine, then on
# multiple devices across multiple machines.
# 
# 
# 
# 
# Figure 12-1. Executing a TensorFlow graph across multiple devices in parallel
# 
# 
# 
#                                                                                   313
# 
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
            "Chapter 12. Distributing TensorFlow Across Devices and Servers",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Chapter 12. Distributing TensorFlow Across Devices and Servers"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter12(HierNode):
    def __init__(self):
        super().__init__("Chapter 12. Distributing TensorFlow Across Devices and Servers")
        self.add(Content())
        self.add(A_MultipleDevices())
        self.add(B_MultipleDevices())
        self.add(C_ParallelizingNeural())
        self.add(D_Exercises())

# eof
