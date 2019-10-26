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
#                        Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 8-7. Selecting the subspace onto which to project
# 
# It seems reasonable to select the axis that preserves the maximum amount of var‐
# iance, as it will most likely lose less information than the other projections. Another
# way to justify this choice is that it is the axis that minimizes the mean squared dis‐
# tance between the original dataset and its projection onto that axis. This is the rather
# simple idea behind PCA.4
# 
# Principal Components
# PCA identifies the axis that accounts for the largest amount of variance in the train‐
# ing set. In Figure 8-7, it is the solid line. It also finds a second axis, orthogonal to the
# first one, that accounts for the largest amount of remaining variance. In this 2D
# example there is no choice: it is the dotted line. If it were a higher-dimensional data‐
# set, PCA would also find a third axis, orthogonal to both previous axes, and a fourth,
# a fifth, and so on—as many axes as the number of dimensions in the dataset.
# The unit vector that defines the ith axis is called the ith principal component (PC). In
# Figure 8-7, the 1st PC is c1 and the 2nd PC is c2. In Figure 8-2 the first two PCs are
# represented by the orthogonal arrows in the plane, and the third PC would be
# orthogonal to the plane (pointing up or down).
# 
# 
# 
# 
# 4 “On Lines and Planes of Closest Fit to Systems of Points in Space,” K. Pearson (1901).
# 
# 
# 
# 212   |   Chapter 8: Dimensionality Reduction
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Preserving the Variance",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Preservingthe(HierNode):
    def __init__(self):
        super().__init__("Preserving the Variance")
        self.add(Content(), "content")

# eof
