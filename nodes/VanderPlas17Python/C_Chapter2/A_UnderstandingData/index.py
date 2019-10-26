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

from .A_APython.index import APython as A_APython
from .B_APython.index import APython as B_APython
from .C_FixedTypeArrays.index import FixedTypeArrays as C_FixedTypeArrays
from .D_CreatingArrays.index import CreatingArrays as D_CreatingArrays
from .E_CreatingArrays.index import CreatingArrays as E_CreatingArrays
from .F_NumPyStandard.index import NumPyStandard as F_NumPyStandard

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# If you followed the advice outlined in the preface and installed the Anaconda stack,
# you already have NumPy installed and ready to go. If you’re more the do-it-yourself
# type, you can go to the NumPy website and follow the installation instructions found
# there. Once you do, you can import NumPy and double-check the version:
#        In[1]: import numpy
#               numpy.__version__
#        Out[1]: '1.11.1'
# For the pieces of the package discussed here, I’d recommend NumPy version 1.8 or
# later. By convention, you’ll find that most people in the SciPy/PyData world will
# import NumPy using np as an alias:
#        In[2]: import numpy as np
# Throughout this chapter, and indeed the rest of the book, you’ll find that this is the
# way we will import and use NumPy.
# 
# 
#                             Reminder About Built-In Documentation
#      As you read through this chapter, don’t forget that IPython gives you the ability to
#      quickly explore the contents of a package (by using the tab-completion feature) as
#      well as the documentation of various functions (using the ? character). Refer back to
#      “Help and Documentation in IPython” on page 3 if you need a refresher on this.
#      For example, to display all the contents of the numpy namespace, you can type this:
#            In [3]: np.<TAB>
#      And to display NumPy’s built-in documentation, you can use this:
#            In [4]: np?
#      More detailed documentation, along with tutorials and other resources, can be found
#      at http://www.numpy.org.
# 
# 
# 
# Understanding Data Types in Python
# Effective data-driven science and computation requires understanding how data is
# stored and manipulated. This section outlines and contrasts how arrays of data are
# handled in the Python language itself, and how NumPy improves on this. Under‐
# standing this difference is fundamental to understanding much of the material
# throughout the rest of the book.
# Users of Python are often drawn in by its ease of use, one piece of which is dynamic
# typing. While a statically typed language like C or Java requires each variable to be
# 
# 
# 
# 
# 34     |   Chapter 2: Introduction to NumPy
# 
# explicitly declared, a dynamically typed language like Python skips this specification.
# For example, in C you might specify a particular operation as follows:
#     /* C code */
#     int result = 0;
#     for(int i=0; i<100; i++){
#         result += i;
#     }
# While in Python the equivalent operation could be written this way:
#     # Python code
#     result = 0
#     for i in range(100):
#         result += i
# Notice the main difference: in C, the data types of each variable are explicitly
# declared, while in Python the types are dynamically inferred. This means, for exam‐
# ple, that we can assign any kind of data to any variable:
#     # Python code
#     x = 4
#     x = "four"
# 
# Here we’ve switched the contents of x from an integer to a string. The same thing in C
# would lead (depending on compiler settings) to a compilation error or other uninten‐
# ded consequences:
#     /* C code */
#     int x = 4;
#     x = "four"; // FAILS
# This sort of flexibility is one piece that makes Python and other dynamically typed
# languages convenient and easy to use. Understanding how this works is an important
# piece of learning to analyze data efficiently and effectively with Python. But what this
# type flexibility also points to is the fact that Python variables are more than just their
# value; they also contain extra information about the type of the value. We’ll explore
# this more in the sections that follow.
# 
# A Python Integer Is More Than Just an Integer
# The standard Python implementation is written in C. This means that every Python
# object is simply a cleverly disguised C structure, which contains not only its value, but
# other information as well. For example, when we define an integer in Python, such as
# x = 10000, x is not just a “raw” integer. It’s actually a pointer to a compound C struc‐
# ture, which contains several values. Looking through the Python 3.4 source code, we
# find that the integer (long) type definition effectively looks like this (once the C mac‐
# ros are expanded):
# 
# 
# 
# 
#                                                         Understanding Data Types in Python   |   35
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Understanding Data Types in Python",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class UnderstandingData(HierNode):
    def __init__(self):
        super().__init__("Understanding Data Types in Python")
        self.add(Content())
        self.add(A_APython())
        self.add(B_APython())
        self.add(C_FixedTypeArrays())
        self.add(D_CreatingArrays())
        self.add(E_CreatingArrays())
        self.add(F_NumPyStandard())

# eof
