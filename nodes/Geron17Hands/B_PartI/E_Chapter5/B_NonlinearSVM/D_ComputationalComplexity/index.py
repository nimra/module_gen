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
#                      Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 5-9. SVM classifiers using an RBF kernel
# 
# Other kernels exist but are used much more rarely. For example, some kernels are
# specialized for specific data structures. String kernels are sometimes used when classi‐
# fying text documents or DNA sequences (e.g., using the string subsequence kernel or
# kernels based on the Levenshtein distance).
# 
#                    With so many kernels to choose from, how can you decide which
#                    one to use? As a rule of thumb, you should always try the linear
#                    kernel first (remember that LinearSVC is much faster than SVC(ker
#                    nel="linear")), especially if the training set is very large or if it
#                    has plenty of features. If the training set is not too large, you should
#                    try the Gaussian RBF kernel as well; it works well in most cases.
#                    Then if you have spare time and computing power, you can also
#                    experiment with a few other kernels using cross-validation and grid
#                    search, especially if there are kernels specialized for your training
#                    set’s data structure.
# 
# 
# Computational Complexity
# The LinearSVC class is based on the liblinear library, which implements an optimized
# algorithm for linear SVMs.1 It does not support the kernel trick, but it scales almost
# 
# 
# 1 “A Dual Coordinate Descent Method for Large-scale Linear SVM,” Lin et al. (2008).
# 
# 
# 
#                                                                           Nonlinear SVM Classification   |   153
# 
#                   Download from finelybook www.finelybook.com
# linearly with the number of training instances and the number of features: its training
# time complexity is roughly O(m × n).
# The algorithm takes longer if you require a very high precision. This is controlled by
# the tolerance hyperparameter ϵ (called tol in Scikit-Learn). In most classification
# tasks, the default tolerance is fine.
# The SVC class is based on the libsvm library, which implements an algorithm that sup‐
# ports the kernel trick.2 The training time complexity is usually between O(m2 × n)
# and O(m3 × n). Unfortunately, this means that it gets dreadfully slow when the num‐
# ber of training instances gets large (e.g., hundreds of thousands of instances). This
# algorithm is perfect for complex but small or medium training sets. However, it scales
# well with the number of features, especially with sparse features (i.e., when each
# instance has few nonzero features). In this case, the algorithm scales roughly with the
# average number of nonzero features per instance. Table 5-1 compares Scikit-Learn’s
# SVM classification classes.
# 
# Table 5-1. Comparison of Scikit-Learn classes for SVM classification
# Class                  Time complexity           Out-of-core support Scaling required Kernel trick
# LinearSVC              O(m × n)                  No                  Yes              No
# SGDClassifier O(m × n)                           Yes                 Yes               No
# SVC                    O(m² × n) to O(m³ × n) No                     Yes               Yes
# 
# 
# SVM Regression
# As we mentioned earlier, the SVM algorithm is quite versatile: not only does it sup‐
# port linear and nonlinear classification, but it also supports linear and nonlinear
# regression. The trick is to reverse the objective: instead of trying to fit the largest pos‐
# sible street between two classes while limiting margin violations, SVM Regression
# tries to fit as many instances as possible on the street while limiting margin violations
# (i.e., instances off the street). The width of the street is controlled by a hyperparame‐
# ter ϵ. Figure 5-10 shows two linear SVM Regression models trained on some random
# linear data, one with a large margin (ϵ = 1.5) and the other with a small margin (ϵ =
# 0.5).
# 
# 
# 
# 
# 2 “Sequential Minimal Optimization (SMO),” J. Platt (1998).
# 
# 
# 
# 154     |   Chapter 5: Support Vector Machines
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Computational Complexity",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ComputationalComplexity(HierNode):
    def __init__(self):
        super().__init__("Computational Complexity")
        self.add(Content(), "content")

# eof
