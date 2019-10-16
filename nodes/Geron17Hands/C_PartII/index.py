# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Chapter9.index import Chapter9 as A_Chapter9
from .B_Chapter10.index import Chapter10 as B_Chapter10
from .C_Chapter11.index import Chapter11 as C_Chapter11
from .D_Chapter12.index import Chapter12 as D_Chapter12
from .E_Chapter13.index import Chapter13 as E_Chapter13
from .F_Chapter14.index import Chapter14 as F_Chapter14
from .G_Chapter15.index import Chapter15 as G_Chapter15
from .H_Chapter16.index import Chapter16 as H_Chapter16

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#     Download from finelybook www.finelybook.com
# 
# 
# 
#                                                   PART II
# Neural Networks and Deep Learning
# 
# Download from finelybook www.finelybook.com
# 
#                 Download from finelybook www.finelybook.com
# 
# 
#                                                                       CHAPTER 9
#                    Up and Running with TensorFlow
# 
# 
# 
# 
# TensorFlow is a powerful open source software library for numerical computation,
# particularly well suited and fine-tuned for large-scale Machine Learning. Its basic
# principle is simple: you first define in Python a graph of computations to perform
# (for example, the one in Figure 9-1), and then TensorFlow takes that graph and runs
# it efficiently using optimized C++ code.
# 
# 
# 
# 
# Figure 9-1. A simple computation graph
# 
# Most importantly, it is possible to break up the graph into several chunks and run
# them in parallel across multiple CPUs or GPUs (as shown in Figure 9-2). TensorFlow
# also supports distributed computing, so you can train colossal neural networks on
# humongous training sets in a reasonable amount of time by splitting the computa‐
# tions across hundreds of servers (see Chapter 12). TensorFlow can train a network
# with millions of parameters on a training set composed of billions of instances with
# millions of features each. This should come as no surprise, since TensorFlow was
# 
# 
#                                                                                  229
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Part II. Neural Networks and Deep Learning",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Part II. Neural Networks and Deep Learning"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PartII(HierNode):
    def __init__(self):
        super().__init__("Part II. Neural Networks and Deep Learning")
        self.add(Content())
        self.add(A_Chapter9())
        self.add(B_Chapter10())
        self.add(C_Chapter11())
        self.add(D_Chapter12())
        self.add(E_Chapter13())
        self.add(F_Chapter14())
        self.add(G_Chapter15())
        self.add(H_Chapter16())

# eof
