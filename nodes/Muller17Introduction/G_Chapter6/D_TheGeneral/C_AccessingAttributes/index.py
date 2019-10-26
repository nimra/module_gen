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
# In[20]:
#     # fit the pipeline defined before to the cancer dataset
#     pipe.fit(cancer.data)
#     # extract the first two principal components from the "pca" step
#     components = pipe.named_steps["pca"].components_
#     print("components.shape: {}".format(components.shape))
# 
# Out[20]:
#     components.shape: (2, 30)
# 
# 
# Accessing Attributes in a Grid-Searched Pipeline
# As we discussed earlier in this chapter, one of the main reasons to use pipelines is for
# doing grid searches. A common task is to access some of the steps of a pipeline inside
# a grid search. Let’s grid search a LogisticRegression classifier on the cancer dataset,
# using Pipeline and StandardScaler to scale the data before passing it to the Logisti
# cRegression classifier. First we create a pipeline using the make_pipeline function:
# In[21]:
#     from sklearn.linear_model import LogisticRegression
# 
#     pipe = make_pipeline(StandardScaler(), LogisticRegression())
# Next, we create a parameter grid. As explained in Chapter 2, the regularization
# parameter to tune for LogisticRegression is the parameter C. We use a logarithmic
# grid for this parameter, searching between 0.01 and 100. Because we used the
# make_pipeline function, the name of the LogisticRegression step in the pipeline is
# the lowercased class name, logisticregression. To tune the parameter C, we there‐
# fore have to specify a parameter grid for logisticregression__C:
# In[22]:
#     param_grid = {'logisticregression__C': [0.01, 0.1, 1, 10, 100]}
# 
# As usual, we split the cancer dataset into training and test sets, and fit a grid search:
# In[23]:
#     X_train, X_test, y_train, y_test = train_test_split(
#         cancer.data, cancer.target, random_state=4)
#     grid = GridSearchCV(pipe, param_grid, cv=5)
#     grid.fit(X_train, y_train)
# 
# So how do we access the coefficients of the best LogisticRegression model that was
# found by GridSearchCV? From Chapter 5 we know that the best model found by
# GridSearchCV, trained on all the training data, is stored in grid.best_estimator_:
# 
# 
# 
# 
#                                                             The General Pipeline Interface   |   315
# 
# In[24]:
#       print("Best estimator:\n{}".format(grid.best_estimator_))
# 
# Out[24]:
#       Best estimator:
#       Pipeline(steps=[
#           ('standardscaler', StandardScaler(copy=True, with_mean=True, with_std=True)),
#           ('logisticregression', LogisticRegression(C=0.1, class_weight=None,
#           dual=False, fit_intercept=True, intercept_scaling=1, max_iter=100,
#           multi_class='ovr', n_jobs=1, penalty='l2', random_state=None,
#           solver='liblinear', tol=0.0001, verbose=0, warm_start=False))])
# 
# This best_estimator_ in our case is a pipeline with two steps, standardscaler and
# logisticregression. To access the logisticregression step, we can use the
# named_steps attribute of the pipeline, as explained earlier:
# In[25]:
#       print("Logistic regression step:\n{}".format(
#             grid.best_estimator_.named_steps["logisticregression"]))
# 
# Out[25]:
#       Logistic regression step:
#       LogisticRegression(C=0.1, class_weight=None, dual=False, fit_intercept=True,
#                         intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
#                         penalty='l2', random_state=None, solver='liblinear', tol=0.0001,
#                         verbose=0, warm_start=False)
# 
# Now that we have the trained LogisticRegression instance, we can access the coeffi‐
# cients (weights) associated with each input feature:
# In[26]:
#       print("Logistic regression coefficients:\n{}".format(
#             grid.best_estimator_.named_steps["logisticregression"].coef_))
# 
# Out[26]:
#       Logistic    regression coefficients:
#       [[-0.389    -0.375 -0.376 -0.396 -0.115 0.017 -0.355 -0.39 -0.058 0.209
#         -0.495    -0.004 -0.371 -0.383 -0.045 0.198 0.004 -0.049 0.21      0.224
#         -0.547    -0.525 -0.499 -0.515 -0.393 -0.123 -0.388 -0.417 -0.325 -0.139]]
# This might be a somewhat lengthy expression, but often it comes in handy in under‐
# standing your models.
# 
# 
# 
# 
# 316   |   Chapter 6: Algorithm Chains and Pipelines
# 
# Grid-Searching Preprocessing Steps and Model
# Parameters
# Using pipelines, we can encapsulate all the processing steps in our machine learning
# workflow in a single scikit-learn estimator. Another benefit of doing this is that we
# can now adjust the parameters of the preprocessing using the outcome of a supervised
# task like regression or classification. In previous chapters, we used polynomial fea‐
# tures on the boston dataset before applying the ridge regressor. Let’s model that using
# a pipeline instead. The pipeline contains three steps—scaling the data, computing
# polynomial features, and ridge regression:
# In[27]:
#     from sklearn.datasets import load_boston
#     boston = load_boston()
#     X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target,
#                                                         random_state=0)
# 
#     from sklearn.preprocessing import PolynomialFeatures
#     pipe = make_pipeline(
#         StandardScaler(),
#         PolynomialFeatures(),
#         Ridge())
# How do we know which degrees of polynomials to choose, or whether to choose any
# polynomials or interactions at all? Ideally we want to select the degree parameter
# based on the outcome of the classification. Using our pipeline, we can search over the
# degree parameter together with the parameter alpha of Ridge. To do this, we define a
# param_grid that contains both, appropriately prefixed by the step names:
# In[28]:
#     param_grid = {'polynomialfeatures__degree': [1, 2, 3],
#                   'ridge__alpha': [0.001, 0.01, 0.1, 1, 10, 100]}
# Now we can run our grid search again:
# In[29]:
#     grid = GridSearchCV(pipe, param_grid=param_grid, cv=5, n_jobs=-1)
#     grid.fit(X_train, y_train)
# We can visualize the outcome of the cross-validation using a heat map (Figure 6-4), as
# we did in Chapter 5:
# In[30]:
#     plt.matshow(grid.cv_results_['mean_test_score'].reshape(3, -1),
#                 vmin=0, cmap="viridis")
#     plt.xlabel("ridge__alpha")
#     plt.ylabel("polynomialfeatures__degree")
# 
# 
#                                      Grid-Searching Preprocessing Steps and Model Parameters   |   317
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Accessing Attributes in a Grid-Searched Pipeline",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class AccessingAttributes(HierNode):
    def __init__(self):
        super().__init__("Accessing Attributes in a Grid-Searched Pipeline")
        self.add(Content(), "content")

# eof
