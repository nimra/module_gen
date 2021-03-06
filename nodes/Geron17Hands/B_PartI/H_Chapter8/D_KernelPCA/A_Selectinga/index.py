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
# 
# 
# 
# 
# Figure 8-10. Swiss roll reduced to 2D using kPCA with various kernels
# 
# Selecting a Kernel and Tuning Hyperparameters
# As kPCA is an unsupervised learning algorithm, there is no obvious performance
# measure to help you select the best kernel and hyperparameter values. However,
# dimensionality reduction is often a preparation step for a supervised learning task
# (e.g., classification), so you can simply use grid search to select the kernel and hyper‐
# parameters that lead to the best performance on that task. For example, the following
# code creates a two-step pipeline, first reducing dimensionality to two dimensions
# using kPCA, then applying Logistic Regression for classification. Then it uses Grid
# SearchCV to find the best kernel and gamma value for kPCA in order to get the best
# classification accuracy at the end of the pipeline:
#     from sklearn.model_selection import GridSearchCV
#     from sklearn.linear_model import LogisticRegression
#     from sklearn.pipeline import Pipeline
# 
#     clf = Pipeline([
#             ("kpca", KernelPCA(n_components=2)),
#             ("log_reg", LogisticRegression())
#         ])
# 
#     param_grid = [{
#             "kpca__gamma": np.linspace(0.03, 0.05, 10),
#             "kpca__kernel": ["rbf", "sigmoid"]
#         }]
# 
#     grid_search = GridSearchCV(clf, param_grid, cv=3)
#     grid_search.fit(X, y)
# 
# The best kernel and hyperparameters are then available through the best_params_
# variable:
#     >>> print(grid_search.best_params_)
#     {'kpca__gamma': 0.043333333333333335, 'kpca__kernel': 'rbf'}
# 
# 
# 
# 
#                                                                          Kernel PCA   |   219
# 
#                    Download from finelybook www.finelybook.com
# Another approach, this time entirely unsupervised, is to select the kernel and hyper‐
# parameters that yield the lowest reconstruction error. However, reconstruction is not
# as easy as with linear PCA. Here’s why. Figure 8-11 shows the original Swiss roll 3D
# dataset (top left), and the resulting 2D dataset after kPCA is applied using an RBF
# kernel (top right). Thanks to the kernel trick, this is mathematically equivalent to
# mapping the training set to an infinite-dimensional feature space (bottom right)
# using the feature map φ, then projecting the transformed training set down to 2D
# using linear PCA. Notice that if we could invert the linear PCA step for a given
# instance in the reduced space, the reconstructed point would lie in feature space, not
# in the original space (e.g., like the one represented by an x in the diagram). Since the
# feature space is infinite-dimensional, we cannot compute the reconstructed point,
# and therefore we cannot compute the true reconstruction error. Fortunately, it is pos‐
# sible to find a point in the original space that would map close to the reconstructed
# point. This is called the reconstruction pre-image. Once you have this pre-image, you
# can measure its squared distance to the original instance. You can then select the ker‐
# nel and hyperparameters that minimize this reconstruction pre-image error.
# 
# 
# 
# 
# Figure 8-11. Kernel PCA and the reconstruction pre-image error
# 
# 
# 
# 
# 220   |   Chapter 8: Dimensionality Reduction
# 
#                  Download from finelybook www.finelybook.com
# You may be wondering how to perform this reconstruction. One solution is to train a
# supervised regression model, with the projected instances as the training set and the
# original instances as the targets. Scikit-Learn will do this automatically if you set
# fit_inverse_transform=True, as shown in the following code:7
#     rbf_pca = KernelPCA(n_components = 2, kernel="rbf", gamma=0.0433,
#                         fit_inverse_transform=True)
#     X_reduced = rbf_pca.fit_transform(X)
#     X_preimage = rbf_pca.inverse_transform(X_reduced)
# 
# 
#                    By default, fit_inverse_transform=False and KernelPCA has no
#                    inverse_transform() method. This method only gets created
#                    when you set fit_inverse_transform=True.
# 
# 
# 
# You can then compute the reconstruction pre-image error:
#     >>> from sklearn.metrics import mean_squared_error
#     >>> mean_squared_error(X, X_preimage)
#     32.786308795766132
# Now you can use grid search with cross-validation to find the kernel and hyperpara‐
# meters that minimize this pre-image reconstruction error.
# 
# LLE
# Locally Linear Embedding (LLE)8 is another very powerful nonlinear dimensionality
# reduction (NLDR) technique. It is a Manifold Learning technique that does not rely
# on projections like the previous algorithms. In a nutshell, LLE works by first measur‐
# ing how each training instance linearly relates to its closest neighbors (c.n.), and then
# looking for a low-dimensional representation of the training set where these local
# relationships are best preserved (more details shortly). This makes it particularly
# good at unrolling twisted manifolds, especially when there is not too much noise.
# For example, the following code uses Scikit-Learn’s LocallyLinearEmbedding class to
# unroll the Swiss roll. The resulting 2D dataset is shown in Figure 8-12. As you can
# see, the Swiss roll is completely unrolled and the distances between instances are
# locally well preserved. However, distances are not preserved on a larger scale: the left
# part of the unrolled Swiss roll is squeezed, while the right part is stretched. Neverthe‐
# less, LLE did a pretty good job at modeling the manifold.
# 
# 
# 7 Scikit-Learn uses the algorithm based on Kernel Ridge Regression described in Gokhan H. Bakır, Jason
#   Weston, and Bernhard Scholkopf, “Learning to Find Pre-images” (Tubingen, Germany: Max Planck Institute
#   for Biological Cybernetics, 2004).
# 8 “Nonlinear Dimensionality Reduction by Locally Linear Embedding,” S. Roweis, L. Saul (2000).
# 
# 
# 
#                                                                                                  LLE     |   221
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Selecting a Kernel and Tuning Hyperparameters",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Selectinga(HierNode):
    def __init__(self):
        super().__init__("Selecting a Kernel and Tuning Hyperparameters")
        self.add(Content(), "content")

# eof
