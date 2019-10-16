# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Dataand.index import Dataand as A_Dataand
from .B_DataTypes.index import DataTypes as B_DataTypes
from .C_Arithmeticand.index import Arithmeticand as C_Arithmeticand
from .D_Theprint.index import Theprint as D_Theprint
from .E_ControlStructures.index import ControlStructures as E_ControlStructures
from .F_Functions.index import Functions as F_Functions
from .G_Packagesand.index import Packagesand as G_Packagesand

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 9
# 
# 
# 
# Python
# Python is one of the preferred languages for data science in the industry primarily
# because of its simple syntax and the number of reusable machine learning/deep
# learning packages. These packages make it easy to develop data science products
# without getting bogged down with the internals of a particular algorithm or method.
# They have been written, debugged, and tested by the best experts in the field, as well as
# by a large supporting community of developers that contribute their time and expertise
# to maintain and improve them.
#     In this section, we will go through the foundations of programming with Python 3.
# This section forms a framework for working with higher-level packages such as NumPy,
# Pandas, Matplotlib, TensorFlow, and Keras. The programming paradigm we will cover
# in this chapter can be easily adapted or applied to similar languages, such as R, which is
# also commonly used in the data science industry.
#     The best way to work through this chapter and the successive chapters in this part is to
# work through the code by executing them on Google Colab or GCP Deep Learning VMs.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 9: Python",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Chapter 9: Python"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter9(HierNode):
    def __init__(self):
        super().__init__("Chapter 9: Python")
        self.add(Content())
        self.add(A_Dataand())
        self.add(B_DataTypes())
        self.add(C_Arithmeticand())
        self.add(D_Theprint())
        self.add(E_ControlStructures())
        self.add(F_Functions())
        self.add(G_Packagesand())

# eof
