# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                                Chapter 34   Regularization for Deep Learning
# 
# # create the model
# def model_fn():
#     model = tf.keras.Sequential()
#     # Adds a densely-connected layer with 256 units to the model:
#     model.add(tf.keras.layers.Dense(256, activation='relu', input_dim=784))
#     # Add Dropout layer
#     model.add(tf.keras.layers.Dropout(rate=0.2))
#     # Add another densely-connected layer with 64 units:
#     model.add(tf.keras.layers.Dense(64, activation='relu'))
#     # Add a softmax layer with 10 output units:
#     model.add(tf.keras.layers.Dense(10, activation='softmax'))
# 
#     # compile the model
#     model.compile(optimizer=tf.train.AdamOptimizer(0.001),
#                     loss='categorical_crossentropy',
#                     metrics=['accuracy'])
#     return model
# 
# 
# 
# Data Augmentation
# Data augmentation is a method for artificially generating more training data points.
# This technique is precipitated on the observation that for an increasingly large training
# dataset mitigates the problem of overfitting. For some problems, it may be easy to
# artificially generate fake data, while for others it may not readily be the case. A classic
# example where we can use data augmentation is in the case of image classification. Here
# artificial images can easily be created by rotating or scaling the original images to create
# more variations of the dataset for a particular image class.
# 
# 
# 
# Noise Injection
# The noise injection regularization method adds some Gaussian noise to the network
# inputs during training. Also, Gaussian noise can be added to the hidden units to mitigate
# overfitting. Yet still another form of injecting noise into the network is to add some
# Gaussian noise to the network weights. Noise injection can be considered as a form
# of data augmentation. The amount of noise added is a configurable hyper-parameter.
# 
#                                                                                         417
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Data Augmentation",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Data Augmentation"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DataAugmentation(HierNode):
    def __init__(self):
        super().__init__("Data Augmentation")
        self.add(Content())

# eof
