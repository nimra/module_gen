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

from .A_Traininga.index import Traininga as A_Traininga
from .B_Trainingto.index import Trainingto as B_Trainingto
from .C_CreativeRNN.index import CreativeRNN as C_CreativeRNN

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                  Download from finelybook www.finelybook.com
# Training RNNs
# To train an RNN, the trick is to unroll it through time (like we just did) and then
# simply use regular backpropagation (see Figure 14-5). This strategy is called backpro‐
# pagation through time (BPTT).
# 
# 
# 
# 
# Figure 14-5. Backpropagation through time
# 
# Just like in regular backpropagation, there is a first forward pass through the unrolled
# network (represented by the dashed arrows); then the output sequence is evaluated
# using a cost function C � t         ,� t             , ⋯, � t         (where tmin and tmax are the first
#                               min          min + 1              max
# and last output time steps, not counting the ignored outputs), and the gradients of
# that cost function are propagated backward through the unrolled network (repre‐
# sented by the solid arrows); and finally the model parameters are updated using the
# gradients computed during BPTT. Note that the gradients flow backward through all
# the outputs used by the cost function, not just through the final output (for example,
# in Figure 14-5 the cost function is computed using the last three outputs of the net‐
# work, Y(2), Y(3), and Y(4), so gradients flow through these three outputs, but not
# through Y(0) and Y(1)). Moreover, since the same parameters W and b are used at each
# time step, backpropagation will do the right thing and sum over all time steps.
# 
# Training a Sequence Classifier
# Let’s train an RNN to classify MNIST images. A convolutional neural network would
# be better suited for image classification (see Chapter 13), but this makes for a simple
# example that you are already familiar with. We will treat each image as a sequence of
# 28 rows of 28 pixels each (since each MNIST image is 28 × 28 pixels). We will use
# cells of 150 recurrent neurons, plus a fully connected layer containing 10 neurons
# 
# 
# 
#                                                                                      Training RNNs   |   389
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Training RNNs",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TrainingRNNs(HierNode):
    def __init__(self):
        super().__init__("Training RNNs")
        self.add(Content(), "content")
        self.add(A_Traininga())
        self.add(B_Trainingto())
        self.add(C_CreativeRNN())

# eof
