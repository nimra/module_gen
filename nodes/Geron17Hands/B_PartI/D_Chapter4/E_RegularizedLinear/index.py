# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_RidgeRegression.index import RidgeRegression as A_RidgeRegression
from .B_LassoRegression.index import LassoRegression as B_LassoRegression
from .C_ElasticNet.index import ElasticNet as C_ElasticNet
from .D_EarlyStopping.index import EarlyStopping as D_EarlyStopping

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                     Download from finelybook www.finelybook.com
#   Irreducible error
#        This part is due to the noisiness of the data itself. The only way to reduce this
#        part of the error is to clean up the data (e.g., fix the data sources, such as broken
#        sensors, or detect and remove outliers).
#   Increasing a model’s complexity will typically increase its variance and reduce its bias.
#   Conversely, reducing a model’s complexity increases its bias and reduces its variance.
#   This is why it is called a tradeoff.
# 
# 
# 
# Regularized Linear Models
# As we saw in Chapters 1 and 2, a good way to reduce overfitting is to regularize the
# model (i.e., to constrain it): the fewer degrees of freedom it has, the harder it will be
# for it to overfit the data. For example, a simple way to regularize a polynomial model
# is to reduce the number of polynomial degrees.
# For a linear model, regularization is typically achieved by constraining the weights of
# the model. We will now look at Ridge Regression, Lasso Regression, and Elastic Net,
# which implement three different ways to constrain the weights.
# 
# Ridge Regression
# Ridge Regression (also called Tikhonov regularization) is a regularized version of Lin‐
# ear Regression: a regularization term equal to α∑ni = 1 θ2i is added to the cost function.
# This forces the learning algorithm to not only fit the data but also keep the model
# weights as small as possible. Note that the regularization term should only be added
# to the cost function during training. Once the model is trained, you want to evaluate
# the model’s performance using the unregularized performance measure.
# 
#                 It is quite common for the cost function used during training to be
#                 different from the performance measure used for testing. Apart
#                 from regularization, another reason why they might be different is
#                 that a good training cost function should have optimization-
#                 friendly derivatives, while the performance measure used for test‐
#                 ing should be as close as possible to the final objective. A good
#                 example of this is a classifier trained using a cost function such as
#                 the log loss (discussed in a moment) but evaluated using precision/
#                 recall.
# 
# The hyperparameter α controls how much you want to regularize the model. If α = 0
# then Ridge Regression is just Linear Regression. If α is very large, then all weights end
# 
# 
# 
# 
#                                                                  Regularized Linear Models   |   127
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Regularized Linear Models",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Regularized Linear Models"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class RegularizedLinear(HierNode):
    def __init__(self):
        super().__init__("Regularized Linear Models")
        self.add(Content())
        self.add(A_RidgeRegression())
        self.add(B_LassoRegression())
        self.add(C_ElasticNet())
        self.add(D_EarlyStopping())

# eof
