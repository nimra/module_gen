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
    "We will start with the most familiar linear regression, a straight-line fit to data. A straight-line fit is a model of the form y = ax + b where a is commonly known as the slope, and b is commonly known as the intercept.",
    "Consider the following data, which is scattered about a line with a slope of 2 and an intercept of –5 (Figure 5-42):",
    cbk(None, """
rng = np.random.RandomState(1)
x = 10 * rng.rand(50)
y = 2 * x - 5 + rng.randn(50)
plt.scatter(x, y);
    """, None),
    ibk(None, "Figure 5-42. Data for linear regression"),
    "We can use Scikit-Learn’s LinearRegression estimator to fit this data and construct the best-fit line (Figure 5-43):",
    cbk(None, """
from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=True)

model.fit(x[:, np.newaxis], y)

xfit = np.linspace(0, 10, 1000)
yfit = model.predict(xfit[:, np.newaxis])

plt.scatter(x, y)
plt.plot(xfit, yfit);
    """, None),
    ibk(None, "Figure 5-43. A linear regression model"),
    "The slope and intercept of the data are contained in the model’s fit parameters, which in Scikit-Learn are always marked by a trailing underscore. Here the relevant parameters are coef_ and intercept_:",
    cbk(None, """
print("Model slope:    ", model.coef_[0])
print("Model intercept:", model.intercept_)
    """, """
Model slope:     2.02720881036
Model intercept: -4.99857708555
    """),
    "We see that the results are very close to the inputs, as we might hope.",
    "The LinearRegression estimator is much more capable than this, however—in addition to simple straight-line fits, it can also handle multidimensional linear models of the form:",
    "$$ y = a_0 + a_1 x_1 + a_2 x_2 + \\cdots $$",
    "where there are multiple x values. Geometrically, this is akin to fitting a plane to points in three dimensions, or fitting a hyper-plane to points in higher dimensions.",
    "The multidimensional nature of such regressions makes them more difficult to visualize, but we can see one of these fits in action by building some example data, using NumPy’s matrix multiplication operator:",
    cbk(None, """
rng = np.random.RandomState(1)
X = 10 * rng.rand(100, 3)
y = 0.5 + np.dot(X, [1.5, -2., 1.])

model.fit(X, y)
print(model.intercept_)
print(model.coef_)
    """, """
0.5
[ 1.5 -2.       1. ]
    """),
    "Here the y data is constructed from three random x values, and the linear regression recovers the coefficients used to construct the data.",
    "In this way, we can use the single LinearRegression estimator to fit lines, planes, or hyperplanes to our data. It still appears that this approach would be limited to strictly linear relationships between variables, but it turns out we can relax this as well.",
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Simple Linear Regression",
            Stage.REMOVE_EXTRANEOUS,
            Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class SimpleLinear(HierNode):
    def __init__(self):
        super().__init__("Simple Linear Regression")
        self.add(Content(), "content")

# eof
