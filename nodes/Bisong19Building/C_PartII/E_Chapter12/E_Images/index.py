# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Images
# Matplotlib is also used to visualize images. This process is utilized when visualizing a
# dataset of image pixels. You will observe that image data is stored in the computer as
# an array of pixel intensity values ranging from 0 to 255 across three bands for colored
# images.
# 
# img = plt.imread('nigeria-coat-of-arms.png')
# # check image dimension
# img.shape
# 'Output': (232, 240, 3)
# 
#    Note that the image contains 232 rows and 240 columns of pixel values across three
# channels (i.e., red, green, and blue).
#    Let’s print the first row of the columns in the first channel of our image data.
# Remember that each pixel is an intensity value from 0 to 255. Values closer to 0 are black,
# while those closer to 255 are white. The output is shown in Figure 12-15.
# 
# img[0,:,0]
# 'Output':
# array([0., 0., 0., ..., 0., 0., 0.], dtype=float32)
# 
#    Now let’s plot the image.
# 
# # plot image
# plt.imshow(img)
# plt.show()
# 
# 
# 
# 
# Figure 12-15. Nigeria Coat of Arms
# 
#     This chapter completes Part 2 of this book, which provides the foundation to
# programming for data science using the Python data science stack. In the next segment,
# Part 3, containing Chapters 13–17, we will provide an introduction to the field of
# machine learning.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Images",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Images"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Images(HierNode):
    def __init__(self):
        super().__init__("Images")
        self.add(Content())

# eof
