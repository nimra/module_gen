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
# Shell or Notebook?
# There are two primary means of using IPython that we’ll discuss in this chapter: the
# IPython shell and the IPython notebook. The bulk of the material in this chapter is
# relevant to both, and the examples will switch between them depending on what is
# most convenient. In the few sections that are relevant to just one or the other, I will
# explicitly state that fact. Before we start, some words on how to launch the IPython
# shell and IPython notebook.
# 
# Launching the IPython Shell
# This chapter, like most of this book, is not designed to be absorbed passively. I recom‐
# mend that as you read through it, you follow along and experiment with the tools and
# syntax we cover: the muscle-memory you build through doing this will be far more
# useful than the simple act of reading about it. Start by launching the IPython inter‐
# preter by typing ipython on the command line; alternatively, if you’ve installed a dis‐
# tribution like Anaconda or EPD, there may be a launcher specific to your system
# (we’ll discuss this more fully in “Help and Documentation in IPython” on page 3).
# Once you do this, you should see a prompt like the following:
#         IPython 4.0.1 -- An enhanced Interactive Python.
#         ?         -> Introduction and overview of IPython's features.
#         %quickref -> Quick reference.
#         help      -> Python's own help system.
#         object?   -> Details about 'object', use 'object??' for extra details.
#         In [1]:
# With that, you’re ready to follow along.
# 
# Launching the Jupyter Notebook
# The Jupyter notebook is a browser-based graphical interface to the IPython shell, and
# builds on it a rich set of dynamic display capabilities. As well as executing Python/
# IPython statements, the notebook allows the user to include formatted text, static and
# dynamic visualizations, mathematical equations, JavaScript widgets, and much more.
# Furthermore, these documents can be saved in a way that lets other people open them
# and execute the code on their own systems.
# Though the IPython notebook is viewed and edited through your web browser win‐
# dow, it must connect to a running Python process in order to execute code. To start
# this process (known as a “kernel”), run the following command in your system shell:
#         $ jupyter notebook
# This command will launch a local web server that will be visible to your browser. It
# immediately spits out a log showing what it is doing; that log will look something like
# this:
# 
# 2   |    Chapter 1: IPython: Beyond Normal Python
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Launching the IPython Shell",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Launchingthe(HierNode):
    def __init__(self):
        super().__init__("Launching the IPython Shell")
        self.add(Content())

# eof
