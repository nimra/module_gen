# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Setting Up an Account on Google Cloud Platform
# This section shows how to set up an account on Google Cloud Platform. A GCP account
# gives access to all of the platform’s products and services. For a new account, a $300
# credit is awarded to be spent over a period of 12 months. This offer is great as it gives
# ample time to explore the different features and services of Google’s cloud offering.
#     Note that a valid credit card is required to register an account to validate that it is an
# authentic user, as opposed to a robot. However, the credit card won’t be charged after
# the trial ends, except Google is authorized to do so:
# 
#       1. Go to https://cloud.google.com/ to open an account (see
#          Figure 3-1).
# 
# 
# 
# 
# Figure 3-1. Google Cloud Platform login page
# 
#       2. Fill in the necessary identity, address, and credit card details.
# 
#       3. Wait a moment while an account is created on the platform (see
#          Figure 3-2).
# 
# 
# 
# 
# 
# Figure 3-2. Creating account
# 
#      4. After account creation, we’re presented with the Welcome to GCP
#         page (see Figure 3-­3).
# 
# 
# 
# 
# Figure 3-3. Welcome to GCP
# 
#       5. Click the icon of three lines in the top-left corner of the page
#          (marked with a circle in Figure 3-3), then click Home (marked
#          with a rectangle in Figure 3-3) to open the Google Cloud Platform
#          dashboard (Figure 3-4).
# 
# 
# 
# 
# Figure 3-4. GCP dashboard
# 
#     The Cloud dashboard provides a bird’s-eye summary of the project such as the
# current billing rate and other resource usage statistics. The activity tab to the right gives
# a breakdown of the resource actions performed on the account. This feature is useful
# when building an audit trail of events.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Setting Up an Account on Google Cloud Platform",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Setting Up an Account on Google Cloud Platform"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class SettingUp(HierNode):
    def __init__(self):
        super().__init__("Setting Up an Account on Google Cloud Platform")
        self.add(Content())

# eof
