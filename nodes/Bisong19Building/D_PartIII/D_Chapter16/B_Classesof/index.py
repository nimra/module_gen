# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Classes of Gradient Descent Algorithm
# The three types of gradient descent algorithms are
# 
#       •   Batch gradient descent
# 
#       •   Mini-batch gradient descent
# 
#       •   Stochastic gradient descent
# 
#      The batch gradient descent algorithm uses the entire training data in computing
# each step of the gradient in the direction of steepest descent. Batch gradient descent
# is most likely to converge to the global minimum. However, the disadvantage of this
# method is that, for massive datasets, the optimization process can be prolonged.
#      In stochastic gradient descent (SGD), the algorithm quickly learns the direction
# of steepest descent using a single example of the training set at each time step. While
# this method has the distinct advantage of being fast, it may never converge to the
# global minimum. However, it approximates the global minimum closely enough. In
# practice, SGD is enhanced by gradually reducing the learning rate over time as the
# algorithm converges. In doing this, we can take advantage of large step sizes to go
# downhill more quickly and then slow down so as not to miss the global minimum. Due
# to its speed when dealing with humongous datasets, SGD is often preferred to batch
# gradient descent.
#      Mini-batch gradient descent on the other hand randomly splits the dataset into
# manageable chunks called mini-batches. It operates on a mini-batch in each time step
# to learn the direction of steepest descent of the function. This method is a compromise
# between stochastic and batch gradient descent. Just like SGD, mini-batch gradient
# descent does not converge to the global minimum. However, it is more robust in
# avoiding local minimum. The advantage of mini-batch gradient descent over stochastic
# gradient descent is that it is more computational efficient by taking advantage of matrix
# vectorization under the hood to efficiently compute the algorithm updates.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Classes of Gradient Descent Algorithm",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Classes of Gradient Descent Algorithm"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Classesof(HierNode):
    def __init__(self):
        super().__init__("Classes of Gradient Descent Algorithm")
        self.add(Content())

# eof
