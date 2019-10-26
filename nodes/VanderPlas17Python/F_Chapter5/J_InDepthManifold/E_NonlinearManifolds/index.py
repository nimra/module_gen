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
# If we try a simple MDS algorithm on this data, it is not able to “unwrap” this nonlin‐
# ear embedding, and we lose track of the fundamental relationships in the embedded
# manifold (Figure 5-101):
#     In[14]: from sklearn.manifold import MDS
#             model = MDS(n_components=2, random_state=2)
#             outS = model.fit_transform(XS)
#             plt.scatter(outS[:, 0], outS[:, 1], **colorize)
#             plt.axis('equal');
# 
# 
# 
# 
# Figure 5-101. The MDS algorithm applied to the nonlinear data; it fails to recover the
# underlying structure
# 
# The best two-dimensional linear embedding does not unwrap the S-curve, but
# instead throws out the original y-axis.
# 
# Nonlinear Manifolds: Locally Linear Embedding
# How can we move forward here? Stepping back, we can see that the source of the
# problem is that MDS tries to preserve distances between faraway points when con‐
# structing the embedding. But what if we instead modified the algorithm such that it
# only preserves distances between nearby points? The resulting embedding would be
# closer to what we want.
# Visually, we can think of it as illustrated in Figure 5-102.
# 
# 
# 
# 
#                                                                In-Depth: Manifold Learning   |   453
# 
# Figure 5-102. Representation of linkages between points within MDS and LLE
# 
# Here each faint line represents a distance that should be preserved in the embedding.
# On the left is a representation of the model used by MDS: it tries to preserve the dis‐
# tances between each pair of points in the dataset. On the right is a representation of
# the model used by a manifold learning algorithm called locally linear embedding
# (LLE): rather than preserving all distances, it instead tries to preserve only the distan‐
# ces between neighboring points: in this case, the nearest 100 neighbors of each point.
# Thinking about the left panel, we can see why MDS fails: there is no way to flatten
# this data while adequately preserving the length of every line drawn between the two
# points. For the right panel, on the other hand, things look a bit more optimistic. We
# could imagine unrolling the data in a way that keeps the lengths of the lines approxi‐
# mately the same. This is precisely what LLE does, through a global optimization of a
# cost function reflecting this logic.
# LLE comes in a number of flavors; here we will use the modified LLE algorithm to
# recover the embedded two-dimensional manifold. In general, modified LLE does bet‐
# ter than other flavors of the algorithm at recovering well-defined manifolds with very
# little distortion (Figure 5-103):
#       In[15]:
#       from sklearn.manifold import LocallyLinearEmbedding
#       model = LocallyLinearEmbedding(n_neighbors=100, n_components=2, method='modified',
#                                      eigen_solver='dense')
#       out = model.fit_transform(XS)
# 
#       fig, ax = plt.subplots()
#       ax.scatter(out[:, 0], out[:, 1], **colorize)
#       ax.set_ylim(0.15, -0.15);
# 
# 
# 
# 
# 454   |   Chapter 5: Machine Learning
# 
# Figure 5-103. Locally linear embedding can recover the underlying data from a nonli‐
# nearly embedded input
# 
# The result remains somewhat distorted compared to our original manifold, but cap‐
# tures the essential relationships in the data!
# 
# Some Thoughts on Manifold Methods
# Though this story and motivation is compelling, in practice manifold learning tech‐
# niques tend to be finicky enough that they are rarely used for anything more than
# simple qualitative visualization of high-dimensional data.
# The following are some of the particular challenges of manifold learning, which all
# contrast poorly with PCA:
# 
#   • In manifold learning, there is no good framework for handling missing data. In
#     contrast, there are straightforward iterative approaches for missing data in PCA.
#   • In manifold learning, the presence of noise in the data can “short-circuit” the
#     manifold and drastically change the embedding. In contrast, PCA naturally filters
#     noise from the most important components.
#   • The manifold embedding result is generally highly dependent on the number of
#     neighbors chosen, and there is generally no solid quantitative way to choose an
#     optimal number of neighbors. In contrast, PCA does not involve such a choice.
#   • In manifold learning, the globally optimal number of output dimensions is diffi‐
#     cult to determine. In contrast, PCA lets you find the output dimension based on
#     the explained variance.
#   • In manifold learning, the meaning of the embedded dimensions is not always
#     clear. In PCA, the principal components have a very clear meaning.
# 
# 
#                                                            In-Depth: Manifold Learning   |   455
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Nonlinear Manifolds: Locally Linear Embedding",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class NonlinearManifolds(HierNode):
    def __init__(self):
        super().__init__("Nonlinear Manifolds: Locally Linear Embedding")
        self.add(Content())

# eof
