# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 30   TensorFlow 2.0 and Keras
# 
# 
# 
# 
# Figure 30-1. TensorFlow API hierarchy
# 
# 
# The Low-Level TensorFlow APIs
# The low-level API gives the tools for building network graphs from the ground up using
# mathematical operations. This API level affords the greatest level of flexibility to tweak
# and tune the model as desired. Moreover, the higher-level APIs implement low-level
# operations under the hood.
# 
# 
# The Mid-Level TensorFlow APIs
# TensorFlow provides a set of reusable packages for simplifying the process involved in
# creating neural network models. Some examples of these functions include the layers
# (tf.keras.layers), Datasets (tf.data), metrics (tf.keras.metrics), loss (tf.keras.losses),
# and FeatureColumns (tf.feature_column) packages.
# 
# L ayers
# The layers package (tf.keras.layers) provides a handy set of functions to simplify the
# construction of layers in a neural network architecture. For example, consider the
# convolutional network architecture in Figure 30-2 and how the layers API simplifies the
# creation of the network layers.
# 
# 
# 
# 348
# 
#                                                       Chapter 30   TensorFlow 2.0 and Keras
# 
# 
# 
# 
# Figure 30-2. Using the layers API to simplify creating the layers of a neural
# network
# 
# 
# D
#  atasets
# The Dataset package (tf.data) provides a convenient set of high-level functions for
# creating complex dataset input pipelines. The goal of the Dataset package is to have
# a fast, flexible, and easy-to-use interface for fetching data from various data sources,
# performing data transform operations on them before passing them as inputs to the
# learning model. The Dataset API provides a more efficient means of fetching records
# from a dataset. The major classes of the Dataset API are illustrated in Figure 30-3.
# 
# 
#                                                                                            349
# 
# Chapter 30    TensorFlow 2.0 and Keras
# 
# 
# 
# 
# Figure 30-3. Dataset API class hierarchy
# 
#       From the illustration in Figure 30-3, the subclasses perform the following functions:
# 
#         •   TextLineDataset: This class is used for reading lines from text files.
# 
#         •   TFRecordDataset: This class is responsible for reading records
#             from TFRecord files. A TFRecord file is a TensorFlow binary storage
#             format. It is faster and easier to work with data stored as TFRecord
#             files as opposed to raw data files. Working with TFRecord also
#             makes the data input pipeline more easily aligned for applying vital
#             transformations such as shuffling and returning data in batches.
# 
#         •   FixedLengthRecordDataset: This class is responsible for reading
#             records of fixed sizes from binary files.
# 
# F eatureColumns
# FeatureColumns tf.feature_column is a TensorFlow functionality for describing the
# features of the dataset that will be fed into a high-level Keras or Estimator models for
# training and validation. FeatureColumns makes it easy to prepare data for modeling by
# carrying out tasks such as the conversion of categorical features of the dataset into a one-­
# hot encoded vector.
#     The feature_column API is broadly divided into two categories; they are the
# categorical and dense columns. The categories and subsequent functions are illustrated
# in Figure 30-4.
# 
# 350
# 
#                                                         Chapter 30    TensorFlow 2.0 and Keras
# 
# 
# 
# 
# Figure 30-4. Function calls of the Feature Column API
# 
#    Let’s go through each API function briefly in Table 30-1.
# 
# Table 30-1. tf.feature_column API Functions
# Function name            Description
# 
# Numeric column –         This is a high-level wrapper for numeric features in the dataset.
# tf.feature_column.
# numeric_column()
# Indicator column –       The indicator column takes as input a categorical column and
# tf.feature_column.       transforms it into a one-hot encoded vector.
# indicator_column()
# Embedding column –       The embedding column function transforms a categorical column
# tf.feature_column.       with multiple levels or classes into a lower-dimensional numeric
# embedding_column()       representation that captures the relationships between the categories.
#                          Using embeddings mitigates the problem of a large sparse vector (an
#                          array with mostly zeros) created via one-hot encoding for a dataset
#                          feature with lots of different classes.
#                                                                                     (continued)
# 
# 
# 
#                                                                                              351
# 
# Chapter 30   TensorFlow 2.0 and Keras
# 
# Table 30-1. (continued)
# Function name             Description
# 
# Categorical column with   This function creates a one-hot encoded output of a categorical
# identity – tf.feature_    column containing identities, e.g, [‘0’, ‘1’, ‘2’, ‘3’].
# column.categorical_
# column_with_identity()
# Categorical column        This function creates a one-hot encoded output of a categorical
# with vocabulary list –    column with strings. It maps each string to an integer based on a
# tf.feature_column.        vocabulary list. However, if the vocabulary list is long, it is best to
# categorical_ column_      create a file containing the vocabulary and use the function tf.feature_
# with_vocabulary_list()    column.categorical_ column_with_vocabulary_file().
# Categorical column with   This function specifies the number of categories by using the hash of
# hash bucket –             the inputs. It is used when it is not possible to create a vocabulary for
# tf.feature_column.        the number of categories due to memory considerations.
# categorical_ column_
# with_hash_buckets()
# Crossed column –          The function gives the ability to combine multiple input features into a
# tf.feature_columns.       single input feature.
# crossed_column()
# Bucketized column –       The function splits a column of numerical inputs into buckets to form
# tf.feature_column.        new classes based on a specified set of numerical ranges.
# bucketized_column()
# 
# 
# 
# The High-Level TensorFlow APIs
# The high-level API provides simplified API calls that encapsulate lots of the details that
# are typically involved in creating a deep learning TensorFlow model. These high-level
# abstractions make it easier to develop powerful deep learning models quickly with fewer
# lines of code.
# 
# 
# 
# 
# 352
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("The Mid-Level TensorFlow APIs")
        self.add(MarkdownBlock("# The Mid-Level TensorFlow APIs"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TheMidLevel(HierNode):
    def __init__(self):
        super().__init__("The Mid-Level TensorFlow APIs")
        self.add(Content())

# eof
