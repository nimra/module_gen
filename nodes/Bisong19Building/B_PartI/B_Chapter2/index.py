# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_CloudCompute.index import CloudCompute as A_CloudCompute
from .B_CloudStorage.index import CloudStorage as B_CloudStorage
from .C_BigData.index import BigData as C_BigData
from .D_CloudArtificial.index import CloudArtificial as D_CloudArtificial

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 2
# 
# 
# 
# An Overview of Google
# Cloud Platform Services
# Google Cloud Platform offers a wide range of services for securing, storing, serving,
# and analyzing data. These cloud services form a secure cloud perimeter for data, where
# different operations and transformations can be carried out on the data without it ever
# leaving the cloud ecosystem.
#      The services offered by Google Cloud include compute, storage, big data/analytics,
# artificial intelligence (AI), and other networking, developer, and management services.
# Let’s briefly review some of the features of the Google Cloud ecosystem.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 2: An Overview of Google Cloud Platform Services",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Chapter 2: An Overview of Google Cloud Platform Services"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter2(HierNode):
    def __init__(self):
        super().__init__("Chapter 2: An Overview of Google Cloud Platform Services")
        self.add(Content())
        self.add(A_CloudCompute())
        self.add(B_CloudStorage())
        self.add(C_BigData())
        self.add(D_CloudArtificial())

# eof
