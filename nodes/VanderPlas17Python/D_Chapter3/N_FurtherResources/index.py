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
# Further Resources
# In this chapter, we’ve covered many of the basics of using Pandas effectively for data
# analysis. Still, much has been omitted from our discussion. To learn more about Pan‐
# das, I recommend the following resources:
# Pandas online documentation
#    This is the go-to source for complete documentation of the package. While the
#    examples in the documentation tend to be small generated datasets, the descrip‐
#    tion of the options is complete and generally very useful for understanding the
#    use of various functions.
# Python for Data Analysis
#     Written by Wes McKinney (the original creator of Pandas), this book contains
#     much more detail on the package than we had room for in this chapter. In partic‐
#     ular, he takes a deep dive into tools for time series, which were his bread and but‐
#     ter as a financial consultant. The book also has many entertaining examples of
#     applying Pandas to gain insight from real-world datasets. Keep in mind, though,
#     that the book is now several years old, and the Pandas package has quite a few
#     new features that this book does not cover (but be on the lookout for a new edi‐
#     tion in 2017).
# Pandas on Stack Overflow
#    Pandas has so many users that any question you have has likely been asked and
#    answered on Stack Overflow. Using Pandas is a case where some Google-Fu is
#    your best friend. Simply go to your favorite search engine and type in the ques‐
#    tion, problem, or error you’re coming across—more than likely you’ll find your
#    answer on a Stack Overflow page.
# Pandas on PyVideo
#    From PyCon to SciPy to PyData, many conferences have featured tutorials from
#    Pandas developers and power users. The PyCon tutorials in particular tend to be
#    given by very well-vetted presenters.
# My hope is that, by using these resources, combined with the walk-through given in
# this chapter, you’ll be poised to use Pandas to tackle any data analysis problem you
# come across!
# 
# 
# 
# 
#                                                                    Further Resources   |   215
# 
# 
#                                                                         CHAPTER 4
#                             Visualization with Matplotlib
# 
# 
# 
# 
# We’ll now take an in-depth look at the Matplotlib tool for visualization in Python.
# Matplotlib is a multiplatform data visualization library built on NumPy arrays, and
# designed to work with the broader SciPy stack. It was conceived by John Hunter in
# 2002, originally as a patch to IPython for enabling interactive MATLAB-style plotting
# via gnuplot from the IPython command line. IPython’s creator, Fernando Perez, was
# at the time scrambling to finish his PhD, and let John know he wouldn’t have time to
# review the patch for several months. John took this as a cue to set out on his own, and
# the Matplotlib package was born, with version 0.1 released in 2003. It received an
# early boost when it was adopted as the plotting package of choice of the Space Tele‐
# scope Science Institute (the folks behind the Hubble Telescope), which financially
# supported Matplotlib’s development and greatly expanded its capabilities.
# One of Matplotlib’s most important features is its ability to play well with many oper‐
# ating systems and graphics backends. Matplotlib supports dozens of backends and
# output types, which means you can count on it to work regardless of which operating
# system you are using or which output format you wish. This cross-platform,
# everything-to-everyone approach has been one of the great strengths of Matplotlib. It
# has led to a large userbase, which in turn has led to an active developer base and Mat‐
# plotlib’s powerful tools and ubiquity within the scientific Python world.
# In recent years, however, the interface and style of Matplotlib have begun to show
# their age. Newer tools like ggplot and ggvis in the R language, along with web visuali‐
# zation toolkits based on D3js and HTML5 canvas, often make Matplotlib feel clunky
# and old-fashioned. Still, I’m of the opinion that we cannot ignore Matplotlib’s
# strength as a well-tested, cross-platform graphics engine. Recent Matplotlib versions
# make it relatively easy to set new global plotting styles (see “Customizing Matplotlib:
# Configurations and Stylesheets” on page 282), and people have been developing new
# packages that build on its powerful internals to drive Matplotlib via cleaner, more
# 
# 
#                                                                                     217
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Further Resources",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class FurtherResources(HierNode):
    def __init__(self):
        super().__init__("Further Resources")
        self.add(Content())

# eof