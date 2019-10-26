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
# explicitly declared, a dynamically typed language like Python skips this specification.
# For example, in C you might specify a particular operation as follows:
#     /* C code */
#     int result = 0;
#     for(int i=0; i<100; i++){
#         result += i;
#     }
# While in Python the equivalent operation could be written this way:
#     # Python code
#     result = 0
#     for i in range(100):
#         result += i
# Notice the main difference: in C, the data types of each variable are explicitly
# declared, while in Python the types are dynamically inferred. This means, for exam‐
# ple, that we can assign any kind of data to any variable:
#     # Python code
#     x = 4
#     x = "four"
# 
# Here we’ve switched the contents of x from an integer to a string. The same thing in C
# would lead (depending on compiler settings) to a compilation error or other uninten‐
# ded consequences:
#     /* C code */
#     int x = 4;
#     x = "four"; // FAILS
# This sort of flexibility is one piece that makes Python and other dynamically typed
# languages convenient and easy to use. Understanding how this works is an important
# piece of learning to analyze data efficiently and effectively with Python. But what this
# type flexibility also points to is the fact that Python variables are more than just their
# value; they also contain extra information about the type of the value. We’ll explore
# this more in the sections that follow.
# 
# A Python Integer Is More Than Just an Integer
# The standard Python implementation is written in C. This means that every Python
# object is simply a cleverly disguised C structure, which contains not only its value, but
# other information as well. For example, when we define an integer in Python, such as
# x = 10000, x is not just a “raw” integer. It’s actually a pointer to a compound C struc‐
# ture, which contains several values. Looking through the Python 3.4 source code, we
# find that the integer (long) type definition effectively looks like this (once the C mac‐
# ros are expanded):
# 
# 
# 
# 
#                                                         Understanding Data Types in Python   |   35
# 
#       struct _longobject {
#           long ob_refcnt;
#           PyTypeObject *ob_type;
#           size_t ob_size;
#           long ob_digit[1];
#       };
# A single integer in Python 3.4 actually contains four pieces:
# 
#      • ob_refcnt, a reference count that helps Python silently handle memory alloca‐
#        tion and deallocation
#      • ob_type, which encodes the type of the variable
#      • ob_size, which specifies the size of the following data members
#      • ob_digit, which contains the actual integer value that we expect the Python vari‐
#        able to represent
# 
# This means that there is some overhead in storing an integer in Python as compared
# to an integer in a compiled language like C, as illustrated in Figure 2-1.
# 
# 
# 
# 
# Figure 2-1. The difference between C and Python integers
# 
# Here PyObject_HEAD is the part of the structure containing the reference count, type
# code, and other pieces mentioned before.
# Notice the difference here: a C integer is essentially a label for a position in memory
# whose bytes encode an integer value. A Python integer is a pointer to a position in
# memory containing all the Python object information, including the bytes that con‐
# tain the integer value. This extra information in the Python integer structure is what
# allows Python to be coded so freely and dynamically. All this additional information
# in Python types comes at a cost, however, which becomes especially apparent in
# structures that combine many of these objects.
# 
# 
# 
# 
# 36    |   Chapter 2: Introduction to NumPy
# 
# A Python List Is More Than Just a List
# Let’s consider now what happens when we use a Python data structure that holds
# many Python objects. The standard mutable multielement container in Python is the
# list. We can create a list of integers as follows:
#     In[1]: L = list(range(10))
#            L
#     Out[1]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     In[2]: type(L[0])
#     Out[2]: int
# Or, similarly, a list of strings:
#     In[3]: L2 = [str(c) for c in L]
#            L2
#     Out[3]: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     In[4]: type(L2[0])
#     Out[4]: str
# Because of Python’s dynamic typing, we can even create heterogeneous lists:
#     In[5]: L3 = [True, "2", 3.0, 4]
#            [type(item) for item in L3]
#     Out[5]: [bool, str, float, int]
# But this flexibility comes at a cost: to allow these flexible types, each item in the list
# must contain its own type info, reference count, and other information—that is, each
# item is a complete Python object. In the special case that all variables are of the same
# type, much of this information is redundant: it can be much more efficient to store
# data in a fixed-type array. The difference between a dynamic-type list and a fixed-type
# (NumPy-style) array is illustrated in Figure 2-2.
# At the implementation level, the array essentially contains a single pointer to one con‐
# tiguous block of data. The Python list, on the other hand, contains a pointer to a
# block of pointers, each of which in turn points to a full Python object like the Python
# integer we saw earlier. Again, the advantage of the list is flexibility: because each list
# element is a full structure containing both data and type information, the list can be
# filled with data of any desired type. Fixed-type NumPy-style arrays lack this flexibil‐
# ity, but are much more efficient for storing and manipulating data.
# 
# 
# 
# 
#                                                         Understanding Data Types in Python   |   37
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "A Python Integer Is More Than Just an Integer",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class APython(HierNode):
    def __init__(self):
        super().__init__("A Python Integer Is More Than Just an Integer")
        self.add(Content())

# eof
