# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# NumPy 1-D Array
# Let’s create a simple 1-D NumPy array:
# 
# my_array = np.array([2,4,6,8,10])
# my_array
# 'Output': array([ 2,  4,  6,  8, 10])
# # the data-type of a NumPy array is the ndarray
# type(my_array)
# 'Output': numpy.ndarray
# 
# # a NumPy 1-D array can also be seen a vector with 1 dimension
# my_array.ndim
# 'Output': 1
# # check the shape to get the number of rows and columns in the array \
# # read as (rows, columns)
# my_array.shape
# 'Output': (5,)
# 
#      We can also create an array from a Python list.
# 
# my_list = [9, 5, 2, 7]
# type(my_list)
# 'Output': list
# # convert a list to a numpy array
# list_to_array = np.array(my_list) # or np.asarray(my_list)
# type(list_to_array)
# 'Output': numpy.ndarray
# 
#      Let’s explore other useful methods often employed for creating arrays.
# 
# # create an array from a range of numbers
# np.arange(10)
# 'Output': [0 1 2 3 4 5 6 7 8 9]
# # create an array from start to end (exclusive) via a step size - (start,
# stop, step)
# np.arange(2, 10, 2)
# 'Output': [2 4 6 8]
# # create a range of points between two numbers
# np.linspace(2, 10, 5)
# 'Output': array([  2.,   4.,   6.,   8.,  10.])
# # create an array of ones
# np.ones(5)
# 'Output': array([ 1.,  1.,  1.,  1.,  1.])
# # create an array of zeros
# np.zeros(5)
# 'Output': array([ 0.,  0.,  0.,  0.,  0.])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "NumPy 1-D Array",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# NumPy 1-D Array"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class NumPy1D(HierNode):
    def __init__(self):
        super().__init__("NumPy 1-D Array")
        self.add(Content())

# eof
