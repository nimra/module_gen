# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.HierBlock import HierBlock as hbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.ListBlock import ListBlock as lbk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                  Download from finelybook www.finelybook.com
# off between these two objectives. This gives us the constrained optimization problem
# in Equation 5-4.
# 
#     Equation 5-4. Soft margin linear SVM classifier objective
#                              m
#                     1 T
#      minimize         � ·�+C ∑ ζ          i
#         �, b, ζ     2       i=1
#                         i    T   i                i              i
#      subject to     t       � ·� +b ≥1−ζ              and    ζ       ≥0   for i = 1, 2, ⋯, m
# 
# 
# Quadratic Programming
# The hard margin and soft margin problems are both convex quadratic optimization
# problems with linear constraints. Such problems are known as Quadratic Program‐
# ming (QP) problems. Many off-the-shelf solvers are available to solve QP problems
# using a variety of techniques that are outside the scope of this book.5 The general
# problem formulation is given by Equation 5-5.
# 
#     Equation 5-5. Quadratic Programming problem
#                     1 T                       T
#     Minimize          � ·�·�         +    � ·�
#          �          2
#     subject to      �·�≤�
#                     � is an n p‐dimensional vector (n p = number of parameters),
#                         � is an n p × n p matrix,
#           where         �   is an n p‐dimensional vector,
#                         � is an nc × n p matrix (nc = number of constraints),
#                         �   is an nc‐dimensional vector.
# 
# Note that the expression A · p ≤ b actually defines nc constraints: pT · a(i) ≤ b(i) for i =
# 1, 2, ⋯, nc, where a(i) is the vector containing the elements of the ith row of A and b(i) is
# the ith element of b.
# You can easily verify that if you set the QP parameters in the following way, you get
# the hard margin linear SVM classifier objective:
# 
#   • np = n + 1, where n is the number of features (the +1 is for the bias term).
# 
# 
# 
# 5 To learn more about Quadratic Programming, you can start by reading Stephen Boyd and Lieven Vanden‐
#   berghe, Convex Optimization (Cambridge, UK: Cambridge University Press, 2004) or watch Richard Brown’s
#   series of video lectures.
# 
# 
# 
#                                                                                    Under the Hood |     159
# 
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
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Quadratic Programming",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class QuadraticProgramming(HierNode):
    def __init__(self):
        super().__init__("Quadratic Programming")
        self.add(Content(), "content")

# eof
