# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_WhatIs.index import WhatIs as A_WhatIs
from .B_Neuronsin.index import Neuronsin as B_Neuronsin
from .C_TrainingFully.index import TrainingFully as C_TrainingFully
from .D_Implementationin.index import Implementationin as D_Implementationin
from .E_Review.index import Review as E_Review

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                                                           CHAPTER 4
#                         Fully Connected Deep Networks
# 
# 
# 
# 
# This chapter will introduce you to fully connected deep networks. Fully connected
# networks are the workhorses of deep learning, used for thousands of applications.
# The major advantage of fully connected networks is that they are “structure agnostic.”
# That is, no special assumptions need to be made about the input (for example, that
# the input consists of images or videos). We will make use of this generality to use fully
# connected deep networks to address a problem in chemical modeling later in this
# chapter.
# We delve briefly into the mathematical theory underpinning fully connected net‐
# works. In particular, we explore the concept that fully connected architectures are
# “universal approximators” capable of learning any function. This concept provides an
# explanation of the generality of fully connected architectures, but comes with many
# caveats that we discuss at some depth.
# While being structure agnostic makes fully connected networks very broadly applica‐
# ble, such networks do tend to have weaker performance than special-purpose net‐
# works tuned to the structure of a problem space. We will discuss some of the
# limitations of fully connected architectures later in this chapter.
# 
# What Is a Fully Connected Deep Network?
# A fully connected neural network consists of a series of fully connected layers. A fully
# connected layer is a function from ℝm to ℝn. Each output dimension depends on
# each input dimension. Pictorially, a fully connected layer is represented as follows in
# Figure 4-1.
# 
# 
# 
# 
#                                                                                        81
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 4. Fully Connected Deep Networks",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Chapter 4. Fully Connected Deep Networks"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter4(HierNode):
    def __init__(self):
        super().__init__("Chapter 4. Fully Connected Deep Networks")
        self.add(Content())
        self.add(A_WhatIs())
        self.add(B_Neuronsin())
        self.add(C_TrainingFully())
        self.add(D_Implementationin())
        self.add(E_Review())

# eof
