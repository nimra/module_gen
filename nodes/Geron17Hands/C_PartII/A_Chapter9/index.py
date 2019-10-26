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

from .A_Installation.index import Installation as A_Installation
from .B_CreatingYour.index import CreatingYour as B_CreatingYour
from .C_ManagingGraphs.index import ManagingGraphs as C_ManagingGraphs
from .D_Lifecycleof.index import Lifecycleof as D_Lifecycleof
from .E_LinearRegression.index import LinearRegression as E_LinearRegression
from .F_ImplementingGradient.index import ImplementingGradient as F_ImplementingGradient
from .G_FeedingData.index import FeedingData as G_FeedingData
from .H_Savingand.index import Savingand as H_Savingand
from .I_Visualizingthe.index import Visualizingthe as I_Visualizingthe
from .J_NameScopes.index import NameScopes as J_NameScopes
from .K_Modularity.index import Modularity as K_Modularity
from .L_SharingVariables.index import SharingVariables as L_SharingVariables
from .M_Exercises.index import Exercises as M_Exercises

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                 Download from finelybook www.finelybook.com
# 
# 
#                                                                       CHAPTER 9
#                    Up and Running with TensorFlow
# 
# 
# 
# 
# TensorFlow is a powerful open source software library for numerical computation,
# particularly well suited and fine-tuned for large-scale Machine Learning. Its basic
# principle is simple: you first define in Python a graph of computations to perform
# (for example, the one in Figure 9-1), and then TensorFlow takes that graph and runs
# it efficiently using optimized C++ code.
# 
# 
# 
# 
# Figure 9-1. A simple computation graph
# 
# Most importantly, it is possible to break up the graph into several chunks and run
# them in parallel across multiple CPUs or GPUs (as shown in Figure 9-2). TensorFlow
# also supports distributed computing, so you can train colossal neural networks on
# humongous training sets in a reasonable amount of time by splitting the computa‐
# tions across hundreds of servers (see Chapter 12). TensorFlow can train a network
# with millions of parameters on a training set composed of billions of instances with
# millions of features each. This should come as no surprise, since TensorFlow was
# 
# 
#                                                                                  229
# 
#                  Download from finelybook www.finelybook.com
# developed by the Google Brain team and it powers many of Google’s large-scale serv‐
# ices, such as Google Cloud Speech, Google Photos, and Google Search.
# 
# 
# 
# 
# Figure 9-2. Parallel computation on multiple CPUs/GPUs/servers
# 
# When TensorFlow was open-sourced in November 2015, there were already many
# popular open source libraries for Deep Learning (Table 9-1 lists a few), and to be fair
# most of TensorFlow’s features already existed in one library or another. Nevertheless,
# TensorFlow’s clean design, scalability, flexibility,1 and great documentation (not to
# mention Google’s name) quickly boosted it to the top of the list. In short, TensorFlow
# was designed to be flexible, scalable, and production-ready, and existing frameworks
# arguably hit only two out of the three of these. Here are some of TensorFlow’s high‐
# lights:
# 
#   • It runs not only on Windows, Linux, and macOS, but also on mobile devices,
#     including both iOS and Android.
# 
# 
# 
# 
# 1 TensorFlow is not limited to neural networks or even Machine Learning; you could run quantum physics sim‐
#   ulations if you wanted.
# 
# 
# 
# 230   |   Chapter 9: Up and Running with TensorFlow
# 
#                  Download from finelybook www.finelybook.com
#   • It provides a very simple Python API called TF.Learn2 (tensorflow.con
#     trib.learn), compatible with Scikit-Learn. As you will see, you can use it to
#     train various types of neural networks in just a few lines of code. It was previ‐
#     ously an independent project called Scikit Flow (or skflow).
#   • It also provides another simple API called TF-slim (tensorflow.contrib.slim)
#     to simplify building, training, and evaluating neural networks.
#   • Several other high-level APIs have been built independently on top of Tensor‐
#     Flow, such as Keras or Pretty Tensor.
#   • Its main Python API offers much more flexibility (at the cost of higher complex‐
#     ity) to create all sorts of computations, including any neural network architecture
#     you can think of.
#   • It includes highly efficient C++ implementations of many ML operations, partic‐
#     ularly those needed to build neural networks. There is also a C++ API to define
#     your own high-performance operations.
#   • It provides several advanced optimization nodes to search for the parameters that
#     minimize a cost function. These are very easy to use since TensorFlow automati‐
#     cally takes care of computing the gradients of the functions you define. This is
#     called automatic differentiating (or autodiff).
#   • It also comes with a great visualization tool called TensorBoard that allows you to
#     browse through the computation graph, view learning curves, and more.
#   • Google also launched a cloud service to run TensorFlow graphs.
#   • Last but not least, it has a dedicated team of passionate and helpful developers,
#     and a growing community contributing to improving it. It is one of the most
#     popular open source projects on GitHub, and more and more great projects are
#     being built on top of it (for examples, check out the resources page on https://
#     www.tensorflow.org/, or https://github.com/jtoy/awesome-tensorflow). To ask
#     technical questions, you should use http://stackoverflow.com/ and tag your ques‐
#     tion with "tensorflow". You can file bugs and feature requests through GitHub.
#     For general discussions, join the Google group.
# 
# In this chapter, we will go through the basics of TensorFlow, from installation to cre‐
# ating, running, saving, and visualizing simple computational graphs. Mastering these
# basics is important before you build your first neural network (which we will do in
# the next chapter).
# 
# 
# 
# 
# 2 Not to be confused with the TFLearn library, which is an independent project.
# 
# 
# 
#                                                                       Up and Running with TensorFlow   |   231
# 
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
            "Chapter 9. Up and Running with TensorFlow",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter9(HierNode):
    def __init__(self):
        super().__init__("Chapter 9. Up and Running with TensorFlow")
        self.add(Content(), "content")
        self.add(A_Installation())
        self.add(B_CreatingYour())
        self.add(C_ManagingGraphs())
        self.add(D_Lifecycleof())
        self.add(E_LinearRegression())
        self.add(F_ImplementingGradient())
        self.add(G_FeedingData())
        self.add(H_Savingand())
        self.add(I_Visualizingthe())
        self.add(J_NameScopes())
        self.add(K_Modularity())
        self.add(L_SharingVariables())
        self.add(M_Exercises())

# eof
