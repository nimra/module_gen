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

from .A_ThinkingAbout.index import ThinkingAbout as A_ThinkingAbout
from .B_Selectingthe.index import Selectingthe as B_Selectingthe
from .C_LearningCurves.index import LearningCurves as C_LearningCurves
from .D_Validationin.index import Validationin as D_Validationin
from .E_Summary.index import Summary as E_Summary

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# Summary
# In this section we have covered the essential features of the Scikit-Learn data repre‐
# sentation, and the estimator API. Regardless of the type of estimator, the same
# import/instantiate/fit/predict pattern holds. Armed with this information about the
# estimator API, you can explore the Scikit-Learn documentation and begin trying out
# various models on your data.
# In the next section, we will explore perhaps the most important topic in machine
# learning: how to select and validate your model.
# 
# Hyperparameters and Model Validation
# In the previous section, we saw the basic recipe for applying a supervised machine
# learning model:
# 
#  1. Choose a class of model
#  2. Choose model hyperparameters
#  3. Fit the model to the training data
#  4. Use the model to predict labels for new data
# 
# The first two pieces of this—the choice of model and choice of hyperparameters—are
# perhaps the most important part of using these tools and techniques effectively. In
# order to make an informed choice, we need a way to validate that our model and our
# hyperparameters are a good fit to the data. While this may sound simple, there are
# some pitfalls that you must avoid to do this effectively.
# 
# Thinking About Model Validation
# In principle, model validation is very simple: after choosing a model and its hyper‐
# parameters, we can estimate how effective it is by applying it to some of the training
# data and comparing the prediction to the known value.
# The following sections first show a naive approach to model validation and why it
# fails, before exploring the use of holdout sets and cross-validation for more robust
# model evaluation.
# 
# Model validation the wrong way
# Let’s demonstrate the naive approach to validation using the Iris data, which we saw
# in the previous section. We will start by loading the data:
#     In[1]: from sklearn.datasets import load_iris
#            iris = load_iris()
# 
# 
# 
# 
#                                                     Hyperparameters and Model Validation   |   359
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Hyperparameters and Model Validation",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Hyperparametersand(HierNode):
    def __init__(self):
        super().__init__("Hyperparameters and Model Validation")
        self.add(Content())
        self.add(A_ThinkingAbout())
        self.add(B_Selectingthe())
        self.add(C_LearningCurves())
        self.add(D_Validationin())
        self.add(E_Summary())

# eof
