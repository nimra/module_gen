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
# The equation of the inverse transformation is shown in Equation 8-3.
# 
#     Equation 8-3. PCA inverse transformation, back to the original number of
#     dimensions
#                                    T
#     �recovered = �d‐proj · �d
# 
# 
# Incremental PCA
# One problem with the preceding implementation of PCA is that it requires the whole
# training set to fit in memory in order for the SVD algorithm to run. Fortunately,
# Incremental PCA (IPCA) algorithms have been developed: you can split the training
# set into mini-batches and feed an IPCA algorithm one mini-batch at a time. This is
# useful for large training sets, and also to apply PCA online (i.e., on the fly, as new
# instances arrive).
# The following code splits the MNIST dataset into 100 mini-batches (using NumPy’s
# array_split() function) and feeds them to Scikit-Learn’s IncrementalPCA class5 to
# reduce the dimensionality of the MNIST dataset down to 154 dimensions (just like
# before). Note that you must call the partial_fit() method with each mini-batch
# rather than the fit() method with the whole training set:
#     from sklearn.decomposition import IncrementalPCA
# 
#     n_batches = 100
#     inc_pca = IncrementalPCA(n_components=154)
#     for X_batch in np.array_split(X_mnist, n_batches):
#         inc_pca.partial_fit(X_batch)
# 
#     X_mnist_reduced = inc_pca.transform(X_mnist)
# 
# Alternatively, you can use NumPy’s memmap class, which allows you to manipulate a
# large array stored in a binary file on disk as if it were entirely in memory; the class
# loads only the data it needs in memory, when it needs it. Since the IncrementalPCA
# class uses only a small part of the array at any given time, the memory usage remains
# under control. This makes it possible to call the usual fit() method, as you can see
# in the following code:
#     X_mm = np.memmap(filename, dtype="float32", mode="readonly", shape=(m, n))
# 
#     batch_size = m // n_batches
#     inc_pca = IncrementalPCA(n_components=154, batch_size=batch_size)
#     inc_pca.fit(X_mm)
# 
# 
# 
# 
# 5 Scikit-Learn uses the algorithm described in “Incremental Learning for Robust Visual Tracking,” D. Ross et al.
#   (2007).
# 
# 
# 
#                                                                                                    PCA   |   217
# 
#                        Download from finelybook www.finelybook.com
# Randomized PCA
# Scikit-Learn offers yet another option to perform PCA, called Randomized PCA. This
# is a stochastic algorithm that quickly finds an approximation of the first d principal
# components. Its computational complexity is O(m × d2) + O(d3), instead of O(m × n2)
# + O(n3), so it is dramatically faster than the previous algorithms when d is much
# smaller than n.
#       rnd_pca = PCA(n_components=154, svd_solver="randomized")
#       X_reduced = rnd_pca.fit_transform(X_mnist)
# 
# 
# Kernel PCA
# In Chapter 5 we discussed the kernel trick, a mathematical technique that implicitly
# maps instances into a very high-dimensional space (called the feature space), enabling
# nonlinear classification and regression with Support Vector Machines. Recall that a
# linear decision boundary in the high-dimensional feature space corresponds to a
# complex nonlinear decision boundary in the original space.
# It turns out that the same trick can be applied to PCA, making it possible to perform
# complex nonlinear projections for dimensionality reduction. This is called Kernel
# PCA (kPCA).6 It is often good at preserving clusters of instances after projection, or
# sometimes even unrolling datasets that lie close to a twisted manifold.
# For example, the following code uses Scikit-Learn’s KernelPCA class to perform kPCA
# with an RBF kernel (see Chapter 5 for more details about the RBF kernel and the
# other kernels):
#       from sklearn.decomposition import KernelPCA
# 
#       rbf_pca = KernelPCA(n_components = 2, kernel="rbf", gamma=0.04)
#       X_reduced = rbf_pca.fit_transform(X)
# Figure 8-10 shows the Swiss roll, reduced to two dimensions using a linear kernel
# (equivalent to simply using the PCA class), an RBF kernel, and a sigmoid kernel
# (Logistic).
# 
# 
# 
# 
# 6 “Kernel Principal Component Analysis,” B. Schölkopf, A. Smola, K. Müller (1999).
# 
# 
# 
# 218   |   Chapter 8: Dimensionality Reduction
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Incremental PCA",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class IncrementalPCA(HierNode):
    def __init__(self):
        super().__init__("Incremental PCA")
        self.add(Content(), "content")

# eof
