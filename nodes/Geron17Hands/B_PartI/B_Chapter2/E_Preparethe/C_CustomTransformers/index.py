# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.HierBlock import HierBlock as hbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.ListBlock import ListBlock as lbk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                        Download from finelybook www.finelybook.com
#                [ 1.,    0.,    0.,    0.,    0.],
#                [ 0.,    0.,    0.,    1.,    0.]])
# We can apply both transformations (from text categories to integer categories, then
# from integer categories to one-hot vectors) in one shot using the LabelBinarizer
# class:
#      >>> from sklearn.preprocessing import LabelBinarizer
#      >>> encoder = LabelBinarizer()
#      >>> housing_cat_1hot = encoder.fit_transform(housing_cat)
#      >>> housing_cat_1hot
#      array([[0, 1, 0, 0, 0],
#             [0, 1, 0, 0, 0],
#             [0, 0, 0, 0, 1],
#             ...,
#             [0, 1, 0, 0, 0],
#             [1, 0, 0, 0, 0],
#             [0, 0, 0, 1, 0]])
# Note that this returns a dense NumPy array by default. You can get a sparse matrix
# instead by passing sparse_output=True to the LabelBinarizer constructor.
# 
# Custom Transformers
# Although Scikit-Learn provides many useful transformers, you will need to write
# your own for tasks such as custom cleanup operations or combining specific
# attributes. You will want your transformer to work seamlessly with Scikit-Learn func‐
# tionalities (such as pipelines), and since Scikit-Learn relies on duck typing (not inher‐
# itance), all you need is to create a class and implement three methods: fit()
# (returning self), transform(), and fit_transform(). You can get the last one for
# free by simply adding TransformerMixin as a base class. Also, if you add BaseEstima
# tor as a base class (and avoid *args and **kargs in your constructor) you will get
# two extra methods (get_params() and set_params()) that will be useful for auto‐
# matic hyperparameter tuning. For example, here is a small transformer class that adds
# the combined attributes we discussed earlier:
#      from sklearn.base import BaseEstimator, TransformerMixin
# 
#      rooms_ix, bedrooms_ix, population_ix, household_ix = 3, 4, 5, 6
# 
#      class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
#          def __init__(self, add_bedrooms_per_room = True): # no *args or **kargs
#              self.add_bedrooms_per_room = add_bedrooms_per_room
#          def fit(self, X, y=None):
#              return self # nothing else to do
#          def transform(self, X, y=None):
#              rooms_per_household = X[:, rooms_ix] / X[:, household_ix]
#              population_per_household = X[:, population_ix] / X[:, household_ix]
#              if self.add_bedrooms_per_room:
#                  bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
# 
# 
# 64   |   Chapter 2: End-to-End Machine Learning Project
# 
#                   Download from finelybook www.finelybook.com
#                 return np.c_[X, rooms_per_household, population_per_household,
#                              bedrooms_per_room]
#             else:
#                 return np.c_[X, rooms_per_household, population_per_household]
# 
#     attr_adder = CombinedAttributesAdder(add_bedrooms_per_room=False)
#     housing_extra_attribs = attr_adder.transform(housing.values)
# 
# In this example the transformer has one hyperparameter, add_bedrooms_per_room,
# set to True by default (it is often helpful to provide sensible defaults). This hyperpara‐
# meter will allow you to easily find out whether adding this attribute helps the
# Machine Learning algorithms or not. More generally, you can add a hyperparameter
# to gate any data preparation step that you are not 100% sure about. The more you
# automate these data preparation steps, the more combinations you can automatically
# try out, making it much more likely that you will find a great combination (and sav‐
# ing you a lot of time).
# 
# Feature Scaling
# One of the most important transformations you need to apply to your data is feature
# scaling. With few exceptions, Machine Learning algorithms don’t perform well when
# the input numerical attributes have very different scales. This is the case for the hous‐
# ing data: the total number of rooms ranges from about 6 to 39,320, while the median
# incomes only range from 0 to 15. Note that scaling the target values is generally not
# required.
# There are two common ways to get all attributes to have the same scale: min-max
# scaling and standardization.
# Min-max scaling (many people call this normalization) is quite simple: values are
# shifted and rescaled so that they end up ranging from 0 to 1. We do this by subtract‐
# ing the min value and dividing by the max minus the min. Scikit-Learn provides a
# transformer called MinMaxScaler for this. It has a feature_range hyperparameter
# that lets you change the range if you don’t want 0–1 for some reason.
# Standardization is quite different: first it subtracts the mean value (so standardized
# values always have a zero mean), and then it divides by the variance so that the result‐
# ing distribution has unit variance. Unlike min-max scaling, standardization does not
# bound values to a specific range, which may be a problem for some algorithms (e.g.,
# neural networks often expect an input value ranging from 0 to 1). However, standard‐
# ization is much less affected by outliers. For example, suppose a district had a median
# income equal to 100 (by mistake). Min-max scaling would then crush all the other
# values from 0–15 down to 0–0.15, whereas standardization would not be much affec‐
# ted. Scikit-Learn provides a transformer called StandardScaler for standardization.
# 
# 
# 
# 
#                                               Prepare the Data for Machine Learning Algorithms   |   65
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Custom Transformers",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class CustomTransformers(HierNode):
    def __init__(self):
        super().__init__("Custom Transformers")
        self.add(Content(), "content")

# eof
