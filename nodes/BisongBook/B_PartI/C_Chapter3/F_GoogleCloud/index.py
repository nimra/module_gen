# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Google Cloud SDK
# The Google Cloud SDK installs command-line tools for interacting with cloud resources
# from the terminal on the local machine:
# 
#      1. Go to https://cloud.google.com/sdk/ to download and install the
#         appropriate Cloud SDK for your machine type (see Figure 3-12).
# 
# 
# 
# 
# Figure 3-12. Download Google Cloud SDK
# 
#      2. Follow the instructions for the operating system (OS) type to
#         install the Google Cloud SDK. The installation installs the default
#         Cloud SDK components.
# 
#      3. Open the terminal application of your OS and run the command
#         ‘gcloud init’ to begin authorization and configuration of the Cloud
#         SDK.
# 
#          gcloud init
# 
#          Welcome! This command will take you through the configuration
#          of gcloud.
# 
#          Pick configuration to use:
#           [1] Create a new configuration
#          Please enter your numeric choice:  1
# 
#       4. Select the name for your configuration. Here, it is set to the name
#          ‘your-­email-­id’.
# 
#             Enter configuration name. Names start with a lower case letter and
#             contain only lower case letters a-z, digits 0-9, and hyphens '-':
#             ­your-­email-­id
# 
#             Your current configuration has been set to: [your-email-id]
# 
#       5. Select the Google account to use for the configuration. The browser
#          will open to log in to the selected account (see Figures 3-13, 3-14,
#          and 3-15). However, if a purely terminal initialization is desired, the
#          user can run ‘gcloud init --console-only’.
# 
#             Choose the account you would like to use to perform operations for
#             this configuration:
#              [1] Log in with a new account
#             Please enter your numeric choice:  1
# 
#             Your browser has been opened to visit:
# 
#             https://accounts.google.com/o/oauth2/auth?redirect_
#             uri=......=offline
# 
# 
# 
# 
# Figure 3-13. Select Google account to authorize for Cloud SDK configuration
# 
# 
# 
# 
# 
# Figure 3-14. Authenticate Cloud SDK to access Google account
# 
# 
# 
# 
# 
# Figure 3-15. Confirmation page for Cloud SDK authentication
# 
#       6. Select the cloud project to use after the browser-based
#          authentication in a Google account.
# 
#             You are logged in as: [your-email-id@gmail.com].
# 
#             Pick cloud project to use:
#              [1] secret-country-192905
#              [2] Create a new project
#             Please enter numeric choice or text value (must exactly match list
#             item): 1
# 
#             Your current project has been set to: [secret-country-192905].
# 
#             Your Google Cloud SDK is configured and ready to use!
# 
#             * Commands that require authentication will use your-email-id@
#             gmail.com by default
#             * Commands will reference project `secret-country-192905` by
#             default
# 
#           Run `gcloud help config` to learn how to change individual
#           settings
# 
#           This gcloud configuration is called [your-configuration-name].
#           You can create additional configurations if you work with multiple
#           accounts and/or projects.
#           Run `gcloud topic configurations` to learn more.
# 
#           Some things to try next:
# 
#           * Run `gcloud --help` to see the Cloud Platform services you can
#           interact with. And run `gcloud help COMMAND` to get help on any
#           gcloud command.
#           * Run `gcloud topic -h` to learn about advanced features of the
#           SDK like arg files and output formatting
# 
#     The Google Cloud SDK is now configured and ready to use. The following are a few
# terminal commands for managing ‘gcloud’ configurations:
# 
#       •   ‘gcloud auth list’: Shows accounts with GCP credentials and indicates
#           which account configuration is currently active.
# 
#           gcloud auth list
# 
#                                 Credentialed Accounts
#           ACTIVE  ACCOUNT
#           *       your-email-id@gmail.com
# 
#           To set the active account, run:
#               $ gcloud config set account `ACCOUNT`
# 
#       •   ‘gcloud config configurations list’: List existing Cloud SDK
#           configurations.
# 
#           gcloud config configurations list
# 
#           NAME  IS_ACTIVE  ACCOUNT  PROJECT  DEFAULT_ZONE  DEFAULT_REGION
#           your-email-id  True  your-email-id@gmail.com     secret-
#           country-192905
# 
#       •     ‘gcloud config configurations activate [CONFIGURATION_NAME]’:
#             Use this command to activate a configuration.
# 
#             gcloud config configurations activate your-email-id
# 
#             Activated [your-email-id].
# 
#       •     ‘gcloud config configurations create [CONFIGURATION_NAME]’:
#             Use this command to create a new configuration.
#     This chapter covers how to set up command-line access for interacting with GCP
# resources. This includes working with the web-based Cloud Shell and installing the
# Cloud SDK to access GCP resources via the terminal on the local machine.
#     In the next chapter, we’ll introduce Google Cloud Storage (GCS) for storing
# ubiquitous data assets on GCP.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Google Cloud SDK",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Google Cloud SDK"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class GoogleCloud(HierNode):
    def __init__(self):
        super().__init__("Google Cloud SDK")
        self.add(Content())

# eof
