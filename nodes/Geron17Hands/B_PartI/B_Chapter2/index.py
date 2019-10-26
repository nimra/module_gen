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

from .A_Workingwith.index import Workingwith as A_Workingwith
from .B_Lookat.index import Lookat as B_Lookat
from .C_Getthe.index import Getthe as C_Getthe
from .D_Discoverand.index import Discoverand as D_Discoverand
from .E_Preparethe.index import Preparethe as E_Preparethe
from .F_Selectand.index import Selectand as F_Selectand
from .G_FineTuneYour.index import FineTuneYour as G_FineTuneYour
from .H_LaunchMonitor.index import LaunchMonitor as H_LaunchMonitor
from .I_TryIt.index import TryIt as I_TryIt
from .J_Exercises.index import Exercises as J_Exercises

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                        Download from finelybook www.finelybook.com
# 
# 
#                                                                                                 CHAPTER 2
#                 End-to-End Machine Learning Project
# 
# 
# 
# 
# In this chapter, you will go through an example project end to end, pretending to be a
# recently hired data scientist in a real estate company.1 Here are the main steps you will
# go through:
# 
#  1. Look at the big picture.
#  2. Get the data.
#  3. Discover and visualize the data to gain insights.
#  4. Prepare the data for Machine Learning algorithms.
#  5. Select a model and train it.
#  6. Fine-tune your model.
#  7. Present your solution.
#  8. Launch, monitor, and maintain your system.
# 
# 
# Working with Real Data
# When you are learning about Machine Learning it is best to actually experiment with
# real-world data, not just artificial datasets. Fortunately, there are thousands of open
# datasets to choose from, ranging across all sorts of domains. Here are a few places
# you can look to get data:
# 
#   • Popular open data repositories:
# 
# 
# 1 The example project is completely fictitious; the goal is just to illustrate the main steps of a Machine Learning
#   project, not to learn anything about the real estate business.
# 
# 
# 
#                                                                                                                  33
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 2. End-to-End Machine Learning Project",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter2(HierNode):
    def __init__(self):
        super().__init__("Chapter 2. End-to-End Machine Learning Project")
        self.add(Content(), "content")
        self.add(A_Workingwith())
        self.add(B_Lookat())
        self.add(C_Getthe())
        self.add(D_Discoverand())
        self.add(E_Preparethe())
        self.add(F_Selectand())
        self.add(G_FineTuneYour())
        self.add(H_LaunchMonitor())
        self.add(I_TryIt())
        self.add(J_Exercises())

# eof
