# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_FromBiological.index import FromBiological as A_FromBiological
from .B_Trainingan.index import Trainingan as B_Trainingan
from .C_Traininga.index import Traininga as C_Traininga
from .D_FineTuningNeural.index import FineTuningNeural as D_FineTuningNeural
from .E_Exercises.index import Exercises as E_Exercises

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                       Download from finelybook www.finelybook.com
# 
# 
#                                                                                              CHAPTER 10
#      Introduction to Artificial Neural Networks
# 
# 
# 
# 
# Birds inspired us to fly, burdock plants inspired velcro, and nature has inspired many
# other inventions. It seems only logical, then, to look at the brain’s architecture for
# inspiration on how to build an intelligent machine. This is the key idea that inspired
# artificial neural networks (ANNs). However, although planes were inspired by birds,
# they don’t have to flap their wings. Similarly, ANNs have gradually become quite dif‐
# ferent from their biological cousins. Some researchers even argue that we should drop
# the biological analogy altogether (e.g., by saying “units” rather than “neurons”), lest
# we restrict our creativity to biologically plausible systems.1
# ANNs are at the very core of Deep Learning. They are versatile, powerful, and scala‐
# ble, making them ideal to tackle large and highly complex Machine Learning tasks,
# such as classifying billions of images (e.g., Google Images), powering speech recogni‐
# tion services (e.g., Apple’s Siri), recommending the best videos to watch to hundreds
# of millions of users every day (e.g., YouTube), or learning to beat the world champion
# at the game of Go by examining millions of past games and then playing against itself
# (DeepMind’s AlphaGo).
# In this chapter, we will introduce artificial neural networks, starting with a quick tour
# of the very first ANN architectures. Then we will present Multi-Layer Perceptrons
# (MLPs) and implement one using TensorFlow to tackle the MNIST digit classification
# problem (introduced in Chapter 3).
# 
# 
# 
# 
# 1 You can get the best of both worlds by being open to biological inspirations without being afraid to create
#   biologically unrealistic models, as long as they work well.
# 
# 
# 
#                                                                                                                 253
# 
#                         Download from finelybook www.finelybook.com
# From Biological to Artificial Neurons
# Surprisingly, ANNs have been around for quite a while: they were first introduced
# back in 1943 by the neurophysiologist Warren McCulloch and the mathematician
# Walter Pitts. In their landmark paper,2 “A Logical Calculus of Ideas Immanent in
# Nervous Activity,” McCulloch and Pitts presented a simplified computational model
# of how biological neurons might work together in animal brains to perform complex
# computations using propositional logic. This was the first artificial neural network
# architecture. Since then many other architectures have been invented, as we will see.
# The early successes of ANNs until the 1960s led to the widespread belief that we
# would soon be conversing with truly intelligent machines. When it became clear that
# this promise would go unfulfilled (at least for quite a while), funding flew elsewhere
# and ANNs entered a long dark era. In the early 1980s there was a revival of interest in
# ANNs as new network architectures were invented and better training techniques
# were developed. But by the 1990s, powerful alternative Machine Learning techniques
# such as Support Vector Machines (see Chapter 5) were favored by most researchers,
# as they seemed to offer better results and stronger theoretical foundations. Finally, we
# are now witnessing yet another wave of interest in ANNs. Will this wave die out like
# the previous ones did? There are a few good reasons to believe that this one is differ‐
# ent and will have a much more profound impact on our lives:
# 
#   • There is now a huge quantity of data available to train neural networks, and
#     ANNs frequently outperform other ML techniques on very large and complex
#     problems.
#   • The tremendous increase in computing power since the 1990s now makes it pos‐
#     sible to train large neural networks in a reasonable amount of time. This is in
#     part due to Moore’s Law, but also thanks to the gaming industry, which has pro‐
#     duced powerful GPU cards by the millions.
#   • The training algorithms have been improved. To be fair they are only slightly dif‐
#     ferent from the ones used in the 1990s, but these relatively small tweaks have a
#     huge positive impact.
#   • Some theoretical limitations of ANNs have turned out to be benign in practice.
#     For example, many people thought that ANN training algorithms were doomed
#     because they were likely to get stuck in local optima, but it turns out that this is
#     rather rare in practice (or when it is the case, they are usually fairly close to the
#     global optimum).
#   • ANNs seem to have entered a virtuous circle of funding and progress. Amazing
#     products based on ANNs regularly make the headline news, which pulls more
# 
# 
# 2 “A Logical Calculus of Ideas Immanent in Nervous Activity,” W. McCulloch and W. Pitts (1943).
# 
# 
# 
# 254   |   Chapter 10: Introduction to Artificial Neural Networks
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 10. Introduction to Artificial Neural Networks",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Chapter 10. Introduction to Artificial Neural Networks"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter10(HierNode):
    def __init__(self):
        super().__init__("Chapter 10. Introduction to Artificial Neural Networks")
        self.add(Content())
        self.add(A_FromBiological())
        self.add(B_Trainingan())
        self.add(C_Traininga())
        self.add(D_FineTuningNeural())
        self.add(E_Exercises())

# eof
