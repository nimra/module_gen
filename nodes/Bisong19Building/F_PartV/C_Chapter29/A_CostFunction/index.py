# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 29   Training a Neural Network
# 
# 
# Cost Function or Loss Function
# The squared error cost function (also known as the mean squared error) finds the sum
# of the squared difference between the estimated target and the actual target for a real-­
# valued problem, while the cross-entropy cost function finds the difference between the
# predicted class from the probability estimates of the actual class label in a classification
# problem.
#      Regardless of the cost function used, when the error loss is small, we say that the cost
# is minimized. In Figure 29-3, the correct output of the example passed into the network
# is 2.3. After the output values are evaluated from the feedforward training, the squared
# error cost function is used to assess the quality of the network’s output.
#      Remember that the MSE finds the average cost over all the data samples in the
# training dataset. In the example illustrated in Figure 29-3, we used just one data sample
# to demonstrate how the cost function works.
# 
# 
# 
# 
# Figure 29-3. MSE estimate of the neural network
# 
# 
# O
#  ne-Hot Encoding
# In a classification problem, one-hot encoding is the process of transforming the class
# labels of the target variable into a matrix of binary variables. The one-hot encoder
# assigns 1 when the output belongs to a particular class and 0 otherwise. An illustration of
# one-hot encoding is shown in Figure 29-4.
# 
# 
# 
# 
# 336
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Cost Function or Loss Function",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Cost Function or Loss Function"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class CostFunction(HierNode):
    def __init__(self):
        super().__init__("Cost Function or Loss Function")
        self.add(Content())

# eof
