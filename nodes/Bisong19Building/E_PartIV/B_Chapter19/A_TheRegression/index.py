# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_AVisual.index import AVisual as A_AVisual
from .B_Findingthe.index import Findingthe as B_Findingthe

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
    mbk("In linear regression, the prevailing assumption is that the target variable (i.e., the unit that we want to predict) can be modeled as a linear combination of the features."),
    mbk("A linear combination is simply the addition of a certain number of vectors that are scaled (or adjusted) by some arbitrary constant. A vector is a mathematical construct for representing a set of numbers."),
    mbk("For example, let us assume a randomly generated dataset consisting of two features and a target variable. The dataset has 50 observations (see Figure 19-1)."),
    ibk("Figure 19-1. Sample dataset"),
    mbk("The vectors of this dataset are"),
    mbk("$$x_1 = \\begin{bmatrix} 40 & 31 & 81 & 57 & ... & 66 \\end{bmatrix}$$"),
    mbk("$$x_2 = \\begin{bmatrix} 73 & 59 & 18 & 69 & ... & 20 \\end{bmatrix}$$"),
    mbk("$$y = \\begin{bmatrix} 105 & 145 & 128 & 116 & ... & 144 \\end{bmatrix}$$"),
    mbk("In a linear regression model, every feature has an assigned “weight.” We can say that the weight parameterizes each feature in the dataset. The weights in the dataset are adjusted to take on values that capture the underlying relationship between the features that optimally approximate the target variable. The linear regression model is formally written as"),
    mbk("$$\\hat{y} = \\theta_0 + \\theta_1 x_1 + \\theta_2 x_2 + ... + \\theta_n x_n$$"),
    mbk("""
where

- $\\hat{y}$ (pronounced y-hat) is the approximate value of the output y that we want to predict.
- $\\theta_i$, where $i = \\{1, 2, ..., n\\}$, is the weight assigned to each feature in the dataset. The notation $n$ is the size of features of the dataset.
- $\\theta_0$ represents the “bias” term.
    """),
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "The Regression Model",
            Stage.REMOVE_EXTRANEOUS,
            Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# The Regression Model"))
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TheRegression(HierNode):
    def __init__(self):
        super().__init__("The Regression Model")
        self.add(Content())
        self.add(A_AVisual())
        self.add(B_Findingthe())

# eof
