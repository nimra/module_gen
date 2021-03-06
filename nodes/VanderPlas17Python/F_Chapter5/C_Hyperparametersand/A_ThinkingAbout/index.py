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
# Summary
# In this section we have covered the essential features of the Scikit-Learn data repre‐
# sentation, and the estimator API. Regardless of the type of estimator, the same
# import/instantiate/fit/predict pattern holds. Armed with this information about the
# estimator API, you can explore the Scikit-Learn documentation and begin trying out
# various models on your data.
# In the next section, we will explore perhaps the most important topic in machine
# learning: how to select and validate your model.
# 
# Hyperparameters and Model Validation
# In the previous section, we saw the basic recipe for applying a supervised machine
# learning model:
# 
#  1. Choose a class of model
#  2. Choose model hyperparameters
#  3. Fit the model to the training data
#  4. Use the model to predict labels for new data
# 
# The first two pieces of this—the choice of model and choice of hyperparameters—are
# perhaps the most important part of using these tools and techniques effectively. In
# order to make an informed choice, we need a way to validate that our model and our
# hyperparameters are a good fit to the data. While this may sound simple, there are
# some pitfalls that you must avoid to do this effectively.
# 
# Thinking About Model Validation
# In principle, model validation is very simple: after choosing a model and its hyper‐
# parameters, we can estimate how effective it is by applying it to some of the training
# data and comparing the prediction to the known value.
# The following sections first show a naive approach to model validation and why it
# fails, before exploring the use of holdout sets and cross-validation for more robust
# model evaluation.
# 
# Model validation the wrong way
# Let’s demonstrate the naive approach to validation using the Iris data, which we saw
# in the previous section. We will start by loading the data:
#     In[1]: from sklearn.datasets import load_iris
#            iris = load_iris()
# 
# 
# 
# 
#                                                     Hyperparameters and Model Validation   |   359
# 
#                X = iris.data
#                y = iris.target
# Next we choose a model and hyperparameters. Here we’ll use a k-neighbors classifier
# with n_neighbors=1. This is a very simple and intuitive model that says “the label of
# an unknown point is the same as the label of its closest training point”:
#       In[2]: from sklearn.neighbors import KNeighborsClassifier
#              model = KNeighborsClassifier(n_neighbors=1)
# Then we train the model, and use it to predict labels for data we already know:
#       In[3]: model.fit(X, y)
#              y_model = model.predict(X)
# Finally, we compute the fraction of correctly labeled points:
#       In[4]: from sklearn.metrics import accuracy_score
#              accuracy_score(y, y_model)
#       Out[4]: 1.0
# We see an accuracy score of 1.0, which indicates that 100% of points were correctly
# labeled by our model! But is this truly measuring the expected accuracy? Have we
# really come upon a model that we expect to be correct 100% of the time?
# As you may have gathered, the answer is no. In fact, this approach contains a funda‐
# mental flaw: it trains and evaluates the model on the same data. Furthermore, the
# nearest neighbor model is an instance-based estimator that simply stores the training
# data, and predicts labels by comparing new data to these stored points; except in con‐
# trived cases, it will get 100% accuracy every time!
# 
# Model validation the right way: Holdout sets
# So what can be done? We can get a better sense of a model’s performance using what’s
# known as a holdout set; that is, we hold back some subset of the data from the training
# of the model, and then use this holdout set to check the model performance. We can
# do this splitting using the train_test_split utility in Scikit-Learn:
#       In[5]: from sklearn.cross_validation import train_test_split
#              # split the data with 50% in each set
#              X1, X2, y1, y2 = train_test_split(X, y, random_state=0,
#                                                train_size=0.5)
# 
#                # fit the model on one set of data
#                model.fit(X1, y1)
# 
#                # evaluate the model on the second set of data
#                y2_model = model.predict(X2)
#                accuracy_score(y2, y2_model)
#       Out[5]: 0.90666666666666662
# 
# 
# 
# 360   |   Chapter 5: Machine Learning
# 
# We see here a more reasonable result: the nearest-neighbor classifier is about 90%
# accurate on this holdout set. The holdout set is similar to unknown data, because the
# model has not “seen” it before.
# 
# Model validation via cross-validation
# One disadvantage of using a holdout set for model validation is that we have lost a
# portion of our data to the model training. In the previous case, half the dataset does
# not contribute to the training of the model! This is not optimal, and can cause prob‐
# lems—especially if the initial set of training data is small.
# One way to address this is to use cross-validation—that is, to do a sequence of fits
# where each subset of the data is used both as a training set and as a validation set.
# Visually, it might look something like Figure 5-22.
# 
# 
# 
# 
# Figure 5-22. Visualization of two-fold cross-validation
# 
# Here we do two validation trials, alternately using each half of the data as a holdout
# set. Using the split data from before, we could implement it like this:
#     In[6]: y2_model = model.fit(X1, y1).predict(X2)
#            y1_model = model.fit(X2, y2).predict(X1)
#            accuracy_score(y1, y1_model), accuracy_score(y2, y2_model)
#     Out[6]: (0.95999999999999996, 0.90666666666666662)
# What comes out are two accuracy scores, which we could combine (by, say, taking the
# mean) to get a better measure of the global model performance. This particular form
# of cross-validation is a two-fold cross-validation—one in which we have split the data
# into two sets and used each in turn as a validation set.
# We could expand on this idea to use even more trials, and more folds in the data—for
# example, Figure 5-23 is a visual depiction of five-fold cross-validation.
# 
# 
# 
# 
#                                                      Hyperparameters and Model Validation   |   361
# 
# Figure 5-23. Visualization of five-fold cross-validation
# 
# Here we split the data into five groups, and use each of them in turn to evaluate the
# model fit on the other 4/5 of the data. This would be rather tedious to do by hand,
# and so we can use Scikit-Learn’s cross_val_score convenience routine to do it
# succinctly:
#       In[7]: from sklearn.cross_validation import cross_val_score
#              cross_val_score(model, X, y, cv=5)
#       Out[7]: array([ 0.96666667,         0.96666667,     0.93333333,       0.93333333,    1.          ])
# Repeating the validation across different subsets of the data gives us an even better
# idea of the performance of the algorithm.
# Scikit-Learn implements a number of cross-validation schemes that are useful in par‐
# ticular situations; these are implemented via iterators in the cross_validation mod‐
# ule. For example, we might wish to go to the extreme case in which our number of
# folds is equal to the number of data points; that is, we train on all points but one in
# each trial. This type of cross-validation is known as leave-one-out cross-validation,
# and can be used as follows:
#       In[8]: from sklearn.cross_validation import LeaveOneOut
#              scores = cross_val_score(model, X, y, cv=LeaveOneOut(len(X)))
#              scores
#       Out[8]: array([ 1.,         1.,   1.,   1.,   1.,   1.,   1.,   1.,    1.,   1.,    1.,   1.,   1.,
#                       1.,         1.,   1.,   1.,   1.,   1.,   1.,   1.,    1.,   1.,    1.,   1.,   1.,
#                       1.,         1.,   1.,   1.,   1.,   1.,   1.,   1.,    1.,   1.,    1.,   1.,   1.,
#                       1.,         1.,   1.,   1.,   1.,   1.,   1.,   1.,    1.,   1.,    1.,   1.,   1.,
#                       1.,         1.,   1.,   1.,   1.,   1.,   1.,   1.,    1.,   1.,    1.,   1.,   1.,
#                       1.,         1.,   1.,   1.,   1.,   0.,   1.,   0.,    1.,   1.,    1.,   1.,   1.,
# 
# 
# 
# 362   |   Chapter 5: Machine Learning
# 
#                      1.,   1.,   1.,   1.,   1.,   0.,   1.,    1.,   1.,   1.,    1.,   1.,        1.,
#                      1.,   1.,   1.,   1.,   1.,   1.,   1.,    1.,   1.,   1.,    1.,   1.,        1.,
#                      1.,   1.,   0.,   1.,   1.,   1.,   1.,    1.,   1.,   1.,    1.,   1.,        1.,
#                      1.,   1.,   0.,   1.,   1.,   1.,   1.,    1.,   1.,   1.,    1.,   1.,        1.,
#                      1.,   1.,   1.,   0.,   1.,   1.,   1.,    1.,   1.,   1.,    1.,   1.,        1.,
#                      1.,   1.,   1.,   1.,   1.,   1.,   1.])
# Because we have 150 samples, the leave-one-out cross-validation yields scores for 150
# trials, and the score indicates either successful (1.0) or unsuccessful (0.0) prediction.
# Taking the mean of these gives an estimate of the error rate:
#     In[9]: scores.mean()
#     Out[9]: 0.95999999999999996
# Other cross-validation schemes can be used similarly. For a description of what is
# available in Scikit-Learn, use IPython to explore the sklearn.cross_validation sub‐
# module, or take a look at Scikit-Learn’s online cross-validation documentation.
# 
# Selecting the Best Model
# Now that we’ve seen the basics of validation and cross-validation, we will go into a
# little more depth regarding model selection and selection of hyperparameters. These
# issues are some of the most important aspects of the practice of machine learning,
# and I find that this information is often glossed over in introductory machine learn‐
# ing tutorials.
# Of core importance is the following question: if our estimator is underperforming, how
# should we move forward? There are several possible answers:
# 
#   • Use a more complicated/more flexible model
#   • Use a less complicated/less flexible model
#   • Gather more training samples
#   • Gather more data to add features to each sample
# 
# The answer to this question is often counterintuitive. In particular, sometimes using a
# more complicated model will give worse results, and adding more training samples
# may not improve your results! The ability to determine what steps will improve your
# model is what separates the successful machine learning practitioners from the
# unsuccessful.
# 
# 
# 
# 
#                                                          Hyperparameters and Model Validation   |     363
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Thinking About Model Validation",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ThinkingAbout(HierNode):
    def __init__(self):
        super().__init__("Thinking About Model Validation")
        self.add(Content())

# eof
