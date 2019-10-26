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
#                        Download from finelybook www.finelybook.com
#                      Scikit-Learn cross-validation features expect a utility function
#                      (greater is better) rather than a cost function (lower is better), so
#                      the scoring function is actually the opposite of the MSE (i.e., a neg‐
#                      ative value), which is why the preceding code computes -scores
#                      before calculating the square root.
# 
# Let’s look at the results:
#      >>> def display_scores(scores):
#      ...     print("Scores:", scores)
#      ...     print("Mean:", scores.mean())
#      ...     print("Standard deviation:", scores.std())
#      ...
#      >>> display_scores(tree_rmse_scores)
#      Scores: [ 74678.4916885   64766.2398337   69632.86942005             69166.67693232
#                71486.76507766 73321.65695983 71860.04741226               71086.32691692
#                76934.2726093   69060.93319262]
#      Mean: 71199.4280043
#      Standard deviation: 3202.70522793
# Now the Decision Tree doesn’t look as good as it did earlier. In fact, it seems to per‐
# form worse than the Linear Regression model! Notice that cross-validation allows
# you to get not only an estimate of the performance of your model, but also a measure
# of how precise this estimate is (i.e., its standard deviation). The Decision Tree has a
# score of approximately 71,200, generally ±3,200. You would not have this information
# if you just used one validation set. But cross-validation comes at the cost of training
# the model several times, so it is not always possible.
# Let’s compute the same scores for the Linear Regression model just to be sure:
#      >>> lin_scores = cross_val_score(lin_reg, housing_prepared, housing_labels,
#      ...                               scoring="neg_mean_squared_error", cv=10)
#      ...
#      >>> lin_rmse_scores = np.sqrt(-lin_scores)
#      >>> display_scores(lin_rmse_scores)
#      Scores: [ 70423.5893262   65804.84913139 66620.84314068 72510.11362141
#                66414.74423281 71958.89083606 67624.90198297 67825.36117664
#                72512.36533141 68028.11688067]
#      Mean: 68972.377566
#      Standard deviation: 2493.98819069
# That’s right: the Decision Tree model is overfitting so badly that it performs worse
# than the Linear Regression model.
# Let’s try one last model now: the RandomForestRegressor. As we will see in Chap‐
# ter 7, Random Forests work by training many Decision Trees on random subsets of
# the features, then averaging out their predictions. Building a model on top of many
# other models is called Ensemble Learning, and it is often a great way to push ML algo‐
# rithms even further. We will skip most of the code since it is essentially the same as
# for the other models:
# 
# 70   |   Chapter 2: End-to-End Machine Learning Project
# 
#                   Download from finelybook www.finelybook.com
#     >>> from sklearn.ensemble import RandomForestRegressor
#     >>> forest_reg = RandomForestRegressor()
#     >>> forest_reg.fit(housing_prepared, housing_labels)
#     >>> [...]
#     >>> forest_rmse
#     22542.396440343684
#     >>> display_scores(forest_rmse_scores)
#     Scores: [ 53789.2879722   50256.19806622 52521.55342602        53237.44937943
#               52428.82176158 55854.61222549 52158.02291609         50093.66125649
#               53240.80406125 52761.50852822]
#     Mean: 52634.1919593
#     Standard deviation: 1576.20472269
# Wow, this is much better: Random Forests look very promising. However, note that
# the score on the training set is still much lower than on the validation sets, meaning
# that the model is still overfitting the training set. Possible solutions for overfitting are
# to simplify the model, constrain it (i.e., regularize it), or get a lot more training data.
# However, before you dive much deeper in Random Forests, you should try out many
# other models from various categories of Machine Learning algorithms (several Sup‐
# port Vector Machines with different kernels, possibly a neural network, etc.), without
# spending too much time tweaking the hyperparameters. The goal is to shortlist a few
# (two to five) promising models.
# 
#                 You should save every model you experiment with, so you can
#                 come back easily to any model you want. Make sure you save both
#                 the hyperparameters and the trained parameters, as well as the
#                 cross-validation scores and perhaps the actual predictions as well.
#                 This will allow you to easily compare scores across model types,
#                 and compare the types of errors they make. You can easily save
#                 Scikit-Learn models by using Python’s pickle module, or using
#                 sklearn.externals.joblib, which is more efficient at serializing
#                 large NumPy arrays:
#                     from sklearn.externals import joblib
# 
#                     joblib.dump(my_model, "my_model.pkl")
#                     # and later...
#                     my_model_loaded = joblib.load("my_model.pkl")
# 
# 
# Fine-Tune Your Model
# Let’s assume that you now have a shortlist of promising models. You now need to
# fine-tune them. Let’s look at a few ways you can do that.
# 
# 
# 
# 
#                                                                     Fine-Tune Your Model   |   71
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Better Evaluation Using Cross-Validation",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class BetterEvaluation(HierNode):
    def __init__(self):
        super().__init__("Better Evaluation Using Cross-Validation")
        self.add(Content(), "content")

# eof
