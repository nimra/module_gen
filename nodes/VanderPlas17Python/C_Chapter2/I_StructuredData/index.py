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

from .A_CreatingStructured.index import CreatingStructured as A_CreatingStructured
from .B_MoreAdvanced.index import MoreAdvanced as B_MoreAdvanced
from .C_RecordArraysStructured.index import RecordArraysStructured as C_RecordArraysStructured
from .D_Onto.index import Onto as D_Onto

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# than the � N 2 of the brute-force algorithm. One example of this is the KD-Tree,
# implemented in Scikit-Learn.
# 
# 
#                                             Big-O Notation
#      Big-O notation is a means of describing how the number of operations required for
#      an algorithm scales as the input grows in size. To use it correctly is to dive deeply into
#      the realm of computer science theory, and to carefully distinguish it from the related
#      small-o notation, big-θ notation, big-Ω notation, and probably many mutant hybrids
#      thereof. While these distinctions add precision to statements about algorithmic scal‐
#      ing, outside computer science theory exams and the remarks of pedantic blog com‐
#      menters, you’ll rarely see such distinctions made in practice. Far more common in the
#      data science world is a less rigid use of big-O notation: as a general (if imprecise)
#      description of the scaling of an algorithm. With apologies to theorists and pedants,
#      this is the interpretation we’ll use throughout this book.
#      Big-O notation, in this loose sense, tells you how much time your algorithm will take
#      as you increase the amount of data. If you have an � N (read “order N”) algorithm
#      that takes 1 second to operate on a list of length N=1,000, then you should expect it to
#      take roughly 5 seconds for a list of length N=5,000. If you have an � N 2 (read “order
#      N squared”) algorithm that takes 1 second for N=1,000, then you should expect it to
#      take about 25 seconds for N=5,000.
#      For our purposes, the N will usually indicate some aspect of the size of the dataset (the
#      number of points, the number of dimensions, etc.). When trying to analyze billions or
#      trillions of samples, the difference between � N and � N 2 can be far from trivial!
#      Notice that the big-O notation by itself tells you nothing about the actual wall-clock
#      time of a computation, but only about its scaling as you change N. Generally, for
#      example, an � N algorithm is considered to have better scaling than an � N 2 algo‐
#      rithm, and for good reason. But for small datasets in particular, the algorithm with
#      better scaling might not be faster. For example, in a given problem an � N 2 algo‐
#      rithm might take 0.01 seconds, while a “better” � N algorithm might take 1 second.
#      Scale up N by a factor of 1,000, though, and the � N algorithm will win out.
#      Even this loose version of Big-O notation can be very useful for comparing the per‐
#      formance of algorithms, and we’ll use this notation throughout the book when talking
#      about how algorithms scale.
# 
# 
# 
# Structured Data: NumPy’s Structured Arrays
# While often our data can be well represented by a homogeneous array of values,
# sometimes this is not the case. This section demonstrates the use of NumPy’s struc‐
# tured arrays and record arrays, which provide efficient storage for compound, hetero‐
# 
# 92     | Chapter 2: Introduction to NumPy
# 
# geneous data. While the patterns shown here are useful for simple operations,
# scenarios like this often lend themselves to the use of Pandas DataFrames, which we’ll
# explore in Chapter 3.
# Imagine that we have several categories of data on a number of people (say, name,
# age, and weight), and we’d like to store these values for use in a Python program. It
# would be possible to store these in three separate arrays:
#     In[2]: name = ['Alice', 'Bob', 'Cathy', 'Doug']
#            age = [25, 45, 37, 19]
#            weight = [55.0, 85.5, 68.0, 61.5]
# But this is a bit clumsy. There’s nothing here that tells us that the three arrays are
# related; it would be more natural if we could use a single structure to store all of this
# data. NumPy can handle this through structured arrays, which are arrays with com‐
# pound data types.
# Recall that previously we created a simple array using an expression like this:
#     In[3]: x = np.zeros(4, dtype=int)
# We can similarly create a structured array using a compound data type specification:
#     In[4]: # Use a compound data type for structured arrays
#            data = np.zeros(4, dtype={'names':('name', 'age', 'weight'),
#                                      'formats':('U10', 'i4', 'f8')})
#            print(data.dtype)
#     [('name', '<U10'), ('age', '<i4'), ('weight', '<f8')]
# 
# Here 'U10' translates to “Unicode string of maximum length 10,” 'i4' translates to
# “4-byte (i.e., 32 bit) integer,” and 'f8' translates to “8-byte (i.e., 64 bit) float.” We’ll
# discuss other options for these type codes in the following section.
# Now that we’ve created an empty container array, we can fill the array with our lists of
# values:
#     In[5]: data['name'] = name
#            data['age'] = age
#            data['weight'] = weight
#            print(data)
#     [('Alice', 25, 55.0) ('Bob', 45, 85.5) ('Cathy', 37, 68.0)
#      ('Doug', 19, 61.5)]
# As we had hoped, the data is now arranged together in one convenient block of
# memory.
# The handy thing with structured arrays is that you can now refer to values either by
# index or by name:
#     In[6]: # Get all names
#            data['name']
# 
# 
# 
#                                                     Structured Data: NumPy’s Structured Arrays   |   93
# 
#      Out[6]: array(['Alice', 'Bob', 'Cathy', 'Doug'],
#                    dtype='<U10')
#      In[7]: # Get first row of data
#             data[0]
#      Out[7]: ('Alice', 25, 55.0)
#      In[8]: # Get the name from the last row
#             data[-1]['name']
#      Out[8]: 'Doug'
# Using Boolean masking, this even allows you to do some more sophisticated opera‐
# tions such as filtering on age:
#      In[9]: # Get names where age is under 30
#             data[data['age'] < 30]['name']
#      Out[9]: array(['Alice', 'Doug'],
#                    dtype='<U10')
# Note that if you’d like to do any operations that are any more complicated than these,
# you should probably consider the Pandas package, covered in the next chapter. As
# we’ll see, Pandas provides a DataFrame object, which is a structure built on NumPy
# arrays that offers a variety of useful data manipulation functionality similar to what
# we’ve shown here, as well as much, much more.
# 
# Creating Structured Arrays
# Structured array data types can be specified in a number of ways. Earlier, we saw the
# dictionary method:
#      In[10]: np.dtype({'names':('name', 'age', 'weight'),
#                        'formats':('U10', 'i4', 'f8')})
#      Out[10]: dtype([('name', '<U10'), ('age', '<i4'), ('weight', '<f8')])
# 
# For clarity, numerical types can be specified with Python types or NumPy dtypes
# instead:
#      In[11]: np.dtype({'names':('name', 'age', 'weight'),
#                        'formats':((np.str_, 10), int, np.float32)})
#      Out[11]: dtype([('name', '<U10'), ('age', '<i8'), ('weight', '<f4')])
# A compound type can also be specified as a list of tuples:
#      In[12]: np.dtype([('name', 'S10'), ('age', 'i4'), ('weight', 'f8')])
#      Out[12]: dtype([('name', 'S10'), ('age', '<i4'), ('weight', '<f8')])
# If the names of the types do not matter to you, you can specify the types alone in a
# comma-separated string:
#      In[13]: np.dtype('S10,i4,f8')
# 
# 
# 
# 94   |   Chapter 2: Introduction to NumPy
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Structured Data: NumPy’s Structured Arrays",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class StructuredData(HierNode):
    def __init__(self):
        super().__init__("Structured Data: NumPy’s Structured Arrays")
        self.add(Content())
        self.add(A_CreatingStructured())
        self.add(B_MoreAdvanced())
        self.add(C_RecordArraysStructured())
        self.add(D_Onto())

# eof
