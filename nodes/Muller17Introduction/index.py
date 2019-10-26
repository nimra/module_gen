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

from .A_Preface.index import Preface as A_Preface
from .B_Chapter1.index import Chapter1 as B_Chapter1
from .C_Chapter2.index import Chapter2 as C_Chapter2
from .D_Chapter3.index import Chapter3 as D_Chapter3
from .E_Chapter4.index import Chapter4 as E_Chapter4
from .F_Chapter5.index import Chapter5 as F_Chapter5
from .G_Chapter6.index import Chapter6 as G_Chapter6
from .H_Chapter7.index import Chapter7 as H_Chapter7
from .I_Chapter8.index import Chapter8 as I_Chapter8
# from .J_Index.index import Index as J_Index

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                                                                           Preface
# 
# 
# 
# 
# Machine learning is an integral part of many commercial applications and research
# projects today, in areas ranging from medical diagnosis and treatment to finding your
# friends on social networks. Many people think that machine learning can only be
# applied by large companies with extensive research teams. In this book, we want to
# show you how easy it can be to build machine learning solutions yourself, and how to
# best go about it. With the knowledge in this book, you can build your own system for
# finding out how people feel on Twitter, or making predictions about global warming.
# The applications of machine learning are endless and, with the amount of data avail‐
# able today, mostly limited by your imagination.
# 
# Who Should Read This Book
# This book is for current and aspiring machine learning practitioners looking to
# implement solutions to real-world machine learning problems. This is an introduc‐
# tory book requiring no previous knowledge of machine learning or artificial intelli‐
# gence (AI). We focus on using Python and the scikit-learn library, and work
# through all the steps to create a successful machine learning application. The meth‐
# ods we introduce will be helpful for scientists and researchers, as well as data scien‐
# tists working on commercial applications. You will get the most out of the book if you
# are somewhat familiar with Python and the NumPy and matplotlib libraries.
# We made a conscious effort not to focus too much on the math, but rather on the
# practical aspects of using machine learning algorithms. As mathematics (probability
# theory, in particular) is the foundation upon which machine learning is built, we
# won’t go into the analysis of the algorithms in great detail. If you are interested in the
# mathematics of machine learning algorithms, we recommend the book The Elements
# of Statistical Learning (Springer) by Trevor Hastie, Robert Tibshirani, and Jerome
# Friedman, which is available for free at the authors’ website. We will also not describe
# how to write machine learning algorithms from scratch, and will instead focus on
# 
# 
# 
#                                                                                         vii
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Muller17Introduction",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Muller17Introduction(HierNode):
    def __init__(self):
        super().__init__("Muller17Introduction")
        self.add(Content(), "content")
        self.add(A_Preface())
        self.add(B_Chapter1())
        self.add(C_Chapter2())
        self.add(D_Chapter3())
        self.add(E_Chapter4())
        self.add(F_Chapter5())
        self.add(G_Chapter6())
        self.add(H_Chapter7())
        self.add(I_Chapter8())
        # self.add(J_Index())

# eof
