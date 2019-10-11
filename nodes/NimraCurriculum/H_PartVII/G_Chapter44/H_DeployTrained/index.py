# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                 Chapter 44   Model to Predict the Critical Temperature of Superconductors
# 
# 
# 
# 
# Figure 44-5. Cloud MLE training output
# 
# 
# Deploy Trained Model
# The best model trial with the lowest objectiveValue is deployed for inference on
# Cloud MLE:
# 
#      •   Display content of selected trained model directory.
# 
#          %%bash
#          gsutil ls gs://${BUCKET}/jobs/superconductor_181222_040429/4/
#          export/superconductor/1545452450
# 
#          'Output':
#          gs://superconductor/jobs/superconductor_181222_040429/4/export/
#          superconductor/1545452450/
#          gs://superconductor/jobs/superconductor_181222_040429/4/export/
#          superconductor/1545452450/saved_model.pb
#          gs://superconductor/jobs/superconductor_181222_040429/4/export/
#          superconductor/1545452450/variables/
# 
# 
# 
#                                                                                      649
# 
# Chapter 44     Model to Predict the Critical Temperature of Superconductors
# 
#       •   Deploy the model.
# 
#              %%bash
#              MODEL_NAME="superconductor"
#              MODEL_VERSION="v1"
#              MODEL_LOCATION=gs://$bucket_name/jobs/
#              superconductor_181222_040429/4/export/superconductor/1545452450
# 
#              echo "Deploying model $MODEL_NAME $MODEL_VERSION"
#              gcloud ai-platform models create ${MODEL_NAME} --regions us-central1
#              gcloud ai-platform versions create ${MODEL_VERSION} --model
#              ${MODEL_NAME} --origin ${MODEL_LOCATION} --runtime-version ${tf_
#              version}
# 
# 
# 
# Batch Prediction
# The following code carries out inference on the deployed model:
# 
#       •   Submit a batch prediction job.
# 
#              %%bash
#              JOB_NAME=superconductor_prediction
#              MODEL_NAME=superconductor
#              MODEL_VERSION=v1
#              TEST_FILE=gs://$bucket_name/preproc_csv/data/eval-00-of-01.csv
#              OUTPUT_DIR=gs://$bucket_name/jobs/$JOB_NAME/predictions
# 
#              echo $OUTPUT_DIR
# 
#              # submit a batched job
#              gcloud ai-platform jobs submit prediction $JOB_NAME \
#                      --model $MODEL_NAME \
#                      --version $MODEL_VERSION \
#                      --data-format TEXT \
#                      --region $region \
#                      --input-paths $TEST_FILE \
#                            --output-path $OUTPUT_DIR
# 
# 
# 
# 650
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Deploy Trained Model")
        self.add(MarkdownBlock("# Deploy Trained Model"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DeployTrained(HierNode):
    def __init__(self):
        super().__init__("Deploy Trained Model")
        self.add(Content())

# eof
