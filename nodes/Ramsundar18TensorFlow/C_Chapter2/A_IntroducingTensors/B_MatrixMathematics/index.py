# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Matrix Mathematics
# There are a number of standard mathematical operations on matrices that machine
# learning programs use repeatedly. We will briefly review some of the most fundamen‐
# tal of these operations.
# The matrix transpose is a convenient operation that flips a matrix around its diago‐
# nal. Mathematically, suppose A is a matrix; then the transpose matrix AT is defined by
# equation ATi j = A ji. For example, the transpose of the rotation matrix Rα is
# 
#                cos α sin α
#      RTα =
#                –sin α cos α
# 
# Addition of matrices is only defined for matrices of the same shape and is simply per‐
# formed elementwise. For example:
# 
#      1 2   1 1   2 3
#          +     =
#      3 4   1 1   4 5
# 
# Similarly, matrices can be multiplied by scalars. In this case, each element of the
# matrix is simply multiplied elementwise by the scalar in question:
# 
#           1 2   2 4
#      2·       =
#           3 4   6 8
# 
# Furthermore, it is sometimes possible to multiply two matrices directly. This notion
# of matrix multiplication is probably the most important mathematical concept associ‐
# ated with matrices. Note specifically that matrix multiplication is not the same notion
# as elementwise multiplication of matrices! Rather, suppose we have a matrix A of
# shape (m, n) with m rows and n columns. Then, A can be multiplied on the right by
# any matrix B of shape (n, k) (where k is any positive integer) to form matrix AB of
# shape (m, k). For the actual mathematical description, suppose A is a matrix of shape
# (m, n) and B is a matrix of shape (n, k). Then AB is defined by
# 
#      AB   ij   =   ∑k AikBk j
# 
# We displayed a matrix multiplication equation earlier in brief. Let’s expand that
# example now that we have the formal definition:
# 
#      cos α –sin α   1   cos α · 1 – sin α · 0   cos α
#                   ·   =                       =
#      sin α cos α    0   sin α · 1 – cos α · 0   sin α
# 
# 
# 24   | Chapter 2: Introduction to TensorFlow Primitives
# 
# The fundamental takeaway is that rows of one matrix are multiplied against columns
# of the other matrix.
# This definition hides a number of subtleties. Note first that matrix multiplication is
# not commutative. That is, AB ≠ BA in general. In fact, AB can exist when BA is not
# meaningful. Suppose, for example, A is a matrix of shape (2, 3) and B is a matrix of
# shape (3, 4). Then AB is a matrix of shape (2, 4). However, BA is not defined since the
# respective dimensions (4 and 2) don’t match. As another subtlety, note that, as in the
# rotation example, a matrix of shape (m, n) can be multiplied on the right by a matrix
# of shape (n, 1). However, a matrix of shape (n, 1) is simply a column vector. So, it is
# meaningful to multiply matrices by vectors. Matrix-vector multiplication is one of the
# fundamental building blocks of common machine learning systems.
# One of the nicest properties of standard multiplication is that it is a linear operation.
# More precisely, a function f is called linear if f x + y = f x + f y and f cx = c f x
# where c is a scalar. To demonstrate that scalar multiplication is linear, suppose that a,
# b, c, d are all real numbers. Then we have
# 
#    a · b · c = b · ac
# 
#    a · c + d = ac + ad
# 
# We make use of the commutative and distributive properties of scalar multiplication
# here. Now suppose that instead, A, C, D are now matrices where C, D are of the same
# size and it is meaningful to multiply A on the right with either C or D (b remains a
# real number). Then matrix multiplication is a linear operator:
# 
#    A b · C = b · AC
# 
#    A C + D = AC + AD
# 
# Put another way, matrix multiplication is distributive and commutes with scalar mul‐
# tiplication. In fact, it can be shown that any linear transformation on vectors corre‐
# sponds to a matrix multiplication. For a computer science analogy, think of linearity
# as a property demanded by an abstract method in a superclass. Then standard multi‐
# plication and matrix multiplication are concrete implementations of that abstract
# method for different subclasses (respectively real numbers and matrices).
# 
# Tensors
# In the previous sections, we introduced the notion of scalars as rank-0 tensors, vec‐
# tors as rank-1 tensors, and matrices as rank-2 tensors. What then is a rank-3 tensor?
# Before passing to a general definition, it can help to think about the commonalities
# 
# 
#                                                                    Introducing Tensors   |   25
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Matrix Mathematics",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(mbk("# Matrix Mathematics"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MatrixMathematics(HierNode):
    def __init__(self):
        super().__init__("Matrix Mathematics")
        self.add(Content())

# eof
