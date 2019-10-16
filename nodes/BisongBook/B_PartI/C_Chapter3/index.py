# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_SettingUp.index import SettingUp as A_SettingUp
from .B_GCPResources.index import GCPResources as B_GCPResources
from .C_AccessingCloud.index import AccessingCloud as C_AccessingCloud
from .D_AccountUsers.index import AccountUsers as D_AccountUsers
from .E_TheCloud.index import TheCloud as E_TheCloud
from .F_GoogleCloud.index import GoogleCloud as F_GoogleCloud

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 3
# 
# 
# 
# The Google Cloud SDK
# and Web CLI
# GCP provides a command-line interface (CLI) for interacting with cloud products and
# services. GCP resources can be accessed via the web-based CLI on GCP or by installing
# the Google Cloud software development kit (SDK) on your local machine to interact with
# GCP via the local command-line terminal.
#     GCP contains shell commands for a wide range of GCP products such as the
# Compute Engine, Cloud Storage, Cloud ML Engine, BigQuery, and Datalab, to mention
# just a few. Major tools of the Cloud SDK include
# 
#        •    gcloud tool: Responsible for cloud authentication, configuration, and
#             other interactions on GCP
# 
#        •    gsutil tool: Responsible for interacting with Google Cloud Storage
#             buckets and objects
# 
#        •    bq tool: Used for interacting and managing Google BigQuery via the
#             command line
# 
#        •    kubectl tool: Used for managing Kubernetes container clusters on GCP
# 
#     The Google Cloud SDK also installs client libraries for developers to
# programmatically interact with GCP products and services through APIs.1 As of this time
# of writing, the Go, Java, Node.js, Python, Ruby, PHP, and C# languages are covered. Many
# more are expected to be added to this list.
#     This chapter works through setting up an account on GCP, installing the Google
# Cloud SDK, and then exploring GCP commands using the CLI.
# 
# ---
# 1 | APIs stands for application programming interfaces, which are packages and tools used in
#  building software applications.
# ---

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 3: The Google Cloud SDK and Web CLI",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Chapter 3: The Google Cloud SDK and Web CLI"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter3(HierNode):
    def __init__(self):
        super().__init__("Chapter 3: The Google Cloud SDK and Web CLI")
        self.add(Content())
        self.add(A_SettingUp())
        self.add(B_GCPResources())
        self.add(C_AccessingCloud())
        self.add(D_AccountUsers())
        self.add(E_TheCloud())
        self.add(F_GoogleCloud())

# eof
