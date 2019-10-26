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
# Algorithm        Large m Out-of-core support Large n Hyperparams Scaling required Scikit-Learn
# Stochastic GD    Fast    Yes                 Fast    ≥2          Yes              SGDRegressor
# Mini-batch GD    Fast      Yes                  Fast      ≥2    Yes             n/a
# 
# 
#                     There is almost no difference after training: all these algorithms
#                     end up with very similar models and make predictions in exactly
#                     the same way.
# 
# 
# 
# 
# Polynomial Regression
# What if your data is actually more complex than a simple straight line? Surprisingly,
# you can actually use a linear model to fit nonlinear data. A simple way to do this is to
# add powers of each feature as new features, then train a linear model on this extended
# set of features. This technique is called Polynomial Regression.
# Let’s look at an example. First, let’s generate some nonlinear data, based on a simple
# quadratic equation9 (plus some noise; see Figure 4-12):
#      m = 100
#      X = 6 * np.random.rand(m, 1) - 3
#      y = 0.5 * X**2 + X + 2 + np.random.randn(m, 1)
# 
# 
# 
# 
# Figure 4-12. Generated nonlinear and noisy dataset
# 
# 
# 
# 
# 9 A quadratic equation is of the form y = ax2 + bx + c.
# 
# 
# 
#                                                                          Polynomial Regression   |   121
# 
#                    Download from finelybook www.finelybook.com
# Clearly, a straight line will never fit this data properly. So let’s use Scikit-Learn’s Poly
# nomialFeatures class to transform our training data, adding the square (2nd-degree
# polynomial) of each feature in the training set as new features (in this case there is
# just one feature):
#       >>> from sklearn.preprocessing import PolynomialFeatures
#       >>> poly_features = PolynomialFeatures(degree=2, include_bias=False)
#       >>> X_poly = poly_features.fit_transform(X)
#       >>> X[0]
#       array([-0.75275929])
#       >>> X_poly[0]
#       array([-0.75275929, 0.56664654])
# 
# X_poly now contains the original feature of X plus the square of this feature. Now you
# can fit a LinearRegression model to this extended training data (Figure 4-13):
#       >>> lin_reg = LinearRegression()
#       >>> lin_reg.fit(X_poly, y)
#       >>> lin_reg.intercept_, lin_reg.coef_
#       (array([ 1.78134581]), array([[ 0.93366893,    0.56456263]]))
# 
# 
# 
# 
# Figure 4-13. Polynomial Regression model predictions
# 
# Not bad: the model estimates y = 0 . 56x21 + 0 . 93x1 + 1 . 78 when in fact the original
# function was y = 0 . 5x21 + 1 . 0x1 + 2 . 0 + Gaussian noise.
# Note that when there are multiple features, Polynomial Regression is capable of find‐
# ing relationships between features (which is something a plain Linear Regression
# model cannot do). This is made possible by the fact that PolynomialFeatures also
# adds all combinations of features up to the given degree. For example, if there were
# 
# 
# 
# 122   |   Chapter 4: Training Models
# 
#                     Download from finelybook www.finelybook.com
# two features a and b, PolynomialFeatures with degree=3 would not only add the
# features a2, a3, b2, and b3, but also the combinations ab, a2b, and ab2.
# 
#                PolynomialFeatures(degree=d) transforms an array containing n
#                                                      n+d !
#                features into an array containing            features, where n! is the
#                                                      d! n!
#                factorial of n, equal to 1 × 2 × 3 × ⋯ × n. Beware of the combinato‐
#                rial explosion of the number of features!
# 
# 
# Learning Curves
# If you perform high-degree Polynomial Regression, you will likely fit the training
# data much better than with plain Linear Regression. For example, Figure 4-14 applies
# a 300-degree polynomial model to the preceding training data, and compares the
# result with a pure linear model and a quadratic model (2nd-degree polynomial).
# Notice how the 300-degree polynomial model wiggles around to get as close as possi‐
# ble to the training instances.
# 
# 
# 
# 
# Figure 4-14. High-degree Polynomial Regression
# 
# Of course, this high-degree Polynomial Regression model is severely overfitting the
# training data, while the linear model is underfitting it. The model that will generalize
# best in this case is the quadratic model. It makes sense since the data was generated
# using a quadratic model, but in general you won’t know what function generated the
# data, so how can you decide how complex your model should be? How can you tell
# that your model is overfitting or underfitting the data?
# 
# 
# 
#                                                                          Learning Curves   |   123
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Polynomial Regression",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PolynomialRegression(HierNode):
    def __init__(self):
        super().__init__("Polynomial Regression")
        self.add(Content(), "content")

# eof
