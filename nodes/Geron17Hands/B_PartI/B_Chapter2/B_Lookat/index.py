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

from .A_Framethe.index import Framethe as A_Framethe
from .B_Selecta.index import Selecta as B_Selecta
from .C_Checkthe.index import Checkthe as C_Checkthe

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                       Download from finelybook www.finelybook.com
# Look at the Big Picture
# Welcome to Machine Learning Housing Corporation! The first task you are asked to
# perform is to build a model of housing prices in California using the California cen‐
# sus data. This data has metrics such as the population, median income, median hous‐
# ing price, and so on for each block group in California. Block groups are the smallest
# geographical unit for which the US Census Bureau publishes sample data (a block
# group typically has a population of 600 to 3,000 people). We will just call them “dis‐
# tricts” for short.
# Your model should learn from this data and be able to predict the median housing
# price in any district, given all the other metrics.
# 
#                     Since you are a well-organized data scientist, the first thing you do
#                     is to pull out your Machine Learning project checklist. You can
#                     start with the one in Appendix B; it should work reasonably well
#                     for most Machine Learning projects but make sure to adapt it to
#                     your needs. In this chapter we will go through many checklist
#                     items, but we will also skip a few, either because they are self-
#                     explanatory or because they will be discussed in later chapters.
# 
# 
# Frame the Problem
# The first question to ask your boss is what exactly is the business objective; building a
# model is probably not the end goal. How does the company expect to use and benefit
# from this model? This is important because it will determine how you frame the
# problem, what algorithms you will select, what performance measure you will use to
# evaluate your model, and how much effort you should spend tweaking it.
# Your boss answers that your model’s output (a prediction of a district’s median hous‐
# ing price) will be fed to another Machine Learning system (see Figure 2-2), along
# with many other signals.3 This downstream system will determine whether it is worth
# investing in a given area or not. Getting this right is critical, as it directly affects reve‐
# nue.
# 
# 
# 
# 
# 3 A piece of information fed to a Machine Learning system is often called a signal in reference to Shannon’s
#   information theory: you want a high signal/noise ratio.
# 
# 
# 
#                                                                                    Look at the Big Picture   |   35
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Look at the Big Picture",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Lookat(HierNode):
    def __init__(self):
        super().__init__("Look at the Big Picture")
        self.add(Content(), "content")
        self.add(A_Framethe())
        self.add(B_Selecta())
        self.add(C_Checkthe())

# eof
