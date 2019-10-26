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
# (or three) makes it possible to plot a high-dimensional training set on a graph and
# often gain some important insights by visually detecting patterns, such as clusters.
# In this chapter we will discuss the curse of dimensionality and get a sense of what
# goes on in high-dimensional space. Then, we will present the two main approaches to
# dimensionality reduction (projection and Manifold Learning), and we will go
# through three of the most popular dimensionality reduction techniques: PCA, Kernel
# PCA, and LLE.
# 
# The Curse of Dimensionality
# We are so used to living in three dimensions1 that our intuition fails us when we try
# to imagine a high-dimensional space. Even a basic 4D hypercube is incredibly hard to
# picture in our mind (see Figure 8-1), let alone a 200-dimensional ellipsoid bent in a
# 1,000-dimensional space.
# 
# 
# 
# 
# Figure 8-1. Point, segment, square, cube, and tesseract (0D to 4D hypercubes)2
# 
# It turns out that many things behave very differently in high-dimensional space. For
# example, if you pick a random point in a unit square (a 1 × 1 square), it will have only
# about a 0.4% chance of being located less than 0.001 from a border (in other words, it
# is very unlikely that a random point will be “extreme” along any dimension). But in a
# 10,000-dimensional unit hypercube (a 1 × 1 × ⋯ × 1 cube, with ten thousand 1s), this
# probability is greater than 99.999999%. Most points in a high-dimensional hypercube
# are very close to the border.3
# 
# 
# 
# 
# 1 Well, four dimensions if you count time, and a few more if you are a string theorist.
# 2 Watch a rotating tesseract projected into 3D space at http://goo.gl/OM7ktJ. Image by Wikipedia user Nerd‐
#   Boy1392 (Creative Commons BY-SA 3.0). Reproduced from https://en.wikipedia.org/wiki/Tesseract.
# 3 Fun fact: anyone you know is probably an extremist in at least one dimension (e.g., how much sugar they put
#   in their coffee), if you consider enough dimensions.
# 
# 
# 
# 206   |   Chapter 8: Dimensionality Reduction
# 
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
            "The Curse of Dimensionality",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TheCurse(HierNode):
    def __init__(self):
        super().__init__("The Curse of Dimensionality")
        self.add(Content(), "content")

# eof
