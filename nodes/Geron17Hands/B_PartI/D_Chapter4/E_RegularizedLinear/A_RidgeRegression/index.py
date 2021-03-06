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
#                   Download from finelybook www.finelybook.com
# up very close to zero and the result is a flat line going through the data’s mean. Equa‐
# tion 4-8 presents the Ridge Regression cost function.11
# 
#       Equation 4-8. Ridge Regression cost function
# 
#                               1 n 2
#                               2i∑
#       J θ = MSE θ + α              θi
#                                 =1
# 
# 
# Note that the bias term θ0 is not regularized (the sum starts at i = 1, not 0). If we
# define w as the vector of feature weights (θ1 to θn), then the regularization term is
# simply equal to ½(∥ w ∥2)2, where ∥ · ∥2 represents the ℓ2 norm of the weight vector.12
# For Gradient Descent, just add αw to the MSE gradient vector (Equation 4-6).
# 
#                       It is important to scale the data (e.g., using a StandardScaler)
#                       before performing Ridge Regression, as it is sensitive to the scale of
#                       the input features. This is true of most regularized models.
# 
# 
# 
# Figure 4-17 shows several Ridge models trained on some linear data using different α
# value. On the left, plain Ridge models are used, leading to linear predictions. On the
# right, the data is first expanded using PolynomialFeatures(degree=10), then it is
# scaled using a StandardScaler, and finally the Ridge models are applied to the result‐
# ing features: this is Polynomial Regression with Ridge regularization. Note how
# increasing α leads to flatter (i.e., less extreme, more reasonable) predictions; this
# reduces the model’s variance but increases its bias.
# As with Linear Regression, we can perform Ridge Regression either by computing a
# closed-form equation or by performing Gradient Descent. The pros and cons are the
# same. Equation 4-9 shows the closed-form solution (where A is the n × n identity
# matrix13 except with a 0 in the top-left cell, corresponding to the bias term).
# 
# 
# 
# 
# 11 It is common to use the notation J(θ) for cost functions that don’t have a short name; we will often use this
#    notation throughout the rest of this book. The context will make it clear which cost function is being dis‐
#    cussed.
# 12 Norms are discussed in Chapter 2.
# 13 A square matrix full of 0s except for 1s on the main diagonal (top-left to bottom-right).
# 
# 
# 
# 128    |   Chapter 4: Training Models
# 
#                        Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 4-17. Ridge Regression
# 
#      Equation 4-9. Ridge Regression closed-form solution
#               T             −1     T
#      θ = � · � + α�              ·� ·�
# 
# Here is how to perform Ridge Regression with Scikit-Learn using a closed-form solu‐
# tion (a variant of Equation 4-9 using a matrix factorization technique by André-Louis
# Cholesky):
#       >>> from sklearn.linear_model import Ridge
#       >>> ridge_reg = Ridge(alpha=1, solver="cholesky")
#       >>> ridge_reg.fit(X, y)
#       >>> ridge_reg.predict([[1.5]])
#       array([[ 1.55071465]])
# And using Stochastic Gradient Descent:14
#       >>> sgd_reg = SGDRegressor(penalty="l2")
#       >>> sgd_reg.fit(X, y.ravel())
#       >>> sgd_reg.predict([[1.5]])
#       array([[ 1.13500145]])
# 
# The penalty hyperparameter sets the type of regularization term to use. Specifying
# "l2" indicates that you want SGD to add a regularization term to the cost function
# equal to half the square of the ℓ2 norm of the weight vector: this is simply Ridge
# Regression.
# 
# 
# 14 Alternatively you can use the Ridge class with the "sag" solver. Stochastic Average GD is a variant of SGD.
#    For more details, see the presentation “Minimizing Finite Sums with the Stochastic Average Gradient Algo‐
#    rithm” by Mark Schmidt et al. from the University of British Columbia.
# 
# 
# 
#                                                                                Regularized Linear Models   |     129
# 
#                         Download from finelybook www.finelybook.com
# Lasso Regression
# Least Absolute Shrinkage and Selection Operator Regression (simply called Lasso
# Regression) is another regularized version of Linear Regression: just like Ridge
# Regression, it adds a regularization term to the cost function, but it uses the ℓ1 norm
# of the weight vector instead of half the square of the ℓ2 norm (see Equation 4-10).
# 
#       Equation 4-10. Lasso Regression cost function
#                                n
#       J θ = MSE θ + α          ∑ θi
#                               i=1
# 
# 
# Figure 4-18 shows the same thing as Figure 4-17 but replaces Ridge models with
# Lasso models and uses smaller α values.
# 
# 
# 
# 
# Figure 4-18. Lasso Regression
# 
# An important characteristic of Lasso Regression is that it tends to completely elimi‐
# nate the weights of the least important features (i.e., set them to zero). For example,
# the dashed line in the right plot on Figure 4-18 (with α = 10-7) looks quadratic, almost
# linear: all the weights for the high-degree polynomial features are equal to zero. In
# other words, Lasso Regression automatically performs feature selection and outputs a
# sparse model (i.e., with few nonzero feature weights).
# You can get a sense of why this is the case by looking at Figure 4-19: on the top-left
# plot, the background contours (ellipses) represent an unregularized MSE cost func‐
# tion (α = 0), and the white circles show the Batch Gradient Descent path with that
# cost function. The foreground contours (diamonds) represent the ℓ1 penalty, and the
# triangles show the BGD path for this penalty only (α → ∞). Notice how the path first
# 
# 
# 130    |   Chapter 4: Training Models
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Ridge Regression",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class RidgeRegression(HierNode):
    def __init__(self):
        super().__init__("Ridge Regression")
        self.add(Content(), "content")

# eof
