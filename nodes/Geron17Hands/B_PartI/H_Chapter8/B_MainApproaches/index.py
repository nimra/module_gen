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

from .A_Projection.index import Projection as A_Projection
from .B_ManifoldLearning.index import ManifoldLearning as B_ManifoldLearning

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                     Download from finelybook www.finelybook.com
# Here is a more troublesome difference: if you pick two points randomly in a unit
# square, the distance between these two points will be, on average, roughly 0.52. If you
# pick two random points in a unit 3D cube, the average distance will be roughly 0.66.
# But what about two points picked randomly in a 1,000,000-dimensional hypercube?
# Well, the average distance, believe it or not, will be about 408.25 (roughly
#   1, 000, 000/6)! This is quite counterintuitive: how can two points be so far apart
# when they both lie within the same unit hypercube? This fact implies that high-
# dimensional datasets are at risk of being very sparse: most training instances are
# likely to be far away from each other. Of course, this also means that a new instance
# will likely be far away from any training instance, making predictions much less relia‐
# ble than in lower dimensions, since they will be based on much larger extrapolations.
# In short, the more dimensions the training set has, the greater the risk of overfitting
# it.
# In theory, one solution to the curse of dimensionality could be to increase the size of
# the training set to reach a sufficient density of training instances. Unfortunately, in
# practice, the number of training instances required to reach a given density grows
# exponentially with the number of dimensions. With just 100 features (much less than
# in the MNIST problem), you would need more training instances than atoms in the
# observable universe in order for training instances to be within 0.1 of each other on
# average, assuming they were spread out uniformly across all dimensions.
# 
# Main Approaches for Dimensionality Reduction
# Before we dive into specific dimensionality reduction algorithms, let’s take a look at
# the two main approaches to reducing dimensionality: projection and Manifold
# Learning.
# 
# Projection
# In most real-world problems, training instances are not spread out uniformly across
# all dimensions. Many features are almost constant, while others are highly correlated
# (as discussed earlier for MNIST). As a result, all training instances actually lie within
# (or close to) a much lower-dimensional subspace of the high-dimensional space. This
# sounds very abstract, so let’s look at an example. In Figure 8-2 you can see a 3D data‐
# set represented by the circles.
# 
# 
# 
# 
#                                                Main Approaches for Dimensionality Reduction   |   207
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Main Approaches for Dimensionality Reduction",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MainApproaches(HierNode):
    def __init__(self):
        super().__init__("Main Approaches for Dimensionality Reduction")
        self.add(Content(), "content")
        self.add(A_Projection())
        self.add(B_ManifoldLearning())

# eof
