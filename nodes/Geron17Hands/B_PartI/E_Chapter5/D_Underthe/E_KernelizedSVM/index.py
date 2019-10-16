# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
#                     Download from finelybook www.finelybook.com
#       Equation 5-9. Kernel trick for a 2nd-degree polynomial mapping
#                                          T
#                                  a12                 b12
#             T                   2 a1a2               2 b1b2 = a12b12 + 2a1b1a2b2 + a22b22
#       ϕ�        ·ϕ �       =                 ·
#                                  a22                 b22
#                                                                 T                2
#                                                            a1           b1                    2
#                                                  2                                     T
#                            = a1b1 + a2b2             =              ·                = � ·�
#                                                            a2           b2
# 
# 
# How about that? The dot product of the transformed vectors is equal to the square of
# the dot product of the original vectors: ϕ(a)T · ϕ(b) = (aT · b)2.
# Now here is the key insight: if you apply the transformation ϕ to all training instan‐
# ces, then the dual problem (see Equation 5-6) will contain the dot product ϕ(x(i))T ·
# ϕ(x(j)). But if ϕ is the 2nd-degree polynomial transformation defined in Equation 5-8,
#                                                                                                   T   2
# then you can replace this dot product of transformed vectors simply by � i · � j .
# So you don’t actually need to transform the training instances at all: just replace the
# dot product by its square in Equation 5-6. The result will be strictly the same as if you
# went through the trouble of actually transforming the training set then fitting a linear
# SVM algorithm, but this trick makes the whole process much more computationally
# efficient. This is the essence of the kernel trick.
# The function K(a, b) = (aT · b)2 is called a 2nd-degree polynomial kernel. In Machine
# Learning, a kernel is a function capable of computing the dot product ϕ(a)T · ϕ(b)
# based only on the original vectors a and b, without having to compute (or even to
# know about) the transformation ϕ. Equation 5-10 lists some of the most commonly
# used kernels.
# 
#       Equation 5-10. Common kernels
#                                              T
#                  Linear:       K �, � = � · �
#                                                  T              d
#            Polynomial:         K �, � = γ� · � + r
#                                                                              2
#       Gaussian RBF:            K �, � = exp −γ∥ � − � ∥
#                                                            T
#                 Sigmoid:       K �, � = tanh γ� · � + r
# 
# 
# 
# 
# 162    |   Chapter 5: Support Vector Machines
# 
#                     Download from finelybook www.finelybook.com
# 
#                                         Mercer’s Theorem
#   According to Mercer’s theorem, if a function K(a, b) respects a few mathematical con‐
#   ditions called Mercer’s conditions (K must be continuous, symmetric in its arguments
#   so K(a, b) = K(b, a), etc.), then there exists a function ϕ that maps a and b into
#   another space (possibly with much higher dimensions) such that K(a, b) = ϕ(a)T ·
#   ϕ(b). So you can use K as a kernel since you know ϕ exists, even if you don’t know
#   what ϕ is. In the case of the Gaussian RBF kernel, it can be shown that ϕ actually
#   maps each training instance to an infinite-dimensional space, so it’s a good thing you
#   don’t need to actually perform the mapping!
#   Note that some frequently used kernels (such as the Sigmoid kernel) don’t respect all
#   of Mercer’s conditions, yet they generally work well in practice.
# 
# 
# There is still one loose end we must tie. Equation 5-7 shows how to go from the dual
# solution to the primal solution in the case of a linear SVM classifier, but if you apply
# the kernel trick you end up with equations that include ϕ(x(i)). In fact, � must have
# the same number of dimensions as ϕ(x(i)), which may be huge or even infinite, so you
# can’t compute it. But how can you make predictions without knowing �? Well, the
# good news is that you can plug in the formula for � from Equation 5-7 into the deci‐
# sion function for a new instance x(n), and you get an equation with only dot products
# between input vectors. This makes it possible to use the kernel trick, once again
# (Equation 5-11).
# 
#    Equation 5-11. Making predictions with a kernelized SVM
#                                                    m                   T
#                 n        T         n
#    h
#     �, b
#            ϕ�       = � ·ϕ �           +b =       ∑
#                                                   i=1
#                                                         αitiϕ�
#                                                                    i
#                                                                            ·ϕ �
#                                                                                   n
#                                                                                       +b
# 
#                          m
#                                             i T
#                     =    ∑ αiti
#                         i=1
#                                        ϕ�         ·ϕ �
#                                                          n
#                                                               +b
# 
#                           m
#                     =     ∑
#                          i=1
#                                              i
#                                  α i t i K � ,�
#                                                    n
#                                                          +b
#                         α i >0
# 
# 
# Note that since α(i) ≠ 0 only for support vectors, making predictions involves comput‐
# ing the dot product of the new input vector x(n) with only the support vectors, not all
# the training instances. Of course, you also need to compute the bias term b , using the
# same trick (Equation 5-12).
# 
# 
# 
# 
#                                                                                        Under the Hood |   163
# 
#                    Download from finelybook www.finelybook.com
#       Equation 5-12. Computing the bias term using the kernel trick
#                          m                                                  m                       m              T
#                 1                                                  1
#       b =
#                 ns        ∑
#                          i=1
#                                 1−t i� ·ϕ �
#                                               T            i
#                                                                =
#                                                                    ns        ∑
#                                                                             i=1
#                                                                                       1−t   i
#                                                                                                      ∑ α jt jϕ�j
#                                                                                                     j=1
#                                                                                                                        ·ϕ �
#                                                                                                                               i
# 
# 
#                      α i >0                                             α i >0
# 
#                          m                    m
#                 1
#            =
#                 ns        ∑
#                          i=1
#                                 1−t   i
#                                                ∑
#                                               j=1
#                                                        α j t j K � ,�
#                                                                         i         j
# 
#                          i >0             α j >0
#                      α
# 
# 
# If you are starting to get a headache, it’s perfectly normal: it’s an unfortunate side
# effects of the kernel trick.
# 
# Online SVMs
# Before concluding this chapter, let’s take a quick look at online SVM classifiers (recall
# that online learning means learning incrementally, typically as new instances arrive).
# For linear SVM classifiers, one method is to use Gradient Descent (e.g., using
# SGDClassifier) to minimize the cost function in Equation 5-13, which is derived
# from the primal problem. Unfortunately it converges much more slowly than the
# methods based on QP.
# 
#       Equation 5-13. Linear SVM classifier cost function
#                                                        m
#               1 T
#       J �, b = � · �
#               2
#                                           +       C    ∑ max 0, 1 − t i
#                                                       i=1
#                                                                                        T
#                                                                                       � ·� +b
#                                                                                                 i
# 
# 
# 
# The first sum in the cost function will push the model to have a small weight vector
# w, leading to a larger margin. The second sum computes the total of all margin viola‐
# tions. An instance’s margin violation is equal to 0 if it is located off the street and on
# the correct side, or else it is proportional to the distance to the correct side of the
# street. Minimizing this term ensures that the model makes the margin violations as
# small and as few as possible
# 
# 
#                                                                Hinge Loss
#   The function max(0, 1 – t) is called the hinge loss function (represented below). It is
#   equal to 0 when t ≥ 1. Its derivative (slope) is equal to –1 if t < 1 and 0 if t > 1. It is not
#   differentiable at t = 1, but just like for Lasso Regression (see “Lasso Regression” on
#   page 130) you can still use Gradient Descent using any subderivative at t = 0 (i.e., any
#   value between –1 and 0).
# 
# 
# 
# 
# 164    |       Chapter 5: Support Vector Machines
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Kernelized SVM",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Kernelized SVM"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class KernelizedSVM(HierNode):
    def __init__(self):
        super().__init__("Kernelized SVM")
        self.add(Content())

# eof
