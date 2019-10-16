# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_LearningFully.index import LearningFully as A_LearningFully
from .B_UniversalConvergence.index import UniversalConvergence as B_UniversalConvergence
from .C_WhyDeep.index import WhyDeep as C_WhyDeep

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Figure 4-2. A multilayer deep fully connected network.
# 
# As a quick implementation note, note that the equation for a single neuron looks very
# similar to a dot-product of two vectors (recall the discussion of tensor basics). For a
# layer of neurons, it is often convenient for efficiency purposes to compute y as a
# matrix multiply:
# 
#    y = σ wx
# 
# where sigma is a matrix in ℝn × m and the nonlinearity σ is applied componentwise.
# 
# “Neurons” in Fully Connected Networks
# The nodes in fully connected networks are commonly referred to as “neurons.” Con‐
# sequently, elsewhere in the literature, fully connected networks will commonly be
# referred to as “neural networks.” This nomenclature is largely a historical accident.
# In the 1940s, Warren S. McCulloch and Walter Pitts published a first mathematical
# model of the brain that argued that neurons were capable of computing arbitrary
# functions on Boolean quantities. Successors to this work slightly refined this logical
# model by making mathematical “neurons” continuous functions that varied between
# zero and one. If the inputs of these functions grew large enough, the neuron “fired”
# 
# 
# 
#                                                      “Neurons” in Fully Connected Networks   |   83
# 
# (took on the value one), else was quiescent. With the addition of adjustable weights,
# this description matches the previous equations.
# Is this how a real neuron behaves? Of course not! A real neuron (Figure 4-3) is an
# exceedingly complex engine, with over 100 trillion atoms, and tens of thousands of
# different signaling proteins capable of responding to varying signals. A microproces‐
# sor is a better analogy for a neuron than a one-line equation.
# 
# 
# 
# 
# Figure 4-3. A more biologically accurate representation of a neuron.
# 
# In many ways, this disconnect between biological neurons and artificial neurons is
# quite unfortunate. Uninitiated experts read breathless press releases claiming artificial
# neural networks with billions of “neurons” have been created (while the brain has
# only 100 billion biological neurons) and reasonably come away believing scientists
# are close to creating human-level intelligences. Needless to say, state of the art in deep
# learning is decades (or centuries) away from such an achievement.
# As you read further about deep learning, you may come across overhyped claims
# about artificial intelligence. Don’t be afraid to call out these statements. Deep learning
# in its current form is a set of techniques for solving calculus problems on fast hard‐
# ware. It is not a precursor to Terminator (Figure 4-4).
# 
# 
# 
# 
# 84   | Chapter 4: Fully Connected Deep Networks
# 
# Figure 4-4. Unfortunately (or perhaps fortunately), this book won’t teach you to build a
# Terminator!
# 
#                 AI Winters
#                 Artificial intelligence has gone through multiple rounds of boom-
#                 and-bust development. This cyclical development is characteristic
#                 of the field. Each new advance in learning spawns a wave of opti‐
#                 mism in which prophets claim that human-level (or superhuman)
#                 intelligences are incipient. After a few years, no such intelligences
#                 manifest, and disappointed funders pull out. The resulting period
#                 is called an AI winter.
#                 There have been multiple AI winters so far. As a thought exercise,
#                 we encourage you to consider when the next AI winter will happen.
#                 The current wave of deep learning progress has solved many more
#                 practical problems than any previous wave of advances. Is it possi‐
#                 ble AI has finally taken off and exited the boom-and-bust cycle or
#                 do you think we’re in for the “Great Depression” of AI soon?
# 
# 
# Learning Fully Connected Networks with Backpropagation
# The first version of a fully connected neural network was the Perceptron,
# (Figure 4-5), created by Frank Rosenblatt in the 1950s. These perceptrons are identi‐
# cal to the “neurons” we introduced in the previous equations.
# 
# 
# 
# 
#                                                         “Neurons” in Fully Connected Networks   |   85
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "“Neurons” in Fully Connected Networks",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# “Neurons” in Fully Connected Networks"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Neuronsin(HierNode):
    def __init__(self):
        super().__init__("“Neurons” in Fully Connected Networks")
        self.add(Content())
        self.add(A_LearningFully())
        self.add(B_UniversalConvergence())
        self.add(C_WhyDeep())

# eof
