# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Chapter1.index import Chapter1 as A_Chapter1
from .B_Chapter2.index import Chapter2 as B_Chapter2
from .C_Chapter3.index import Chapter3 as C_Chapter3
from .D_Chapter4.index import Chapter4 as D_Chapter4
from .E_Chapter5.index import Chapter5 as E_Chapter5
from .F_Chapter6.index import Chapter6 as F_Chapter6
from .G_Chapter7.index import Chapter7 as G_Chapter7

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PART I
# 
# Getting Started with
# Google Cloud Platform
# 
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
# 
# 
# 
# 
#                                                                                           3
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_1
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Part I: Getting Started with Google Cloud Platform")
        self.add(MarkdownBlock("# Part I: Getting Started with Google Cloud Platform"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PartI(HierNode):
    def __init__(self):
        super().__init__("Part I: Getting Started with Google Cloud Platform")
        self.add(Content())
        self.add(A_Chapter1())
        self.add(B_Chapter2())
        self.add(C_Chapter3())
        self.add(D_Chapter4())
        self.add(E_Chapter5())
        self.add(F_Chapter6())
        self.add(G_Chapter7())

# eof
