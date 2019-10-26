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

from .A_VisualizingGeographical.index import VisualizingGeographical as A_VisualizingGeographical
from .B_Lookingfor.index import Lookingfor as B_Lookingfor
from .C_Experimentingwith.index import Experimentingwith as C_Experimentingwith

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#               Download from finelybook www.finelybook.com
# Now you should remove the income_cat attribute so the data is back to its original
# state:
#     for set in (strat_train_set, strat_test_set):
#         set.drop(["income_cat"], axis=1, inplace=True)
# We spent quite a bit of time on test set generation for a good reason: this is an often
# neglected but critical part of a Machine Learning project. Moreover, many of these
# ideas will be useful later when we discuss cross-validation. Now it’s time to move on
# to the next stage: exploring the data.
# 
# Discover and Visualize the Data to Gain Insights
# So far you have only taken a quick glance at the data to get a general understanding of
# the kind of data you are manipulating. Now the goal is to go a little bit more in depth.
# First, make sure you have put the test set aside and you are only exploring the train‐
# ing set. Also, if the training set is very large, you may want to sample an exploration
# set, to make manipulations easy and fast. In our case, the set is quite small so you can
# just work directly on the full set. Let’s create a copy so you can play with it without
# harming the training set:
#     housing = strat_train_set.copy()
# 
# 
# Visualizing Geographical Data
# Since there is geographical information (latitude and longitude), it is a good idea to
# create a scatterplot of all districts to visualize the data (Figure 2-11):
#     housing.plot(kind="scatter", x="longitude", y="latitude")
# 
# 
# 
# 
# Figure 2-11. A geographical scatterplot of the data
# 
# 
#                                                 Discover and Visualize the Data to Gain Insights   |   53
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Discover and Visualize the Data to Gain Insights",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Discoverand(HierNode):
    def __init__(self):
        super().__init__("Discover and Visualize the Data to Gain Insights")
        self.add(Content(), "content")
        self.add(A_VisualizingGeographical())
        self.add(B_Lookingfor())
        self.add(C_Experimentingwith())

# eof
