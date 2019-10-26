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
#                  Download from finelybook www.finelybook.com
# Exercises
# 1. Draw an ANN using the original artificial neurons (like the ones in Figure 10-3)
#    that computes A ⊕ B (where ⊕ represents the XOR operation). Hint: A ⊕ B = (A
#    ∧ ¬ B) ∨ (¬ A ∧ B).
# 2. Why is it generally preferable to use a Logistic Regression classifier rather than a
#    classical Perceptron (i.e., a single layer of linear threshold units trained using the
#    Perceptron training algorithm)? How can you tweak a Perceptron to make it
#    equivalent to a Logistic Regression classifier?
# 3. Why was the logistic activation function a key ingredient in training the first
#    MLPs?
# 4. Name three popular activation functions. Can you draw them?
# 5. Suppose you have an MLP composed of one input layer with 10 passthrough
#    neurons, followed by one hidden layer with 50 artificial neurons, and finally one
#    output layer with 3 artificial neurons. All artificial neurons use the ReLU activa‐
#    tion function.
#    • What is the shape of the input matrix X?
#    • What about the shape of the hidden layer’s weight vector Wh, and the shape of
#      its bias vector bh?
#    • What is the shape of the output layer’s weight vector Wo, and its bias vector bo?
#    • What is the shape of the network’s output matrix Y?
#    • Write the equation that computes the network’s output matrix Y as a function
#      of X, Wh, bh, Wo and bo.
# 
# 6. How many neurons do you need in the output layer if you want to classify email
#    into spam or ham? What activation function should you use in the output layer?
#    If instead you want to tackle MNIST, how many neurons do you need in the out‐
#    put layer, using what activation function? Answer the same questions for getting
#    your network to predict housing prices as in Chapter 2.
# 7. What is backpropagation and how does it work? What is the difference between
#    backpropagation and reverse-mode autodiff?
# 8. Can you list all the hyperparameters you can tweak in an MLP? If the MLP over‐
#    fits the training data, how could you tweak these hyperparameters to try to solve
#    the problem?
# 9. Train a deep MLP on the MNIST dataset and see if you can get over 98% preci‐
#    sion. Just like in the last exercise of Chapter 9, try adding all the bells and whistles
# 
# 
# 
# 
#                                                                             Exercises   |   273
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Activation Functions",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ActivationFunctions(HierNode):
    def __init__(self):
        super().__init__("Activation Functions")
        self.add(Content(), "content")

# eof
