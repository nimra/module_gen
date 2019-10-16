# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_AppendixA.index import AppendixA as A_AppendixA
from .B_AppendixB.index import AppendixB as B_AppendixB
from .C_AppendixC.index import AppendixC as C_AppendixC
from .D_AppendixD.index import AppendixD as D_AppendixD
from .E_AppendixE.index import AppendixE as E_AppendixE

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                 Download from finelybook www.finelybook.com
# 
# 
#                                                                            APPENDIX A
#                                                      Exercise Solutions
# 
# 
# 
# 
#               Solutions to the coding exercises are available in the online Jupyter
#               notebooks at https://github.com/ageron/handson-ml.
# 
# 
# 
# 
# Chapter 1: The Machine Learning Landscape
# 1. Machine Learning is about building systems that can learn from data. Learning
#    means getting better at some task, given some performance measure.
# 2. Machine Learning is great for complex problems for which we have no algorith‐
#    mic solution, to replace long lists of hand-tuned rules, to build systems that adapt
#    to fluctuating environments, and finally to help humans learn (e.g., data mining).
# 3. A labeled training set is a training set that contains the desired solution (a.k.a. a
#    label) for each instance.
# 4. The two most common supervised tasks are regression and classification.
# 5. Common unsupervised tasks include clustering, visualization, dimensionality
#    reduction, and association rule learning.
# 6. Reinforcement Learning is likely to perform best if we want a robot to learn to
#    walk in various unknown terrains since this is typically the type of problem that
#    Reinforcement Learning tackles. It might be possible to express the problem as a
#    supervised or semisupervised learning problem, but it would be less natural.
# 7. If you don’t know how to define the groups, then you can use a clustering algo‐
#    rithm (unsupervised learning) to segment your customers into clusters of similar
#    customers. However, if you know what groups you would like to have, then you
# 
# 
# 
#                                                                                       471
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Appendices",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Appendices"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Appendices(HierNode):
    def __init__(self):
        super().__init__("Appendices")
        self.add(Content())
        self.add(A_AppendixA())
        self.add(B_AppendixB())
        self.add(C_AppendixC())
        self.add(D_AppendixD())
        self.add(E_AppendixE())

# eof
