# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                 Download from finelybook www.finelybook.com
# works (BNN)4 is still the subject of active research, but some parts of the brain have
# been mapped, and it seems that neurons are often organized in consecutive layers, as
# shown in Figure 10-2.
# 
# 
# 
# 
# Figure 10-2. Multiple layers in a biological neural network (human cortex)5
# 
# Logical Computations with Neurons
# Warren McCulloch and Walter Pitts proposed a very simple model of the biological
# neuron, which later became known as an artificial neuron: it has one or more binary
# (on/off) inputs and one binary output. The artificial neuron simply activates its out‐
# put when more than a certain number of its inputs are active. McCulloch and Pitts
# showed that even with such a simplified model it is possible to build a network of
# artificial neurons that computes any logical proposition you want. For example, let’s
# build a few ANNs that perform various logical computations (see Figure 10-3),
# assuming that a neuron is activated when at least two of its inputs are active.
# 
# 
# 
# 
# Figure 10-3. ANNs performing simple logical computations
# 
# 
# 
# 
# 4 In the context of Machine Learning, the phrase “neural networks” generally refers to ANNs, not BNNs.
# 5 Drawing of a cortical lamination by S. Ramon y Cajal (public domain). Reproduced from https://en.wikipe
#   dia.org/wiki/Cerebral_cortex.
# 
# 
# 
# 256   |   Chapter 10: Introduction to Artificial Neural Networks
# 
#                  Download from finelybook www.finelybook.com
#   • The first network on the left is simply the identity function: if neuron A is activa‐
#     ted, then neuron C gets activated as well (since it receives two input signals from
#     neuron A), but if neuron A is off, then neuron C is off as well.
#   • The second network performs a logical AND: neuron C is activated only when
#     both neurons A and B are activated (a single input signal is not enough to acti‐
#     vate neuron C).
#   • The third network performs a logical OR: neuron C gets activated if either neu‐
#     ron A or neuron B is activated (or both).
#   • Finally, if we suppose that an input connection can inhibit the neuron’s activity
#     (which is the case with biological neurons), then the fourth network computes a
#     slightly more complex logical proposition: neuron C is activated only if neuron A
#     is active and if neuron B is off. If neuron A is active all the time, then you get a
#     logical NOT: neuron C is active when neuron B is off, and vice versa.
# 
# You can easily imagine how these networks can be combined to compute complex
# logical expressions (see the exercises at the end of the chapter).
# 
# The Perceptron
# The Perceptron is one of the simplest ANN architectures, invented in 1957 by Frank
# Rosenblatt. It is based on a slightly different artificial neuron (see Figure 10-4) called
# a linear threshold unit (LTU): the inputs and output are now numbers (instead of
# binary on/off values) and each input connection is associated with a weight. The LTU
# computes a weighted sum of its inputs (z = w1 x1 + w2 x2 + ⋯ + wn xn = wT · x), then
# applies a step function to that sum and outputs the result: hw(x) = step (z) = step (wT ·
# x).
# 
# 
# 
# 
# Figure 10-4. Linear threshold unit
# 
# The most common step function used in Perceptrons is the Heaviside step function
# (see Equation 10-1). Sometimes the sign function is used instead.
# 
# 
# 
# 
#                                                        From Biological to Artificial Neurons   |   257
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Logical Computations with Neurons",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Logical Computations with Neurons"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LogicalComputations(HierNode):
    def __init__(self):
        super().__init__("Logical Computations with Neurons")
        self.add(Content())

# eof
