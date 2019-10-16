# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Moreon.index import Moreon as A_Moreon
from .B_Strings.index import Strings as B_Strings

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Data Types
# Python has the number and string data types in addition to other supported specialized
# datatypes. The number datatype, for instance, can be an int or a float. Strings are
# surrounded by quotes in Python.
# 
# # data types
# type(3)
# 'Output': int
# type(3.0)
# 'Output': float
# type('Jesam Ujong')
# 'Output': str
# 
#    Other fundamental data types in Python include the lists, tuple, and dictionary.
# These data types hold a group of items together in sequence. Sequences in Python are
# indexed from 0.
#    Tuples are an immutable ordered sequence of items. Immutable means the data
# cannot be changed after being assigned. Tuple can contain elements of different types.
# Tuples are surrounded by brackets (…).
# 
# my_tuple = (5, 4, 3, 2, 1, 'hello')
# type(my_tuple)
# 'Output': tuple
# my_tuple[5]           # return the sixth element (indexed from 0)
# 'Output': 'hello'
# my_tuple[5] = 'hi'    # we cannot alter an immutable data type
# Traceback (most recent call last):
# 
#   File "<ipython-input-49-f0e593f95bc7>", line 1, in <module>
#     my_tuple[5] = 'hi'
# 
# TypeError: 'tuple' object does not support item assignment
# 
#     Lists are very similar to tuples, only that they are mutable. This means that list elements
# can be changed after being assigned. Lists are surrounded by square brackets […].
# 
# my_list = [4, 8, 16, 32, 64]
# print(my_list)    # print list items to console
# 'Output': [4, 8, 16, 32, 64]
# my_list[3]        # return the fourth list element (indexed from 0)
# 'Output': 32
# my_list[4] = 256
# print(my_list)
# 'Output': [4, 8, 16, 32, 256]
# 
#     Dictionaries contain a mapping from keys to values. A key/value pair is an item in a
# dictionary. The items in a dictionary are indexed by their keys. The keys in a dictionary
# can be any hashable datatype (hashing transforms a string of characters into a key to
# speed up search). Values can be of any datatype. In other languages, a dictionary is
# analogous to a hash table or a map. Dictionaries are surrounded by a pair of braces {…}.
# A dictionary is not ordered.
# 
# my_dict = {'name':'Rijami', 'age':42, 'height':72}
# my_dict               # dictionary items are un-ordered
# 'Output': {'age': 42, 'height': 72, 'name': 'Rijami'}
# my_dict['age']        # get dictionary value by indexing on keys
# 'Output': 42
# my_dict['age'] = 35   # change the value of a dictionary item
# my_dict['age']
# 'Output': 35

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Data Types",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Data Types"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DataTypes(HierNode):
    def __init__(self):
        super().__init__("Data Types")
        self.add(Content())
        self.add(A_Moreon())
        self.add(B_Strings())

# eof
