# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 47   Deploying an End-to-­End Machine Learning Solution on Kubeflow Pipelines
# 
# 
#  pload and Execute the Pipeline to Kubeflow
# U
# Pipelines
# The following steps upload and execute the compiled pipeline on Kubeflow Pipelines:
# 
#       1. Upload the pipeline to Kubeflow Pipelines (Figure 47-1).
# 
# 
# 
# 
# Figure 47-1. Upload the compiled pipeline to Kubeflow Pipelines
# 
# 
# 
# 
# 690
# 
#      Chapter 47    Deploying an End-to-­End Machine Learning Solution on Kubeflow Pipelines
# 
#      2. Click the pipeline to see the static graph of the flow (Figure 47-2).
# 
# 
# 
# 
# Figure 47-2. Pipeline summary graph
# 
#      3. Create an Experiment and run to execute the pipeline
#         (Figure 47-3).
# 
# 
# 
# 
#                                                                                        691
# 
# Chapter 47   Deploying an End-to-­End Machine Learning Solution on Kubeflow Pipelines
# 
# 
# 
# 
# Figure 47-3. Create and run the Experiment
# 
# 
# 
# 
# 692
# 
#        Chapter 47   Deploying an End-to-­End Machine Learning Solution on Kubeflow Pipelines
# 
#       4. Completed Pipeline run (Figure 47-4).
# 
# 
# 
# 
# Figure 47-4. Completed Pipeline run
# 
#     Completed Dataflow Pipeline: The completed run of the second component of
# the Pipeline, which is to transform the dataset with Cloud Dataflow, is illustrated in
# Figure 47-5.
# 
# 
# 
# 
#                                                                                          693
# 
# Chapter 47   Deploying an End-to-­End Machine Learning Solution on Kubeflow Pipelines
# 
# 
# 
# 
# Figure 47-5. Completed Dataflow run
# 
#      Deployed model on Cloud MLE: The deployed model on Cloud MLE, which is the
# fifth component of the Pipeline, is illustrated in Figure 47-6.
# 
# 
# 
# 
# Figure 47-6. Deployed model on Cloud MLE
# 
# 
#  Note Always remember to clean up cloud resources when they are no longer
#  needed.
# 
# 
# 694
# 
#        Chapter 47   Deploying an End-to-­End Machine Learning Solution on Kubeflow Pipelines
# 
#    Delete Kubeflow: Run the script to delete the deployment.
# 
# # navigate to kubeflow app
# cd ${KFAPP}
# 
# # run script to delete the deployment
# ${KUBEFLOW_SRC}/scripts/kfctl.sh delete all
# 
#    Delete the Kubernetes cluster: Replace name with your own cluster name.
# 
# # delete the kubernetes cluster
# gcloud container clusters delete ekaba-gke-cluster
# 
#    This chapter covered building an end-to-end machine learning product as a
# containerized application on Kubernetes with Kubeflow and Kubeflow pipelines. Again, the
# code for this chapter may be accessed by cloning the book repository to the Cloud Shell.
#    This concludes this book.
# 
# 
# 
# 
#                                                                                         695
# 
# Index
# A                                                       B
# Accuracy, 181, 294                                      Backpropagation
# Activation functions                                             algorithm, 337, 338
#    hyperbolic tangent (tanh), 341                       Backpropagation through time
#    Leaky ReLU, 342, 343                                          (BPTT), 453, 454
#    Maxout, 343                                          Bar plot, 154, 155
#    non-linear function, 339                             Batch gradient descent
#    ReLU, 342                                                     algorithm, 205
#    sigmoid, 340                                         Batch learning, 199–200
# Adaptive learning rates, 413                            Batch normalization, 408–410
# Alpine Linux package, 661                               Beam programming
# append() method, 76, 128, 129                              data processing pipeline
# Area under the receiver operating curve                        build/run, 541, 542
#          (AUC-ROC), 183–184, 294                               creation, 540
# argparse.ArgumentParser()                                      preprocessing, 543
#          method, 558                                       pipeline transformation
# Artificial neural network                                      I/O transforms, 539
#          (ANN), 329, 331, 332                                  Pcollection, 538
# assign method, 127                                             Ptransform, 538
# Autoencoder                                             Bias vs. variance trade-Off
#    architecture, 476                                       hidden layers, 402–403
#    defined, 475                                            high bias, 178
#    denoising, 481, 482                                     high variance, 178
#    undercomplete, 475                                      machine learning, 177
# AutoML NLP                                                 quality/performance, 178
#    custom language classification                       BigQuery
#           model (see Custom language                       defined, 485
#           classification model)                            first query
#    dataset, training, 602–604                                  census_bureau_international, 490
#    GCP, 599–601                                                Query editor, 491
#                                                                                              697
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Upload and Execute the Pipeline to Kubeflow Pipelines",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Upload and Execute the Pipeline to Kubeflow Pipelines"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Uploadand(HierNode):
    def __init__(self):
        super().__init__("Upload and Execute the Pipeline to Kubeflow Pipelines")
        self.add(Content())

# eof
