# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
#                          Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 6-5. Predictions of two Decision Tree regression models
# 
# The CART algorithm works mostly the same way as earlier, except that instead of try‐
# ing to split the training set in a way that minimizes impurity, it now tries to split the
# training set in a way that minimizes the MSE. Equation 6-4 shows the cost function
# that the algorithm tries to minimize.
# 
#       Equation 6-4. CART cost function for regression
#                                                                                                     2
#                   mleft           mright
#                                                             MSEnode =        ∑       y node − y i
#                                                                           i ∈ node
#       J k, tk   =       MSEleft +        MSEright   where
#                    m               m                                     1
#                                                                        mnode i ∈ ∑
#                                                             y node =                    yi
#                                                                                  node
# 
# 
# Just like for classification tasks, Decision Trees are prone to overfitting when dealing
# with regression tasks. Without any regularization (i.e., using the default hyperpara‐
# meters), you get the predictions on the left of Figure 6-6. It is obviously overfitting
# the training set very badly. Just setting min_samples_leaf=10 results in a much more
# reasonable model, represented on the right of Figure 6-6.
# 
# 
# 
# 
# Figure 6-6. Regularizing a Decision Tree regressor
# 
# 
# 
# 176    |   Chapter 6: Decision Trees
# 
#                        Download from finelybook www.finelybook.com
# Instability
# Hopefully by now you are convinced that Decision Trees have a lot going for them:
# they are simple to understand and interpret, easy to use, versatile, and powerful.
# However they do have a few limitations. First, as you may have noticed, Decision
# Trees love orthogonal decision boundaries (all splits are perpendicular to an axis),
# which makes them sensitive to training set rotation. For example, Figure 6-7 shows a
# simple linearly separable dataset: on the left, a Decision Tree can split it easily, while
# on the right, after the dataset is rotated by 45°, the decision boundary looks unneces‐
# sarily convoluted. Although both Decision Trees fit the training set perfectly, it is very
# likely that the model on the right will not generalize well. One way to limit this prob‐
# lem is to use PCA (see Chapter 8), which often results in a better orientation of the
# training data.
# 
# 
# 
# 
# Figure 6-7. Sensitivity to training set rotation
# 
# More generally, the main issue with Decision Trees is that they are very sensitive to
# small variations in the training data. For example, if you just remove the widest Iris-
# Versicolor from the iris training set (the one with petals 4.8 cm long and 1.8 cm wide)
# and train a new Decision Tree, you may get the model represented in Figure 6-8. As
# you can see, it looks very different from the previous Decision Tree (Figure 6-2).
# Actually, since the training algorithm used by Scikit-Learn is stochastic6 you may
# get very different models even on the same training data (unless you set the
# random_state hyperparameter).
# 
# 
# 
# 
# 6 It randomly selects the set of features to evaluate at each node.
# 
# 
# 
#                                                                           Instability   |   177
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Regression",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Regression"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Regression(HierNode):
    def __init__(self):
        super().__init__("Regression")
        self.add(Content())

# eof
