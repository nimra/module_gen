# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_MatrixMultiplication.index import MatrixMultiplication as A_MatrixMultiplication
from .B_ElementWiseOperations.index import ElementWiseOperations as B_ElementWiseOperations
from .C_ScalarOperation.index import ScalarOperation as C_ScalarOperation
from .D_MatrixTransposition.index import MatrixTransposition as D_MatrixTransposition
from .E_TheInverse.index import TheInverse as E_TheInverse

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Matrix Operations: Linear Algebra
# Linear algebra is a convenient and powerful system for manipulating a set of data
# features and is one of the strong points of NumPy. Linear algebra is a crucial component
# of machine learning and deep learning research and implementation of learning
# algorithms. NumPy has vectorized routines for various matrix operations. Let’s go
# through a few of them.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Matrix Operations: Linear Algebra",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Matrix Operations: Linear Algebra"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MatrixOperations(HierNode):
    def __init__(self):
        super().__init__("Matrix Operations: Linear Algebra")
        self.add(Content())
        self.add(A_MatrixMultiplication())
        self.add(B_ElementWiseOperations())
        self.add(C_ScalarOperation())
        self.add(D_MatrixTransposition())
        self.add(E_TheInverse())

# eof
