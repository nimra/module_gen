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

from .A_Installingscikitlearn.index import Installingscikitlearn as A_Installingscikitlearn

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#   • What question(s) am I trying to answer? Do I think the data collected can answer
#     that question?
#   • What is the best way to phrase my question(s) as a machine learning problem?
#   • Have I collected enough data to represent the problem I want to solve?
#   • What features of the data did I extract, and will these enable the right
#     predictions?
#   • How will I measure success in my application?
#   • How will the machine learning solution interact with other parts of my research
#     or business product?
# 
# In a larger context, the algorithms and methods in machine learning are only one
# part of a greater process to solve a particular problem, and it is good to keep the big
# picture in mind at all times. Many people spend a lot of time building complex
# machine learning solutions, only to find out they don’t solve the right problem.
# When going deep into the technical aspects of machine learning (as we will in this
# book), it is easy to lose sight of the ultimate goals. While we will not discuss the ques‐
# tions listed here in detail, we still encourage you to keep in mind all the assumptions
# that you might be making, explicitly or implicitly, when you start building machine
# learning models.
# 
# Why Python?
# Python has become the lingua franca for many data science applications. It combines
# the power of general-purpose programming languages with the ease of use of
# domain-specific scripting languages like MATLAB or R. Python has libraries for data
# loading, visualization, statistics, natural language processing, image processing, and
# more. This vast toolbox provides data scientists with a large array of general- and
# special-purpose functionality. One of the main advantages of using Python is the abil‐
# ity to interact directly with the code, using a terminal or other tools like the Jupyter
# Notebook, which we’ll look at shortly. Machine learning and data analysis are funda‐
# mentally iterative processes, in which the data drives the analysis. It is essential for
# these processes to have tools that allow quick iteration and easy interaction.
# As a general-purpose programming language, Python also allows for the creation of
# complex graphical user interfaces (GUIs) and web services, and for integration into
# existing systems.
# 
# scikit-learn
# scikit-learn is an open source project, meaning that it is free to use and distribute,
# and anyone can easily obtain the source code to see what is going on behind the
# 
#                                                                           Why Python?   |   5
# 
# scenes. The scikit-learn project is constantly being developed and improved, and it
# has a very active user community. It contains a number of state-of-the-art machine
# learning algorithms, as well as comprehensive documentation about each algorithm.
# scikit-learn is a very popular tool, and the most prominent Python library for
# machine learning. It is widely used in industry and academia, and a wealth of tutori‐
# als and code snippets are available online. scikit-learn works well with a number of
# other scientific Python tools, which we will discuss later in this chapter.
# While reading this, we recommend that you also browse the scikit-learn user guide
# and API documentation for additional details on and many more options for each
# algorithm. The online documentation is very thorough, and this book will provide
# you with all the prerequisites in machine learning to understand it in detail.
# 
# Installing scikit-learn
# scikit-learn depends on two other Python packages, NumPy and SciPy. For plot‐
# ting and interactive development, you should also install matplotlib, IPython, and
# the Jupyter Notebook. We recommend using one of the following prepackaged
# Python distributions, which will provide the necessary packages:
# Anaconda
#    A Python distribution made for large-scale data processing, predictive analytics,
#    and scientific computing. Anaconda comes with NumPy, SciPy, matplotlib,
#    pandas, IPython, Jupyter Notebook, and scikit-learn. Available on Mac OS,
#    Windows, and Linux, it is a very convenient solution and is the one we suggest
#    for people without an existing installation of the scientific Python packages. Ana‐
#    conda now also includes the commercial Intel MKL library for free. Using MKL
#    (which is done automatically when Anaconda is installed) can give significant
#    speed improvements for many algorithms in scikit-learn.
# Enthought Canopy
#     Another Python distribution for scientific computing. This comes with NumPy,
#     SciPy, matplotlib, pandas, and IPython, but the free version does not come with
#     scikit-learn. If you are part of an academic, degree-granting institution, you
#     can request an academic license and get free access to the paid subscription ver‐
#     sion of Enthought Canopy. Enthought Canopy is available for Python 2.7.x, and
#     works on Mac OS, Windows, and Linux.
# Python(x,y)
#     A free Python distribution for scientific computing, specifically for Windows.
#     Python(x,y) comes with NumPy, SciPy, matplotlib, pandas, IPython, and
#     scikit-learn.
# 
# 
# 
# 
# 6   |   Chapter 1: Introduction
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "scikit-learn",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class scikitlearn(HierNode):
    def __init__(self):
        super().__init__("scikit-learn")
        self.add(Content(), "content")
        self.add(A_Installingscikitlearn())

# eof
