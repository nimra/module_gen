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

from .A_Numberof.index import Numberof as A_Numberof
from .B_Numberof.index import Numberof as B_Numberof
from .C_ActivationFunctions.index import ActivationFunctions as C_ActivationFunctions

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
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
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Fine-Tuning Neural Network Hyperparameters",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class FineTuningNeural(HierNode):
    def __init__(self):
        super().__init__("Fine-Tuning Neural Network Hyperparameters")
        self.add(Content(), "content")
        self.add(A_Numberof())
        self.add(B_Numberof())
        self.add(C_ActivationFunctions())

# eof
