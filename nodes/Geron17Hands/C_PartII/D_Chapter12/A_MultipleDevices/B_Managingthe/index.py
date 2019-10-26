# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.HierBlock import HierBlock as hbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.ListBlock import ListBlock as lbk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                  Download from finelybook www.finelybook.com
# Managing the GPU RAM
# By default TensorFlow automatically grabs all the RAM in all available GPUs the first
# time you run a graph, so you will not be able to start a second TensorFlow program
# while the first one is still running. If you try, you will get the following error:
#     E [...]/cuda_driver.cc:965] failed to allocate 3.66G (3928915968 bytes) from
#     device: CUDA_ERROR_OUT_OF_MEMORY
# One solution is to run each process on different GPU cards. To do this, the simplest
# option is to set the CUDA_VISIBLE_DEVICES environment variable so that each process
# only sees the appropriate GPU cards. For example, you could start two programs like
# this:
#     $ CUDA_VISIBLE_DEVICES=0,1 python3 program_1.py
#     # and in another terminal:
#     $ CUDA_VISIBLE_DEVICES=3,2 python3 program_2.py
# Program #1 will only see GPU cards 0 and 1 (numbered 0 and 1, respectively), and
# program #2 will only see GPU cards 2 and 3 (numbered 1 and 0, respectively). Every‐
# thing will work fine (see Figure 12-3).
# 
# 
# 
# 
# Figure 12-3. Each program gets two GPUs for itself
# 
# Another option is to tell TensorFlow to grab only a fraction of the memory. For
# example, to make TensorFlow grab only 40% of each GPU’s memory, you must create
# a ConfigProto object, set its gpu_options.per_process_gpu_memory_fraction
# option to 0.4, and create the session using this configuration:
#     config = tf.ConfigProto()
#     config.gpu_options.per_process_gpu_memory_fraction = 0.4
#     session = tf.Session(config=config)
# Now two programs like this one can run in parallel using the same GPU cards (but
# not three, since 3 × 0.4 > 1). See Figure 12-4.
# 
# 
# 
# 
#                                                       Multiple Devices on a Single Machine   |   317
# 
#                          Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 12-4. Each program gets all four GPUs, but with only 40% of the RAM each
# 
# If you run the nvidia-smi command while both programs are running, you should
# see that each process holds roughly 40% of the total RAM of each card:
#       $ nvidia-smi
#       [...]
#       +-----------------------------------------------------------------------------+
#       | Processes:                                                       GPU Memory |
#       | GPU         PID Type Process name                                Usage      |
#       |=============================================================================|
#       |     0      5231   C   python                                        1677MiB |
#       |     0      5262   C   python                                        1677MiB |
#       |     1      5231   C   python                                        1677MiB |
#       |     1      5262   C   python                                        1677MiB |
#       [...]
# Yet another option is to tell TensorFlow to grab memory only when it needs it. To do
# this you must set config.gpu_options.allow_growth to True. However, TensorFlow
# never releases memory once it has grabbed it (to avoid memory fragmentation) so
# you may still run out of memory after a while. It may be harder to guarantee a deter‐
# ministic behavior using this option, so in general you probably want to stick with one
# of the previous options.
# Okay, now you have a working GPU-enabled TensorFlow installation. Let’s see how
# to use it!
# 
# Placing Operations on Devices
# The TensorFlow whitepaper1 presents a friendly dynamic placer algorithm that auto‐
# magically distributes operations across all available devices, taking into account
# things like the measured computation time in previous runs of the graph, estimations
# of the size of the input and output tensors to each operation, the amount of RAM
# available in each device, communication delay when transferring data in and out of
# 
# 
# 1 “TensorFlow: Large-Scale Machine Learning on Heterogeneous Distributed Systems,” Google Research
#   (2015).
# 
# 
# 
# 318   |     Chapter 12: Distributing TensorFlow Across Devices and Servers
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Managing the GPU RAM",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Managingthe(HierNode):
    def __init__(self):
        super().__init__("Managing the GPU RAM")
        self.add(Content(), "content")

# eof
