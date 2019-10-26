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

from .A_Typesof.index import Typesof as A_Typesof
from .B_ExampleApplication.index import ExampleApplication as B_ExampleApplication
from .C_RepresentingText.index import RepresentingText as C_RepresentingText
from .D_Stopwords.index import Stopwords as D_Stopwords
from .E_Rescalingthe.index import Rescalingthe as E_Rescalingthe
from .F_InvestigatingModel.index import InvestigatingModel as F_InvestigatingModel
from .G_BagofWordswith.index import BagofWordswith as G_BagofWordswith
from .H_AdvancedTokenization.index import AdvancedTokenization as H_AdvancedTokenization
from .I_TopicModeling.index import TopicModeling as I_TopicModeling
from .J_Summaryand.index import Summaryand as J_Summaryand

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                                                                             CHAPTER 7
#                                          Working with Text Data
# 
# 
# 
# 
# In Chapter 4, we talked about two kinds of features that can represent properties of
# the data: continuous features that describe a quantity, and categorical features that are
# items from a fixed list. There is a third kind of feature that can be found in many
# applications, which is text. For example, if we want to classify an email message as
# either a legitimate email or spam, the content of the email will certainly contain
# important information for this classification task. Or maybe we want to learn about
# the opinion of a politician on the topic of immigration. Here, that individual’s
# speeches or tweets might provide useful information. In customer service, we often
# want to find out if a message is a complaint or an inquiry. We can use the subject line
# and content of a message to automatically determine the customer’s intent, which
# allows us to send the message to the appropriate department, or even send a fully
# automatic reply.
# Text data is usually represented as strings, made up of characters. In any of the exam‐
# ples just given, the length of the text data will vary. This feature is clearly very differ‐
# ent from the numeric features that we’ve discussed so far, and we will need to process
# the data before we can apply our machine learning algorithms to it.
# 
# Types of Data Represented as Strings
# Before we dive into the processing steps that go into representing text data for
# machine learning, we want to briefly discuss different kinds of text data that you
# might encounter. Text is usually just a string in your dataset, but not all string features
# should be treated as text. A string feature can sometimes represent categorical vari‐
# ables, as we discussed in Chapter 5. There is no way to know how to treat a string
# feature before looking at the data.
# 
# 
# 
# 
#                                                                                          323
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 7. Working with Text Data",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter7(HierNode):
    def __init__(self):
        super().__init__("Chapter 7. Working with Text Data")
        self.add(Content(), "content")
        self.add(A_Typesof())
        self.add(B_ExampleApplication())
        self.add(C_RepresentingText())
        self.add(D_Stopwords())
        self.add(E_Rescalingthe())
        self.add(F_InvestigatingModel())
        self.add(G_BagofWordswith())
        self.add(H_AdvancedTokenization())
        self.add(I_TopicModeling())
        self.add(J_Summaryand())

# eof
