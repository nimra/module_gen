# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# learning and its foundation on continuous, vectorial mathematics. Modern machine
# learning is founded upon the manipulation and calculus of tensors.
# 
# Scalars, Vectors, and Matrices
# To start, we will give some simple examples of tensors that you might be familiar
# with. The simplest example of a tensor is a scalar, a single constant value drawn from
# the real numbers (recall that the real numbers are decimal numbers of arbitrary pre‐
# cision, with both positive and negative numbers permitted). Mathematically, we
# denote the real numbers by ℝ. More formally, we call a scalar a rank-0 tensor.
# 
#                          Aside on Fields
#                          Mathematically sophisticated readers will protest that it’s entirely
#                          meaningful to define tensors based on the complex numbers, or
#                          with binary numbers. More generally, it’s sufficient that the num‐
#                          bers come from a field: a mathematical collection of numbers
#                          where 0, 1, addition, multiplication, subtraction, and division are
#                          defined. Common fields include the real numbers ℝ, the rational
#                          numbers ℚ, the complex numbers ℂ, and finite fields such as ℤ2.
#                          For simplicity, in much of the discussion, we will assume real val‐
#                          ued tensors, but substituting in values from other fields is entirely
#                          reasonable.
# 
# If scalars are rank-0 tensors, what constitutes a rank-1 tensor? Formally, speaking, a
# rank-1 tensor is a vector; a list of real numbers. Traditionally, vectors are written as
# either column vectors
# 
#          a
#          b
# 
# or as row vectors
# 
#          a b
# 
# Notationally, the collection of all column vectors of length 2 is denoted ℝ2 × 1 while
# the set of all row vectors of length 2 is ℝ1 × 2. More computationally, we might say
# that the shape of a column vector is (2, 1), while the shape of a row vector is (1, 2). If
# we don’t wish to specify whether a vector is a row vector or column vector, we can say
# it comes from the set ℝ2 and has shape (2). This notion of tensor shape is quite
# important for understanding TensorFlow computations, and we will return to it later
# on in this chapter.
# 
# 
# 
# 20   |       Chapter 2: Introduction to TensorFlow Primitives
# 
# One of the simplest uses of vectors is to represent coordinates in the real world. Sup‐
# pose that we decide on an origin point (say the position where you’re currently stand‐
# ing). Then any position in the world can be represented by three displacement values
# from your current position (left-right displacement, front-back displacement, up-
# down displacement). Thus, the set of vectors (vector space) ℝ3 can represent any
# position in the world.
# For a different example, let’s suppose that a cat is described by its height, weight, and
# color. Then a video game cat can be represented as a vector
# 
#     height
#     weight
#     color
# 
# in the space ℝ3. This type of representation is often called a featurization. That is, a
# featurization is a representation of a real-world entity as a vector (or more generally
# as a tensor). Nearly all machine learning algorithms operate on vectors or tensors.
# Thus the process of featurization is a critical part of any machine learning pipeline.
# Often, the featurization system can be the most sophisticated part of a machine learn‐
# ing system. Suppose we have a benzene molecule as illustrated in Figure 2-1.
# 
# 
# 
# 
# Figure 2-1. A representation of a benzene molecule.
# 
# How can we transform this molecule into a vector suitable for a query to a machine
# learning system? There are a number of potential solutions to this problem, most of
# which exploit the idea of marking the presence of subfragments of the molecule. The
# presence or absence of specific subfragments is marked by setting indices in a binary
# vector (in 0, 1 n) to 1/0, respectively. This process is illustrated in Figure 2-2.
# 
# 
# 
# 
#                                                                    Introducing Tensors   |   21
# 
# Figure 2-2. Subfragments of the molecule to be featurized are selected (those containing
# OH). These fragments are hashed into indices in a fixed-length vector. These positions
# are set to 1 and all other positions are set to 0.
# 
# Note that this process sounds (and is) fairly complex. In fact, one of the most chal‐
# lenging aspects of building a machine learning system is deciding how to transform
# the data in question into a tensorial format. For some types of data, this transforma‐
# tion is obvious. For others (such as molecules), the transformation required can be
# quite subtle. For the practitioner of machine learning, it isn’t usually necessary to
# invent a new featurization method since the scholarly literature is extensive, but it will
# often be necessary to read research papers to understand best practices for transform‐
# ing a new data stream.
# Now that we have established that rank-0 tensors are scalars (ℝ) and that rank-1 ten‐
# sors are vectors (ℝn), what is a rank-2 tensor? Traditionally, a rank-2 tensor is
# referred to as a matrix:
# 
#          a b
#          c d
# 
# This matrix has two rows and two columns. The set of all such matrices is referred to
# as ℝ2 × 2. Returning to our notion of tensor shape earlier, the shape of this matrix is
# 
# 
# 22   |    Chapter 2: Introduction to TensorFlow Primitives
# 
# (2, 2). Matrices are traditionally used to represent transformations of vectors. For
# example, the action of rotating a vector in the plane by angle α can be performed by
# the matrix
# 
#           cos α –sin α
#    Rα =
#           sin α cos α
# 
# To see this, note that the x unit vector (1, 0) is transformed by matrix multiplication
# into the vector (cos (α), sin (α)). (We will cover the detailed definition of matrix mul‐
# tiplication later in the chapter, but will simply display the result for the moment).
# 
#     cos α –sin α   1   cos α
#                  ·   =
#     sin α cos α    0   sin α
# 
# This transformation can be visualized graphically as well. Figure 2-3 demonstrates
# how the final vector corresponds to a rotation of the original unit vector.
# 
# 
# 
# 
# Figure 2-3. Positions on the unit circle are parameterized by cosine and sine.
# 
# 
#                                                                      Introducing Tensors   |   23
# 
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Scalars, Vectors, and Matrices",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(mbk("# Scalars, Vectors, and Matrices"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ScalarsVectors(HierNode):
    def __init__(self):
        super().__init__("Scalars, Vectors, and Matrices")
        self.add(Content())

# eof
