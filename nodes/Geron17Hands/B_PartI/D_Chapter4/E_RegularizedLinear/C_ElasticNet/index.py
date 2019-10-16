# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                    Download from finelybook www.finelybook.com
#       Equation 4-11. Lasso Regression subgradient vector
#                                         sign θ1
#                                                                    −1 if θi < 0
#                                         sign θ2
#       g θ, J = ∇θ MSE θ + α                        where sign θi = 0   if θi = 0
#                                             ⋮
#                                                                    +1 if θi > 0
#                                         sign θn
# 
# 
# Here is a small Scikit-Learn example using the Lasso class. Note that you could
# instead use an SGDRegressor(penalty="l1").
#       >>> from sklearn.linear_model import Lasso
#       >>> lasso_reg = Lasso(alpha=0.1)
#       >>> lasso_reg.fit(X, y)
#       >>> lasso_reg.predict([[1.5]])
#       array([ 1.53788174])
# 
# 
# Elastic Net
# Elastic Net is a middle ground between Ridge Regression and Lasso Regression. The
# regularization term is a simple mix of both Ridge and Lasso’s regularization terms,
# and you can control the mix ratio r. When r = 0, Elastic Net is equivalent to Ridge
# Regression, and when r = 1, it is equivalent to Lasso Regression (see Equation 4-12).
# 
#       Equation 4-12. Elastic Net cost function
#                                  n
#                                              1−r n 2
#       J θ = MSE θ + rα          ∑ θi
#                                i=1
#                                          +
#                                               2 i∑
#                                                 α
#                                                   =1
#                                                      θi
# 
# 
# So when should you use Linear Regression, Ridge, Lasso, or Elastic Net? It is almost
# always preferable to have at least a little bit of regularization, so generally you should
# avoid plain Linear Regression. Ridge is a good default, but if you suspect that only a
# few features are actually useful, you should prefer Lasso or Elastic Net since they tend
# to reduce the useless features’ weights down to zero as we have discussed. In general,
# Elastic Net is preferred over Lasso since Lasso may behave erratically when the num‐
# ber of features is greater than the number of training instances or when several fea‐
# tures are strongly correlated.
# Here is a short example using Scikit-Learn’s ElasticNet (l1_ratio corresponds to
# the mix ratio r):
#       >>> from sklearn.linear_model import ElasticNet
#       >>> elastic_net = ElasticNet(alpha=0.1, l1_ratio=0.5)
#       >>> elastic_net.fit(X, y)
#       >>> elastic_net.predict([[1.5]])
#       array([ 1.54333232])
# 
# 
# 
# 132    |   Chapter 4: Training Models
# 
#                  Download from finelybook www.finelybook.com
# Early Stopping
# A very different way to regularize iterative learning algorithms such as Gradient
# Descent is to stop training as soon as the validation error reaches a minimum. This is
# called early stopping. Figure 4-20 shows a complex model (in this case a high-degree
# Polynomial Regression model) being trained using Batch Gradient Descent. As the
# epochs go by, the algorithm learns and its prediction error (RMSE) on the training set
# naturally goes down, and so does its prediction error on the validation set. However,
# after a while the validation error stops decreasing and actually starts to go back up.
# This indicates that the model has started to overfit the training data. With early stop‐
# ping you just stop training as soon as the validation error reaches the minimum. It is
# such a simple and efficient regularization technique that Geoffrey Hinton called it a
# “beautiful free lunch.”
# 
# 
# 
# 
# Figure 4-20. Early stopping regularization
# 
#                With Stochastic and Mini-batch Gradient Descent, the curves are
#                not so smooth, and it may be hard to know whether you have
#                reached the minimum or not. One solution is to stop only after the
#                validation error has been above the minimum for some time (when
#                you are confident that the model will not do any better), then roll
#                back the model parameters to the point where the validation error
#                was at a minimum.
# 
# Here is a basic implementation of early stopping:
#     from sklearn.base import clone
# 
# 
# 
# 
#                                                                Regularized Linear Models   |   133
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Elastic Net",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Elastic Net"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ElasticNet(HierNode):
    def __init__(self):
        super().__init__("Elastic Net")
        self.add(Content())

# eof
