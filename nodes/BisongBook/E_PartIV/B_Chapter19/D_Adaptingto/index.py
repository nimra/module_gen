# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Adapting to Non-linearity
# Although linear regression has the premise that the underlying structure of the
# dataset features is linear, this is, however, not the case for most datasets. It is
# nevertheless possible to adapt linear regression to fit or build a model for non-linear
# datasets. This process of adding non-linearity to linear models is called polynomial
# regression.
#     Polynomial regression fits a non-linear relationship to the data by adding higher-­
# order polynomial terms of existing data features as new features in the dataset. More of
# this is visualized in Figure 19-5.
# 
# 
# 
# 
# Figure 19-5. Adding polynomial features to the dataset
# 
#     It is important to note that from a statistical point of view, when approximating the
# optimal values of the weights to minimize the model, the underlying assumption of
# the interactions of the parameters is linear. Non-linear regression models may tend to
# overfit the data, but this can be mitigated by adding regularization to the model. Here is
# a formal example of the polynomial regression model.
# 
#                        ŷ = q 0 + q1 x1 + q 2 x12 + q 3 x 2 + q 4 x 22 +¼+ qn xn + qn xn2
# 
#       An illustration of polynomial regression is shown in Figure 19-6.
# 
# 
# 
# 
# Figure 19-6. Fitting a non-linear model with polynomial regression

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Adapting to Non-linearity",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Adapting to Non-linearity"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Adaptingto(HierNode):
    def __init__(self):
        super().__init__("Adapting to Non-linearity")
        self.add(Content())

# eof