# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Reshape vs. Resize Method
# NumPy has the np.reshape and np.resize methods. The reshape method returns an
# ndarray with a modified shape without changing the original array, whereas the resize
# method changes the original array. Let’s see an example.
# 
# # generate 9 elements evenly spaced between 0 and 5
# a = np.linspace(0,5,9)
# a
# 'Output':  array([ 0.   ,  0.625,  1.25 ,  1.875,  2.5  ,  3.125,  3.75 ,  
# 4.375,  5.   ])
# # the original shape
# a.shape
# 'Output':  (9,)
# # call the reshape method
# a.reshape(3,3)
# 'Output':
# array([[ 0.   ,  0.625,  1.25 ],
#        [ 1.875,  2.5  ,  3.125],
#        [ 3.75 ,  4.375,  5.   ]])
# # the original array maintained its shape
# a.shape
# 'Output':  (9,)
# # call the resize method - resize does not return an array
# a.resize(3,3)
# # the resize method has changed the shape of the original array
# a.shape
# 'Output':  (3, 3)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Reshape vs. Resize Method",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Reshape vs. Resize Method"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Reshapevs(HierNode):
    def __init__(self):
        super().__init__("Reshape vs. Resize Method")
        self.add(Content())

# eof
