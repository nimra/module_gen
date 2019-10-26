# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Introduction to Broadcasting
# Broadcasting is a term (introduced by NumPy) for when a tensor system’s matrices
# and vectors of different sizes can be added together. These rules allow for convenien‐
# ces like adding a vector to every row of a matrix. Broadcasting rules can be quite
# complex, so we will not dive into a formal discussion of the rules. It’s often easier to
# experiment and see how the broadcasting works (Example 2-18).
# 
# Example 2-18. Examples of broadcasting
# 
# >>> a = tf.ones((2, 2))
# >>> a.eval()
# array([[ 1., 1.],
#        [ 1., 1.]], dtype=float32)
# >>> b = tf.range(0, 2, 1, dtype=tf.float32)
# >>> b.eval()
# array([ 0., 1.], dtype=float32)
# >>> c = a + b
# >>> c.eval()
# array([[ 1., 2.],
#        [ 1., 2.]], dtype=float32)
# 
# Notice that the vector b is added to every row of matrix a. Notice another subtlety; we
# explicitly set the dtype for b. If the dtype isn’t set, TensorFlow will report a type error.
# Let’s see what would have happened if we hadn’t set the dtype (Example 2-19).
# 
# Example 2-19. TensorFlow doesn’t perform implicit type casting
# 
# >>> b = tf.range(0, 2, 1)
# >>> b.eval()
# array([0, 1], dtype=int32)
# >>> c = a + b
# ValueError: Tensor conversion requested dtype float32 for Tensor with dtype int32:
# 'Tensor("range_2:0", shape=(2,), dtype=int32)
# 
# Unlike languages like C, TensorFlow doesn’t perform implicit type casting under the
# hood. It’s often necessary to perform explicit type casts when doing arithmetic opera‐
# tions.
# 
# Imperative and Declarative Programming
# Most situations in computer science involve imperative programming. Consider a
# simple Python program (Example 2-20).
# 
# 
# 
# 
#                                                      Imperative and Declarative Programming   |   37
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Introduction to Broadcasting",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(mbk("# Introduction to Broadcasting"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Introductionto(HierNode):
    def __init__(self):
        super().__init__("Introduction to Broadcasting")
        self.add(Content())

# eof
