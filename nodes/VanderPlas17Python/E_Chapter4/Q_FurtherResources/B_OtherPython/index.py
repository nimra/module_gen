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
# Matplotlib gallery linked on that page: it shows thumbnails of hundreds of different
# plot types, each one linked to a page with the Python code snippet used to generate it.
# In this way, you can visually inspect and learn about a wide range of different plotting
# styles and visualization techniques.
# For a book-length treatment of Matplotlib, I would recommend Interactive Applica‐
# tions Using Matplotlib, written by Matplotlib core developer Ben Root.
# 
# Other Python Graphics Libraries
# Although Matplotlib is the most prominent Python visualization library, there are
# other more modern tools that are worth exploring as well. I’ll mention a few of them
# briefly here:
# 
#   • Bokeh is a JavaScript visualization library with a Python frontend that creates
#     highly interactive visualizations capable of handling very large and/or streaming
#     datasets. The Python frontend outputs a JSON data structure that can be inter‐
#     preted by the Bokeh JS engine.
#   • Plotly is the eponymous open source product of the Plotly company, and is simi‐
#     lar in spirit to Bokeh. Because Plotly is the main product of a startup, it is receiv‐
#     ing a high level of development effort. Use of the library is entirely free.
#   • Vispy is an actively developed project focused on dynamic visualizations of very
#     large datasets. Because it is built to target OpenGL and make use of efficient
#     graphics processors in your computer, it is able to render some quite large and
#     stunning visualizations.
#   • Vega and Vega-Lite are declarative graphics representations, and are the product
#     of years of research into the fundamental language of data visualization. The ref‐
#     erence rendering implementation is JavaScript, but the API is language agnostic.
#     There is a Python API under development in the Altair package. Though it’s not
#     mature yet, I’m quite excited for the possibilities of this project to provide a com‐
#     mon reference point for visualization in Python and other languages.
# 
# The visualization space in the Python community is very dynamic, and I fully expect
# this list to be out of date as soon as it is published. Keep an eye out for what’s coming
# in the future!
# 
# 
# 
# 
# 330   |   Chapter 4: Visualization with Matplotlib
# 
#                                                                           CHAPTER 5
#                                                     Machine Learning
# 
# 
# 
# 
# In many ways, machine learning is the primary means by which data science mani‐
# fests itself to the broader world. Machine learning is where these computational and
# algorithmic skills of data science meet the statistical thinking of data science, and the
# result is a collection of approaches to inference and data exploration that are not
# about effective theory so much as effective computation.
# The term “machine learning” is sometimes thrown around as if it is some kind of
# magic pill: apply machine learning to your data, and all your problems will be solved!
# As you might expect, the reality is rarely this simple. While these methods can be
# incredibly powerful, to be effective they must be approached with a firm grasp of the
# strengths and weaknesses of each method, as well as a grasp of general concepts such
# as bias and variance, overfitting and underfitting, and more.
# This chapter will dive into practical aspects of machine learning, primarily using
# Python’s Scikit-Learn package. This is not meant to be a comprehensive introduction
# to the field of machine learning; that is a large subject and necessitates a more techni‐
# cal approach than we take here. Nor is it meant to be a comprehensive manual for the
# use of the Scikit-Learn package (for this, see “Further Machine Learning Resources”
# on page 514). Rather, the goals of this chapter are:
# 
#   • To introduce the fundamental vocabulary and concepts of machine learning.
#   • To introduce the Scikit-Learn API and show some examples of its use.
#   • To take a deeper dive into the details of several of the most important machine
#     learning approaches, and develop an intuition into how they work and when and
#     where they are applicable.
# 
# Much of this material is drawn from the Scikit-Learn tutorials and workshops I have
# given on several occasions at PyCon, SciPy, PyData, and other conferences. Any
# 
# 
#                                                                                       331
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Other Python Graphics Libraries",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class OtherPython(HierNode):
    def __init__(self):
        super().__init__("Other Python Graphics Libraries")
        self.add(Content())

# eof
