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

from .A_Preface.index import Preface as A_Preface
from .B_PartI.index import PartI as B_PartI
from .C_PartII.index import PartII as C_PartII
from .D_Appendices.index import Appendices as D_Appendices
# from .E_Index.index import Index as E_Index

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                       Download from finelybook www.finelybook.com
# 
# 
# 
#                                                                                           Preface
# 
# 
# 
# 
# The Machine Learning Tsunami
# In 2006, Geoffrey Hinton et al. published a paper1 showing how to train a deep neural
# network capable of recognizing handwritten digits with state-of-the-art precision
# (>98%). They branded this technique “Deep Learning.” Training a deep neural net
# was widely considered impossible at the time,2 and most researchers had abandoned
# the idea since the 1990s. This paper revived the interest of the scientific community
# and before long many new papers demonstrated that Deep Learning was not only
# possible, but capable of mind-blowing achievements that no other Machine Learning
# (ML) technique could hope to match (with the help of tremendous computing power
# and great amounts of data). This enthusiasm soon extended to many other areas of
# Machine Learning.
# Fast-forward 10 years and Machine Learning has conquered the industry: it is now at
# the heart of much of the magic in today’s high-tech products, ranking your web
# search results, powering your smartphone’s speech recognition, and recommending
# videos, beating the world champion at the game of Go. Before you know it, it will be
# driving your car.
# 
# Machine Learning in Your Projects
# So naturally you are excited about Machine Learning and you would love to join the
# party!
# Perhaps you would like to give your homemade robot a brain of its own? Make it rec‐
# ognize faces? Or learn to walk around?
# 
# 
# 1 Available on Hinton’s home page at http://www.cs.toronto.edu/~hinton/.
# 2 Despite the fact that Yann Lecun’s deep convolutional neural networks had worked well for image recognition
#   since the 1990s, although they were not as general purpose.
# 
# 
# 
#                                                                                                           xiii
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Geron17Hands",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Geron17Hands(HierNode):
    def __init__(self):
        super().__init__("Geron17Hands")
        self.add(Content(), "content")
        self.add(A_Preface())
        self.add(B_PartI())
        self.add(C_PartII())
        self.add(D_Appendices())
        # self.add(E_Index())

# eof
