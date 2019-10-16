# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                    Download from finelybook www.finelybook.com
#      • This will make it possible for you to easily try various transformations and see
#        which combination of transformations works best.
# 
# But first let’s revert to a clean training set (by copying strat_train_set once again),
# and let’s separate the predictors and the labels since we don’t necessarily want to apply
# the same transformations to the predictors and the target values (note that drop()
# creates a copy of the data and does not affect strat_train_set):
#        housing = strat_train_set.drop("median_house_value", axis=1)
#        housing_labels = strat_train_set["median_house_value"].copy()
# 
# 
# Data Cleaning
# Most Machine Learning algorithms cannot work with missing features, so let’s create
# a few functions to take care of them. You noticed earlier that the total_bedrooms
# attribute has some missing values, so let’s fix this. You have three options:
# 
#      • Get rid of the corresponding districts.
#      • Get rid of the whole attribute.
#      • Set the values to some value (zero, the mean, the median, etc.).
# 
# You can accomplish these easily using DataFrame’s dropna(), drop(), and fillna()
# methods:
#        housing.dropna(subset=["total_bedrooms"])           # option 1
#        housing.drop("total_bedrooms", axis=1)              # option 2
#        median = housing["total_bedrooms"].median()
#        housing["total_bedrooms"].fillna(median)            # option 3
# If you choose option 3, you should compute the median value on the training set, and
# use it to fill the missing values in the training set, but also don’t forget to save the
# median value that you have computed. You will need it later to replace missing values
# in the test set when you want to evaluate your system, and also once the system goes
# live to replace missing values in new data.
# Scikit-Learn provides a handy class to take care of missing values: Imputer. Here is
# how to use it. First, you need to create an Imputer instance, specifying that you want
# to replace each attribute’s missing values with the median of that attribute:
#        from sklearn.preprocessing import Imputer
# 
#        imputer = Imputer(strategy="median")
# Since the median can only be computed on numerical attributes, we need to create a
# copy of the data without the text attribute ocean_proximity:
#        housing_num = housing.drop("ocean_proximity", axis=1)
# 
# 
# 
# 
# 60    |   Chapter 2: End-to-End Machine Learning Project
# 
#                  Download from finelybook www.finelybook.com
# Now you can fit the imputer instance to the training data using the fit() method:
#      imputer.fit(housing_num)
# 
# The imputer has simply computed the median of each attribute and stored the result
# in its statistics_ instance variable. Only the total_bedrooms attribute had missing
# values, but we cannot be sure that there won’t be any missing values in new data after
# the system goes live, so it is safer to apply the imputer to all the numerical attributes:
#      >>> imputer.statistics_
#      array([ -118.51 , 34.26 , 29. , 2119. , 433. , 1164. , 408. , 3.5414])
#      >>> housing_num.median().values
#      array([ -118.51 , 34.26 , 29. , 2119. , 433. , 1164. , 408. , 3.5414])
# 
# Now you can use this “trained” imputer to transform the training set by replacing
# missing values by the learned medians:
#      X = imputer.transform(housing_num)
# The result is a plain Numpy array containing the transformed features. If you want to
# put it back into a Pandas DataFrame, it’s simple:
#      housing_tr = pd.DataFrame(X, columns=housing_num.columns)
# 
# 
#                                             Scikit-Learn Design
#    Scikit-Learn’s API is remarkably well designed. The main design principles are:16
# 
#       • Consistency. All objects share a consistent and simple interface:
#          — Estimators. Any object that can estimate some parameters based on a dataset
#            is called an estimator (e.g., an imputer is an estimator). The estimation itself is
#            performed by the fit() method, and it takes only a dataset as a parameter (or
#            two for supervised learning algorithms; the second dataset contains the
#            labels). Any other parameter needed to guide the estimation process is con‐
#            sidered a hyperparameter (such as an imputer’s strategy), and it must be set
#            as an instance variable (generally via a constructor parameter).
#          — Transformers. Some estimators (such as an imputer) can also transform a
#            dataset; these are called transformers. Once again, the API is quite simple: the
#            transformation is performed by the transform() method with the dataset to
#            transform as a parameter. It returns the transformed dataset. This transforma‐
#            tion generally relies on the learned parameters, as is the case for an imputer.
#            All transformers also have a convenience method called fit_transform()
# 
# 
# 
# 
# 16 For more details on the design principles, see “API design for machine learning software: experiences from
#    the scikit-learn project,” L. Buitinck, G. Louppe, M. Blondel, F. Pedregosa, A. Müller, et al. (2013).
# 
# 
# 
#                                                             Prepare the Data for Machine Learning Algorithms   |   61
# 
#                      Download from finelybook www.finelybook.com
#             that is equivalent to calling fit() and then transform() (but sometimes
#             fit_transform() is optimized and runs much faster).
#          — Predictors. Finally, some estimators are capable of making predictions given a
#            dataset; they are called predictors. For example, the LinearRegression model
#            in the previous chapter was a predictor: it predicted life satisfaction given a
#            country’s GDP per capita. A predictor has a predict() method that takes a
#            dataset of new instances and returns a dataset of corresponding predictions. It
#            also has a score() method that measures the quality of the predictions given
#            a test set (and the corresponding labels in the case of supervised learning
#            algorithms).17
#      • Inspection. All the estimator’s hyperparameters are accessible directly via public
#        instance variables (e.g., imputer.strategy), and all the estimator’s learned
#        parameters are also accessible via public instance variables with an underscore
#        suffix (e.g., imputer.statistics_).
#      • Nonproliferation of classes. Datasets are represented as NumPy arrays or SciPy
#        sparse matrices, instead of homemade classes. Hyperparameters are just regular
#        Python strings or numbers.
#      • Composition. Existing building blocks are reused as much as possible. For
#        example, it is easy to create a Pipeline estimator from an arbitrary sequence of
#        transformers followed by a final estimator, as we will see.
#      • Sensible defaults. Scikit-Learn provides reasonable default values for most
#        parameters, making it easy to create a baseline working system quickly.
# 
# 
# 
# Handling Text and Categorical Attributes
# Earlier we left out the categorical attribute ocean_proximity because it is a text
# attribute so we cannot compute its median. Most Machine Learning algorithms pre‐
# fer to work with numbers anyway, so let’s convert these text labels to numbers.
# Scikit-Learn provides a transformer for this task called LabelEncoder:
#      >>> from sklearn.preprocessing import LabelEncoder
#      >>> encoder = LabelEncoder()
#      >>> housing_cat = housing["ocean_proximity"]
#      >>> housing_cat_encoded = encoder.fit_transform(housing_cat)
#      >>> housing_cat_encoded
#      array([1, 1, 4, ..., 1, 0, 3])
# 
# 
# 
# 
# 17 Some predictors also provide methods to measure the confidence of their predictions.
# 
# 
# 
# 62   |   Chapter 2: End-to-End Machine Learning Project
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Data Cleaning",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Data Cleaning"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DataCleaning(HierNode):
    def __init__(self):
        super().__init__("Data Cleaning")
        self.add(Content())

# eof
