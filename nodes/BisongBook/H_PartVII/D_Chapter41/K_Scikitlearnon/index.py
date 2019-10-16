# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 41     Google Cloud Machine Learning Engine (Cloud MLE)
# 
#       To execute the code, run
# 
# source ./scripts/gpu-hyper-tune.sh
# 
# gs://iris-dataset/jobs/iris_20181112_211040
# Job [iris_20181112_211040] submitted successfully.
# ...
# INFO    2018-11-12 21:35:36 -0500   ps-replica-2    4   Module completed;
#                                                          cleaning up.
# INFO    2018-11-12 21:35:36 -0500   ps-replica-2    4   Clean up finished.
# INFO    2018-11-12 21:36:18 -0500   service     Finished tearing down
#                                                  training program.
# INFO    2018-11-12 21:36:25 -0500   service     Finished tearing down
#                                                  training program.
# INFO    2018-11-12 21:37:11 -0500   service     Job completed successfully.
# INFO    2018-11-12 21:37:11 -0500   service     Job completed successfully.
# endTime: '2018-11-12T21:38:26'
# jobId: iris_20181112_211040
# startTime: '2018-11-12T21:10:47'
# state: SUCCEEDED
# 
# 
# 
# Scikit-learn on Cloud MLE
# This section will provide a walk-through of training a Scikit-learn model on Google
# Cloud MLE using the same Iris dataset example. We’ll begin by moving the appropriate
# data files from the GitHub repository of this book to GCS.
# 
# 
# 
# Move the Data Files to GCS
# Walk through the following steps to move the data files to GCS:
# 
#         1. Create bucket to hold the datasets.
# 
#              gsutil mb gs://iris-sklearn
# 
# 
# 
# 
# 572
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Scikit-learn on Cloud MLE",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Scikit-learn on Cloud MLE"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Scikitlearnon(HierNode):
    def __init__(self):
        super().__init__("Scikit-learn on Cloud MLE")
        self.add(Content())

# eof
