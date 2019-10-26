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
#                        Download from finelybook www.finelybook.com
#                      As with all the transformations, it is important to fit the scalers to
#                      the training data only, not to the full dataset (including the test set).
#                      Only then can you use them to transform the training set and the
#                      test set (and new data).
# 
# 
# Transformation Pipelines
# As you can see, there are many data transformation steps that need to be executed in
# the right order. Fortunately, Scikit-Learn provides the Pipeline class to help with
# such sequences of transformations. Here is a small pipeline for the numerical
# attributes:
#      from sklearn.pipeline import Pipeline
#      from sklearn.preprocessing import StandardScaler
# 
#      num_pipeline = Pipeline([
#              ('imputer', Imputer(strategy="median")),
#              ('attribs_adder', CombinedAttributesAdder()),
#              ('std_scaler', StandardScaler()),
#          ])
# 
#      housing_num_tr = num_pipeline.fit_transform(housing_num)
# 
# The Pipeline constructor takes a list of name/estimator pairs defining a sequence of
# steps. All but the last estimator must be transformers (i.e., they must have a
# fit_transform() method). The names can be anything you like.
# When you call the pipeline’s fit() method, it calls fit_transform() sequentially on
# all transformers, passing the output of each call as the parameter to the next call, until
# it reaches the final estimator, for which it just calls the fit() method.
# The pipeline exposes the same methods as the final estimator. In this example, the last
# estimator is a StandardScaler, which is a transformer, so the pipeline has a trans
# form() method that applies all the transforms to the data in sequence (it also has a
# fit_transform method that we could have used instead of calling fit() and then
# transform()).
# You now have a pipeline for numerical values, and you also need to apply the LabelBi
# narizer on the categorical values: how can you join these transformations into a sin‐
# gle pipeline? Scikit-Learn provides a FeatureUnion class for this. You give it a list of
# transformers (which can be entire transformer pipelines), and when its transform()
# method is called it runs each transformer’s transform() method in parallel, waits for
# their output, and then concatenates them and returns the result (and of course calling
# its fit() method calls all each transformer’s fit() method). A full pipeline handling
# both numerical and categorical attributes may look like this:
# 
# 
# 
# 66   |   Chapter 2: End-to-End Machine Learning Project
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Feature Scaling",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class FeatureScaling(HierNode):
    def __init__(self):
        super().__init__("Feature Scaling")
        self.add(Content(), "content")

# eof
