# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Categoriesof.index import Categoriesof as A_Categoriesof
from .B_CloudComputing.index import CloudComputing as B_CloudComputing

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 1
# 
# 
# 
# What Is Cloud
# Computing?
# Cloud computing is the practice where computing services such as storage options,
# processing units, and networking capabilities are exposed for consumption by users over
# the Internet (the cloud). These services range from free to pay-as-you-use billing.
#      The central idea behind cloud computing is to make aggregated computational
# power available for large-scale consumption. By doing so, the microeconomics principle
# of economies of scale kicks into effect where cost per unit output is minimized with
# increasing scale of operations.
#      In a cloud computing environment, enterprises or individuals can take advantage
# of the same speed and power of aggregated high-performance computing services and
# only pay for what they use and relinquish these compute resources when they are no
# longer needed.
#      The concept of cloud computing had existed as time-sharing systems from the
# early years of the modern computer where jobs submitted from different users were
# scheduled to execute on a mainframe. The idea of time-sharing machines fizzled away
# at the advent of the PC. Now, with the rise of enterprise data centers managed by big IT
# companies such as Google, Microsoft, Amazon, IBM, and Oracle, the cloud computing
# notion has resurfaced with the added twist of multi-tenancy as opposed to time-sharing.
# This computing model is set to disrupt the way we work and utilize software systems and
# services.
#      In addition to storage, networking, and processing services, cloud computing
# provides offer other product solutions such as databases, artificial intelligence, and data
# analytics capabilities and serverless infrastructures.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 1: What Is Cloud Computing?",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Chapter 1: What Is Cloud Computing?"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter1(HierNode):
    def __init__(self):
        super().__init__("Chapter 1: What Is Cloud Computing?")
        self.add(Content())
        self.add(A_Categoriesof())
        self.add(B_CloudComputing())

# eof
