# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_Chapter45.index import Chapter45 as A_Chapter45
from .B_Chapter46.index import Chapter46 as B_Chapter46
from .C_Chapter47.index import Chapter47 as C_Chapter47

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PART VIII
# 
# Productionalizing
# Machine Learning
# Solutions on GCP
# 
# CHAPTER 45
# 
# 
# 
# Containers and Google
# Kubernetes Engine
# The microservice architecture is an approach for developing and deploying enterprise
# cloud-native software applications that involve separating the core business capabilities
# of the application into decoupled components. Each business capability represents
# some functionality that the application provides as services to the end user. The idea
# of microservices is in contrast to the monolithic architecture which involves building
# applications as a composite of its “individual” capabilities. See an illustration in
# Figure 45-1.
# 
# 
# 
# 
# Figure 45-1. Microservice applications (right) vs. monolithic applications (left)
# 
# 
# 
# 
#                                                                                           655
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_45
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Part VIII: Productionalizing Machine Learning Solutions on GCP",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Part VIII: Productionalizing Machine Learning Solutions on GCP"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PartVIII(HierNode):
    def __init__(self):
        super().__init__("Part VIII: Productionalizing Machine Learning Solutions on GCP")
        self.add(Content())
        self.add(A_Chapter45())
        self.add(B_Chapter46())
        self.add(C_Chapter47())

# eof
