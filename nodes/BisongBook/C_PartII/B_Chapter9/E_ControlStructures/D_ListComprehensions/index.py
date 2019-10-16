# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# List Comprehensions
# Using list comprehension, we can succinctly rewrite a for loop that iteratively builds a
# new list using an elegant syntax. Assuming we want to build a new list using a for loop,
# we will write it as
# 
# new_list = []
# for item in iterable:
#     new_list.append(expression)
# 
#    We can rewrite this as
# 
# [expression for item in iterable]
# 
#    Let’s have some program examples.
# 
# squares = []
# for elem in range(0,5):
#     squares.append((elem+1)**2)
# 
# squares
# 'Output': [1, 4, 9, 16, 25]
# 
#    The preceding code can be concisely written as
# 
# [(elem+1)**2 for elem in range(0,5)]
# 'Output': [1, 4, 9, 16, 25]
# 
#    This is even more elegant in the presence of nested control structures.
# 
# evens = []
# for elem in range(0,20):
#     if elem % 2 == 0 and elem != 0:
#         evens.append(elem)
# 
# evens
# 'Output': [2, 4, 6, 8, 10, 12, 14, 16, 18]
# 
#    With list comprehension, we can code this as
# 
# [elem for elem in range(0,20) if elem % 2 == 0 and elem != 0]
# 'Output': [2, 4, 6, 8, 10, 12, 14, 16, 18]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "List Comprehensions",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# List Comprehensions"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ListComprehensions(HierNode):
    def __init__(self):
        super().__init__("List Comprehensions")
        self.add(Content())

# eof
