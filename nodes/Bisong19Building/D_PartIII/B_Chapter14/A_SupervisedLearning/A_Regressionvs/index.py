# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Regression vs. Classification
# In supervised learning, we typically have two types of modeling task, and they are
# regression and classification.
# 
# Regression
# The supervised learning problem is a regression task when the values of the target
# variable are real-valued numbers.
#     Let’s take, for example, that we are given a housing dataset and are asked to build a
# model that can predict the price of a house. The dataset, for example, has features such
# as the price of the house, the number of bedrooms, the number of bathrooms, and the
# total square feet. Let’s illustrate how this dataset will look like with a contrived example
# in Figure 14-2.
# 
# 
# 
# 
# Figure 14-2. Regression problem: housing dataset
# 
#      From the learning problem, the features of the dataset are the number of bedrooms,
# the number of bathrooms, and the square foot of the floor area, while the target feature
# is the price of the house. The use case presented in Figure 14-3 is framed as a regression
# task because the target feature is a real-valued number.
# 
# 
# Classification
# In a classification task, the target feature is a label denoting some sort of class
# membership. These labels are also called categorical variables, because they represent
# labels that belong to two or more categories. Also, no natural ordering exists between the
# categories or labels.
#      As an example, suppose we are given a dataset containing the heart disease
# diagnosis of patients, and we are asked to build a model to predict if a patient has a
# heart disease or not. Like the previous example, let’s assume the dataset has features
# blood pressure, cholesterol level, heart rate, and heart disease diagnosis. A contrived
# illustration of this example is shown in Figure 14-3.
# 
# 
# 
# 
# Figure 14-3. Classification task: heart disease dataset
# 
#     From the table in Figure 14-3, the target variable denotes a class membership of
# heart disease or no heart disease; hence, the target is categorical and can be termed as
# a classification problem.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Regression vs. Classification",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Regression vs. Classification"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Regressionvs(HierNode):
    def __init__(self):
        super().__init__("Regression vs. Classification")
        self.add(Content())

# eof
