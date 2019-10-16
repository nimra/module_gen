# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Review
# In this chapter, we’ve shown you how to build and train some simple learning systems
# in TensorFlow. We started by reviewing some foundational mathematical concepts
# including loss functions and gradient descent. We then introduced you to some new
# TensorFlow concepts such as placeholders, scopes, and TensorBoard. We ended the
# chapter with case studies that trained linear and logistic regression systems on toy
# datasets. We covered a lot of material in this chapter, and it’s OK if you haven’t yet
# internalized everything. The foundational material introduced here will be used
# throughout the remainder of this book.
# In Chapter 4, we will introduce you to your first deep learning model and to fully
# connected networks, and will show you how to define and train fully connected net‐
# works in TensorFlow. In following chapters, we will explore more complicated deep
# networks, but all of these architectures will use the same fundamental learning princi‐
# ples introduced in this chapter.
# 
# 
# 
# 
#                                                                            Review   |   79
# 
# 
#                                                                           CHAPTER 4
#                         Fully Connected Deep Networks
# 
# 
# 
# 
# This chapter will introduce you to fully connected deep networks. Fully connected
# networks are the workhorses of deep learning, used for thousands of applications.
# The major advantage of fully connected networks is that they are “structure agnostic.”
# That is, no special assumptions need to be made about the input (for example, that
# the input consists of images or videos). We will make use of this generality to use fully
# connected deep networks to address a problem in chemical modeling later in this
# chapter.
# We delve briefly into the mathematical theory underpinning fully connected net‐
# works. In particular, we explore the concept that fully connected architectures are
# “universal approximators” capable of learning any function. This concept provides an
# explanation of the generality of fully connected architectures, but comes with many
# caveats that we discuss at some depth.
# While being structure agnostic makes fully connected networks very broadly applica‐
# ble, such networks do tend to have weaker performance than special-purpose net‐
# works tuned to the structure of a problem space. We will discuss some of the
# limitations of fully connected architectures later in this chapter.
# 
# What Is a Fully Connected Deep Network?
# A fully connected neural network consists of a series of fully connected layers. A fully
# connected layer is a function from ℝm to ℝn. Each output dimension depends on
# each input dimension. Pictorially, a fully connected layer is represented as follows in
# Figure 4-1.
# 
# 
# 
# 
#                                                                                        81
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Review",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Review"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Review(HierNode):
    def __init__(self):
        super().__init__("Review")
        self.add(Content())

# eof
