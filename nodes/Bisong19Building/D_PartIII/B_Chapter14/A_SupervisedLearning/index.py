# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Regressionvs.index import Regressionvs as A_Regressionvs
from .B_HowDo.index import HowDo as B_HowDo
from .C_TrainingTest.index import TrainingTest as C_TrainingTest
from .D_Biasvs.index import Biasvs as D_Biasvs
from .E_EvaluatingModel.index import EvaluatingModel as E_EvaluatingModel
from .F_ResamplingTechniques.index import ResamplingTechniques as F_ResamplingTechniques
from .G_ImprovingModel.index import ImprovingModel as G_ImprovingModel

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Supervised Learning
# To easily understand the concept of supervised learning, let’s revisit the problem of
# identifying spam emails from a set of emails. We will use this example to understand
# key concepts that are central to the definition and the framing of a supervised learning
# problem, and they are
# 
#        •    Features
# 
#        •    Samples
# 
#        •    Targets
# 
#      For this contrived example, let’s assume that we have a dictionary of the top 4 words
# in the set of emails and we record the frequency of occurrence for each email sample.
# This information is represented in a tabular format, where each feature is a column and
# the rows are email samples. This tabular representation is called a dataset. Figure 14-1
# illustrates this depiction.
# 
# 
# 
# 
# Figure 14-1. Dataset representation
# 
#      The fundamental concept behind supervised machine learning is that each sample
# is associated with a target variable, and the goal is to teach the computer to learn the
# patterns from the dataset features that results in a target as a prediction outcome. The
# columns of a dataset in machine learning are referred to as features; other names you
# may find commonly used are variables or attributes of the dataset, but in this book, we
# will use the term features to describe the measurement units of a data sample. Moreover,
# the samples of a dataset are also referred to as rows, data points, or observations, but we
# will use the term samples throughout this book.
#      Hence, in supervised learning, a set of features are used to build a learning model
# that will predict the outcome of a target variable as shown in Figure 14-1.
#      Next, we will cover important modeling considerations for building supervised
# learning models.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Supervised Learning",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Supervised Learning"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class SupervisedLearning(HierNode):
    def __init__(self):
        super().__init__("Supervised Learning")
        self.add(Content())
        self.add(A_Regressionvs())
        self.add(B_HowDo())
        self.add(C_TrainingTest())
        self.add(D_Biasvs())
        self.add(E_EvaluatingModel())
        self.add(F_ResamplingTechniques())
        self.add(G_ImprovingModel())

# eof
