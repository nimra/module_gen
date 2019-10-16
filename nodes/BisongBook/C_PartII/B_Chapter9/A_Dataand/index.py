# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Data and Operations
# Fundamentally, programming involves storing data and operating on that data to
# generate information. Techniques for efficient data storage are studied in the field called
# data structures, while the techniques for operating on data are studied as algorithms.
#     Data is stored in a memory block on the computer. Think of a memory block as a
# container holding data (Figure 9-1). When data is operated upon, the newly processed
# data is also stored in memory. Data is operated by using arithmetic and boolean
# expressions and functions.
# 
# 
# 
# 
# 
# Figure 9-1. An illustration of a memory cell holding data
# 
#      In programming, a memory location is called a variable. A variable is a container
# for storing the data that is assigned to it. A variable is usually given a unique name by
# the programmer to represent a particular memory cell. In python, variable names are
# programmer defined, but it must follow a valid naming condition of only alphanumeric
# lowercase characters with words separated by an underscore. Also, a variable name
# should have semantic meaning to the data that is stored in that variable. This helps to
# improve code readability later in the future.
#      The act of placing data to a variable is called assignment.
# 
# # assigning data to a variable
# x = 1
# user_name = 'Emmanuel Okoi'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Data and Operations",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Data and Operations"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Dataand(HierNode):
    def __init__(self):
        super().__init__("Data and Operations")
        self.add(Content())

# eof
