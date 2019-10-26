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
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Why Python?",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class WhyPython(HierNode):
    def __init__(self):
        super().__init__("Why Python?")
        self.add(Content(), "content")

# eof
