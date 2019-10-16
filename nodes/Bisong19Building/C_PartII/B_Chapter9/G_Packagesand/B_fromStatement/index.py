# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# from Statement
# The from statement allows you to import a specific feature from a module into your
# source file. The syntax is as follows:
# 
# from module_name import module_feature [as user_defined_name][,...]
# 
#    Let’s see an example:
# 
# from numpy import mean
# 
# mean([2,4,6,8])
# 'Output': 5.0
# 
#    This chapter provides the fundamentals for programming with Python.
# Programming is a very active endeavor, and competency is gained by experience and
# repetition. What is presented in this chapter provides just enough to be dangerous.
#    In the next chapter, we’ll introduce NumPy, a Python package for numerical
# computing.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "from Statement",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# from Statement"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class fromStatement(HierNode):
    def __init__(self):
        super().__init__("from Statement")
        self.add(Content())

# eof
