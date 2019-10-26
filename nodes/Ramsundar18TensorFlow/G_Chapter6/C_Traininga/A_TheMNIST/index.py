# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Figure 6-16. The CycleGAN is capable of performing complex image transformations,
# such as transforming images of horses into those of zebras (and vice versa).
# 
# Unfortunately, generative adversarial networks are still challenging to train in prac‐
# tice. Making generators and discriminators learn reasonable functions requires a
# deep bag of tricks. As a result, while there have been many exciting GAN demonstra‐
# tions, GANs have not yet matured into a state where they can be widely deployed in
# industrial applications.
# 
# Training a Convolutional Network in TensorFlow
# In this section we consider a code sample for training a simple convolutional neural
# network. In particular, our code sample will demonstrate how to train a LeNet-5 con‐
# volutional architecture on the MNIST dataset using TensorFlow. As always, we rec‐
# ommend that you follow along by running the full code sample from the GitHub
# repo associated with the book.
# 
# The MNIST Dataset
# The MNIST dataset consists of images of handwritten digits. The machine learning
# challenge associated with MNIST consists of creating a model trained on the training
# set of digits that generalizes to the validation set. Figure 6-17 shows some images
# drawn from the MNIST dataset.
# 
# 
# 
# 
# 134   |   Chapter 6: Convolutional Neural Networks
# 
# Figure 6-17. Some images of handwritten digits from the MNIST dataset. The learning
# challenge is to predict the digit from the image.
# 
# MNIST was a very important dataset for the development of machine learning meth‐
# ods for computer vision. The dataset is challenging enough that obvious, non-
# learning methods don’t tend to do well. At the same time, MNIST is small enough
# that experimenting with new architectures doesn’t require very large amounts of
# computing power.
# However, the MNIST dataset has mostly become obsolete. The best models achieve
# near one hundred percent test accuracy. Note that this fact doesn’t mean that the
# problem of handwritten digit recognition is solved! Rather, it is likely that human sci‐
# entists have overfit architectures to the MNIST dataset and capitalized on its quirks to
# achieve very high predictive accuracies. As a result, it’s no longer good practice to use
# MNIST to design new deep architectures. That said, MNIST is still a superb dataset
# for pedagogical purposes.
# 
# Loading MNIST
# The MNIST codebase is located online on Yann LeCun’s website. The download
# script pulls down the raw file from the website. Notice how the script caches the
# download so repeated calls to download() won’t waste effort.
# 
# 
# 
#                                               Training a Convolutional Network in TensorFlow   |   135
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "The MNIST Dataset",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(mbk("# The MNIST Dataset"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TheMNIST(HierNode):
    def __init__(self):
        super().__init__("The MNIST Dataset")
        self.add(Content())

# eof
