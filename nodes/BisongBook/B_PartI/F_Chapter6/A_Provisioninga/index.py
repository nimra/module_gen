# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Provisioning a Notebook Instance
# The following steps provide a walk-through for deploying a Notebook instance on a deep
# learning VM:
# 
#        1. In the group named ‘ARTIFICIAL INTELLIGENCE’ on the GCP
#           resources drawer, click the arrow beside ‘AI Platform’ and select
#           ‘Notebooks’ as shown in Figure 6-1.
# 
# 
# 
# 
# 
# Figure 6-1. Open Notebooks on GCP AI Platform
# 
#       2. Click ‘NEW INSTANCE’ to initiate a notebook instance as shown
#          in Figure 6-2; there is an option to customize your instance or
#          to use one of the pre-configured instances with TensorFlow,
#          PyTorch, or RAPIDS XGBoost installed.
# 
# 
# 
# 
# Figure 6-2. Start a new Notebook instance
# 
#      3. For this example, we will create a Notebook instance pre-
#         configured with TensorFlow 2.0 (see Figure 6-3).
# 
# 
# 
# 
# Figure 6-3. Start a new Notebook instance
# 
#      4. Click ‘OPEN JUPYTERLAB’ to launch the JupyterLab notebook
#         instance in a new window (see Figure 6-4).
# 
# 
# 
# 
# Figure 6-4. Open JupyterLab
#                                                                                  #       5. From the JupyterLab Launcher in Figure 6-5, options exist to open
#          a Python notebook, a Python interactive shell, a bash terminal,
#          a text file, or a Tensorboard dashboard (more on Tensorboard in
#          Part 6).
# 
# 
# 
# 
# Figure 6-5. JupyterLab Launcher
# 
#       6. Open a Python 3 Notebook (see Figure 6-6). We’ll work with
#          Python notebooks in later chapters to carry out data science tasks.
# 
# 
# 
# 
# 
# Figure 6-6. Python 3 Notebook

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Provisioning a Notebook Instance",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Provisioning a Notebook Instance"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Provisioninga(HierNode):
    def __init__(self):
        super().__init__("Provisioning a Notebook Instance")
        self.add(Content())

# eof
