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
#      [ 0.16666667 1.                        0.25      0.25        0.125        ]
#      [ 0.16666667 1.                        0.25      0.25        0.125        ]
# Looking at the execution time for our big array, we see that it completes orders of
# magnitude faster than the Python loop:
#      In[4]: %timeit (1.0 / big_array)
#      100 loops, best of 3: 4.6 ms per loop
# Vectorized operations in NumPy are implemented via ufuncs, whose main purpose is
# to quickly execute repeated operations on values in NumPy arrays. Ufuncs are
# extremely flexible—before we saw an operation between a scalar and an array, but we
# can also operate between two arrays:
#      In[5]: np.arange(5) / np.arange(1, 6)
#      Out[5]: array([ 0.                     ,   0.5   ,   0.66666667,   0.75       ,   0.8   ])
# And ufunc operations are not limited to one-dimensional arrays—they can act on
# multidimensional arrays as well:
#      In[6]: x = np.arange(9).reshape((3, 3))
#             2 ** x
#      Out[6]: array([[ 1,    2,   4],
#                     [ 8, 16, 32],
#                     [ 64, 128, 256]])
# Computations using vectorization through ufuncs are nearly always more efficient
# than their counterpart implemented through Python loops, especially as the arrays
# grow in size. Any time you see such a loop in a Python script, you should consider
# whether it can be replaced with a vectorized expression.
# 
# Exploring NumPy’s UFuncs
# Ufuncs exist in two flavors: unary ufuncs, which operate on a single input, and binary
# ufuncs, which operate on two inputs. We’ll see examples of both these types of func‐
# tions here.
# 
# Array arithmetic
# NumPy’s ufuncs feel very natural to use because they make use of Python’s native
# arithmetic operators. The standard addition, subtraction, multiplication, and division
# can all be used:
#      In[7]: x = np.arange(4)
#             print("x     =",          x)
#             print("x + 5 =",          x + 5)
#             print("x - 5 =",          x - 5)
#             print("x * 2 =",          x * 2)
# 
# 
# 
# 
# 52   |   Chapter 2: Introduction to NumPy
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Introducing UFuncs",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class IntroducingUFuncs(HierNode):
    def __init__(self):
        super().__init__("Introducing UFuncs")
        self.add(Content())

# eof
