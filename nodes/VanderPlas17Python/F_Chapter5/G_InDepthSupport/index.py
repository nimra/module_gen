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

from .A_MotivatingSupport.index import MotivatingSupport as A_MotivatingSupport
from .B_SupportVector.index import SupportVector as B_SupportVector
from .C_ExampleFace.index import ExampleFace as C_ExampleFace
from .D_SupportVector.index import SupportVector as D_SupportVector

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# additional hour of daylight, 129 ± 9 more people choose to ride; a temperature
# increase of one degree Celsius encourages 65 ± 4 people to grab their bicycle; a dry
# day means an average of 546 ± 33 more riders; and each inch of precipitation means
# 665 ± 62 more people leave their bike at home. Once all these effects are accounted
# for, we see a modest increase of 28 ± 18 new daily riders each year.
# Our model is almost certainly missing some relevant information. For example, non‐
# linear effects (such as effects of precipitation and cold temperature) and nonlinear
# trends within each variable (such as disinclination to ride at very cold and very hot
# temperatures) cannot be accounted for in this model. Additionally, we have thrown
# away some of the finer-grained information (such as the difference between a rainy
# morning and a rainy afternoon), and we have ignored correlations between days
# (such as the possible effect of a rainy Tuesday on Wednesday’s numbers, or the effect
# of an unexpected sunny day after a streak of rainy days). These are all potentially
# interesting effects, and you now have the tools to begin exploring them if you wish!
# 
# In-Depth: Support Vector Machines
# Support vector machines (SVMs) are a particularly powerful and flexible class of
# supervised algorithms for both classification and regression. In this section, we will
# develop the intuition behind support vector machines and their use in classification
# problems. We begin with the standard imports:
#     In[1]: %matplotlib inline
#            import numpy as np
#            import matplotlib.pyplot as plt
#            from scipy import stats
# 
#            # use Seaborn plotting defaults
#            import seaborn as sns; sns.set()
# 
# 
# Motivating Support Vector Machines
# As part of our discussion of Bayesian classification (see “In Depth: Naive Bayes Clas‐
# sification” on page 382), we learned a simple model describing the distribution of
# each underlying class, and used these generative models to probabilistically deter‐
# mine labels for new points. That was an example of generative classification; here we
# will consider instead discriminative classification: rather than modeling each class, we
# simply find a line or curve (in two dimensions) or manifold (in multiple dimensions)
# that divides the classes from each other.
# As an example of this, consider the simple case of a classification task, in which the
# two classes of points are well separated (Figure 5-53):
# 
# 
# 
# 
#                                                        In-Depth: Support Vector Machines   |   405
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "In-Depth: Support Vector Machines",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class InDepthSupport(HierNode):
    def __init__(self):
        super().__init__("In-Depth: Support Vector Machines")
        self.add(Content())
        self.add(A_MotivatingSupport())
        self.add(B_SupportVector())
        self.add(C_ExampleFace())
        self.add(D_SupportVector())

# eof
