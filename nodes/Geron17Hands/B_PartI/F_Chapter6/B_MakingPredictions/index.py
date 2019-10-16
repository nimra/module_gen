# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                      Download from finelybook www.finelybook.com
# Making Predictions
# Let’s see how the tree represented in Figure 6-1 makes predictions. Suppose you find
# an iris flower and you want to classify it. You start at the root node (depth 0, at the
# top): this node asks whether the flower’s petal length is smaller than 2.45 cm. If it is,
# then you move down to the root’s left child node (depth 1, left). In this case, it is a leaf
# node (i.e., it does not have any children nodes), so it does not ask any questions: you
# can simply look at the predicted class for that node and the Decision Tree predicts
# that your flower is an Iris-Setosa (class=setosa).
# Now suppose you find another flower, but this time the petal length is greater than
# 2.45 cm. You must move down to the root’s right child node (depth 1, right), which is
# not a leaf node, so it asks another question: is the petal width smaller than 1.75 cm? If
# it is, then your flower is most likely an Iris-Versicolor (depth 2, left). If not, it is likely
# an Iris-Virginica (depth 2, right). It’s really that simple.
# 
#                    One of the many qualities of Decision Trees is that they require
#                    very little data preparation. In particular, they don’t require feature
#                    scaling or centering at all.
# 
# 
# 
# A node’s samples attribute counts how many training instances it applies to. For
# example, 100 training instances have a petal length greater than 2.45 cm (depth 1,
# right), among which 54 have a petal width smaller than 1.75 cm (depth 2, left). A
# node’s value attribute tells you how many training instances of each class this node
# applies to: for example, the bottom-right node applies to 0 Iris-Setosa, 1 Iris-
# Versicolor, and 45 Iris-Virginica. Finally, a node’s gini attribute measures its impur‐
# ity: a node is “pure” (gini=0) if all training instances it applies to belong to the same
# class. For example, since the depth-1 left node applies only to Iris-Setosa training
# instances, it is pure and its gini score is 0. Equation 6-1 shows how the training algo‐
# rithm computes the gini score Gi of the ith node. For example, the depth-2 left node
# has a gini score equal to 1 – (0/54)2 – (49/54)2 – (5/54)2 ≈ 0.168. Another impurity
# measure is discussed shortly.
# 
#    Equation 6-1. Gini impurity
#                n
#    Gi = 1 −    ∑ pi, k2
#               k=1
# 
# 
#   • pi,k is the ratio of class k instances among the training instances in the ith node.
# 
# 
# 
# 
#                                                                            Making Predictions |   169
# 
#                        Download from finelybook www.finelybook.com
#                      Scikit-Learn uses the CART algorithm, which produces only binary
#                      trees: nonleaf nodes always have two children (i.e., questions only
#                      have yes/no answers). However, other algorithms such as ID3 can
#                      produce Decision Trees with nodes that have more than two chil‐
#                      dren.
# 
# Figure 6-2 shows this Decision Tree’s decision boundaries. The thick vertical line rep‐
# resents the decision boundary of the root node (depth 0): petal length = 2.45 cm.
# Since the left area is pure (only Iris-Setosa), it cannot be split any further. However,
# the right area is impure, so the depth-1 right node splits it at petal width = 1.75 cm
# (represented by the dashed line). Since max_depth was set to 2, the Decision Tree
# stops right there. However, if you set max_depth to 3, then the two depth-2 nodes
# would each add another decision boundary (represented by the dotted lines).
# 
# 
# 
# 
# Figure 6-2. Decision Tree decision boundaries
# 
# 
#                    Model Interpretation: White Box Versus Black Box
#   As you can see Decision Trees are fairly intuitive and their decisions are easy to inter‐
#   pret. Such models are often called white box models. In contrast, as we will see, Ran‐
#   dom Forests or neural networks are generally considered black box models. They
#   make great predictions, and you can easily check the calculations that they performed
#   to make these predictions; nevertheless, it is usually hard to explain in simple terms
#   why the predictions were made. For example, if a neural network says that a particu‐
#   lar person appears on a picture, it is hard to know what actually contributed to this
#   prediction: did the model recognize that person’s eyes? Her mouth? Her nose? Her
#   shoes? Or even the couch that she was sitting on? Conversely, Decision Trees provide
#   nice and simple classification rules that can even be applied manually if need be (e.g.,
#   for flower classification).
# 
# 
# 
# 
# 170   |   Chapter 6: Decision Trees
# 
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
            "Making Predictions",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Making Predictions"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MakingPredictions(HierNode):
    def __init__(self):
        super().__init__("Making Predictions")
        self.add(Content())

# eof