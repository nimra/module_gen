# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Introduction.index import Introduction as A_Introduction
from .B_PartI.index import PartI as B_PartI
from .C_PartII.index import PartII as C_PartII
from .D_PartIII.index import PartIII as D_PartIII
from .E_PartIV.index import PartIV as E_PartIV
from .F_PartV.index import PartV as F_PartV
from .G_PartVI.index import PartVI as G_PartVI
from .H_PartVII.index import PartVII as H_PartVII
from .I_PartVIII.index import PartVIII as I_PartVIII
# from .J_Index.index import Index as J_Index

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Introduction
# Machine learning and deep learning technologies have impacted the world in profound
# ways, from how we interact with technological products and with one another. These
# technologies are disrupting how we relate, how we work, and how we engage life in
# general. Today, and in the foreseeable future, intelligent machines increasingly form
# the core upon which sociocultural and socioeconomic relationships rest. We are indeed
# already in the "age of intelligence."
# 
# 
# 
# What Are Machine Learning and Deep Learning?
# Machine learning can be described as an assortment of tools and techniques for
# predicting or classifying a future event based on a set of interactions between variables
# (also referred to as features or attributes) in a particular dataset. Deep learning, on the
# other hand, extends a machine learning algorithm called neural network for learning
# complex tasks which are incredibly difficult for a computer to perform. Examples of
# these tasks may include recognizing faces and understanding languages in their varied
# contextual meanings.
# 
# 
# 
# The Role of Big Data
# A key ingredient that is critical to the rise and future improved performance of
# machine learning and deep learning is data. Since the turn of the twenty-first century,
# there has been a steady exponential increase in the amount of data generated and
# stored. The rise of humongous data is partly due to the emergence of the Internet and
# the miniaturization of processors that have spurned the "Internet of Things (IoT)"
# technologies. These vast amounts of data have made it possible to train the computer to
# learn complex tasks where an explicit instruction set is infeasible.
# 
# 
# 
# 
#                                                                                         xxvii
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Nimra Curriculum")
        self.add(MarkdownBlock("# Nimra Curriculum"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class NimraCurriculum(HierNode):
    def __init__(self):
        super().__init__("Nimra Curriculum")
        self.add(Content())
        self.add(A_Introduction())
        self.add(B_PartI())
        self.add(C_PartII())
        self.add(D_PartIII())
        self.add(E_PartIV())
        self.add(F_PartV())
        self.add(G_PartVI())
        self.add(H_PartVII())
        self.add(I_PartVIII())
        # self.add(J_Index())

# eof
