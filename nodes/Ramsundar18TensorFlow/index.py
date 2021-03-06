# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
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
from .J_Chapter9.index import Chapter9 as J_Chapter9
from .K_Chapter10.index import Chapter10 as K_Chapter10
# from .L_Index.index import Index as L_Index

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                                                        Preface
# 
# 
# 
# 
# This book will introduce you to the fundamentals of machine learning through Ten‐
# sorFlow. TensorFlow is Google’s new software library for deep learning that makes it
# straightforward for engineers to design and deploy sophisticated deep learning archi‐
# tectures. You will learn how to use TensorFlow to build systems capable of detecting
# objects in images, understanding human text, and predicting the properties of poten‐
# tial medicines. Furthermore, you will gain an intuitive understanding of TensorFlow’s
# potential as a system for performing tensor calculus and will learn how to use Tensor‐
# Flow for tasks outside the traditional purview of machine learning.
# Importantly, TensorFlow for Deep Learning is one of the first deep learning books
# written for practitioners. It teaches fundamental concepts through practical examples
# and builds understanding of machine learning foundations from the ground up. The
# target audience for this book is practicing developers, who are comfortable with
# designing software systems, but not necessarily with creating learning systems. At
# times we use some basic linear algebra and calculus, but we will review all necessary
# fundamentals. We also anticipate that our book will prove useful for scientists and
# other professionals who are comfortable with scripting, but not necessarily with
# designing learning algorithms.
# 
# Conventions Used in This Book
# The following typographical conventions are used in this book:
# Italic
#      Indicates new terms, URLs, email addresses, filenames, and file extensions.
# Constant width
#     Used for program listings, as well as within paragraphs to refer to program ele‐
#     ments such as variable or function names, databases, data types, environment
#     variables, statements, and keywords.
# 
# 
# 
#                                                                                     ix
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Ramsundar18TensorFlow",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(mbk("# Ramsundar18TensorFlow"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Ramsundar18TensorFlow(HierNode):
    def __init__(self):
        super().__init__("Ramsundar18TensorFlow")
        self.add(Content())
        self.add(A_Preface())
        self.add(B_Chapter1())
        self.add(C_Chapter2())
        self.add(D_Chapter3())
        self.add(E_Chapter4())
        self.add(F_Chapter5())
        self.add(G_Chapter6())
        self.add(H_Chapter7())
        self.add(I_Chapter8())
        self.add(J_Chapter9())
        self.add(K_Chapter10())
        # self.add(L_Index())

# eof
