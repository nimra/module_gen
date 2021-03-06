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


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# Python 2 Versus Python 3
# There are two major versions of Python that are widely used at the moment: Python 2
# (more precisely, 2.7) and Python 3 (with the latest release being 3.5 at the time of
# writing). This sometimes leads to some confusion. Python 2 is no longer actively
# developed, but because Python 3 contains major changes, Python 2 code usually does
# not run on Python 3. If you are new to Python, or are starting a new project from
# scratch, we highly recommend using the latest version of Python 3 without changes.
# If you have a large codebase that you rely on that is written for Python 2, you are
# excused from upgrading for now. However, you should try to migrate to Python 3 as
# soon as possible. When writing any new code, it is for the most part quite easy to
# write code that runs under Python 2 and Python 3. 2 If you don’t have to interface with
# legacy software, you should definitely use Python 3. All the code in this book is writ‐
# ten in a way that works for both versions. However, the exact output might differ
# slightly under Python 2.
# 
# Versions Used in this Book
# We are using the following versions of the previously mentioned libraries in this
# book:
# In[9]:
#      import sys
#      print("Python version: {}".format(sys.version))
# 
#      import pandas as pd
#      print("pandas version: {}".format(pd.__version__))
# 
#      import matplotlib
#      print("matplotlib version: {}".format(matplotlib.__version__))
# 
#      import numpy as np
#      print("NumPy version: {}".format(np.__version__))
# 
#      import scipy as sp
#      print("SciPy version: {}".format(sp.__version__))
# 
#      import IPython
#      print("IPython version: {}".format(IPython.__version__))
# 
#      import sklearn
#      print("scikit-learn version: {}".format(sklearn.__version__))
# 
# 
# 
# 
# 2 The six package can be very handy for that.
# 
# 
# 
# 12   |   Chapter 1: Introduction
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Python 2 Versus Python 3",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Python2(HierNode):
    def __init__(self):
        super().__init__("Python 2 Versus Python 3")
        self.add(Content(), "content")

# eof
