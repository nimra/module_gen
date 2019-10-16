# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 42     Google AutoML: Cloud Vision
# 
#           The first part is the image path or URI, while the other is the
#           image label.
# 
#       6. When preparing the image dataset, it is useful to have a ‘None_
#          of_the_above’ image class. This class will contain random images
#          that do not belong to any of the predicted classes. Adding this
#          class can have an overall effect on the model accuracy.
# 
#       7. Clone the GitHub book repository to the Notebook instance.
#       8. Navigate to the folder chapter and copy the image files to the GCS
#          bucket.
# 
#              gsutil cp -r cereal_photos gs://quantum-ally-219323-vcm
# 
#       9. Copy the CSV data file containing the image paths and their labels
#          to the GCS bucket.
# 
#              gsutil cp data.csv gs://quantum-ally-219323-vcm/cereal_photos/
# 
# 
# 
#  uilding Custom Image Models on Cloud
# B
# AutoML Vision
# In AutoML for Cloud Vision, a dataset contains the images that will be used in building
# the classifier and their corresponding labels. This section will walk through creating a
# dataset and building a custom image model on AutoML Vision.
#       1. From the Cloud AutoML Vision Dashboard, click NEW DATASET
#          as shown in Figure 42-8.
# 
# 
# 
# 
# 588
# 
#                                                Chapter 42   Google AutoML: Cloud Vision
# 
# 
# 
# 
# Figure 42-8. New Dataset on AutoML Vision
# 
#      2. To create a Dataset on Cloud AutoML Vision, set the following
#         parameters as shown in Figure 42-9:
# 
# 
# 
# 
#                                                                                    589
# 
# Chapter 42     Google AutoML: Cloud Vision
# 
# 
# 
# 
# Figure 42-9. Create a Dataset on Cloud AutoML Vision
# 
#              a. Dataset name: cereal_classifier.
# 
#              b. Select a CSV file on Cloud Storage (this is the CSV file placed on the bucket
#                 created when Cloud AutoML was configured that contains the path to the
#                 images): gs://quantum-ally-219323-vcm/cereal_photos/data.csv.
# 
#              c. Click CREATE DATASET to begin importing images (see Figure 42-10).
# 
# 
# 
# 
# 590
# 
#                                                 Chapter 42   Google AutoML: Cloud Vision
# 
# 
# 
# 
# Figure 42-10. Cloud AutoML Vision: Importing images
# 
#      3. After importing the Dataset, click TRAIN (see Figure 42-11) to
#         initiate the process of building a custom image recognition model.
# 
# 
# 
# 
# Figure 42-11. Cloud AutoML Vision: Imported images and their labels
# 
#      4. In machine learning, more labeled training examples boost the
#         performance of the model. Likewise, when using AutoML, there
#         should be at least 100 training examples for each image class. In
#         the example used in this section, some classes do not have up to
# 
#                                                                                     591
# 
# Chapter 42   Google AutoML: Cloud Vision
# 
#          100 examples, so AutoML gives a warning as seen in Figure 42-12.
#          However, for the purposes of this exercise, we will continue with
#          training. Click START TRAINING.
# 
# 
# 
# 
# Figure 42-12. Cloud AutoML Vision requesting for more training examples per
# image class
# 
#       5. Choose how long the model will be trained. More training time
#          might have an effect on the model accuracy, but this may cost
#          more for running on Cloud AutoML’s machines (see Figure 42-13).
#          Again, click START TRAINING to begin building the model (see
#          Figure 42-14).
# 
# 592
# 
#                                               Chapter 42   Google AutoML: Cloud Vision
# 
# 
# 
# 
# Figure 42-13. Select training budget
# 
# 
# 
# 
# Figure 42-14. Training vision model on Cloud AutoML Vision
# 
#      6. The training summary is shown in Figure 42-15.
# 
# 
# 
# 
#                                                                                   593
# 
# Chapter 42   Google AutoML: Cloud Vision
# 
# 
# 
# 
# Figure 42-15. Cloud AutoML Vision: Training summary
# 
#       7. AutoML Vision uses the set-aside test images to evaluate the
#          quality of the model after training as seen in Figure 42-16. The F1
#          plot showing the trade-off between precision and recall is shown
#          in Figure 42-17. Also, a visual confusion matrix is provided to
#          further evaluate the model quality (see Figure 42-18).
# 
# 
# 
# 
# 594
# 
#                                           Chapter 42   Google AutoML: Cloud Vision
# 
# 
# 
# 
# Figure 42-16. Cloud AutoML Vision: Model evaluation
# 
# 
# 
# 
# Figure 42-17. F1 evaluation matrix on Cloud AutoML Vision
# 
# 
# 
# 
#                                                                               595
# 
# Chapter 42   Google AutoML: Cloud Vision
# 
# 
# 
# 
# Figure 42-18. Confusion matrix for model evaluation on Cloud AutoML Vision
# 
#       8. The custom image recognition model is exposed as a REST or
#          Python API for integration into software applications as a prediction
#          service (see Figure 42-19). We can test our model by uploading a
#          sample image for classification as shown in Figure 42-20.
# 
# 
# 
# 
# Figure 42-19. Cloud AutoML Vision: Model as a prediction service
# 596
# 
#                                                  Chapter 42    Google AutoML: Cloud Vision
# 
# 
# 
# 
# Figure 42-20. Test prediction service on Cloud AutoML Vision
# 
#      9. To delete a model, click the triple dash and select Models to
#         navigate to the Models Dashboard (see Figure 42-21). At the side
#         of the model, click the triple dot and select Delete model (see
#         Figure 42-22). Confirm deletion as shown in Figure 42-23. Note,
#         however, that API calls affiliated with a deleted model will cease to
#         be operational.
# 
# 
# 
# 
#                                                                                       597
# 
# Chapter 42   Google AutoML: Cloud Vision
# 
# 
# 
# 
# Figure 42-21. Return to Models dashboard
# 
# 
# 
# 
# Figure 42-22. Select model to delete
# 
# 
# 
# 
# Figure 42-23. Delete a model on Cloud AutoML Vision
# 
#     This chapter covered building and deploying custom image classification models
# using Google AutoML Cloud Vision. In the next chapter, we will discover how to build
# and deploy custom text classification models with Google Cloud AutoML for natural
# language processing.
# 
# 598
# 
# CHAPTER 43
# 
# 
# 
# Google AutoML: Cloud
# Natural Language
# Processing
# This chapter will build a language toxicity classification model to classify and recognize
# toxic and non-toxic or clean phrases using Google Cloud AutoML for natural language
# processing (NLP). The data used in this project is from the Toxic Comment Classification
# Challenge on Kaggle by Jigsaw and Google. The data is modified to have a sample of
# 16,000 toxic and 16,000 non-toxic words as inputs to build the model on AutoML NLP.
# 
# 
# 
# Enable AutoML NLP on GCP
# The following steps will enable AutoML NLP on GCP:
# 
#        1. Click the triple dash in the top-left corner of the interface and
#           select Natural Language under the category ARTIFICIAL
#           INTELLIGENCE as shown in Figure 43-1.
# 
# 
# 
# 
#                                                                                           599
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_43
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Building Custom Image Models on Cloud AutoML Vision",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Building Custom Image Models on Cloud AutoML Vision"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class BuildingCustom(HierNode):
    def __init__(self):
        super().__init__("Building Custom Image Models on Cloud AutoML Vision")
        self.add(Content())

# eof
