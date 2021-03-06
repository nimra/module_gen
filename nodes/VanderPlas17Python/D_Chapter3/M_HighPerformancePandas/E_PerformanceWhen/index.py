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
# In addition to being a more efficient computation, compared to the masking expres‐
# sion this is much easier to read and understand. Note that the query() method also
# accepts the @ flag to mark local variables:
#       In[25]: Cmean = df['C'].mean()
#               result1 = df[(df.A < Cmean) & (df.B < Cmean)]
#               result2 = df.query('A < @Cmean and B < @Cmean')
#               np.allclose(result1, result2)
#       Out[25]: True
# 
# 
# Performance: When to Use These Functions
# When considering whether to use these functions, there are two considerations: com‐
# putation time and memory use. Memory use is the most predictable aspect. As already
# mentioned, every compound expression involving NumPy arrays or Pandas Data
# Frames will result in implicit creation of temporary arrays: For example, this:
#       In[26]: x = df[(df.A < 0.5) & (df.B < 0.5)]
# is roughly equivalent to this:
#       In[27]: tmp1 = df.A < 0.5
#               tmp2 = df.B < 0.5
#               tmp3 = tmp1 & tmp2
#               x = df[tmp3]
# 
# If the size of the temporary DataFrames is significant compared to your available sys‐
# tem memory (typically several gigabytes), then it’s a good idea to use an eval() or
# query() expression. You can check the approximate size of your array in bytes using
# this:
#       In[28]: df.values.nbytes
#       Out[28]: 32000
# 
# On the performance side, eval() can be faster even when you are not maxing out
# your system memory. The issue is how your temporary DataFrames compare to the
# size of the L1 or L2 CPU cache on your system (typically a few megabytes in 2016); if
# they are much bigger, then eval() can avoid some potentially slow movement of val‐
# ues between the different memory caches. In practice, I find that the difference in
# computation time between the traditional methods and the eval/query method is
# usually not significant—if anything, the traditional method is faster for smaller
# arrays! The benefit of eval/query is mainly in the saved memory, and the sometimes
# cleaner syntax they offer.
# We’ve covered most of the details of eval() and query() here; for more information
# on these, you can refer to the Pandas documentation. In particular, different parsers
# and engines can be specified for running these queries; for details on this, see the dis‐
# cussion within the “Enhancing Performance” section.
# 
# 214   | Chapter 3: Data Manipulation with Pandas
# 
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
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Performance: When to Use These Functions",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PerformanceWhen(HierNode):
    def __init__(self):
        super().__init__("Performance: When to Use These Functions")
        self.add(Content())

# eof
