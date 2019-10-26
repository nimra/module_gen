# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# of shape (224, 224, 3). Continuing the analogy, consider a color video. Suppose that
# each frame of the video is a 224 × 224 color image. Then a minute of video (at 60 fps)
# would be a rank-4 tensor of shape (224, 224, 3, 3600). Continuing even further, a col‐
# lection of 10 such videos would then form a rank-5 tensor of shape (10, 224, 224, 3,
# 3600). In general, tensors provide for a convenient representation of numeric data. In
# practice, it’s not common to see tensors of higher order than rank-5 tensors, but it’s
# smart to design any tensor software to allow for arbitrary tensors since intelligent
# users will always come up with use cases designers don’t consider.
# 
# Tensors in Physics
# Tensors are used widely in physics to encode fundamental physical quantities. For
# example, the stress tensor is commonly used in material science to define the stress at
# a point within a material. Mathematically, the stress tensor is a rank-2 tensor of shape
# (3, 3):
# 
#         σ 11 τ12 τ13
#    σ = τ21 σ 22 τ23
#         τ31 τ32 σ 33
# 
# 
# Then, suppose that n is a vector of shape (3) that encodes a direction. The stress T n in
# direction n is specified by the vector T n = T · n (note the matrix-vector multiplica‐
# tion). This relationship is depicted pictorially in Figure 2-5.
# 
# 
# 
# 
# Figure 2-5. A 3D pictorial depiction of the components of stress.
# 
# 
#                                                                     Introducing Tensors   |   27
# 
# As another physical example, Einstein’s field equations of general relativity are com‐
# monly expressed in tensorial format:
# 
#           1               8πG
#      Rμν − Rg μν + Λg μν = 4 T μν
#           2                c
# 
# Here Rμν is the Ricci curvature tensor, g μν is the metric tensor, T μν is the stress-energy
# tensor, and the remaining quantities are scalars. Note, however, that there’s an impor‐
# tant subtlety distinguishing these tensors and the other tensors we’ve discussed previ‐
# ously. Quantities like the metric tensor provide a separate tensor (in the sense of an
# array of numbers) for each point in space-time (mathematically, the metric tensor is a
# tensor field). The same holds for the stress tensor previously discussed, and for the
# other tensors in these equations. At a given point in space-time, each of these quanti‐
# ties becomes a symmetric rank-2 tensor of shape (4, 4) using our notation.
# Part of the power of modern tensor calculus systems such as TensorFlow is that some
# of the mathematical machinery long used for classical physics can now be adapted to
# solve applied problems in image processing and language understanding. At the same
# time, today’s tensor calculus systems are still limited compared with the mathematical
# machinery of physicists. For example, there’s no simple way to talk about a quantity
# such as the metric tensor using TensorFlow yet. We hope that as tensor calculus
# becomes more fundamental to computer science, the situation will change and that
# systems like TensorFlow will serve as a bridge between the physical world and the
# computational world.
# 
# Mathematical Asides
# The discussion so far in this chapter has introduced tensors informally via example
# and illustration. In our definition, a tensor is simply an array of numbers. It’s often
# convenient to view a tensor as a function instead. The most common definition intro‐
# duces a tensor as a multilinear function from a product of vector spaces to the real
# numbers:
# 
#      T: V 1 × V 2 × ⋯V n          ℝ
# 
# This definition uses a number of terms you haven’t seen. A vector space is simply a
# collection of vectors. You’ve seen a few examples of vector spaces such as ℝ3 or gener‐
#                                                                   d
# ally ℝn. We won’t lose any generality by holding that V i = ℝ i. As we defined previ‐
# ously, a function f is linear if f x + y = f x + f y and f cx = c f x . A multilinear
# function is simply a function that is linear in each argument. This function can be
# 
# 
# 
# 
# 28   |   Chapter 2: Introduction to TensorFlow Primitives
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Tensors in Physics",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(mbk("# Tensors in Physics"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Tensorsin(HierNode):
    def __init__(self):
        super().__init__("Tensors in Physics")
        self.add(Content())

# eof
