# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Bar Plot
# Let’s create a simple bar plot using the bar method. The output with matplotlib is shown
# in Figure 12-3, and the output with seaborn is shown in Figure 12-4.
# 
# states = ["Cross River", "Lagos", "Rivers", "Kano"]
# population = [3737517, 17552940, 5198716, 11058300]
# # create barplot using matplotlib
# plt.bar(states, population)
# plt.show()
# # create barplot using seaborn
# sns.barplot(x=states, y=population)
# plt.show()
# 
# 
# 
# 
# Figure 12-3. Barplot with Matplotlib
# 
# 
# 
# 
# 
# Figure 12-4. Barplot with seaborn

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Bar Plot",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Bar Plot"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class BarPlot(HierNode):
    def __init__(self):
        super().__init__("Bar Plot")
        self.add(Content())

# eof
