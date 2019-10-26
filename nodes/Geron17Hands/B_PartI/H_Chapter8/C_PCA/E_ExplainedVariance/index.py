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
#                  Download from finelybook www.finelybook.com
# Choosing the Right Number of Dimensions
# Instead of arbitrarily choosing the number of dimensions to reduce down to, it is
# generally preferable to choose the number of dimensions that add up to a sufficiently
# large portion of the variance (e.g., 95%). Unless, of course, you are reducing dimen‐
# sionality for data visualization—in that case you will generally want to reduce the
# dimensionality down to 2 or 3.
# The following code computes PCA without reducing dimensionality, then computes
# the minimum number of dimensions required to preserve 95% of the training set’s
# variance:
#     pca = PCA()
#     pca.fit(X)
#     cumsum = np.cumsum(pca.explained_variance_ratio_)
#     d = np.argmax(cumsum >= 0.95) + 1
# 
# You could then set n_components=d and run PCA again. However, there is a much
# better option: instead of specifying the number of principal components you want to
# preserve, you can set n_components to be a float between 0.0 and 1.0, indicating the
# ratio of variance you wish to preserve:
#     pca = PCA(n_components=0.95)
#     X_reduced = pca.fit_transform(X)
# Yet another option is to plot the explained variance as a function of the number of
# dimensions (simply plot cumsum; see Figure 8-8). There will usually be an elbow in the
# curve, where the explained variance stops growing fast. You can think of this as the
# intrinsic dimensionality of the dataset. In this case, you can see that reducing the
# dimensionality down to about 100 dimensions wouldn’t lose too much explained var‐
# iance.
# 
# 
# 
# 
# Figure 8-8. Explained variance as a function of the number of dimensions
# 
# 
# 
# 
#                                                                            PCA   |   215
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Explained Variance Ratio",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ExplainedVariance(HierNode):
    def __init__(self):
        super().__init__("Explained Variance Ratio")
        self.add(Content(), "content")

# eof
