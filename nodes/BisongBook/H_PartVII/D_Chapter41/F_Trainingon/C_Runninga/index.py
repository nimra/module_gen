# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
# Chapter 41   Google Cloud Machine Learning Engine (Cloud MLE)
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
# 
# hptuning_config.yaml File
# This file contains the hyper-parameter and the ranges we wish to explore in tuning
# our training job on Cloud MLE. The goal of the tuning job is to ‘MAXIMIZE’ the
# ‘accuracy’ metric.
# 
# trainingInput:
#   hyperparameters:
#     goal: MAXIMIZE
#     hyperparameterMetricTag: accuracy
#     maxTrials: 4
#     maxParallelTrials: 2
#     params:
#       - parameterName: learning-rate
#         type: DOUBLE
#         minValue: 0.00001
#         maxValue: 0.005
#         scaleType: UNIT_LOG_SCALE
#       - parameterName: first-layer-size
#         type: INTEGER
#         minValue: 50
#         maxValue: 500
#         scaleType: UNIT_LINEAR_SCALE
#       - parameterName: num-layers
#         type: INTEGER
#         minValue: 1
# 
# 562
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Running a Distributed Training Job with Hyper-parameter Tuning",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Running a Distributed Training Job with Hyper-parameter Tuning"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Runninga(HierNode):
    def __init__(self):
        super().__init__("Running a Distributed Training Job with Hyper-parameter Tuning")
        self.add(Content())

# eof
