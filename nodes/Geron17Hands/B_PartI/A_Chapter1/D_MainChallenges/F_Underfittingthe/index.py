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
#                         Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 1-23. Regularization reduces the risk of overfitting
# 
# The amount of regularization to apply during learning can be controlled by a hyper‐
# parameter. A hyperparameter is a parameter of a learning algorithm (not of the
# model). As such, it is not affected by the learning algorithm itself; it must be set prior
# to training and remains constant during training. If you set the regularization hyper‐
# parameter to a very large value, you will get an almost flat model (a slope close to
# zero); the learning algorithm will almost certainly not overfit the training data, but it
# will be less likely to find a good solution. Tuning hyperparameters is an important
# part of building a Machine Learning system (you will see a detailed example in the
# next chapter).
# 
# Underfitting the Training Data
# As you might guess, underfitting is the opposite of overfitting: it occurs when your
# model is too simple to learn the underlying structure of the data. For example, a lin‐
# ear model of life satisfaction is prone to underfit; reality is just more complex than
# the model, so its predictions are bound to be inaccurate, even on the training exam‐
# ples.
# The main options to fix this problem are:
# 
#      • Selecting a more powerful model, with more parameters
#      • Feeding better features to the learning algorithm (feature engineering)
#      • Reducing the constraints on the model (e.g., reducing the regularization hyper‐
#        parameter)
# 
# 
# Stepping Back
# By now you already know a lot about Machine Learning. However, we went through
# so many concepts that you may be feeling a little lost, so let’s step back and look at the
# big picture:
# 
# 
# 28    |   Chapter 1: The Machine Learning Landscape
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Underfitting the Training Data",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Underfittingthe(HierNode):
    def __init__(self):
        super().__init__("Underfitting the Training Data")
        self.add(Content(), "content")

# eof
