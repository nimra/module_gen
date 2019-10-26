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
#                        Download from finelybook www.finelybook.com
# PCA for Compression
# Obviously after dimensionality reduction, the training set takes up much less space.
# For example, try applying PCA to the MNIST dataset while preserving 95% of its var‐
# iance. You should find that each instance will have just over 150 features, instead of
# the original 784 features. So while most of the variance is preserved, the dataset is
# now less than 20% of its original size! This is a reasonable compression ratio, and you
# can see how this can speed up a classification algorithm (such as an SVM classifier)
# tremendously.
# It is also possible to decompress the reduced dataset back to 784 dimensions by
# applying the inverse transformation of the PCA projection. Of course this won’t give
# you back the original data, since the projection lost a bit of information (within the
# 5% variance that was dropped), but it will likely be quite close to the original data.
# The mean squared distance between the original data and the reconstructed data
# (compressed and then decompressed) is called the reconstruction error. For example,
# the following code compresses the MNIST dataset down to 154 dimensions, then uses
# the inverse_transform() method to decompress it back to 784 dimensions.
# Figure 8-9 shows a few digits from the original training set (on the left), and the cor‐
# responding digits after compression and decompression. You can see that there is a
# slight image quality loss, but the digits are still mostly intact.
#       pca = PCA(n_components = 154)
#       X_mnist_reduced = pca.fit_transform(X_mnist)
#       X_mnist_recovered = pca.inverse_transform(X_mnist_reduced)
# 
# 
# 
# 
# Figure 8-9. MNIST compression preserving 95% of the variance
# 
# 
# 
# 
# 216   |   Chapter 8: Dimensionality Reduction
# 
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
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "PCA for Compression",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PCAfor(HierNode):
    def __init__(self):
        super().__init__("PCA for Compression")
        self.add(Content(), "content")

# eof
