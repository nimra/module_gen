# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Starting Out with Colab
# The following steps provide a walk-through for launching a Notebook on Google Colab:
# 
#        1. Go to https://colab.research.google.com/ and log in using
#           your existing Google account to access the Colab homepage
#           (see Figure 7-1).
# 
# 
# 
# 
# 
# Figure 7-1. Google Colab homepage
# 
#       2. Open a Python 3 Notebook (see Figure 7-2).
# 
# 
# 
# 
# Figure 7-2. Python 3 Notebook

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Starting Out with Colab",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Starting Out with Colab"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class StartingOut(HierNode):
    def __init__(self):
        super().__init__("Starting Out with Colab")
        self.add(Content())

# eof
