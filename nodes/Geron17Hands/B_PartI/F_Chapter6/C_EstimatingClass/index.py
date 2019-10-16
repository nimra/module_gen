# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                   Download from finelybook www.finelybook.com
# Estimating Class Probabilities
# A Decision Tree can also estimate the probability that an instance belongs to a partic‐
# ular class k: first it traverses the tree to find the leaf node for this instance, and then it
# returns the ratio of training instances of class k in this node. For example, suppose
# you have found a flower whose petals are 5 cm long and 1.5 cm wide. The corre‐
# sponding leaf node is the depth-2 left node, so the Decision Tree should output the
# following probabilities: 0% for Iris-Setosa (0/54), 90.7% for Iris-Versicolor (49/54),
# and 9.3% for Iris-Virginica (5/54). And of course if you ask it to predict the class, it
# should output Iris-Versicolor (class 1) since it has the highest probability. Let’s check
# this:
#     >>> tree_clf.predict_proba([[5, 1.5]])
#     array([[ 0. , 0.90740741, 0.09259259]])
#     >>> tree_clf.predict([[5, 1.5]])
#     array([1])
# Perfect! Notice that the estimated probabilities would be identical anywhere else in
# the bottom-right rectangle of Figure 6-2—for example, if the petals were 6 cm long
# and 1.5 cm wide (even though it seems obvious that it would most likely be an Iris-
# Virginica in this case).
# 
# The CART Training Algorithm
# Scikit-Learn uses the Classification And Regression Tree (CART) algorithm to train
# Decision Trees (also called “growing” trees). The idea is really quite simple: the algo‐
# rithm first splits the training set in two subsets using a single feature k and a thres‐
# hold tk (e.g., “petal length ≤ 2.45 cm”). How does it choose k and tk? It searches for the
# pair (k, tk) that produces the purest subsets (weighted by their size). The cost function
# that the algorithm tries to minimize is given by Equation 6-2.
# 
#    Equation 6-2. CART cost function for classification
#               mleft         mright
#      J k, tk =       G +           Gright
#                 m left        m
#              Gleft/right measures the impurity of the left/right subset,
#      where
#              mleft/right is the number of instances in the left/right subset.
# 
# Once it has successfully split the training set in two, it splits the subsets using the
# same logic, then the sub-subsets and so on, recursively. It stops recursing once it rea‐
# ches the maximum depth (defined by the max_depth hyperparameter), or if it cannot
# find a split that will reduce impurity. A few other hyperparameters (described in a
# 
# 
# 
# 
#                                                                Estimating Class Probabilities   |   171
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Estimating Class Probabilities",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Estimating Class Probabilities"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class EstimatingClass(HierNode):
    def __init__(self):
        super().__init__("Estimating Class Probabilities")
        self.add(Content())

# eof
