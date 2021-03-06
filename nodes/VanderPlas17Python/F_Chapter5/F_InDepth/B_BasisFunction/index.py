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
    "One trick you can use to adapt linear regression to nonlinear relationships between variables is to transform the data according to basis functions. We have seen one version of this before, in the PolynomialRegression pipeline used in “Hyperparameters and Model Validation” on page 359 and “Feature Engineering” on page 375. The idea is to take our multidimensional linear model:",
    "$$ y = a_0 + a_1 x_1 + a_2 x_2 + a_3 x_3 + \\cdots $$",
    "and build the x1, x2, x3, and so on from our single-dimensional input x. That is, we let xn = f n x , where f n is some function that transforms our data.",
    "For example, if f n x = xn, our model becomes a polynomial regression:",
    "$$ y = a_0 + a_1 x + a_2 x^2 + a_3 x^3 + \\cdots $$",
    "Notice that this is still a linear model—the linearity refers to the fact that the coefficients an never multiply or divide each other. What we have effectively done is taken our one-dimensional x values and projected them into a higher dimension, so that a linear fit can fit more complicated relationships between x and y.",
    hbk("Polynomial basis functions", [
        "This polynomial projection is useful enough that it is built into Scikit-Learn, using the PolynomialFeatures transformer:",
        cbk(None, """
from sklearn.preprocessing import PolynomialFeatures
x = np.array([2, 3, 4])
poly = PolynomialFeatures(3, include_bias=False)
poly.fit_transform(x[:, None])
        """, """
array([[   2.,    4.,    8.],
       [   3.,    9.,   27.],
       [   4.,   16.,   64.]])
        """),
        "We see here that the transformer has converted our one-dimensional array into a three-dimensional array by taking the exponent of each value. This new, higher-dimensional data representation can then be plugged into a linear regression.",
        "As we saw in “Feature Engineering” on page 375, the cleanest way to accomplish this is to use a pipeline. Let’s make a 7th-degree polynomial model in this way:",
        cbk(None, """
from sklearn.pipeline import make_pipeline
poly_model = make_pipeline(PolynomialFeatures(7),
                           LinearRegression())
        """, None),
        "With this transform in place, we can use the linear model to fit much more complicated relationships between x and y. For example, here is a sine wave with noise (Figure 5-44):",
        cbk(None, """
rng = np.random.RandomState(1)
x = 10 * rng.rand(50)
y = np.sin(x) + 0.1 * rng.randn(50)

poly_model.fit(x[:, np.newaxis], y)
yfit = poly_model.predict(xfit[:, np.newaxis])

plt.scatter(x, y)
plt.plot(xfit, yfit);
        """, None),
        ibk(None, "Figure 5-44. A linear polynomial fit to nonlinear training data"),
        "Our linear model, through the use of 7th-order polynomial basis functions, can provide an excellent fit to this nonlinear data!",
    ]),
    hbk("Gaussian basis functions", [
        "Of course, other basis functions are possible. For example, one useful pattern is to fit a model that is not a sum of polynomial bases, but a sum of Gaussian bases. The result might look something like Figure 5-45.",
        ibk(None, "Figure 5-45. A Gaussian basis function fit to nonlinear data"),
        "The shaded regions in the plot shown in Figure 5-45 are the scaled basis functions, and when added together they reproduce the smooth curve through the data. These Gaussian basis functions are not built into Scikit-Learn, but we can write a custom transformer that will create them, as shown here and illustrated in Figure 5-46 (Scikit-Learn transformers are implemented as Python classes; reading Scikit-Learn’s source is a good way to see how they can be created):",
        cbk(None, """
from sklearn.base import BaseEstimator, TransformerMixin

class GaussianFeatures(BaseEstimator, TransformerMixin):
    \"\"\"Uniformly spaced Gaussian features for one-dimensional input\"\"\"

    def __init__(self, N, width_factor=2.0):
        self.N = N
        self.width_factor = width_factor

    @staticmethod
    def _gauss_basis(x, y, width, axis=None):
        arg = (x - y) / width
        return np.exp(-0.5 * np.sum(arg ** 2, axis))

    def fit(self, X, y=None):
        # create N centers spread along the data range
        self.centers_ = np.linspace(X.min(), X.max(), self.N)
        self.width_ = self.width_factor * (self.centers_[1] - self.centers_[0])
        return self

    def transform(self, X):
        return self._gauss_basis(X[:, :, np.newaxis], self.centers_,
                                 self.width_, axis=1)

gauss_model = make_pipeline(GaussianFeatures(20),
                            LinearRegression())
gauss_model.fit(x[:, np.newaxis], y)
yfit = gauss_model.predict(xfit[:, np.newaxis])

plt.scatter(x, y)
plt.plot(xfit, yfit)
plt.xlim(0, 10);
        """, None),
        ibk(None, "Figure 5-46. A Gaussian basis function fit computed with a custom transformer"),
        "We put this example here just to make clear that there is nothing magic about polynomial basis functions: if you have some sort of intuition into the generating process of your data that makes you think one basis or another might be appropriate, you can use them as well.",
    ]),
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Basis Function Regression",
            Stage.REMOVE_EXTRANEOUS,
            Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class BasisFunction(HierNode):
    def __init__(self):
        super().__init__("Basis Function Regression")
        self.add(Content(), "content")

# eof
