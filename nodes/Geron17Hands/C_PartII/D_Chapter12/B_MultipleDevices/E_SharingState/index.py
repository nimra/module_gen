# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                        Download from finelybook www.finelybook.com
# Sharing State Across Sessions Using Resource Containers
# When you are using a plain local session (not the distributed kind), each variable’s
# state is managed by the session itself; as soon as it ends, all variable values are lost.
# Moreover, multiple local sessions cannot share any state, even if they both run the
# same graph; each session has its own copy of every variable (as we discussed in Chap‐
# ter 9). In contrast, when you are using distributed sessions, variable state is managed
# by resource containers located on the cluster itself, not by the sessions. So if you create
# a variable named x using one client session, it will automatically be available to any
# other session on the same cluster (even if both sessions are connected to a different
# server). For example, consider the following client code:
#       # simple_client.py
#       import tensorflow as tf
#       import sys
# 
#       x = tf.Variable(0.0, name="x")
#       increment_x = tf.assign(x, x + 1)
# 
#       with tf.Session(sys.argv[1]) as sess:
#           if sys.argv[2:]==["init"]:
#               sess.run(x.initializer)
#           sess.run(increment_x)
#           print(x.eval())
# Let’s suppose you have a TensorFlow cluster up and running on machines A and B,
# port 2222. You could launch the client, have it open a session with the server on
# machine A, and tell it to initialize the variable, increment it, and print its value by
# launching the following command:
#       $ python3 simple_client.py grpc://machine-a.example.com:2222 init
#       1.0
# Now if you launch the client with the following command, it will connect to the
# server on machine B and magically reuse the same variable x (this time we don’t ask
# the server to initialize the variable):
#       $ python3 simple_client.py grpc://machine-b.example.com:2222
#       2.0
# This feature cuts both ways: it’s great if you want to share variables across multiple
# sessions, but if you want to run completely independent computations on the same
# cluster you will have to be careful not to use the same variable names by accident.
# One way to ensure that you won’t have name clashes is to wrap all of your construc‐
# tion phase inside a variable scope with a unique name for each computation, for
# example:
#       with tf.variable_scope("my_problem_1"):
#           [...] # Construction phase of problem 1
# 
# 
# 
# 328   |   Chapter 12: Distributing TensorFlow Across Devices and Servers
# 
#                   Download from finelybook www.finelybook.com
# A better option is to use a container block:
#     with tf.container("my_problem_1"):
#         [...] # Construction phase of problem 1
# This will use a container dedicated to problem #1, instead of the default one (whose
# name is an empty string ""). One advantage is that variable names remain nice and
# short. Another advantage is that you can easily reset a named container. For example,
# the following command will connect to the server on machine A and ask it to reset
# the container named "my_problem_1", which will free all the resources this container
# used (and also close all sessions open on the server). Any variable managed by this
# container must be initialized before you can use it again:
#     tf.Session.reset("grpc://machine-a.example.com:2222", ["my_problem_1"])
# Resource containers make it easy to share variables across sessions in flexible ways.
# For example, Figure 12-7 shows four clients running different graphs on the same
# cluster, but sharing some variables. Clients A and B share the same variable x man‐
# aged by the default container, while clients C and D share another variable named x
# managed by the container named "my_problem_1". Note that client C even uses vari‐
# ables from both containers.
# 
# 
# 
# 
# Figure 12-7. Resource containers
# 
# Resource containers also take care of preserving the state of other stateful operations,
# namely queues and readers. Let’s take a look at queues first.
# 
# Asynchronous Communication Using TensorFlow Queues
# Queues are another great way to exchange data between multiple sessions; for exam‐
# ple, one common use case is to have a client create a graph that loads the training data
# and pushes it into a queue, while another client creates a graph that pulls the data
# from the queue and trains a model (see Figure 12-8). This can speed up training con‐
# 
# 
#                                                    Multiple Devices Across Multiple Servers   |   329
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Sharing State Across Sessions Using Resource Containers",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Sharing State Across Sessions Using Resource Containers"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class SharingState(HierNode):
    def __init__(self):
        super().__init__("Sharing State Across Sessions Using Resource Containers")
        self.add(Content())

# eof
