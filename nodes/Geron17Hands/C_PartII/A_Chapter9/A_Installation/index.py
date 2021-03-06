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
#                   Download from finelybook www.finelybook.com
# Table 9-1. Open source Deep Learning libraries (not an exhaustive list)
# Library            API                 Platforms                            Started by                         Year
# Caffe              Python, C++, Matlab Linux, macOS, Windows                Y. Jia, UC Berkeley (BVLC)         2013
# Deeplearning4j Java, Scala, Clojure      Linux, macOS, Windows, Android     A. Gibson, J.Patterson             2014
# H2O                Python, R             Linux, macOS, Windows              H2O.ai                             2014
# MXNet              Python, C++, others   Linux, macOS, Windows, iOS, Android DMLC                              2015
# TensorFlow         Python, C++           Linux, macOS, Windows, iOS, Android Google                            2015
# Theano             Python                Linux, macOS, iOS                  University of Montreal             2010
# Torch              C++, Lua              Linux, macOS, iOS, Android         R. Collobert, K. Kavukcuoglu, C.   2002
#                                                                             Farabet
# 
# 
# Installation
# Let’s get started! Assuming you installed Jupyter and Scikit-Learn by following the
# installation instructions in Chapter 2, you can simply use pip to install TensorFlow. If
# you created an isolated environment using virtualenv, you first need to activate it:
#       $ cd $ML_PATH                           # Your ML working directory (e.g., $HOME/ml)
#       $ source env/bin/activate
# Next, install TensorFlow:
#       $ pip3 install --upgrade tensorflow
# 
# 
#                       For GPU support, you need to install tensorflow-gpu instead of
#                       tensorflow. See Chapter 12 for more details.
# 
# 
# 
# 
# To test your installation, type the following command. It should output the version of
# TensorFlow you installed.
#       $ python3 -c 'import tensorflow; print(tensorflow.__version__)'
#       1.0.0
# 
# 
# Creating Your First Graph and Running It in a Session
# The following code creates the graph represented in Figure 9-1:
#       import tensorflow as tf
# 
#       x = tf.Variable(3, name="x")
#       y = tf.Variable(4, name="y")
#       f = x*x*y + y + 2
# 
# 
# 
# 
# 232     |   Chapter 9: Up and Running with TensorFlow
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Installation",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Installation(HierNode):
    def __init__(self):
        super().__init__("Installation")
        self.add(Content(), "content")

# eof
