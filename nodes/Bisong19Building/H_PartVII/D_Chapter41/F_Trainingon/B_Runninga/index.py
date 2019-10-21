# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 41   Google Cloud Machine Learning Engine (Cloud MLE)
# 
# INFO    2018-11-12 01:05:32 -0500   service     Waiting for training
#                                                  program to start.
# ...
# INFO    2018-11-12 01:09:05 -0500   ps-replica-2        Module completed;
#                                                          cleaning up.
# INFO    2018-11-12 01:09:05 -0500   ps-replica-2        Clean up finished.
# INFO    2018-11-12 01:09:55 -0500   service             Finished tearing
#                                                          down training
#                                                          program.
# INFO    2018-11-12 01:10:53 -0500   service             Job completed
#                                                          successfully.
# endTime: '2018-11-12T01:08:35'
# jobId: iris_20181112_010123
# startTime: '2018-11-12T01:07:34'
# state: SUCCEEDED
# 
# 
# Running a Distributed Training Job
# The code for initiating distributed training on Cloud MLE is shown in the following, and
# the code is stored in the file ‘distributed-training.sh’. For a distributed job, the attribute
# ‘- -scale-tier’ is set to a tier above the basic machine type. Change the bucket names
# accordingly.
# 
# export SCALE_TIER=STANDARD_1 # BASIC | BASIC_GPU | STANDARD_1 | PREMIUM_1 |
# BASIC_TPU
# DATE=`date '+%Y%m%d_%H%M%S'`
# export JOB_NAME=iris_$DATE
# export GCS_JOB_DIR=gs://iris-dataset/jobs/$JOB_NAME
# export TRAIN_FILE=gs://iris-dataset/train_data.csv
# export EVAL_FILE=gs://iris-dataset/test_data.csv
# 
# echo $GCS_JOB_DIR
# 
# gcloud ai-platform jobs submit training $JOB_NAME \
#                                     --stream-logs \
#                                     --scale-tier $SCALE_TIER \
#                                     --runtime-version 1.8 \
# 
# 560
# 
#                              Chapter 41    Google Cloud Machine Learning Engine (Cloud MLE)
# 
#                                     --job-dir $GCS_JOB_DIR \
#                                     --module-name trainer.task \
#                                     --package-path trainer/ \
#                                     --region us-central1 \
#                                     -- \
#                                     --train-files $TRAIN_FILE \
#                                     --eval-files $EVAL_FILE \
#                                     --train-steps 5000 \
#                                     --eval-steps 100
# 
#    The following executes a distributed training job.
# 
# source ./scripts/distributed-training.sh
# 
# 
#  unning a Distributed Training Job with
# R
# Hyper-parameter Tuning
# To run a training job with hyper-parameter tuning, add the ‘- -config’ attribute and link
# to the ‘.yaml’ hyper-parameter configuration file. The code for running the job is the
# same, but with the attribute ‘- -config’ added. Change the bucket names accordingly.
# 
# export SCALE_TIER=STANDARD_1 # BASIC | BASIC_GPU | STANDARD_1 | PREMIUM_1 |
# BASIC_TPU
# DATE=`date '+%Y%m%d_%H%M%S'`
# export JOB_NAME=iris_$DATE
# export HPTUNING_CONFIG=hptuning_config.yaml
# export GCS_JOB_DIR=gs://iris-dataset/jobs/$JOB_NAME
# export TRAIN_FILE=gs://iris-dataset/train_data.csv
# export EVAL_FILE=gs://iris-dataset/test_data.csv
# 
# echo $GCS_JOB_DIR
# 
# gcloud ai-platform jobs submit training $JOB_NAME \
#                                     --stream-logs \
#                                     --scale-tier $SCALE_TIER \
#                                     --runtime-version 1.8 \
#                                     --config $HPTUNING_CONFIG \
# 
# 
#                                                                                        561
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Running a Distributed Training Job",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Running a Distributed Training Job"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Runninga(HierNode):
    def __init__(self):
        super().__init__("Running a Distributed Training Job")
        self.add(Content())

# eof
