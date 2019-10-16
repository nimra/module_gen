# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                   Download from finelybook www.finelybook.com
# Figure 5-12 shows the decision function that corresponds to the model on the right of
# Figure 5-4: it is a two-dimensional plane since this dataset has two features (petal
# width and petal length). The decision boundary is the set of points where the decision
# function is equal to 0: it is the intersection of two planes, which is a straight line (rep‐
# resented by the thick solid line).3
# 
# 
# 
# 
# Figure 5-12. Decision function for the iris dataset
# 
# The dashed lines represent the points where the decision function is equal to 1 or –1:
# they are parallel and at equal distance to the decision boundary, forming a margin
# around it. Training a linear SVM classifier means finding the value of w and b that
# make this margin as wide as possible while avoiding margin violations (hard margin)
# or limiting them (soft margin).
# 
# Training Objective
# Consider the slope of the decision function: it is equal to the norm of the weight vec‐
# tor, ∥ w ∥. If we divide this slope by 2, the points where the decision function is equal
# to ±1 are going to be twice as far away from the decision boundary. In other words,
# dividing the slope by 2 will multiply the margin by 2. Perhaps this is easier to visual‐
# ize in 2D in Figure 5-13. The smaller the weight vector w, the larger the margin.
# 
# 
# 
# 
# 3 More generally, when there are n features, the decision function is an n-dimensional hyperplane, and the deci‐
#   sion boundary is an (n – 1)-dimensional hyperplane.
# 
# 
# 
#                                                                                         Under the Hood   |   157
# 
#                         Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 5-13. A smaller weight vector results in a larger margin
# 
# So we want to minimize ∥ w ∥ to get a large margin. However, if we also want to avoid
# any margin violation (hard margin), then we need the decision function to be greater
# than 1 for all positive training instances, and lower than –1 for negative training
# instances. If we define t(i) = –1 for negative instances (if y(i) = 0) and t(i) = 1 for positive
# instances (if y(i) = 1), then we can express this constraint as t(i)(wT · x(i) + b) ≥ 1 for all
# instances.
# We can therefore express the hard margin linear SVM classifier objective as the con‐
# strained optimization problem in Equation 5-3.
# 
#       Equation 5-3. Hard margin linear SVM classifier objective
#                         1 T
#        minimize           � ·�
#            �, b         2
#                            i    T    i
#        subject to      t       � ·� +b ≥1             for i = 1, 2, ⋯, m
# 
#                                                 1                          1
#                      We are minimizing 2 wT · w, which is equal to 2 ∥ w ∥2, rather than
#                      minimizing ∥ w ∥. This is because it will give the same result (since
#                      the values of w and b that minimize a value also minimize half of
#                                           1
#                      its square), but 2 ∥ w ∥2 has a nice and simple derivative (it is just
#                      w) while ∥ w ∥ is not differentiable at w = 0. Optimization algo‐
#                      rithms work much better on differentiable functions.
# 
# To get the soft margin objective, we need to introduce a slack variable ζ(i) ≥ 0 for each
# instance:4 ζ(i) measures how much the ith instance is allowed to violate the margin. We
# now have two conflicting objectives: making the slack variables as small as possible to
#                                             1
# reduce the margin violations, and making 2 wT · w as small as possible to increase the
# margin. This is where the C hyperparameter comes in: it allows us to define the trade‐
# 
# 
# 
# 4 Zeta (ζ) is the 8th letter of the Greek alphabet.
# 
# 
# 
# 158    |   Chapter 5: Support Vector Machines
# 
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Training Objective",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Training Objective"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TrainingObjective(HierNode):
    def __init__(self):
        super().__init__("Training Objective")
        self.add(Content())

# eof
