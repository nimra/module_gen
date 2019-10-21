# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Optimizing Gradient Descent with Feature Scaling
# This process involves making sure that the features in the dataset are all on the same
# scale. Typically all real-valued features in the dataset should lie between −1 ≤ xi ≤ 1 or
# a range around that region. Any range too large or arbitrarily too small can generate a
# contour plot that is too narrow and hence will take a longer time for gradient descent
# to converge to the optimal solution. The plot in Figure 16-3 is called a contour plot.
# Contour plots are used to represent 3-D surfaces on a 2-D plane. The smaller circles
# represent the lowest point (or the global optimum) of the convex function.
# 
# 
# 
# 
# Figure 16-3. Feature scaling – contour plots. Left: without feature scaling.
# Right: with feature scaling
# 
#    A popular technique for feature scaling is called mean normalization. In mean
# normalization, for each feature, the mean of the feature is subtracted from each record
# and divided by the feature’s range (i.e., the difference between the maximum and
# minimum elements in the feature). Alternatively, it can be divided by the standard
# deviation of the features. Feature scaling is formally written as
# 
#                  x i - mi                      x - mi
#          xi =             divided by range xi = i     divided by standard deviation
#                 max - min                         s
# 
#       Figure 16-4 is an example of a dataset with feature scaling.
# 
# 
# 
# 
# 
# Figure 16-4. Feature scaling example
# 
#     In this chapter, we discussed gradient descent, an important algorithm for
# optimizing machine learning models. In the next chapter, we will introduce a suite of
# supervised and unsupervised machine learning algorithms.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Optimizing Gradient Descent with Feature Scaling",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Optimizing Gradient Descent with Feature Scaling"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class OptimizingGradient(HierNode):
    def __init__(self):
        super().__init__("Optimizing Gradient Descent with Feature Scaling")
        self.add(Content())

# eof
