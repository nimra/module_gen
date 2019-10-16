# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# >>> c = tf.matmul(a, b)
# >>> c.eval()
# array([[ 3., 3., 3., 3.],
#        [ 3., 3., 3., 3.]], dtype=float32)
# 
# You can check that this answer matches the mathematical definition of matrix multi‐
# plication we provided earlier.
# 
# Tensor Types
# You may have noticed the dtype notation in the preceding examples. Tensors in Ten‐
# sorFlow come in a variety of types such as tf.float32, tf.float64, tf.int32,
# tf.int64. It’s possible to to create tensors of specified types by setting dtype in tensor
# construction functions. Furthermore, given a tensor, it’s possible to change its type
# using casting functions such as tf.to_double(), tf.to_float(), tf.to_int32(),
# tf.to_int64(), and others (Example 2-15).
# 
# Example 2-15. Creating tensors of different types
# 
# >>> a = tf.ones((2,2), dtype=tf.int32)
# >>> a.eval()
# array([[0, 0],
#        [0, 0]], dtype=int32)
# >>> b = tf.to_float(a)
# >>> b.eval()
# array([[ 0., 0.],
#        [ 0., 0.]], dtype=float32)
# 
# 
# Tensor Shape Manipulations
# Within TensorFlow, tensors are just collections of numbers written in memory. The
# different shapes are views into the underlying set of numbers that provide different
# ways of interacting with the set of numbers. At different times, it can be useful to view
# the same set of numbers as forming tensors with different shapes. tf.reshape()
# allows tensors to be converted into tensors with different shapes (Example 2-16).
# 
# Example 2-16. Manipulating tensor shapes
# 
# >>> a = tf.ones(8)
# >>> a.eval()
# array([ 1., 1., 1., 1., 1., 1.,          1.,   1.], dtype=float32)
# >>> b = tf.reshape(a, (4, 2))
# >>> b.eval()
# array([[ 1., 1.],
#        [ 1., 1.],
#        [ 1., 1.],
#        [ 1., 1.]], dtype=float32)
# 
# 
# 
#                                                           Basic Computations in TensorFlow   |   35
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Tensor Types",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Tensor Types"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TensorTypes(HierNode):
    def __init__(self):
        super().__init__("Tensor Types")
        self.add(Content())

# eof
