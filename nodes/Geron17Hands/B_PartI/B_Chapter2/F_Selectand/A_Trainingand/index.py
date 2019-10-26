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
#                      Download from finelybook www.finelybook.com
# select a more powerful model, to feed the training algorithm with better features, or
# to reduce the constraints on the model. This model is not regularized, so this rules
# out the last option. You could try to add more features (e.g., the log of the popula‐
# tion), but first let’s try a more complex model to see how it does.
# Let’s train a DecisionTreeRegressor. This is a powerful model, capable of finding
# complex nonlinear relationships in the data (Decision Trees are presented in more
# detail in Chapter 6). The code should look familiar by now:
#     from sklearn.tree import DecisionTreeRegressor
# 
#     tree_reg = DecisionTreeRegressor()
#     tree_reg.fit(housing_prepared, housing_labels)
# Now that the model is trained, let’s evaluate it on the training set:
#     >>>   housing_predictions = tree_reg.predict(housing_prepared)
#     >>>   tree_mse = mean_squared_error(housing_labels, housing_predictions)
#     >>>   tree_rmse = np.sqrt(tree_mse)
#     >>>   tree_rmse
#     0.0
# Wait, what!? No error at all? Could this model really be absolutely perfect? Of course,
# it is much more likely that the model has badly overfit the data. How can you be sure?
# As we saw earlier, you don’t want to touch the test set until you are ready to launch a
# model you are confident about, so you need to use part of the training set for train‐
# ing, and part for model validation.
# 
# Better Evaluation Using Cross-Validation
# One way to evaluate the Decision Tree model would be to use the train_test_split
# function to split the training set into a smaller training set and a validation set, then
# train your models against the smaller training set and evaluate them against the vali‐
# dation set. It’s a bit of work, but nothing too difficult and it would work fairly well.
# A great alternative is to use Scikit-Learn’s cross-validation feature. The following code
# performs K-fold cross-validation: it randomly splits the training set into 10 distinct
# subsets called folds, then it trains and evaluates the Decision Tree model 10 times,
# picking a different fold for evaluation every time and training on the other 9 folds.
# The result is an array containing the 10 evaluation scores:
#     from sklearn.model_selection import cross_val_score
#     scores = cross_val_score(tree_reg, housing_prepared, housing_labels,
#                              scoring="neg_mean_squared_error", cv=10)
#     rmse_scores = np.sqrt(-scores)
# 
# 
# 
# 
#                                                                   Select and Train a Model   |   69
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Training and Evaluating on the Training Set",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Trainingand(HierNode):
    def __init__(self):
        super().__init__("Training and Evaluating on the Training Set")
        self.add(Content(), "content")

# eof
