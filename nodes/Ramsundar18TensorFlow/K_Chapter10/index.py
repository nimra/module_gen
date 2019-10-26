# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_DeepLearning.index import DeepLearning as A_DeepLearning
from .B_UsingDeep.index import UsingDeep as B_UsingDeep
from .C_IsArtificial.index import IsArtificial as C_IsArtificial
from .D_Whereto.index import Whereto as D_Whereto

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                                                        CHAPTER 10
#                               The Future of Deep Learning
# 
# 
# 
# 
# In this book, we have covered the foundations of modern deep learning. We’ve dis‐
# cussed a wide variety of algorithms, and delved deeply into a number of sophisticated
# case studies. Readers who’ve been working through the examples covered in this book
# are now well prepared to use deep learning on the job, and to start reading the large
# research literature on deep learning methods.
# It’s worth emphasizing how unique this skill set is. Deep learning has had tremendous
# impact in the technology industry already, but deep learning is beginning to dramati‐
# cally alter the state of essentially all nontech industries and to even shift the global
# geopolitical balance. Your understanding of this epochal technology will open many
# doors you may not have envisioned. In this final chapter, we will briefly survey some
# of the important applications of deep learning outside the software industry.
# We will also use this chapter to help you answer the question of how to use your new
# knowledge effectively and ethically. Deep learning is a technology of such power that
# it’s important for practitioners to think about how to use their skills properly. There
# have already been numerous misuses of deep learning, so it behooves new practition‐
# ers to pause before building sophisticated deep learning systems to ask whether the
# systems they are building are ethically sound. We will attempt to provide a brief dis‐
# cussion of ethical best practices, but caution the area of software ethics is complex
# enough that brief discussions are unlikely to do it full justice.
# Finally, we will examine where deep learning is going. Is deep learning the first step
# toward building artificially general intelligences, computational entities that have the
# full range of abilities of humans? There exist a wide range of expert opinions, which
# we survey.
# 
# 
# 
# 
#                                                                                      225
# 
# Deep Learning Outside the Tech Industry
# Technological companies such as Google, Facebook, Microsoft, and others have made
# heavy investments in deep learning infrastructure. Most of these companies were
# already familiar with machine learning systems, likely from past experiences with
# machine learning such as with ad prediction systems or search engines. As a result,
# shifting to deep learning from older machine learning systems took only a small con‐
# ceptual shift. Also, the success of past machine learning applications has made tech
# management quite open to the argument that deep learning could be more widely
# applied within companies. For these reasons, software companies are likely to remain
# the most prominent users of deep learning for the near future. If you intend to find a
# job using deep learning within the next couple years, it’s likely that you will end up at
# a tech company.
# However, at the same time, there is a broader shift brewing in which deep learning is
# beginning to infiltrate industries that historically have not used much machine learn‐
# ing. Unlike simpler machine learning methods, deep learning reduces the need for
# sophisticated feature preprocessing and allows for direct input of perceptual, textual,
# and molecular data. As a result, a number of industries are taking note, and large-
# scale efforts to overhaul these industries have already begun in many innovative start‐
# ups. We will now briefly discuss some of the changes happening in nearby industries
# and note that many new job opportunities for deep learning experts may become
# available in the near future.
# 
#                      Applications Are Synergistic
#                      You will soon learn about a number of deep learning applications
#                      in different industries. The striking fact about these applications is
#                      that all of them use the same fundamental deep learning algo‐
#                      rithms. Techniques you’ve seen such as fully connected networks,
#                      convolutional networks, recurrent networks, and reinforcement
#                      learning are broadly applicable to any of these fields. In particular,
#                      that means core improvements in convolutional network design
#                      will yield fruit in pharmaceutical, agricultural, and robotics appli‐
#                      cations. In reverse, deep learning innovations discovered by roboti‐
#                      cists will filter back and strengthen the foundations of deep
#                      learning. This virtuous cycle of fundamentals driving application
#                      driving fundamentals means that deep learning is a force that’s here
#                      to stay.
# 
# 
# Deep Learning in the Pharmaceutical Industry
# Deep learning is showing signs of taking off in a big way in drug discovery. Drug dis‐
# covery is broken down into multiple phases. There’s the preclinical discovery phase,
# 
# 
# 
# 226   |   Chapter 10: The Future of Deep Learning
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 10. The Future of Deep Learning",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(mbk("# Chapter 10. The Future of Deep Learning"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter10(HierNode):
    def __init__(self):
        super().__init__("Chapter 10. The Future of Deep Learning")
        self.add(Content())
        self.add(A_DeepLearning())
        self.add(B_UsingDeep())
        self.add(C_IsArtificial())
        self.add(D_Whereto())

# eof
