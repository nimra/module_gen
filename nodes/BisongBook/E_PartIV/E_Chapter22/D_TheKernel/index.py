# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_AddingPolynomial.index import AddingPolynomial as A_AddingPolynomial
from .B_Kernels.index import Kernels as B_Kernels

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The Kernel Trick: Fitting Non-linear Decision
#  Boundaries
# Non-linear datasets occur more often than not in real world scenarios.
#     Technically speaking, the name support vector machine is when a support vector
# classifier is used with a non-linear kernel to learn non-linear decision boundaries.
# 
#     SVM uses an essential technique for extending the feature space of a dataset to
# construct a non-linear classifier. This technique is called kernel and is popularly known
# as the kernel trick. Figure 22-10 illustrates the kernel trick as an extra dimension is added
# to the feature space.
# 
# 
# 
# 
# Figure 22-10. Left: Linear discriminant to non-linear data. Right: By using the
# kernel trick, we can linearly separate a non-linear dataset by adding an extra
# dimension to the feature space.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "The Kernel Trick: Fitting Non-linear Decision Boundaries",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# The Kernel Trick: Fitting Non-linear Decision Boundaries"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TheKernel(HierNode):
    def __init__(self):
        super().__init__("The Kernel Trick: Fitting Non-linear Decision Boundaries")
        self.add(Content())
        self.add(A_AddingPolynomial())
        self.add(B_Kernels())

# eof
