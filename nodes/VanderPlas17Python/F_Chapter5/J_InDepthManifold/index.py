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

from .A_ManifoldLearning.index import ManifoldLearning as A_ManifoldLearning
from .B_MultidimensionalScaling.index import MultidimensionalScaling as B_MultidimensionalScaling
from .C_MDSas.index import MDSas as C_MDSas
from .D_NonlinearEmbeddings.index import NonlinearEmbeddings as D_NonlinearEmbeddings
from .E_NonlinearManifolds.index import NonlinearManifolds as E_NonlinearManifolds
from .F_SomeThoughts.index import SomeThoughts as F_SomeThoughts
from .G_ExampleIsomap.index import ExampleIsomap as G_ExampleIsomap
from .H_ExampleVisualizing.index import ExampleVisualizing as H_ExampleVisualizing

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# The top row here shows the input images, while the bottom row shows the recon‐
# struction of the images from just 150 of the ~3,000 initial features. This visualization
# makes clear why the PCA feature selection used in “In-Depth: Support Vector
# Machines” on page 405 was so successful: although it reduces the dimensionality of
# the data by nearly a factor of 20, the projected images contain enough information
# that we might, by eye, recognize the individuals in the image. What this means is that
# our classification algorithm needs to be trained on 150-dimensional data rather than
# 3,000-dimensional data, which depending on the particular algorithm we choose, can
# lead to a much more efficient classification.
# 
# Principal Component Analysis Summary
# In this section we have discussed the use of principal component analysis for dimen‐
# sionality reduction, for visualization of high-dimensional data, for noise filtering, and
# for feature selection within high-dimensional data. Because of the versatility and
# interpretability of PCA, it has been shown to be effective in a wide variety of contexts
# and disciplines. Given any high-dimensional dataset, I tend to start with PCA in
# order to visualize the relationship between points (as we did with the digits), to
# understand the main variance in the data (as we did with the eigenfaces), and to
# understand the intrinsic dimensionality (by plotting the explained variance ratio).
# Certainly PCA is not useful for every high-dimensional dataset, but it offers a
# straightforward and efficient path to gaining insight into high-dimensional data.
# PCA’s main weakness is that it tends to be highly affected by outliers in the data. For
# this reason, many robust variants of PCA have been developed, many of which act to
# iteratively discard data points that are poorly described by the initial components.
# Scikit-Learn contains a couple interesting variants on PCA, including RandomizedPCA
# and SparsePCA, both also in the sklearn.decomposition submodule. Randomi
# zedPCA, which we saw earlier, uses a nondeterministic method to quickly approxi‐
# mate the first few principal components in very high-dimensional data, while
# SparsePCA introduces a regularization term (see “In Depth: Linear Regression” on
# page 390) that serves to enforce sparsity of the components.
# In the following sections, we will look at other unsupervised learning methods that
# build on some of the ideas of PCA.
# 
# In-Depth: Manifold Learning
# We have seen how principal component analysis can be used in the dimensionality
# reduction task—reducing the number of features of a dataset while maintaining the
# essential relationships between the points. While PCA is flexible, fast, and easily
# interpretable, it does not perform so well when there are nonlinear relationships
# within the data; we will see some examples of these below.
# 
# 
# 
#                                                             In-Depth: Manifold Learning   |   445
# 
# To address this deficiency, we can turn to a class of methods known as manifold learn‐
# ing—a class of unsupervised estimators that seeks to describe datasets as low-
# dimensional manifolds embedded in high-dimensional spaces. When you think of a
# manifold, I’d suggest imagining a sheet of paper: this is a two-dimensional object that
# lives in our familiar three-dimensional world, and can be bent or rolled in two
# dimensions. In the parlance of manifold learning, we can think of this sheet as a two-
# dimensional manifold embedded in three-dimensional space.
# Rotating, reorienting, or stretching the piece of paper in three-dimensional space
# doesn’t change the flat geometry of the paper: such operations are akin to linear
# embeddings. If you bend, curl, or crumple the paper, it is still a two-dimensional
# manifold, but the embedding into the three-dimensional space is no longer linear.
# Manifold learning algorithms would seek to learn about the fundamental two-
# dimensional nature of the paper, even as it is contorted to fill the three-dimensional
# space.
# Here we will demonstrate a number of manifold methods, going most deeply into a
# couple techniques: multidimensional scaling (MDS), locally linear embedding (LLE),
# and isometric mapping (Isomap). We begin with the standard imports:
#       In[1]: %matplotlib inline
#              import matplotlib.pyplot as plt
#              import seaborn as sns; sns.set()
#              import numpy as np
# 
# 
# Manifold Learning: “HELLO”
# To make these concepts more clear, let’s start by generating some two-dimensional
# data that we can use to define a manifold. Here is a function that will create data in
# the shape of the word “HELLO”:
#       In[2]:
#       def make_hello(N=1000, rseed=42):
#           # Make a plot with "HELLO" text; save as PNG
#           fig, ax = plt.subplots(figsize=(4, 1))
#           fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
#           ax.axis('off')
#           ax.text(0.5, 0.4, 'HELLO', va='center', ha='center', weight='bold', size=85)
#           fig.savefig('hello.png')
#           plt.close(fig)
# 
#           # Open this PNG and draw random points from it
#           from matplotlib.image import imread
#           data = imread('hello.png')[::-1, :, 0].T
#           rng = np.random.RandomState(rseed)
#           X = rng.rand(4 * N, 2)
#           i, j = (X * data.shape).astype(int).T
#           mask = (data[i, j] < 1)
#           X = X[mask]
# 
# 
# 446   |   Chapter 5: Machine Learning
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "In-Depth: Manifold Learning",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class InDepthManifold(HierNode):
    def __init__(self):
        super().__init__("In-Depth: Manifold Learning")
        self.add(Content())
        self.add(A_ManifoldLearning())
        self.add(B_MultidimensionalScaling())
        self.add(C_MDSas())
        self.add(D_NonlinearEmbeddings())
        self.add(E_NonlinearManifolds())
        self.add(F_SomeThoughts())
        self.add(G_ExampleIsomap())
        self.add(H_ExampleVisualizing())

# eof
