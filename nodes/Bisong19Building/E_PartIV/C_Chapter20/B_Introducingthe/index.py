# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
    mbk("The logistic function, also known as the logit or the sigmoid function, is responsible for constraining the output of the cost function so that it becomes a probability output between 0 and 1. The sigmoid function is formally written as"),
    mbk("$$ h \\left( t \\right) = \\frac{1}{1 + e^{-t}} $$"),
    mbk("The logistic regression model is formally similar to the linear regression model except that it is acted upon by the sigmoid model. The following is the formal representation:"),
    mbk("$$ \\hat{y} = \\theta_0 + \\theta_1 x_1 + \\theta_2 x_2 + ... + \\theta_n x_n $$"),
    mbk("$$ h \\left( \\hat{y} \\right) = \\frac{1}{1 + e^{-\\hat{y}}} $$"),
    mbk("where $0 \\leq h(t) \\leq 1$. The sigmoid function is graphically shown in Figure 20-4."),
    ibk(None, "Figure 20-4. Logistic function"),
    mbk("The sigmoid function, which looks like an S curve, rises from 0 and plateaus at 1. From the sigmoid function shown in Figure 20-4, as $\\hat{y}$ increases to positive infinity, the sigmoid output gets closer to 1, and as t decreases toward negative infinity, the sigmoid function outputs 0."),
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Introducing the Logit or Sigmoid Model",
            Stage.REMOVE_EXTRANEOUS,
            Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Introducing the Logit or Sigmoid Model"))
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Introducingthe(HierNode):
    def __init__(self):
        super().__init__("Introducing the Logit or Sigmoid Model")
        self.add(Content())

# eof
