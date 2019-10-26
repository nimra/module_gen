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

from .A_Preservingthe.index import Preservingthe as A_Preservingthe
from .B_PrincipalComponents.index import PrincipalComponents as B_PrincipalComponents
from .C_ProjectingDown.index import ProjectingDown as C_ProjectingDown
from .D_UsingScikitLearn.index import UsingScikitLearn as D_UsingScikitLearn
from .E_ExplainedVariance.index import ExplainedVariance as E_ExplainedVariance
from .F_Choosingthe.index import Choosingthe as F_Choosingthe
from .G_PCAfor.index import PCAfor as G_PCAfor
from .H_IncrementalPCA.index import IncrementalPCA as H_IncrementalPCA
from .I_RandomizedPCA.index import RandomizedPCA as I_RandomizedPCA

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                   Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 8-6. The decision boundary may not always be simpler with lower dimensions
# 
# PCA
# Principal Component Analysis (PCA) is by far the most popular dimensionality reduc‐
# tion algorithm. First it identifies the hyperplane that lies closest to the data, and then
# it projects the data onto it.
# 
# Preserving the Variance
# Before you can project the training set onto a lower-dimensional hyperplane, you
# first need to choose the right hyperplane. For example, a simple 2D dataset is repre‐
# sented on the left of Figure 8-7, along with three different axes (i.e., one-dimensional
# hyperplanes). On the right is the result of the projection of the dataset onto each of
# these axes. As you can see, the projection onto the solid line preserves the maximum
# variance, while the projection onto the dotted line preserves very little variance, and
# the projection onto the dashed line preserves an intermediate amount of variance.
# 
# 
# 
# 
#                                                                                PCA   |   211
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "PCA",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PCA(HierNode):
    def __init__(self):
        super().__init__("PCA")
        self.add(Content(), "content")
        self.add(A_Preservingthe())
        self.add(B_PrincipalComponents())
        self.add(C_ProjectingDown())
        self.add(D_UsingScikitLearn())
        self.add(E_ExplainedVariance())
        self.add(F_Choosingthe())
        self.add(G_PCAfor())
        self.add(H_IncrementalPCA())
        self.add(I_RandomizedPCA())

# eof
