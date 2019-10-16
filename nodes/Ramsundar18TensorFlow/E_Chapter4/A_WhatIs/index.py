# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
# Figure 4-1. A fully connected layer in a deep network.
# 
# Let’s dig a little deeper into what the mathematical form of a fully connected network
# is. Let x ∈ ℝm represent the input to a fully connected layer. Let yi ∈ ℝ be the i-th
# output from the fully connected layer. Then yi ∈ ℝ is computed as follows:
# 
#      yi = σ w1x1 + ⋯ + wmxm
# 
# Here, σ is a nonlinear function (for now, think of σ as the sigmoid function intro‐
# duced in the previous chapter), and the wi are learnable parameters in the network.
# The full output y is then
# 
#           σ w1, 1x1 + ⋯ + w1, mxm
#      y=                  ⋮
#           σ wn, 1x1 + ⋯ + wn, mxm
# 
# Note that it’s directly possible to stack fully connected networks. A network with mul‐
# tiple fully connected networks is often called a “deep” network as depicted in
# Figure 4-2.
# 
# 
# 
# 
# 82   | Chapter 4: Fully Connected Deep Networks
# 
# Figure 4-2. A multilayer deep fully connected network.
# 
# As a quick implementation note, note that the equation for a single neuron looks very
# similar to a dot-product of two vectors (recall the discussion of tensor basics). For a
# layer of neurons, it is often convenient for efficiency purposes to compute y as a
# matrix multiply:
# 
#    y = σ wx
# 
# where sigma is a matrix in ℝn × m and the nonlinearity σ is applied componentwise.
# 
# “Neurons” in Fully Connected Networks
# The nodes in fully connected networks are commonly referred to as “neurons.” Con‐
# sequently, elsewhere in the literature, fully connected networks will commonly be
# referred to as “neural networks.” This nomenclature is largely a historical accident.
# In the 1940s, Warren S. McCulloch and Walter Pitts published a first mathematical
# model of the brain that argued that neurons were capable of computing arbitrary
# functions on Boolean quantities. Successors to this work slightly refined this logical
# model by making mathematical “neurons” continuous functions that varied between
# zero and one. If the inputs of these functions grew large enough, the neuron “fired”
# 
# 
# 
#                                                      “Neurons” in Fully Connected Networks   |   83
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "What Is a Fully Connected Deep Network?",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# What Is a Fully Connected Deep Network?"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class WhatIs(HierNode):
    def __init__(self):
        super().__init__("What Is a Fully Connected Deep Network?")
        self.add(Content())

# eof
