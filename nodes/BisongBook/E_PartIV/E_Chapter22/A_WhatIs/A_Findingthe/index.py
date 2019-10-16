# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Finding the Optimal Hyperplane
# The best hyperplane that linearly separates two classes is identified as the line lying at
# the largest margin from the nearest vectors at the boundary of the two classes.
#      In Figure 22-3, we observe that the best hyperplane is the line at the exact center
# of the two classes and constitutes the largest margin between both classes. Hence, this
# optimal hyperplane is also known as the largest margin classifier.
# 
# 
# 
# 
# Figure 22-3. The largest margin classifier
# 
#      The boundary points of the respective classes which are known as the support
# vectors are essential in finding the optimal hyperplane. The support vectors are
# illustrated in Figure 22-4. The boundary points are called support vectors because they
# are used to determine the maximum distance between the class they belong to and the
# discriminant function separating the classes.
# 
# 
# 
# 
# Figure 22-4. Support vectors
# 
#     The mathematical formulation for finding the margin and consequently the
# hyperplane that maximizes the margin is beyond the scope of this book, but suffice to
# say this technique involves the Lagrange multiplier.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Finding the Optimal Hyperplane",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Finding the Optimal Hyperplane"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Findingthe(HierNode):
    def __init__(self):
        super().__init__("Finding the Optimal Hyperplane")
        self.add(Content())

# eof
