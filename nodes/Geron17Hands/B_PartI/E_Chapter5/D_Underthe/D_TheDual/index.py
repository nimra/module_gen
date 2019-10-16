# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                 Download from finelybook www.finelybook.com
#   • nc = m, where m is the number of training instances.
#   • H is the np × np identity matrix, except with a zero in the top-left cell (to ignore
#     the bias term).
#   • f = 0, an np-dimensional vector full of 0s.
#   • b = 1, an nc-dimensional vector full of 1s.
#   • a(i) = –t(i) �˙ (i), where �˙ (i) is equal to x(i) with an extra bias feature �˙ 0 = 1.
# 
# So one way to train a hard margin linear SVM classifier is just to use an off-the-shelf
# QP solver by passing it the preceding parameters. The resulting vector p will contain
# the bias term b = p0 and the feature weights wi = pi for i = 1, 2, ⋯, m. Similarly, you
# can use a QP solver to solve the soft margin problem (see the exercises at the end of
# the chapter).
# However, to use the kernel trick we are going to look at a different constrained opti‐
# mization problem.
# 
# The Dual Problem
# Given a constrained optimization problem, known as the primal problem, it is possi‐
# ble to express a different but closely related problem, called its dual problem. The sol‐
# ution to the dual problem typically gives a lower bound to the solution of the primal
# problem, but under some conditions it can even have the same solutions as the pri‐
# mal problem. Luckily, the SVM problem happens to meet these conditions,6 so you
# can choose to solve the primal problem or the dual problem; both will have the same
# solution. Equation 5-6 shows the dual form of the linear SVM objective (if you are
# interested in knowing how to derive the dual problem from the primal problem, see
# Appendix C).
# 
#       Equation 5-6. Dual form of the linear SVM objective
# 
#                    1 m m i j i j iT                                  m
# 
#                    2i∑  ∑ α α t t � ·�                   j
#       minimize
#            α         =1j=1
#                                                              −      ∑ αi
#                                                                    i=1
# 
#                              subject to         αi ≥0   for i = 1, 2, ⋯, m
# 
# 
# 
# 
# 6 The objective function is convex, and the inequality constraints are continuously differentiable and convex
#   functions.
# 
# 
# 
# 160    |   Chapter 5: Support Vector Machines
# 
#                 Download from finelybook www.finelybook.com
# Once you find the vector α that minimizes this equation (using a QP solver), you can
# compute � and b that minimize the primal problem by using Equation 5-7.
# 
#    Equation 5-7. From the dual solution to the primal solution
#           m
#     �=    ∑ αiti�i
#          i=1
#                 m
#          1
#     b=
#          ns     ∑
#                i=1
#                        1−t   i    T
#                                  � ·�
#                                         i
# 
# 
#               α i >0
# 
# 
# The dual problem is faster to solve than the primal when the number of training
# instances is smaller than the number of features. More importantly, it makes the ker‐
# nel trick possible, while the primal does not. So what is this kernel trick anyway?
# 
# Kernelized SVM
# Suppose you want to apply a 2nd-degree polynomial transformation to a two-
# dimensional training set (such as the moons training set), then train a linear SVM
# classifier on the transformed training set. Equation 5-8 shows the 2nd-degree polyno‐
# mial mapping function ϕ that you want to apply.
# 
#    Equation 5-8. Second-degree polynomial mapping
#                            x12
#                 x1
#    ϕ� =ϕ               =   2 x1x2
#                 x2
#                            x22
# 
# Notice that the transformed vector is three-dimensional instead of two-dimensional.
# Now let’s look at what happens to a couple of two-dimensional vectors, a and b, if we
# apply this 2nd-degree polynomial mapping and then compute the dot product of the
# transformed vectors (See Equation 5-9).
# 
# 
# 
# 
#                                                                   Under the Hood   |   161
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "The Dual Problem",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# The Dual Problem"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TheDual(HierNode):
    def __init__(self):
        super().__init__("The Dual Problem")
        self.add(Content())

# eof
