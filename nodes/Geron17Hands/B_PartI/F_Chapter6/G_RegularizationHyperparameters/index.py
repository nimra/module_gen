# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                  Download from finelybook www.finelybook.com
# the average information content of a message:4 entropy is zero when all messages are
# identical. In Machine Learning, it is frequently used as an impurity measure: a set’s
# entropy is zero when it contains instances of only one class. Equation 6-3 shows the
# definition of the entropy of the ith node. For example, the depth-2 left node in
#                                      49     49     5      5
# Figure 6-1 has an entropy equal to − 54 log 54 − 54 log 54 ≈ 0.31.
# 
#     Equation 6-3. Entropy
#                   n
#     Hi = −       ∑
#                 k=1
#                            pi, k log pi, k
#                pi, k ≠ 0
# 
# 
# So should you use Gini impurity or entropy? The truth is, most of the time it does not
# make a big difference: they lead to similar trees. Gini impurity is slightly faster to
# compute, so it is a good default. However, when they differ, Gini impurity tends to
# isolate the most frequent class in its own branch of the tree, while entropy tends to
# produce slightly more balanced trees.5
# 
# Regularization Hyperparameters
# Decision Trees make very few assumptions about the training data (as opposed to lin‐
# ear models, which obviously assume that the data is linear, for example). If left
# unconstrained, the tree structure will adapt itself to the training data, fitting it very
# closely, and most likely overfitting it. Such a model is often called a nonparametric
# model, not because it does not have any parameters (it often has a lot) but because the
# number of parameters is not determined prior to training, so the model structure is
# free to stick closely to the data. In contrast, a parametric model such as a linear model
# has a predetermined number of parameters, so its degree of freedom is limited,
# reducing the risk of overfitting (but increasing the risk of underfitting).
# To avoid overfitting the training data, you need to restrict the Decision Tree’s freedom
# during training. As you know by now, this is called regularization. The regularization
# hyperparameters depend on the algorithm used, but generally you can at least restrict
# the maximum depth of the Decision Tree. In Scikit-Learn, this is controlled by the
# max_depth hyperparameter (the default value is None, which means unlimited).
# Reducing max_depth will regularize the model and thus reduce the risk of overfitting.
# The DecisionTreeClassifier class has a few other parameters that similarly restrict
# the shape of the Decision Tree: min_samples_split (the minimum number of sam‐
# 
# 
# 4 A reduction of entropy is often called an information gain.
# 5 See Sebastian Raschka’s interesting analysis for more details.
# 
# 
# 
#                                                                    Regularization Hyperparameters   |   173
# 
#                  Download from finelybook www.finelybook.com
# ples a node must have before it can be split), min_samples_leaf (the minimum num‐
# ber of samples a leaf node must have), min_weight_fraction_leaf (same as
# min_samples_leaf but expressed as a fraction of the total number of weighted
# instances), max_leaf_nodes (maximum number of leaf nodes), and max_features
# (maximum number of features that are evaluated for splitting at each node). Increas‐
# ing min_* hyperparameters or reducing max_* hyperparameters will regularize the
# model.
# 
#                      Other algorithms work by first training the Decision Tree without
#                      restrictions, then pruning (deleting) unnecessary nodes. A node
#                      whose children are all leaf nodes is considered unnecessary if the
#                      purity improvement it provides is not statistically significant. Stan‐
#                      dard statistical tests, such as the χ2 test, are used to estimate the
#                      probability that the improvement is purely the result of chance
#                      (which is called the null hypothesis). If this probability, called the p-
#                      value, is higher than a given threshold (typically 5%, controlled by
#                      a hyperparameter), then the node is considered unnecessary and its
#                      children are deleted. The pruning continues until all unnecessary
#                      nodes have been pruned.
# 
# Figure 6-3 shows two Decision Trees trained on the moons dataset (introduced in
# Chapter 5). On the left, the Decision Tree is trained with the default hyperparameters
# (i.e., no restrictions), and on the right the Decision Tree is trained with min_sam
# ples_leaf=4. It is quite obvious that the model on the left is overfitting, and the
# model on the right will probably generalize better.
# 
# 
# 
# 
# Figure 6-3. Regularization using min_samples_leaf
# 
# 
# 
# 
# 174   |   Chapter 6: Decision Trees
# 
#                   Download from finelybook www.finelybook.com
# Regression
# Decision Trees are also capable of performing regression tasks. Let’s build a regres‐
# sion tree using Scikit-Learn’s DecisionTreeRegressor class, training it on a noisy
# quadratic dataset with max_depth=2:
#     from sklearn.tree import DecisionTreeRegressor
# 
#     tree_reg = DecisionTreeRegressor(max_depth=2)
#     tree_reg.fit(X, y)
# The resulting tree is represented on Figure 6-4.
# 
# 
# 
# 
# Figure 6-4. A Decision Tree for regression
# 
# This tree looks very similar to the classification tree you built earlier. The main differ‐
# ence is that instead of predicting a class in each node, it predicts a value. For example,
# suppose you want to make a prediction for a new instance with x1 = 0.6. You traverse
# the tree starting at the root, and you eventually reach the leaf node that predicts
# value=0.1106. This prediction is simply the average target value of the 110 training
# instances associated to this leaf node. This prediction results in a Mean Squared Error
# (MSE) equal to 0.0151 over these 110 instances.
# This model’s predictions are represented on the left of Figure 6-5. If you set
# max_depth=3, you get the predictions represented on the right. Notice how the pre‐
# dicted value for each region is always the average target value of the instances in that
# region. The algorithm splits each region in a way that makes most training instances
# as close as possible to that predicted value.
# 
# 
# 
#                                                                            Regression   |   175
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Regularization Hyperparameters",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Regularization Hyperparameters"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class RegularizationHyperparameters(HierNode):
    def __init__(self):
        super().__init__("Regularization Hyperparameters")
        self.add(Content())

# eof
