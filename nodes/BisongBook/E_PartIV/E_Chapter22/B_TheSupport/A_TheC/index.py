# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The C Parameter
# The C parameter is the hyper-parameter that is responsible for controlling the degree
# of violations to the margins or the number of intentionally misclassified points allowed
# by the support vector classifier. The C hyper-parameter is a non-negative real number.
# When this C parameter is set to 0, the classifier becomes the large margin classifier.
#      In a soft margin classifier, the C parameter is tuned by adjusting its values to
# control the tolerance of the margin. With larger values of C, the classifier margins
# become wider and more tolerant to violations and misclassifications. However, with
# smaller values of C, the margins become narrower and are less tolerant of violations
# and misclassified points.
#      Observe that the C hyper-parameter is vital for regulating the bias/variance trade-off
# of the support vector classifier. The higher the value of C, our classifier is more prone to
# variability in the data points and can under-simplify the learning problem. Also, if C is
# set closer to zero, it results in a much narrower margin, and this can overfit the classifier,
# leading to high variance – and this will likely fail to generalize to new examples (see
# Figure 22-7).
# 
# 
# 
# 
# Figure 22-7. Left: Higher values of C result in wider margins with more tolerance.
# Right: Lower values of C result in narrower margins with less tolerance

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "The C Parameter",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# The C Parameter"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TheC(HierNode):
    def __init__(self):
        super().__init__("The C Parameter")
        self.add(Content())

# eof
