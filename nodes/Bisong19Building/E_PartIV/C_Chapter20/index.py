# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_WhyLogistic.index import WhyLogistic as A_WhyLogistic
from .B_Introducingthe.index import Introducingthe as B_Introducingthe
from .C_Trainingthe.index import Trainingthe as C_Trainingthe
from .D_MulticlassClassificationMultinomial.index import MulticlassClassificationMultinomial as D_MulticlassClassificationMultinomial
from .E_LogisticRegression.index import LogisticRegression as E_LogisticRegression
from .F_Optimizingthe.index import Optimizingthe as F_Optimizingthe

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
    mbk("Logistic regression is a supervised machine learning algorithm developed for learning classification problems. A classification learning problem is when the target variable is categorical. The goal of logistic regression is to map a function from the features of the dataset to the targets to predict the probability that a new example belongs to one of the target classes. Figure 20-1 is an example of a dataset with categorical targets."),
    ibk("Figure 20-1. Dataset with qualitative variables as output"),
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 20: Logistic Regression",
            Stage.REMOVE_EXTRANEOUS,
            Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Chapter 20: Logistic Regression"))
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter20(HierNode):
    def __init__(self):
        super().__init__("Chapter 20: Logistic Regression")
        self.add(Content())
        self.add(A_WhyLogistic())
        self.add(B_Introducingthe())
        self.add(C_Trainingthe())
        self.add(D_MulticlassClassificationMultinomial())
        self.add(E_LogisticRegression())
        self.add(F_Optimizingthe())

# eof
