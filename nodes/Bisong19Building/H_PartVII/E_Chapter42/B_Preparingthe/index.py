# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 42     Google AutoML: Cloud Vision
# 
# 
# Preparing the Training Dataset
# Before building a custom image recognition model with AutoML Cloud Vision, the
# dataset must be prepared in a particular format; they include
# 
#       1. For training, JPEG, PNG, WEBP, GIF, BMP, TIFF, and ICO image
#          formats are supported with a maximum size of 30mb per image.
# 
#       2. For inference, the image formats JPEG, PNG, and GIF are
#          supported with each image being of maximum size 1.5mb.
# 
#       3. It is best to place each image category into containing sub-folder
#          within an image folder For example:
# 
#          •      [image-directory]
# 
#                •   [image-class-1-dir]
# 
#                •   [image-class-2-dir]
# 
#                •   …
# 
#                •   [image-class-n-dir]
# 
#       4. Next, a CSV must be created that points to the paths of the images
#          and their corresponding label. AutoML uses the CSV file to point
#          to the location of the training images and their labels. The CSV
#          file is placed in the same GCS bucket containing the image files.
#          Use the bucket automatically created when AutoML Vision was
#          configured. In our case, this bucket is named ‘gs://quantum-ally-
#          219323-vcm’. We use the following code segment to create the CSV
#          file used in the cereal classifier example.
# 
#              import os
#              import numpy as np
#              import pandas as pd
# 
#              directory = 'cereal_photos/
# 
#              data = []
# 
#              # go through sub-directories in the image directory and get the
#              image paths
# 
# 586
# 
#                                            Chapter 42   Google AutoML: Cloud Vision
# 
#    for subdir, dirs, files in os.walk(directory):
#        for file in files:
#            filepath = subdir + os.sep + file
# 
#            if filepath.endswith(".jpg"):
#                
#                entry = ['{}/{}'.format('gs://quantum-ally-219323-­
#                vcm',filepath), os.path.basename(subdir)]
#                data.append(entry)
# 
#    # convert to Pandas DataFrame
#    data_pd = pd.DataFrame(np.array(data))
# 
#    # export CSV
#    data_pd.to_csv("data.csv", header=None, index=None)
# 
# 5. The preceding code will result in a CSV looking like the following
#    sample:
# 
#    gs://quantum-ally-219323-vcm/cereal_photos/apple_cinnamon_
#    cheerios/001.jpg,apple_cinnamon_cheerios
#    gs://quantum-ally-219323-vcm/cereal_photos/apple_cinnamon_
#    cheerios/002.jpg,apple_cinnamon_cheerios
#    gs://quantum-ally-219323-vcm/cereal_photos/apple_cinnamon_
#    cheerios/003.jpg,apple_cinnamon_cheerios
#    ...
#    gs://quantum-ally-219323-vcm/cereal_photos/none_of_the_above/
#    images_(97).jpg,none_of_the_above
#    gs://quantum-ally-219323-vcm/cereal_photos/none_of_the_above/
#    images_(98).jpg,none_of_the_above
#    gs://quantum-ally-219323-vcm/cereal_photos/none_of_the_above/
#    images_(99).jpg,none_of_the_above
#    ...
#    gs://quantum-ally-219323-vcm/cereal_photos/sugar_crisp/001.
#    jpg,sugar_crisp
#    gs://quantum-ally-219323-vcm/cereal_photos/sugar_crisp/002.
#    jpg,sugar_crisp
#    gs://quantum-ally-219323-vcm/cereal_photos/sugar_crisp/003.
#    jpg,sugar_crisp
# 
#                                                                                587
# 
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Preparing the Training Dataset",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Preparing the Training Dataset"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Preparingthe(HierNode):
    def __init__(self):
        super().__init__("Preparing the Training Dataset")
        self.add(Content())

# eof
