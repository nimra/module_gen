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
#                       Download from finelybook www.finelybook.com
# 
# 
# 
# 
# It is also possible to implement online kernelized SVMs—for example, using “Incre‐
# mental and Decremental SVM Learning”7 or “Fast Kernel Classifiers with Online and
# Active Learning.”8 However, these are implemented in Matlab and C++. For large-
# scale nonlinear problems, you may want to consider using neural networks instead
# (see Part II).
# 
# Exercises
#  1. What is the fundamental idea behind Support Vector Machines?
#  2. What is a support vector?
#  3. Why is it important to scale the inputs when using SVMs?
#  4. Can an SVM classifier output a confidence score when it classifies an instance?
#     What about a probability?
#  5. Should you use the primal or the dual form of the SVM problem to train a model
#     on a training set with millions of instances and hundreds of features?
#  6. Say you trained an SVM classifier with an RBF kernel. It seems to underfit the
#     training set: should you increase or decrease γ (gamma)? What about C?
#  7. How should you set the QP parameters (H, f, A, and b) to solve the soft margin
#     linear SVM classifier problem using an off-the-shelf QP solver?
#  8. Train a LinearSVC on a linearly separable dataset. Then train an SVC and a
#     SGDClassifier on the same dataset. See if you can get them to produce roughly
#     the same model.
#  9. Train an SVM classifier on the MNIST dataset. Since SVM classifiers are binary
#     classifiers, you will need to use one-versus-all to classify all 10 digits. You may
# 
# 
# 7 “Incremental and Decremental Support Vector Machine Learning,” G. Cauwenberghs, T. Poggio (2001).
# 8 “Fast Kernel Classifiers with Online and Active Learning,“ A. Bordes, S. Ertekin, J. Weston, L. Bottou (2005).
# 
# 
# 
#                                                                                                Exercises   |   165
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Online SVMs",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class OnlineSVMs(HierNode):
    def __init__(self):
        super().__init__("Online SVMs")
        self.add(Content(), "content")

# eof
