# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Choosing the Right Number of Dimensions",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Choosing the Right Number of Dimensions"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Choosingthe(HierNode):
    def __init__(self):
        super().__init__("Choosing the Right Number of Dimensions")
        self.add(Content())

# eof