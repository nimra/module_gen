# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 19   Linear Regression
# 
# F inding the Regression Line – How Do We Optimize
#  the Parameters of the Linear Model?
# To find the regression line, we need to define the cost function, which is also called the
# loss function. Remember that the cost in machine learning is the error measure that
# the learning algorithm minimizes. We can also define the cost as the penalty when the
# model outputs an incorrect prediction.
#      In the case of the linear regression model, the cost function is defined as half the sum
# of the squared difference between the predicted value and the actual value. The linear
# regression cost function is called the squared error cost function and is written as
# 
#                                              1
#                                      C (q ) = å ( yˆ - y )
#                                                            2
# 
#                                              2
# 
#     To put it more simply, the closer the approximate value of the target variable ŷ is to
# the actual variable y, the lower our cost and the better our model.
#     Having defined the cost function, an optimization algorithm such as gradient
# descent is used to minimize the cost C(θ) by updating the weights of the linear
# regression model.
# 
# 
# 
# How Do We Interpret the Linear Regression Model?
# In machine learning, the focus of linear regression differs slightly from traditional
# statistics. In statistics, the goal of a regression model is to understand the relationships
# between the features and targets by interpreting p-values, whereas in machine learning,
# the goal of the linear regression model is to predict the targets given new samples.
#     Figure 19-4 shows a regression model with a line of best fit that optimizes the
# squared difference between the data features and the targets. This difference is also
# called the residuals (shown as the purple vertical lines in Figure 19-4). What we care
# about in a linear regression model is to minimize the error between the predicted labels
# and the actual labels in the dataset.
# 
# 
# 
# 
# 234
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Finding the Regression Line – How Do We Optimize the Parameters of the Linear Model?")
        self.add(MarkdownBlock("# Finding the Regression Line – How Do We Optimize the Parameters of the Linear Model?"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Findingthe(HierNode):
    def __init__(self):
        super().__init__("Finding the Regression Line – How Do We Optimize the Parameters of the Linear Model?")
        self.add(Content())

# eof
