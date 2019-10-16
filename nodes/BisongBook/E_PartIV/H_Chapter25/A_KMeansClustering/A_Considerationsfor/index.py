# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Considerations for Selecting K
# There’s really no way of telling the number of clusters in a dataset from the onset. The
# best way of selecting k is to try out different values of K to see what works best in creating
# distinct clusters.
#      Another strategy, which is widely employed in practice, is to compute the average
# distance of the points in the cluster to the cluster centroid for all clusters. This estimate
# is plotted on a graph as we progressively increase the value of K. We observe that as K
# increases, the distance of points from the centroid of its cluster gradually reduces, and
# the generated curve resembles the elbow of an arm. From practice, we choose the value
# of K just after the elbow as the best K value for that dataset. This method is called the
# elbow method for selecting K as is illustrated in Figure 25-3.
# 
# 
# 
# 
# Figure 25-3. The elbow method for choosing the best value of k

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Considerations for Selecting K",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Considerations for Selecting K"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Considerationsfor(HierNode):
    def __init__(self):
        super().__init__("Considerations for Selecting K")
        self.add(Content())

# eof
