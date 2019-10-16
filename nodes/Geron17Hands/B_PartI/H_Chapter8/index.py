# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_TheCurse.index import TheCurse as A_TheCurse
from .B_MainApproaches.index import MainApproaches as B_MainApproaches
from .C_PCA.index import PCA as C_PCA
from .D_KernelPCA.index import KernelPCA as D_KernelPCA
from .E_LLE.index import LLE as E_LLE
from .F_OtherDimensionality.index import OtherDimensionality as F_OtherDimensionality
from .G_Exercises.index import Exercises as G_Exercises

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                  Download from finelybook www.finelybook.com
# 
# 
#                                                                             CHAPTER 8
#                                     Dimensionality Reduction
# 
# 
# 
# 
# Many Machine Learning problems involve thousands or even millions of features for
# each training instance. Not only does this make training extremely slow, it can also
# make it much harder to find a good solution, as we will see. This problem is often
# referred to as the curse of dimensionality.
# Fortunately, in real-world problems, it is often possible to reduce the number of fea‐
# tures considerably, turning an intractable problem into a tractable one. For example,
# consider the MNIST images (introduced in Chapter 3): the pixels on the image bor‐
# ders are almost always white, so you could completely drop these pixels from the
# training set without losing much information. Figure 7-6 confirms that these pixels
# are utterly unimportant for the classification task. Moreover, two neighboring pixels
# are often highly correlated: if you merge them into a single pixel (e.g., by taking the
# mean of the two pixel intensities), you will not lose much information.
# 
#                Reducing dimensionality does lose some information (just like
#                compressing an image to JPEG can degrade its quality), so even
#                though it will speed up training, it may also make your system per‐
#                form slightly worse. It also makes your pipelines a bit more com‐
#                plex and thus harder to maintain. So you should first try to train
#                your system with the original data before considering using dimen‐
#                sionality reduction if training is too slow. In some cases, however,
#                reducing the dimensionality of the training data may filter out
#                some noise and unnecessary details and thus result in higher per‐
#                formance (but in general it won’t; it will just speed up training).
# 
# Apart from speeding up training, dimensionality reduction is also extremely useful
# for data visualization (or DataViz). Reducing the number of dimensions down to two
# 
# 
# 
#                                                                                       205
# 
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 8. Dimensionality Reduction",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Chapter 8. Dimensionality Reduction"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter8(HierNode):
    def __init__(self):
        super().__init__("Chapter 8. Dimensionality Reduction")
        self.add(Content())
        self.add(A_TheCurse())
        self.add(B_MainApproaches())
        self.add(C_PCA())
        self.add(D_KernelPCA())
        self.add(E_LLE())
        self.add(F_OtherDimensionality())
        self.add(G_Exercises())

# eof
