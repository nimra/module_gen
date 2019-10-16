# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                    Download from finelybook www.finelybook.com
#      outliers are exponentially rare (like in a bell-shaped curve), the RMSE performs
#      very well and is generally preferred.
# 
# 
# Check the Assumptions
# Lastly, it is good practice to list and verify the assumptions that were made so far (by
# you or others); this can catch serious issues early on. For example, the district prices
# that your system outputs are going to be fed into a downstream Machine Learning
# system, and we assume that these prices are going to be used as such. But what if the
# downstream system actually converts the prices into categories (e.g., “cheap,”
# “medium,” or “expensive”) and then uses those categories instead of the prices them‐
# selves? In this case, getting the price perfectly right is not important at all; your sys‐
# tem just needs to get the category right. If that’s so, then the problem should have
# been framed as a classification task, not a regression task. You don’t want to find this
# out after working on a regression system for months.
# Fortunately, after talking with the team in charge of the downstream system, you are
# confident that they do indeed need the actual prices, not just categories. Great! You’re
# all set, the lights are green, and you can start coding now!
# 
# Get the Data
# It’s time to get your hands dirty. Don’t hesitate to pick up your laptop and walk
# through the following code examples in a Jupyter notebook. The full Jupyter note‐
# book is available at https://github.com/ageron/handson-ml.
# 
# Create the Workspace
# First you will need to have Python installed. It is probably already installed on your
# system. If not, you can get it at https://www.python.org/.7
# Next you need to create a workspace directory for your Machine Learning code and
# datasets. Open a terminal and type the following commands (after the $ prompts):
#      $ export ML_PATH="$HOME/ml"                   # You can change the path if you prefer
#      $ mkdir -p $ML_PATH
# You will need a number of Python modules: Jupyter, NumPy, Pandas, Matplotlib, and
# Scikit-Learn. If you already have Jupyter running with all these modules installed,
# you can safely skip to “Download the Data” on page 43. If you don’t have them yet,
# there are many ways to install them (and their dependencies). You can use your sys‐
# tem’s packaging system (e.g., apt-get on Ubuntu, or MacPorts or HomeBrew on
# 
# 
# 7 The latest version of Python 3 is recommended. Python 2.7+ should work fine too, but it is deprecated.
# 
# 
# 
# 40   |   Chapter 2: End-to-End Machine Learning Project
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Check the Assumptions",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Check the Assumptions"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Checkthe(HierNode):
    def __init__(self):
        super().__init__("Check the Assumptions")
        self.add(Content())

# eof
