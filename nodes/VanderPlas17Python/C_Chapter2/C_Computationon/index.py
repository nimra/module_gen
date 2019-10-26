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

from .A_TheSlowness.index import TheSlowness as A_TheSlowness
from .B_IntroducingUFuncs.index import IntroducingUFuncs as B_IntroducingUFuncs
from .C_ExploringNumPys.index import ExploringNumPys as C_ExploringNumPys
from .D_AdvancedUfunc.index import AdvancedUfunc as D_AdvancedUfunc
from .E_UfuncsLearning.index import UfuncsLearning as E_UfuncsLearning

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#      [[ 8 9 10 11]
#       [12 13 14 15]]
#      In[53]: left, right = np.hsplit(grid, [2])
#              print(left)
#              print(right)
#      [[ 0 1]
#       [ 4 5]
#       [ 8 9]
#       [12 13]]
#      [[ 2 3]
#       [ 6 7]
#       [10 11]
#       [14 15]]
# 
# Similarly, np.dsplit will split arrays along the third axis.
# 
# Computation on NumPy Arrays: Universal Functions
# Up until now, we have been discussing some of the basic nuts and bolts of NumPy; in
# the next few sections, we will dive into the reasons that NumPy is so important in the
# Python data science world. Namely, it provides an easy and flexible interface to opti‐
# mized computation with arrays of data.
# Computation on NumPy arrays can be very fast, or it can be very slow. The key to
# making it fast is to use vectorized operations, generally implemented through Num‐
# Py’s universal functions (ufuncs). This section motivates the need for NumPy’s ufuncs,
# which can be used to make repeated calculations on array elements much more effi‐
# cient. It then introduces many of the most common and useful arithmetic ufuncs
# available in the NumPy package.
# 
# The Slowness of Loops
# Python’s default implementation (known as CPython) does some operations very
# slowly. This is in part due to the dynamic, interpreted nature of the language: the fact
# that types are flexible, so that sequences of operations cannot be compiled down to
# efficient machine code as in languages like C and Fortran. Recently there have been
# various attempts to address this weakness: well-known examples are the PyPy project,
# a just-in-time compiled implementation of Python; the Cython project, which con‐
# verts Python code to compilable C code; and the Numba project, which converts
# snippets of Python code to fast LLVM bytecode. Each of these has its strengths and
# weaknesses, but it is safe to say that none of the three approaches has yet surpassed
# the reach and popularity of the standard CPython engine.
# The relative sluggishness of Python generally manifests itself in situations where
# many small operations are being repeated—for instance, looping over arrays to oper‐
# 
# 
# 
# 50   |   Chapter 2: Introduction to NumPy
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Computation on NumPy Arrays: Universal Functions",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Computationon(HierNode):
    def __init__(self):
        super().__init__("Computation on NumPy Arrays: Universal Functions")
        self.add(Content())
        self.add(A_TheSlowness())
        self.add(B_IntroducingUFuncs())
        self.add(C_ExploringNumPys())
        self.add(D_AdvancedUfunc())
        self.add(E_UfuncsLearning())

# eof
