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
# certain relationships within the data. In the case of MDS, the quantity preserved is the
# distance between every pair of points.
# 
# Nonlinear Embeddings: Where MDS Fails
# Our discussion so far has considered linear embeddings, which essentially consist of
# rotations, translations, and scalings of data into higher-dimensional spaces. Where
# MDS breaks down is when the embedding is nonlinear—that is, when it goes beyond
# this simple set of operations. Consider the following embedding, which takes the
# input and contorts it into an “S” shape in three dimensions:
#       In[12]: def make_hello_s_curve(X):
#                   t = (X[:, 0] - 2) * 0.75 * np.pi
#                   x = np.sin(t)
#                   y = X[:, 1]
#                   z = np.sign(t) * (np.cos(t) - 1)
#                   return np.vstack((x, y, z)).T
# 
#                 XS = make_hello_s_curve(X)
# This is again three-dimensional data, but we can see that the embedding is much
# more complicated (Figure 5-100):
#       In[13]: from mpl_toolkits import mplot3d
#               ax = plt.axes(projection='3d')
#               ax.scatter3D(XS[:, 0], XS[:, 1], XS[:, 2],
#                            **colorize);
# 
# 
# 
# 
# Figure 5-100. Data embedded nonlinearly into three dimensions
# 
# The fundamental relationships between the data points are still there, but this time
# the data has been transformed in a nonlinear way: it has been wrapped up into the
# shape of an “S.”
# 
# 
# 
# 452   |   Chapter 5: Machine Learning
# 
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
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Nonlinear Embeddings: Where MDS Fails",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class NonlinearEmbeddings(HierNode):
    def __init__(self):
        super().__init__("Nonlinear Embeddings: Where MDS Fails")
        self.add(Content())

# eof
