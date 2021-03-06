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
#                       Download from finelybook www.finelybook.com
#      from sklearn.pipeline import FeatureUnion
# 
#      num_attribs = list(housing_num)
#      cat_attribs = ["ocean_proximity"]
# 
#      num_pipeline = Pipeline([
#              ('selector', DataFrameSelector(num_attribs)),
#              ('imputer', Imputer(strategy="median")),
#              ('attribs_adder', CombinedAttributesAdder()),
#              ('std_scaler', StandardScaler()),
#          ])
# 
#      cat_pipeline = Pipeline([
#              ('selector', DataFrameSelector(cat_attribs)),
#              ('label_binarizer', LabelBinarizer()),
#          ])
# 
#      full_pipeline = FeatureUnion(transformer_list=[
#              ("num_pipeline", num_pipeline),
#              ("cat_pipeline", cat_pipeline),
#          ])
# And you can run the whole pipeline simply:
#      >>> housing_prepared = full_pipeline.fit_transform(housing)
#      >>> housing_prepared
#      array([[ 0.73225807, -0.67331551, 0.58426443, ..., 0.                             ,
#               0.        , 0.         ],
#             [-0.99102923, 1.63234656, -0.92655887, ..., 0.                             ,
#               0.        , 0.         ],
#             [...]
#      >>> housing_prepared.shape
#      (16513, 17)
# Each subpipeline starts with a selector transformer: it simply transforms the data by
# selecting the desired attributes (numerical or categorical), dropping the rest, and con‐
# verting the resulting DataFrame to a NumPy array. There is nothing in Scikit-Learn
# to handle Pandas DataFrames,20 so we need to write a simple custom transformer for
# this task:
#      from sklearn.base import BaseEstimator, TransformerMixin
# 
#      class DataFrameSelector(BaseEstimator, TransformerMixin):
#          def __init__(self, attribute_names):
#              self.attribute_names = attribute_names
#          def fit(self, X, y=None):
#              return self
# 
# 
# 
# 20 But check out Pull Request #3886, which may introduce a ColumnTransformer class making attribute-specific
#    transformations easy. You could also run pip3 install sklearn-pandas to get a DataFrameMapper class with
#    a similar objective.
# 
# 
# 
#                                                        Prepare the Data for Machine Learning Algorithms   |   67
# 
#                        Download from finelybook www.finelybook.com
#            def transform(self, X):
#                return X[self.attribute_names].values
# 
# 
# Select and Train a Model
# At last! You framed the problem, you got the data and explored it, you sampled a
# training set and a test set, and you wrote transformation pipelines to clean up and
# prepare your data for Machine Learning algorithms automatically. You are now ready
# to select and train a Machine Learning model.
# 
# Training and Evaluating on the Training Set
# The good news is that thanks to all these previous steps, things are now going to be
# much simpler than you might think. Let’s first train a Linear Regression model, like
# we did in the previous chapter:
#      from sklearn.linear_model import LinearRegression
# 
#      lin_reg = LinearRegression()
#      lin_reg.fit(housing_prepared, housing_labels)
# Done! You now have a working Linear Regression model. Let’s try it out on a few
# instances from the training set:
#      >>> some_data = housing.iloc[:5]
#      >>> some_labels = housing_labels.iloc[:5]
#      >>> some_data_prepared = full_pipeline.transform(some_data)
#      >>> print("Predictions:\t", lin_reg.predict(some_data_prepared))
#      Predictions:     [ 303104.   44800. 308928. 294208. 368704.]
#      >>> print("Labels:\t\t", list(some_labels))
#      Labels:          [359400.0, 69700.0, 302100.0, 301300.0, 351900.0]
# It works, although the predictions are not exactly accurate (e.g., the second prediction
# is off by more than 50%!). Let’s measure this regression model’s RMSE on the whole
# training set using Scikit-Learn’s mean_squared_error function:
#      >>> from sklearn.metrics import mean_squared_error
#      >>> housing_predictions = lin_reg.predict(housing_prepared)
#      >>> lin_mse = mean_squared_error(housing_labels, housing_predictions)
#      >>> lin_rmse = np.sqrt(lin_mse)
#      >>> lin_rmse
#      68628.413493824875
# Okay, this is better than nothing but clearly not a great score: most districts’
# median_housing_values range between $120,000 and $265,000, so a typical predic‐
# tion error of $68,628 is not very satisfying. This is an example of a model underfitting
# the training data. When this happens it can mean that the features do not provide
# enough information to make good predictions, or that the model is not powerful
# enough. As we saw in the previous chapter, the main ways to fix underfitting are to
# 
# 
# 68   |   Chapter 2: End-to-End Machine Learning Project
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Transformation Pipelines",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TransformationPipelines(HierNode):
    def __init__(self):
        super().__init__("Transformation Pipelines")
        self.add(Content(), "content")

# eof
