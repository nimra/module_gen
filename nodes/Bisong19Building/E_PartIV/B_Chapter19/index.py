# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_TheRegression.index import TheRegression as A_TheRegression
from .B_HowDo.index import HowDo as B_HowDo
from .C_LinearRegression.index import LinearRegression as C_LinearRegression
from .D_Adaptingto.index import Adaptingto as D_Adaptingto
from .E_HigherOrderLinear.index import HigherOrderLinear as E_HigherOrderLinear
from .F_Improvingthe.index import Improvingthe as F_Improvingthe

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
    mbk("The fundamental idea behind the linear regression algorithm is that it assumes a linear relationship between the features of the dataset. As a result of the pre-defined structure that is imposed on the parameters of the model, it is also called a parametric learning algorithm. Linear regression is used to predict targets that contain real values. As we will see later in Chapter 20 on logistic regression, the linear regression model is not adequate to deal with learning problems whose targets are categorical."),
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 19: Linear Regression",
            Stage.REMOVE_EXTRANEOUS,
            Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Chapter 19: Linear Regression"))
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter19(HierNode):
    def __init__(self):
        super().__init__("Chapter 19: Linear Regression")
        self.add(Content())
        self.add(A_TheRegression())
        self.add(B_HowDo())
        self.add(C_LinearRegression())
        self.add(D_Adaptingto())
        self.add(E_HigherOrderLinear())
        self.add(F_Improvingthe())

# eof
