# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                    Download from finelybook www.finelybook.com
# AdaGrad often performs well for simple quadratic problems, but unfortunately it
# often stops too early when training neural networks. The learning rate gets scaled
# down so much that the algorithm ends up stopping entirely before reaching the
# global optimum. So even though TensorFlow has an AdagradOptimizer, you should
# not use it to train deep neural networks (it may be efficient for simpler tasks such as
# Linear Regression, though).
# 
# RMSProp
# Although AdaGrad slows down a bit too fast and ends up never converging to the
# global optimum, the RMSProp algorithm14 fixes this by accumulating only the gradi‐
# ents from the most recent iterations (as opposed to all the gradients since the begin‐
# ning of training). It does so by using exponential decay in the first step (see Equation
# 11-7).
# 
#       Equation 11-7. RMSProp algorithm
#       1.     �     β� + 1 − β ∇θJ θ ⊗ ∇θJ θ
#       2.     θ      θ − η ∇θ J θ ⊘ � + �
# 
# The decay rate β is typically set to 0.9. Yes, it is once again a new hyperparameter, but
# this default value often works well, so you may not need to tune it at all.
# As you might expect, TensorFlow has an RMSPropOptimizer class:
#       optimizer = tf.train.RMSPropOptimizer(learning_rate=learning_rate,
#                                             momentum=0.9, decay=0.9, epsilon=1e-10)
# Except on very simple problems, this optimizer almost always performs much better
# than AdaGrad. It also generally performs better than Momentum optimization and
# Nesterov Accelerated Gradients. In fact, it was the preferred optimization algorithm
# of many researchers until Adam optimization came around.
# 
# Adam Optimization
# Adam,15 which stands for adaptive moment estimation, combines the ideas of Momen‐
# tum optimization and RMSProp: just like Momentum optimization it keeps track of
# an exponentially decaying average of past gradients, and just like RMSProp it keeps
# 
# 
# 
# 14 This algorithm was created by Tijmen Tieleman and Geoffrey Hinton in 2012, and presented by Geoffrey
#    Hinton in his Coursera class on neural networks (slides: http://goo.gl/RsQeis; video: https://goo.gl/XUbIyJ).
#    Amusingly, since the authors have not written a paper to describe it, researchers often cite “slide 29 in lecture
#    6” in their papers.
# 15 “Adam: A Method for Stochastic Optimization,” D. Kingma, J. Ba (2015).
# 
# 
# 
# 298    |   Chapter 11: Training Deep Neural Nets
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "RMSProp",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# RMSProp"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class RMSProp(HierNode):
    def __init__(self):
        super().__init__("RMSProp")
        self.add(Content())

# eof
