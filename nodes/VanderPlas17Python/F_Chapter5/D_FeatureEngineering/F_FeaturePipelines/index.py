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
# Imputation of Missing Data
# Another common need in feature engineering is handling missing data. We discussed
# the handling of missing data in DataFrames in “Handling Missing Data” on page 119,
# and saw that often the NaN value is used to mark missing values. For example, we
# might have a dataset that looks like this:
#     In[14]: from numpy import nan
#             X = np.array([[ nan, 0,            3 ],
#                           [ 3,    7,           9 ],
#                           [ 3,    5,           2 ],
#                           [ 4,    nan,         6 ],
#                           [ 8,    8,           1 ]])
#             y = np.array([14, 16, -1,           8, -5])
# When applying a typical machine learning model to such data, we will need to first
# replace such missing data with some appropriate fill value. This is known as imputa‐
# tion of missing values, and strategies range from simple (e.g., replacing missing values
# with the mean of the column) to sophisticated (e.g., using matrix completion or a
# robust model to handle such data).
# The sophisticated approaches tend to be very application-specific, and we won’t dive
# into them here. For a baseline imputation approach, using the mean, median, or most
# frequent value, Scikit-Learn provides the Imputer class:
#     In[15]: from sklearn.preprocessing import Imputer
#             imp = Imputer(strategy='mean')
#             X2 = imp.fit_transform(X)
#             X2
#     Out[15]: array([[   4.5,    0.   ,   3.   ],
#                     [   3. ,    7.   ,   9.   ],
#                     [   3. ,    5.   ,   2.   ],
#                     [   4. ,    5.   ,   6.   ],
#                     [   8. ,    8.   ,   1.   ]])
# We see that in the resulting data, the two missing values have been replaced with the
# mean of the remaining values in the column. This imputed data can then be fed
# directly into, for example, a LinearRegression estimator:
#     In[16]: model = LinearRegression().fit(X2, y)
#             model.predict(X2)
#     Out[16]:
#     array([ 13.14869292,       14.3784627 ,         -1.15539732,   10.96606197,   -5.33782027])
# 
# 
# Feature Pipelines
# With any of the preceding examples, it can quickly become tedious to do the transfor‐
# mations by hand, especially if you wish to string together multiple steps. For example,
# we might want a processing pipeline that looks something like this:
# 
# 
#                                                                             Feature Engineering   |   381
# 
#  1. Impute missing values using the mean
#  2. Transform features to quadratic
#  3. Fit a linear regression
# 
# To streamline this type of processing pipeline, Scikit-Learn provides a pipeline object,
# which can be used as follows:
#       In[17]: from sklearn.pipeline import make_pipeline
# 
#                model = make_pipeline(Imputer(strategy='mean'),
#                                      PolynomialFeatures(degree=2),
#                                      LinearRegression())
# This pipeline looks and acts like a standard Scikit-Learn object, and will apply all the
# specified steps to any input data.
#       In[18]: model.fit(X, y) # X with missing values, from above
#               print(y)
#               print(model.predict(X))
#       [14 16 -1 8 -5]
#       [ 14. 16. -1.         8.   -5.]
# All the steps of the model are applied automatically. Notice that for the simplicity of
# this demonstration, we’ve applied the model to the data it was trained on; this is why
# it was able to perfectly predict the result (refer back to “Hyperparameters and Model
# Validation” on page 359 for further discussion of this).
# For some examples of Scikit-Learn pipelines in action, see the following section on
# naive Bayes classification as well as “In Depth: Linear Regression” on page 390 and
# “In-Depth: Support Vector Machines” on page 405.
# 
# In Depth: Naive Bayes Classification
# The previous four sections have given a general overview of the concepts of machine
# learning. In this section and the ones that follow, we will be taking a closer look at
# several specific algorithms for supervised and unsupervised learning, starting here
# with naive Bayes classification.
# Naive Bayes models are a group of extremely fast and simple classification algorithms
# that are often suitable for very high-dimensional datasets. Because they are so fast
# and have so few tunable parameters, they end up being very useful as a quick-and-
# dirty baseline for a classification problem. This section will focus on an intuitive
# explanation of how naive Bayes classifiers work, followed by a couple examples of
# them in action on some datasets.
# 
# 
# 
# 
# 382   | Chapter 5: Machine Learning
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Feature Pipelines",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class FeaturePipelines(HierNode):
    def __init__(self):
        super().__init__("Feature Pipelines")
        self.add(Content())

# eof
