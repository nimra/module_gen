# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                         Download from finelybook www.finelybook.com
# Using the Neural Network
# Now that the neural network is trained, you can use it to make predictions. To do
# that, you can reuse the same construction phase, but change the execution phase like
# this:
#       with tf.Session() as sess:
#           saver.restore(sess, "./my_model_final.ckpt")
#           X_new_scaled = [...] # some new images (scaled from 0 to 1)
#           Z = logits.eval(feed_dict={X: X_new_scaled})
#           y_pred = np.argmax(Z, axis=1)
# First the code loads the model parameters from disk. Then it loads some new images
# that you want to classify. Remember to apply the same feature scaling as for the train‐
# ing data (in this case, scale it from 0 to 1). Then the code evaluates the logits node.
# If you wanted to know all the estimated class probabilities, you would need to apply
# the softmax() function to the logits, but if you just want to predict a class, you can
# simply pick the class that has the highest logit value (using the argmax() function
# does the trick).
# 
# Fine-Tuning Neural Network Hyperparameters
# The flexibility of neural networks is also one of their main drawbacks: there are many
# hyperparameters to tweak. Not only can you use any imaginable network topology
# (how neurons are interconnected), but even in a simple MLP you can change the
# number of layers, the number of neurons per layer, the type of activation function to
# use in each layer, the weight initialization logic, and much more. How do you know
# what combination of hyperparameters is the best for your task?
# Of course, you can use grid search with cross-validation to find the right hyperpara‐
# meters, like you did in previous chapters, but since there are many hyperparameters
# to tune, and since training a neural network on a large dataset takes a lot of time, you
# will only be able to explore a tiny part of the hyperparameter space in a reasonable
# amount of time. It is much better to use randomized search, as we discussed in Chap‐
# ter 2. Another option is to use a tool such as Oscar, which implements more complex
# algorithms to help you find a good set of hyperparameters quickly.
# It helps to have an idea of what values are reasonable for each hyperparameter, so you
# can restrict the search space. Let’s start with the number of hidden layers.
# 
# Number of Hidden Layers
# For many problems, you can just begin with a single hidden layer and you will get
# reasonable results. It has actually been shown that an MLP with just one hidden layer
# can model even the most complex functions provided it has enough neurons. For a
# long time, these facts convinced researchers that there was no need to investigate any
# 
# 
# 270   |   Chapter 10: Introduction to Artificial Neural Networks
# 
#                  Download from finelybook www.finelybook.com
# deeper neural networks. But they overlooked the fact that deep networks have a much
# higher parameter efficiency than shallow ones: they can model complex functions
# using exponentially fewer neurons than shallow nets, making them much faster to
# train.
# To understand why, suppose you are asked to draw a forest using some drawing soft‐
# ware, but you are forbidden to use copy/paste. You would have to draw each tree
# individually, branch per branch, leaf per leaf. If you could instead draw one leaf,
# copy/paste it to draw a branch, then copy/paste that branch to create a tree, and
# finally copy/paste this tree to make a forest, you would be finished in no time. Real-
# world data is often structured in such a hierarchical way and DNNs automatically
# take advantage of this fact: lower hidden layers model low-level structures (e.g., line
# segments of various shapes and orientations), intermediate hidden layers combine
# these low-level structures to model intermediate-level structures (e.g., squares, cir‐
# cles), and the highest hidden layers and the output layer combine these intermediate
# structures to model high-level structures (e.g., faces).
# Not only does this hierarchical architecture help DNNs converge faster to a good sol‐
# ution, it also improves their ability to generalize to new datasets. For example, if you
# have already trained a model to recognize faces in pictures, and you now want to
# train a new neural network to recognize hairstyles, then you can kickstart training by
# reusing the lower layers of the first network. Instead of randomly initializing the
# weights and biases of the first few layers of the new neural network, you can initialize
# them to the value of the weights and biases of the lower layers of the first network.
# This way the network will not have to learn from scratch all the low-level structures
# that occur in most pictures; it will only have to learn the higher-level structures (e.g.,
# hairstyles).
# In summary, for many problems you can start with just one or two hidden layers and
# it will work just fine (e.g., you can easily reach above 97% accuracy on the MNIST
# dataset using just one hidden layer with a few hundred neurons, and above 98% accu‐
# racy using two hidden layers with the same total amount of neurons, in roughly the
# same amount of training time). For more complex problems, you can gradually ramp
# up the number of hidden layers, until you start overfitting the training set. Very com‐
# plex tasks, such as large image classification or speech recognition, typically require
# networks with dozens of layers (or even hundreds, but not fully connected ones, as
# we will see in Chapter 13), and they need a huge amount of training data. However,
# you will rarely have to train such networks from scratch: it is much more common to
# reuse parts of a pretrained state-of-the-art network that performs a similar task.
# Training will be a lot faster and require much less data (we will discuss this in Chap‐
# ter 11).
# 
# 
# 
# 
#                                                 Fine-Tuning Neural Network Hyperparameters   |   271
# 
#                         Download from finelybook www.finelybook.com
# Number of Neurons per Hidden Layer
# Obviously the number of neurons in the input and output layers is determined by the
# type of input and output your task requires. For example, the MNIST task requires 28
# x 28 = 784 input neurons and 10 output neurons. As for the hidden layers, a common
# practice is to size them to form a funnel, with fewer and fewer neurons at each layer—
# the rationale being that many low-level features can coalesce into far fewer high-level
# features. For example, a typical neural network for MNIST may have two hidden lay‐
# ers, the first with 300 neurons and the second with 100. However, this practice is not
# as common now, and you may simply use the same size for all hidden layers—for
# example, all hidden layers with 150 neurons: that’s just one hyperparameter to tune
# instead of one per layer. Just like for the number of layers, you can try increasing the
# number of neurons gradually until the network starts overfitting. In general you will
# get more bang for the buck by increasing the number of layers than the number of
# neurons per layer. Unfortunately, as you can see, finding the perfect amount of neu‐
# rons is still somewhat of a black art.
# A simpler approach is to pick a model with more layers and neurons than you
# actually need, then use early stopping to prevent it from overfitting (and other regu‐
# larization techniques, especially dropout, as we will see in Chapter 11). This has been
# dubbed the “stretch pants” approach:12 instead of wasting time looking for pants that
# perfectly match your size, just use large stretch pants that will shrink down to the
# right size.
# 
# Activation Functions
# In most cases you can use the ReLU activation function in the hidden layers (or one
# of its variants, as we will see in Chapter 11). It is a bit faster to compute than other
# activation functions, and Gradient Descent does not get stuck as much on plateaus,
# thanks to the fact that it does not saturate for large input values (as opposed to the
# logistic function or the hyperbolic tangent function, which saturate at 1).
# For the output layer, the softmax activation function is generally a good choice for
# classification tasks (when the classes are mutually exclusive). For regression tasks,
# you can simply use no activation function at all.
# This concludes this introduction to artificial neural networks. In the following chap‐
# ters, we will discuss techniques to train very deep nets, and distribute training across
# multiple servers and GPUs. Then we will explore a few other popular neural network
# architectures: convolutional neural networks, recurrent neural networks, and autoen‐
# coders.13
# 
# 
# 12 By Vincent Vanhoucke in his Deep Learning class on Udacity.com.
# 13 A few extra ANN architectures are presented in Appendix E.
# 
# 
# 
# 272   |   Chapter 10: Introduction to Artificial Neural Networks
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Number of Hidden Layers",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Number of Hidden Layers"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Numberof(HierNode):
    def __init__(self):
        super().__init__("Number of Hidden Layers")
        self.add(Content())

# eof
