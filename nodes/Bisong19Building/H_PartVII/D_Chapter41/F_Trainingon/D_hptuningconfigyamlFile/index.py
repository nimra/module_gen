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
#                              Chapter 41   Google Cloud Machine Learning Engine (Cloud MLE)
# 
#         maxValue: 15
#         scaleType: UNIT_LINEAR_SCALE
#       - parameterName: scale-factor
#         type: DOUBLE
#         minValue: 0.1
#         maxValue: 1.0
#         scaleType: UNIT_REVERSE_LOG_SCALE
# 
# 
# 
# Execute Training Job with Hyper-parameter Tuning
# Run the following code on the terminal to launch a distributed training job.
# 
# source ./scripts/hyper-tune.sh
# 
# gs://iris-dataset/jobs/iris_20181114_190121
# Job [iris_20181114_190121] submitted successfully.
# INFO    2018-11-14 12:41:07 -0500   service     Validating job
#                                                  requirements...
# INFO    2018-11-14 12:41:07 -0500   service     Job creation request
#                                                  has been successfully
#                                                  validated.
# INFO    2018-11-14 12:41:08 -0500   service     Job iris_20181114_190121 is
#                                                  queued.
# INFO    2018-11-14 12:41:18 -0500   service     Waiting for job to be
#                                                  provisioned.
# INFO    2018-11-14 12:41:18 -0500   service     Waiting for job to be
#                                                  provisioned.
# ...
# INFO    2018-11-14 12:56:38 -0500   service     Finished tearing down
#                                                  training program.
# INFO    2018-11-14 12:56:45 -0500   service     Finished tearing down
#                                                  training program.
# INFO    2018-11-14 12:57:37 -0500   service     Job completed successfully.
# INFO    2018-11-14 12:57:43 -0500   service     Job completed successfully.
# endTime: '2018-11-14T13:04:34'
# jobId: iris_20181114_190121
# 
#                                                                                       563
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "hptuning_config.yaml File",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# hptuning_config.yaml File"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class hptuningconfigyamlFile(HierNode):
    def __init__(self):
        super().__init__("hptuning_config.yaml File")
        self.add(Content())

# eof
