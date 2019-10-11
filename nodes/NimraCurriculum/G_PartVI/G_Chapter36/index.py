# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_TheRecurrent.index import TheRecurrent as A_TheRecurrent
from .B_Unfoldingthe.index import Unfoldingthe as B_Unfoldingthe
from .C_BasicRecurrent.index import BasicRecurrent as C_BasicRecurrent
from .D_RecurrentConnection.index import RecurrentConnection as D_RecurrentConnection
from .E_SequenceMappings.index import SequenceMappings as E_SequenceMappings
from .F_Trainingthe.index import Trainingthe as F_Trainingthe
from .G_TheLong.index import TheLong as G_TheLong
from .H_PeepholeConnection.index import PeepholeConnection as H_PeepholeConnection
from .I_GatedRecurrent.index import GatedRecurrent as I_GatedRecurrent
from .J_RecurrentNeural.index import RecurrentNeural as J_RecurrentNeural
from .K_RNNwith.index import RNNwith as K_RNNwith
from .L_RNNwith.index import RNNwith as L_RNNwith

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 36
# 
# 
# 
# Recurrent Neural
# Networks (RNNs)
# Recurrent neural networks (RNNs) are another specialized scheme of neural network
# architectures. RNNs are developed to solve learning problems where information about
# the past (i.e., past instants/events) is directly linked to making future predictions. Such
# sequential examples play up frequently in many real-world tasks such as language
# modeling where the previous words in the sentence are used to determine what the next
# word will be. Also in stock market prediction, the last hour/day/week stock prices define
# the future stock movement. RNNs are particularly tuned for time series or sequential tasks.
#     In a sequential problem, there is a looping or feedback framework that connects the
# output of one sequence to the input of the next sequence. RNNs are ideal for processing
# 1-D sequential data, unlike the grid-like 2-D image data in convolutional neural networks.
#     This feedback framework enables the network to incorporate information from past
# sequences or from time-dependent datasets when making a prediction.
# In this section, we will cover the broad conceptual overview of recurrent neural
# networks and in particular the Long Short-Term Memory RNN variant (LSTM) which is
# the state-of-the-­art technique for various sequential problems such as image captioning,
# stock market prediction, machine translation, and text classification.
# 
# 
# 
# The Recurrent Neuron
# The first building block of the RNN is the recurrent neuron (see Figure 36-1). The
# neurons of the recurrent network are entirely different from those of other neural
# network architectures. The key difference here is that the recurrent neuron maintains a
# memory or a state from past computations. It does this by taking as input the output of
# the previous instant yt − 1 in addition to its current input at a particular instant xt.
# 
#                                                                                           443
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_36
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Chapter 36: Recurrent Neural Networks (RNNs)")
        self.add(MarkdownBlock("# Chapter 36: Recurrent Neural Networks (RNNs)"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter36(HierNode):
    def __init__(self):
        super().__init__("Chapter 36: Recurrent Neural Networks (RNNs)")
        self.add(Content())
        self.add(A_TheRecurrent())
        self.add(B_Unfoldingthe())
        self.add(C_BasicRecurrent())
        self.add(D_RecurrentConnection())
        self.add(E_SequenceMappings())
        self.add(F_Trainingthe())
        self.add(G_TheLong())
        self.add(H_PeepholeConnection())
        self.add(I_GatedRecurrent())
        self.add(J_RecurrentNeural())
        self.add(K_RNNwith())
        self.add(L_RNNwith())

# eof
