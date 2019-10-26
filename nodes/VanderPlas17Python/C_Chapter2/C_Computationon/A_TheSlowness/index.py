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
# ate on each element. For example, imagine we have an array of values and we’d like to
# compute the reciprocal of each. A straightforward approach might look like this:
#     In[1]: import numpy as np
#            np.random.seed(0)
# 
#            def compute_reciprocals(values):
#                output = np.empty(len(values))
#                for i in range(len(values)):
#                    output[i] = 1.0 / values[i]
#                return output
# 
#            values = np.random.randint(1, 10, size=5)
#            compute_reciprocals(values)
#     Out[1]: array([ 0.16666667,   1.        ,   0.25          ,   0.25         ,   0.125           ])
# This implementation probably feels fairly natural to someone from, say, a C or Java
# background. But if we measure the execution time of this code for a large input, we
# see that this operation is very slow, perhaps surprisingly so! We’ll benchmark this
# with IPython’s %timeit magic (discussed in “Profiling and Timing Code” on page 25):
#     In[2]: big_array = np.random.randint(1, 100, size=1000000)
#            %timeit compute_reciprocals(big_array)
#     1 loop, best of 3: 2.91 s per loop
# It takes several seconds to compute these million operations and to store the result!
# When even cell phones have processing speeds measured in Giga-FLOPS (i.e., bil‐
# lions of numerical operations per second), this seems almost absurdly slow. It turns
# out that the bottleneck here is not the operations themselves, but the type-checking
# and function dispatches that CPython must do at each cycle of the loop. Each time
# the reciprocal is computed, Python first examines the object’s type and does a
# dynamic lookup of the correct function to use for that type. If we were working in
# compiled code instead, this type specification would be known before the code exe‐
# cutes and the result could be computed much more efficiently.
# 
# Introducing UFuncs
# For many types of operations, NumPy provides a convenient interface into just this
# kind of statically typed, compiled routine. This is known as a vectorized operation.
# You can accomplish this by simply performing an operation on the array, which will
# then be applied to each element. This vectorized approach is designed to push the
# loop into the compiled layer that underlies NumPy, leading to much faster execution.
# Compare the results of the following two:
#     In[3]: print(compute_reciprocals(values))
#            print(1.0 / values)
# 
# 
# 
# 
#                                             Computation on NumPy Arrays: Universal Functions   |   51
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "The Slowness of Loops",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TheSlowness(HierNode):
    def __init__(self):
        super().__init__("The Slowness of Loops")
        self.add(Content())

# eof
