# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                    Download from finelybook www.finelybook.com
# iterate until you find the right number of layers to reuse. If you have plenty of train‐
# ing data, you may try replacing the top hidden layers instead of dropping them, and
# even add more hidden layers.
# 
# Model Zoos
# Where can you find a neural network trained for a task similar to the one you want to
# tackle? The first place to look is obviously in your own catalog of models. This is one
# good reason to save all your models and organize them so you can retrieve them later
# easily. Another option is to search in a model zoo. Many people train Machine Learn‐
# ing models for various tasks and kindly release their pretrained models to the public.
# TensorFlow has its own model zoo available at https://github.com/tensorflow/models.
# In particular, it contains most of the state-of-the-art image classification nets such as
# VGG, Inception, and ResNet (see Chapter 13, and check out the models/slim direc‐
# tory), including the code, the pretrained models, and tools to download popular
# image datasets.
# Another popular model zoo is Caffe’s Model Zoo. It also contains many computer
# vision models (e.g., LeNet, AlexNet, ZFNet, GoogLeNet, VGGNet, inception) trained
# on various datasets (e.g., ImageNet, Places Database, CIFAR10, etc.). Saumitro Das‐
# gupta wrote a converter, which is available at https://github.com/ethereon/caffe-
# tensorflow.
# 
# Unsupervised Pretraining
# Suppose you want to tackle a complex task for which you don’t have much labeled
# training data, but unfortunately you cannot find a model trained on a similar task.
# Don’t lose all hope! First, you should of course try to gather more labeled training
# data, but if this is too hard or too expensive, you may still be able to perform unsuper‐
# vised pretraining (see Figure 11-5). That is, if you have plenty of unlabeled training
# data, you can try to train the layers one by one, starting with the lowest layer and then
# going up, using an unsupervised feature detector algorithm such as Restricted Boltz‐
# mann Machines (RBMs; see Appendix E) or autoencoders (see Chapter 15). Each
# layer is trained on the output of the previously trained layers (all layers except the one
# being trained are frozen). Once all layers have been trained this way, you can fine-
# tune the network using supervised learning (i.e., with backpropagation).
# This is a rather long and tedious process, but it often works well; in fact, it is this
# technique that Geoffrey Hinton and his team used in 2006 and which led to the
# revival of neural networks and the success of Deep Learning. Until 2010, unsuper‐
# vised pretraining (typically using RBMs) was the norm for deep nets, and it was only
# after the vanishing gradients problem was alleviated that it became much more com‐
# mon to train DNNs purely using backpropagation. However, unsupervised pretrain‐
# ing (today typically using autoencoders rather than RBMs) is still a good option when
# 
#                                                               Reusing Pretrained Layers   |   291
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Model Zoos",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Model Zoos"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ModelZoos(HierNode):
    def __init__(self):
        super().__init__("Model Zoos")
        self.add(Content())

# eof
