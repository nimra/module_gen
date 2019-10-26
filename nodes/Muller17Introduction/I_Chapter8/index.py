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

from .A_Approachinga.index import Approachinga as A_Approachinga
from .B_FromPrototype.index import FromPrototype as B_FromPrototype
from .C_TestingProduction.index import TestingProduction as C_TestingProduction
from .D_BuildingYour.index import BuildingYour as D_BuildingYour
from .E_Whereto.index import Whereto as E_Whereto
from .F_Conclusion.index import Conclusion as F_Conclusion

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                                                                         CHAPTER 8
#                                                             Wrapping Up
# 
# 
# 
# 
# You now know how to apply the important machine learning algorithms for super‐
# vised and unsupervised learning, which allow you to solve a wide variety of machine
# learning problems. Before we leave you to explore all the possibilities that machine
# learning offers, we want to give you some final words of advice, point you toward
# some additional resources, and give you suggestions on how you can further improve
# your machine learning and data science skills.
# 
# Approaching a Machine Learning Problem
# With all the great methods that we introduced in this book now at your fingertips, it
# may be tempting to jump in and start solving your data-related problem by just run‐
# ning your favorite algorithm. However, this is not usually a good way to begin your
# analysis. The machine learning algorithm is usually only a small part of a larger data
# analysis and decision-making process. To make effective use of machine learning, we
# need to take a step back and consider the problem at large. First, you should think
# about what kind of question you want to answer. Do you want to do exploratory anal‐
# ysis and just see if you find something interesting in the data? Or do you already have
# a particular goal in mind? Often you will start with a goal, like detecting fraudulent
# user transactions, making movie recommendations, or finding unknown planets. If
# you have such a goal, before building a system to achieve it, you should first think
# about how to define and measure success, and what the impact of a successful solu‐
# tion would be to your overall business or research goals. Let’s say your goal is fraud
# detection.
# 
# 
# 
# 
#                                                                                     357
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 8. Wrapping Up",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter8(HierNode):
    def __init__(self):
        super().__init__("Chapter 8. Wrapping Up")
        self.add(Content(), "content")
        self.add(A_Approachinga())
        self.add(B_FromPrototype())
        self.add(C_TestingProduction())
        self.add(D_BuildingYour())
        self.add(E_Whereto())
        self.add(F_Conclusion())

# eof
