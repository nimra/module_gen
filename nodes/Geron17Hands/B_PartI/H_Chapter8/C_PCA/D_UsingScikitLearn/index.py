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
#                    Download from finelybook www.finelybook.com
# ing the first d principal components (i.e., the matrix composed of the first d columns
# of VT), as shown in Equation 8-2.
# 
#       Equation 8-2. Projecting the training set down to d dimensions
#       �d‐proj = � · �d
# 
# The following Python code projects the training set onto the plane defined by the first
# two principal components:
#       W2 = V.T[:, :2]
#       X2D = X_centered.dot(W2)
# There you have it! You now know how to reduce the dimensionality of any dataset
# down to any number of dimensions, while preserving as much variance as possible.
# 
# Using Scikit-Learn
# Scikit-Learn’s PCA class implements PCA using SVD decomposition just like we did
# before. The following code applies PCA to reduce the dimensionality of the dataset
# down to two dimensions (note that it automatically takes care of centering the data):
#       from sklearn.decomposition import PCA
# 
#       pca = PCA(n_components = 2)
#       X2D = pca.fit_transform(X)
# 
# After fitting the PCA transformer to the dataset, you can access the principal compo‐
# nents using the components_ variable (note that it contains the PCs as horizontal vec‐
# tors, so, for example, the first principal component is equal to pca.components_.T[:,
# 0]).
# 
# Explained Variance Ratio
# Another very useful piece of information is the explained variance ratio of each prin‐
# cipal component, available via the explained_variance_ratio_ variable. It indicates
# the proportion of the dataset’s variance that lies along the axis of each principal com‐
# ponent. For example, let’s look at the explained variance ratios of the first two compo‐
# nents of the 3D dataset represented in Figure 8-2:
#       >>> print(pca.explained_variance_ratio_)
#       array([ 0.84248607, 0.14631839])
# This tells you that 84.2% of the dataset’s variance lies along the first axis, and 14.6%
# lies along the second axis. This leaves less than 1.2% for the third axis, so it is reason‐
# able to assume that it probably carries little information.
# 
# 
# 
# 
# 214    |   Chapter 8: Dimensionality Reduction
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Using Scikit-Learn",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class UsingScikitLearn(HierNode):
    def __init__(self):
        super().__init__("Using Scikit-Learn")
        self.add(Content(), "content")

# eof
