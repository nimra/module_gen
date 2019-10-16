# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_IntroducingTensors.index import IntroducingTensors as A_IntroducingTensors
from .B_BasicComputations.index import BasicComputations as B_BasicComputations
from .C_Imperativeand.index import Imperativeand as C_Imperativeand
from .D_Review.index import Review as D_Review

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                                                        CHAPTER 2
#            Introduction to TensorFlow Primitives
# 
# 
# 
# 
# This chapter will introduce you to fundamental aspects of TensorFlow. In particular,
# you will learn how to perform basic computation using TensorFlow. A large part of
# this chapter will be spent introducing the concept of tensors, and discussing how ten‐
# sors are represented and manipulated within TensorFlow. This discussion will neces‐
# sitate a brief overview of some of the mathematical concepts that underlie tensorial
# mathematics. In particular, we’ll briefly review basic linear algebra and demonstrate
# how to perform basic linear algebraic operations with TensorFlow.
# We’ll follow this discussion of basic mathematics with a discussion of the differences
# between declarative and imperative programming styles. Unlike many programming
# languages, TensorFlow is largely declarative. Calling a TensorFlow operation adds a
# description of a computation to TensorFlow’s “computation graph.” In particular,
# TensorFlow code “describes” computations and doesn’t actually perform them. In
# order to run TensorFlow code, users need to create tf.Session objects. We introduce
# the concept of sessions and describe how users perform computations with them in
# TensorFlow.
# We end the chapter by discussing the notion of variables. Variables in TensorFlow
# hold tensors and allow for stateful computation that modifies variables to occur. We
# demonstrate how to create variables and update their values via TensorFlow.
# 
# Introducing Tensors
# Tensors are fundamental mathematical constructs in fields such as physics and engi‐
# neering. Historically, however, tensors have made fewer inroads in computer science,
# which has traditionally been more associated with discrete mathematics and logic.
# This state of affairs has started to change significantly with the advent of machine
# 
# 
# 
# 
#                                                                                     19
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 2. Introduction to TensorFlow Primitives",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Chapter 2. Introduction to TensorFlow Primitives"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter2(HierNode):
    def __init__(self):
        super().__init__("Chapter 2. Introduction to TensorFlow Primitives")
        self.add(Content())
        self.add(A_IntroducingTensors())
        self.add(B_BasicComputations())
        self.add(C_Imperativeand())
        self.add(D_Review())

# eof
