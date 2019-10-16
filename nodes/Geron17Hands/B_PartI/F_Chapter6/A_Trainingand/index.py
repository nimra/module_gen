# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                  Download from finelybook www.finelybook.com
# 
# 
#                                                                         CHAPTER 6
#                                                           Decision Trees
# 
# 
# 
# 
# Like SVMs, Decision Trees are versatile Machine Learning algorithms that can per‐
# form both classification and regression tasks, and even multioutput tasks. They are
# very powerful algorithms, capable of fitting complex datasets. For example, in Chap‐
# ter 2 you trained a DecisionTreeRegressor model on the California housing dataset,
# fitting it perfectly (actually overfitting it).
# Decision Trees are also the fundamental components of Random Forests (see Chap‐
# ter 7), which are among the most powerful Machine Learning algorithms available
# today.
# In this chapter we will start by discussing how to train, visualize, and make predic‐
# tions with Decision Trees. Then we will go through the CART training algorithm
# used by Scikit-Learn, and we will discuss how to regularize trees and use them for
# regression tasks. Finally, we will discuss some of the limitations of Decision Trees.
# 
# Training and Visualizing a Decision Tree
# To understand Decision Trees, let’s just build one and take a look at how it makes pre‐
# dictions. The following code trains a DecisionTreeClassifier on the iris dataset
# (see Chapter 4):
#     from sklearn.datasets import load_iris
#     from sklearn.tree import DecisionTreeClassifier
# 
#     iris = load_iris()
#     X = iris.data[:, 2:] # petal length and width
#     y = iris.target
# 
#     tree_clf = DecisionTreeClassifier(max_depth=2)
#     tree_clf.fit(X, y)
# 
# 
# 
#                                                                                     167
# 
#                 Download from finelybook www.finelybook.com
# You can visualize the trained Decision Tree by first using the export_graphviz()
# method to output a graph definition file called iris_tree.dot:
#       from sklearn.tree import export_graphviz
# 
#       export_graphviz(
#               tree_clf,
#               out_file=image_path("iris_tree.dot"),
#               feature_names=iris.feature_names[2:],
#               class_names=iris.target_names,
#               rounded=True,
#               filled=True
#           )
# Then you can convert this .dot file to a variety of formats such as PDF or PNG using
# the dot command-line tool from the graphviz package.1 This command line converts
# the .dot file to a .png image file:
#       $ dot -Tpng iris_tree.dot -o iris_tree.png
# Your first decision tree looks like Figure 6-1.
# 
# 
# 
# 
# Figure 6-1. Iris Decision Tree
# 
# 
# 1 Graphviz is an open source graph visualization software package, available at http://www.graphviz.org/.
# 
# 
# 
# 168   |   Chapter 6: Decision Trees
# 
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Training and Visualizing a Decision Tree",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Training and Visualizing a Decision Tree"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Trainingand(HierNode):
    def __init__(self):
        super().__init__("Training and Visualizing a Decision Tree")
        self.add(Content())

# eof
