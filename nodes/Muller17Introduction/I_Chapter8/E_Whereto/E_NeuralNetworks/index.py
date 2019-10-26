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
# already know about how the real world works. If the compass and accelerometer tell
# you a user is going north, and the GPS is telling you the user is going south, you
# probably can’t trust the GPS. If your position estimate tells you the user just walked
# through a wall, you should also be highly skeptical. It’s possible to express this situa‐
# tion using a probabilistic model, and then use machine learning or probabilistic
# inference to find out how much you should trust each measurement, and to reason
# about what the best guess for the location of a user is.
# Once you’ve expressed the situation and your model of how the different factors work
# together in the right way, there are methods to compute the predictions using these
# custom models directly. The most general of these methods are called probabilistic
# programming languages, and they provide a very elegant and compact way to express
# a learning problem. Examples of popular probabilistic programming languages are
# PyMC (which can be used in Python) and Stan (a framework that can be used from
# several languages, including Python). While these packages require some under‐
# standing of probability theory, they simplify the creation of new models significantly.
# 
# Neural Networks
# While we touched on the subject of neural networks briefly in Chapters 2 and 7, this
# is a rapidly evolving area of machine learning, with innovations and new applications
# being announced on a weekly basis. Recent breakthroughs in machine learning and
# artificial intelligence, such as the victory of the Alpha Go program against human
# champions in the game of Go, the constantly improving performance of speech
# understanding, and the availability of near-instantaneous speech translation, have all
# been driven by these advances. While the progress in this field is so fast-paced that
# any current reference to the state of the art will soon be outdated, the recent book
# Deep Learning by Ian Goodfellow, Yoshua Bengio, and Aaron Courville (MIT Press)
# is a comprehensive introduction into the subject.2
# 
# Scaling to Larger Datasets
# In this book, we always assumed that the data we were working with could be stored
# in a NumPy array or SciPy sparse matrix in memory (RAM). Even though modern
# servers often have hundreds of gigabytes (GB) of RAM, this is a fundamental restric‐
# tion on the size of data you can work with. Not everybody can afford to buy such a
# large machine, or even to rent one from a cloud provider. In most applications, the
# data that is used to build a machine learning system is relatively small, though, and
# few machine learning datasets consist of hundreds of gigabites of data or more. This
# makes expanding your RAM or renting a machine from a cloud provider a viable sol‐
# ution in many cases. If you need to work with terabytes of data, however, or you need
# 
# 
# 2 A preprint of Deep Learning can be viewed at http://www.deeplearningbook.org/.
# 
# 
# 
# 364   |   Chapter 8: Wrapping Up
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Neural Networks",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class NeuralNetworks(HierNode):
    def __init__(self):
        super().__init__("Neural Networks")
        self.add(Content(), "content")

# eof
