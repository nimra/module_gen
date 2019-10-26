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
# Strengths, weaknesses, and parameters
# Kernelized support vector machines are powerful models and perform well on a vari‐
# ety of datasets. SVMs allow for complex decision boundaries, even if the data has only
# a few features. They work well on low-dimensional and high-dimensional data (i.e.,
# few and many features), but don’t scale very well with the number of samples. Run‐
# ning an SVM on data with up to 10,000 samples might work well, but working with
# datasets of size 100,000 or more can become challenging in terms of runtime and
# memory usage.
# Another downside of SVMs is that they require careful preprocessing of the data and
# tuning of the parameters. This is why, these days, most people instead use tree-based
# models such as random forests or gradient boosting (which require little or no pre‐
# processing) in many applications. Furthermore, SVM models are hard to inspect; it
# can be difficult to understand why a particular prediction was made, and it might be
# tricky to explain the model to a nonexpert.
# Still, it might be worth trying SVMs, particularly if all of your features represent
# measurements in similar units (e.g., all are pixel intensities) and they are on similar
# scales.
# The important parameters in kernel SVMs are the regularization parameter C, the
# choice of the kernel, and the kernel-specific parameters. Although we primarily
# focused on the RBF kernel, other choices are available in scikit-learn. The RBF
# kernel has only one parameter, gamma, which is the inverse of the width of the Gaus‐
# sian kernel. gamma and C both control the complexity of the model, with large values
# in either resulting in a more complex model. Therefore, good settings for the two
# parameters are usually strongly correlated, and C and gamma should be adjusted
# together.
# 
# Neural Networks (Deep Learning)
# A family of algorithms known as neural networks has recently seen a revival under
# the name “deep learning.” While deep learning shows great promise in many machine
# learning applications, deep learning algorithms are often tailored very carefully to a
# specific use case. Here, we will only discuss some relatively simple methods, namely
# multilayer perceptrons for classification and regression, that can serve as a starting
# point for more involved deep learning methods. Multilayer perceptrons (MLPs) are
# also known as (vanilla) feed-forward neural networks, or sometimes just neural
# networks.
# 
# The neural network model
# MLPs can be viewed as generalizations of linear models that perform multiple stages
# of processing to come to a decision.
# 
# 
# 104   |   Chapter 2: Supervised Learning
# 
# Remember that the prediction by a linear regressor is given as:
# 
#     ŷ = w[0] * x[0] + w[1] * x[1] + ... + w[p] * x[p] + b
# 
# In plain English, ŷ is a weighted sum of the input features x[0] to x[p], weighted by
# the learned coefficients w[0] to w[p]. We could visualize this graphically as shown in
# Figure 2-44:
# In[89]:
#     display(mglearn.plots.plot_logistic_regression_graph())
# 
# 
# 
# 
# Figure 2-44. Visualization of logistic regression, where input features and predictions are
# shown as nodes, and the coefficients are connections between the nodes
# 
# Here, each node on the left represents an input feature, the connecting lines represent
# the learned coefficients, and the node on the right represents the output, which is a
# weighted sum of the inputs.
# In an MLP this process of computing weighted sums is repeated multiple times, first
# computing hidden units that represent an intermediate processing step, which are
# again combined using weighted sums to yield the final result (Figure 2-45):
# In[90]:
#     display(mglearn.plots.plot_single_hidden_layer_graph())
# 
# 
# 
# 
#                                                     Supervised Machine Learning Algorithms   |   105
# 
# Figure 2-45. Illustration of a multilayer perceptron with a single hidden layer
# 
# This model has a lot more coefficients (also called weights) to learn: there is one
# between every input and every hidden unit (which make up the hidden layer), and
# one between every unit in the hidden layer and the output.
# Computing a series of weighted sums is mathematically the same as computing just
# one weighted sum, so to make this model truly more powerful than a linear model,
# we need one extra trick. After computing a weighted sum for each hidden unit, a
# nonlinear function is applied to the result—usually the rectifying nonlinearity (also
# known as rectified linear unit or relu) or the tangens hyperbolicus (tanh). The result of
# this function is then used in the weighted sum that computes the output, ŷ. The two
# functions are visualized in Figure 2-46. The relu cuts off values below zero, while tanh
# saturates to –1 for low input values and +1 for high input values. Either nonlinear
# function allows the neural network to learn much more complicated functions than a
# linear model could:
# In[91]:
#       line = np.linspace(-3, 3, 100)
#       plt.plot(line, np.tanh(line), label="tanh")
#       plt.plot(line, np.maximum(line, 0), label="relu")
#       plt.legend(loc="best")
#       plt.xlabel("x")
#       plt.ylabel("relu(x), tanh(x)")
# 
# 
# 
# 
# 106   |   Chapter 2: Supervised Learning
# 
# Figure 2-46. The hyperbolic tangent activation function and the rectified linear activa‐
# tion function
# 
# For the small neural network pictured in Figure 2-45, the full formula for computing
# ŷ in the case of regression would be (when using a tanh nonlinearity):
# 
#     h[0] = tanh(w[0, 0] * x[0] + w[1, 0] * x[1] + w[2, 0] * x[2] + w[3, 0] * x[3])
#     h[1] = tanh(w[0, 0] * x[0] + w[1, 0] * x[1] + w[2, 0] * x[2] + w[3, 0] * x[3])
#     h[2] = tanh(w[0, 0] * x[0] + w[1, 0] * x[1] + w[2, 0] * x[2] + w[3, 0] * x[3])
#     ŷ = v[0] * h[0] + v[1] * h[1] + v[2] * h[2]
# 
# Here, w are the weights between the input x and the hidden layer h, and v are the
# weights between the hidden layer h and the output ŷ. The weights v and w are learned
# from data, x are the input features, ŷ is the computed output, and h are intermediate
# computations. An important parameter that needs to be set by the user is the number
# of nodes in the hidden layer. This can be as small as 10 for very small or simple data‐
# sets and as big as 10,000 for very complex data. It is also possible to add additional
# hidden layers, as shown in Figure 2-47:
# 
# 
# 
# 
#                                                     Supervised Machine Learning Algorithms   |   107
# 
# In[92]:
#       mglearn.plots.plot_two_hidden_layer_graph()
# 
# 
# 
# 
# Figure 2-47. A multilayer perceptron with two hidden layers
# 
# Having large neural networks made up of many of these layers of computation is
# what inspired the term “deep learning.”
# 
# Tuning neural networks
# Let’s look into the workings of the MLP by applying the MLPClassifier to the
# two_moons dataset we used earlier in this chapter. The results are shown in
# Figure 2-48:
# In[93]:
#       from sklearn.neural_network import MLPClassifier
#       from sklearn.datasets import make_moons
# 
#       X, y = make_moons(n_samples=100, noise=0.25, random_state=3)
# 
#       X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y,
#                                                           random_state=42)
# 
#       mlp = MLPClassifier(algorithm='l-bfgs', random_state=0).fit(X_train, y_train)
#       mglearn.plots.plot_2d_separator(mlp, X_train, fill=True, alpha=.3)
#       mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train)
#       plt.xlabel("Feature 0")
#       plt.ylabel("Feature 1")
# 
# 
# 
# 
# 108   |   Chapter 2: Supervised Learning
# 
# Figure 2-48. Decision boundary learned by a neural network with 100 hidden units on
# the two_moons dataset
# 
# As you can see, the neural network learned a very nonlinear but relatively smooth
# decision boundary. We used algorithm='l-bfgs', which we will discuss later.
# By default, the MLP uses 100 hidden nodes, which is quite a lot for this small dataset.
# We can reduce the number (which reduces the complexity of the model) and still get
# a good result (Figure 2-49):
# In[94]:
#     mlp = MLPClassifier(algorithm='l-bfgs', random_state=0, hidden_layer_sizes=[10])
#     mlp.fit(X_train, y_train)
#     mglearn.plots.plot_2d_separator(mlp, X_train, fill=True, alpha=.3)
#     mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train)
#     plt.xlabel("Feature 0")
#     plt.ylabel("Feature 1")
# 
# 
# 
# 
#                                                   Supervised Machine Learning Algorithms   |   109
# 
# Figure 2-49. Decision boundary learned by a neural network with 10 hidden units on
# the two_moons dataset
# 
# With only 10 hidden units, the decision boundary looks somewhat more ragged. The
# default nonlinearity is relu, shown in Figure 2-46. With a single hidden layer, this
# means the decision function will be made up of 10 straight line segments. If we want
# a smoother decision boundary, we could add more hidden units (as in Figure 2-49),
# add a second hidden layer (Figure 2-50), or use the tanh nonlinearity (Figure 2-51):
# In[95]:
#       # using two hidden layers, with 10 units each
#       mlp = MLPClassifier(algorithm='l-bfgs', random_state=0,
#                           hidden_layer_sizes=[10, 10])
#       mlp.fit(X_train, y_train)
#       mglearn.plots.plot_2d_separator(mlp, X_train, fill=True, alpha=.3)
#       mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train)
#       plt.xlabel("Feature 0")
#       plt.ylabel("Feature 1")
# 
# 
# 
# 
# 110   |   Chapter 2: Supervised Learning
# 
# In[96]:
#     # using two hidden layers, with 10 units each, now with tanh nonlinearity
#     mlp = MLPClassifier(algorithm='l-bfgs', activation='tanh',
#                         random_state=0, hidden_layer_sizes=[10, 10])
#     mlp.fit(X_train, y_train)
#     mglearn.plots.plot_2d_separator(mlp, X_train, fill=True, alpha=.3)
#     mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train)
#     plt.xlabel("Feature 0")
#     plt.ylabel("Feature 1")
# 
# 
# 
# 
# Figure 2-50. Decision boundary learned using 2 hidden layers with 10 hidden units
# each, with rect activation function
# 
# 
# 
# 
#                                                  Supervised Machine Learning Algorithms   |   111
# 
# Figure 2-51. Decision boundary learned using 2 hidden layers with 10 hidden units
# each, with tanh activation function
# 
# Finally, we can also control the complexity of a neural network by using an l2 penalty
# to shrink the weights toward zero, as we did in ridge regression and the linear classifi‐
# ers. The parameter for this in the MLPClassifier is alpha (as in the linear regression
# models), and it’s set to a very low value (little regularization) by default. Figure 2-52
# shows the effect of different values of alpha on the two_moons dataset, using two hid‐
# den layers of 10 or 100 units each:
# In[97]:
#       fig, axes = plt.subplots(2, 4, figsize=(20, 8))
#       for axx, n_hidden_nodes in zip(axes, [10, 100]):
#           for ax, alpha in zip(axx, [0.0001, 0.01, 0.1, 1]):
#               mlp = MLPClassifier(algorithm='l-bfgs', random_state=0,
#                                   hidden_layer_sizes=[n_hidden_nodes, n_hidden_nodes],
#                                   alpha=alpha)
#               mlp.fit(X_train, y_train)
#               mglearn.plots.plot_2d_separator(mlp, X_train, fill=True, alpha=.3, ax=ax)
#               mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train, ax=ax)
#               ax.set_title("n_hidden=[{}, {}]\nalpha={:.4f}".format(
#                             n_hidden_nodes, n_hidden_nodes, alpha))
# 
# 
# 
# 
# 112   |   Chapter 2: Supervised Learning
# 
# Figure 2-52. Decision functions for different numbers of hidden units and different set‐
# tings of the alpha parameter
# 
# As you probably have realized by now, there are many ways to control the complexity
# of a neural network: the number of hidden layers, the number of units in each hidden
# layer, and the regularization (alpha). There are actually even more, which we won’t
# go into here.
# An important property of neural networks is that their weights are set randomly
# before learning is started, and this random initialization affects the model that is
# learned. That means that even when using exactly the same parameters, we can
# obtain very different models when using different random seeds. If the networks are
# large, and their complexity is chosen properly, this should not affect accuracy too
# much, but it is worth keeping in mind (particularly for smaller networks).
# Figure 2-53 shows plots of several models, all learned with the same settings of the
# parameters:
# In[98]:
#     fig, axes = plt.subplots(2, 4, figsize=(20, 8))
#     for i, ax in enumerate(axes.ravel()):
#         mlp = MLPClassifier(algorithm='l-bfgs', random_state=i,
#                             hidden_layer_sizes=[100, 100])
#         mlp.fit(X_train, y_train)
#         mglearn.plots.plot_2d_separator(mlp, X_train, fill=True, alpha=.3, ax=ax)
#         mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train, ax=ax)
# 
# 
# 
# 
#                                                    Supervised Machine Learning Algorithms   |   113
# 
# Figure 2-53. Decision functions learned with the same parameters but different random
# initializations
# 
# To get a better understanding of neural networks on real-world data, let’s apply the
# MLPClassifier to the Breast Cancer dataset. We start with the default parameters:
# In[99]:
#       print("Cancer data per-feature maxima:\n{}".format(cancer.data.max(axis=0)))
# 
# Out[99]:
#       Cancer data per-feature maxima:
#       [   28.110    39.280   188.500 2501.000      0.163      0.345     0.427
#            0.201     0.304     0.097    2.873      4.885     21.980   542.200
#            0.031     0.135     0.396    0.053      0.079      0.030    36.040
#           49.540   251.200 4254.000     0.223      1.058      1.252     0.291
#            0.664     0.207]
# 
# In[100]:
#       X_train, X_test, y_train, y_test = train_test_split(
#           cancer.data, cancer.target, random_state=0)
# 
#       mlp = MLPClassifier(random_state=42)
#       mlp.fit(X_train, y_train)
# 
#       print("Accuracy on training set: {:.2f}".format(mlp.score(X_train, y_train)))
#       print("Accuracy on test set: {:.2f}".format(mlp.score(X_test, y_test)))
# 
# Out[100]:
#       Accuracy on training set: 0.92
#       Accuracy on test set: 0.90
# The accuracy of the MLP is quite good, but not as good as the other models. As in the
# earlier SVC example, this is likely due to scaling of the data. Neural networks also
# expect all input features to vary in a similar way, and ideally to have a mean of 0, and
# 
# 
# 114   | Chapter 2: Supervised Learning
# 
# a variance of 1. We must rescale our data so that it fulfills these requirements. Again,
# we will do this by hand here, but we’ll introduce the StandardScaler to do this auto‐
# matically in Chapter 3:
# In[101]:
#     # compute the mean value per feature on the training set
#     mean_on_train = X_train.mean(axis=0)
#     # compute the standard deviation of each feature on the training set
#     std_on_train = X_train.std(axis=0)
# 
#     # subtract the mean, and scale by inverse standard deviation
#     # afterward, mean=0 and std=1
#     X_train_scaled = (X_train - mean_on_train) / std_on_train
#     # use THE SAME transformation (using training mean and std) on the test set
#     X_test_scaled = (X_test - mean_on_train) / std_on_train
# 
#     mlp = MLPClassifier(random_state=0)
#     mlp.fit(X_train_scaled, y_train)
# 
#     print("Accuracy on training set: {:.3f}".format(
#         mlp.score(X_train_scaled, y_train)))
#     print("Accuracy on test set: {:.3f}".format(mlp.score(X_test_scaled, y_test)))
# 
# Out[101]:
#     Accuracy on training set: 0.991
#     Accuracy on test set: 0.965
# 
#     ConvergenceWarning:
#         Stochastic Optimizer: Maximum iterations reached and the optimization
#         hasn't converged yet.
# The results are much better after scaling, and already quite competitive. We got a
# warning from the model, though, that tells us that the maximum number of iterations
# has been reached. This is part of the adam algorithm for learning the model, and tells
# us that we should increase the number of iterations:
# In[102]:
#     mlp = MLPClassifier(max_iter=1000, random_state=0)
#     mlp.fit(X_train_scaled, y_train)
# 
#     print("Accuracy on training set: {:.3f}".format(
#         mlp.score(X_train_scaled, y_train)))
#     print("Accuracy on test set: {:.3f}".format(mlp.score(X_test_scaled, y_test)))
# 
# Out[102]:
#     Accuracy on training set: 0.995
#     Accuracy on test set: 0.965
# 
# 
# 
# 
#                                                   Supervised Machine Learning Algorithms   |   115
# 
# Increasing the number of iterations only increased the training set performance, not
# the generalization performance. Still, the model is performing quite well. As there is
# some gap between the training and the test performance, we might try to decrease the
# model’s complexity to get better generalization performance. Here, we choose to
# increase the alpha parameter (quite aggressively, from 0.0001 to 1) to add stronger
# regularization of the weights:
# In[103]:
#       mlp = MLPClassifier(max_iter=1000, alpha=1, random_state=0)
#       mlp.fit(X_train_scaled, y_train)
# 
#       print("Accuracy on training set: {:.3f}".format(
#           mlp.score(X_train_scaled, y_train)))
#       print("Accuracy on test set: {:.3f}".format(mlp.score(X_test_scaled, y_test)))
# 
# Out[103]:
#       Accuracy on training set: 0.988
#       Accuracy on test set: 0.972
# This leads to a performance on par with the best models so far.12
# While it is possible to analyze what a neural network has learned, this is usually much
# trickier than analyzing a linear model or a tree-based model. One way to introspect
# what was learned is to look at the weights in the model. You can see an example of
# this in the scikit-learn example gallery. For the Breast Cancer dataset, this might
# be a bit hard to understand. The following plot (Figure 2-54) shows the weights that
# were learned connecting the input to the first hidden layer. The rows in this plot cor‐
# respond to the 30 input features, while the columns correspond to the 100 hidden
# units. Light colors represent large positive values, while dark colors represent nega‐
# tive values:
# In[104]:
#       plt.figure(figsize=(20, 5))
#       plt.imshow(mlp.coefs_[0], interpolation='none', cmap='viridis')
#       plt.yticks(range(30), cancer.feature_names)
#       plt.xlabel("Columns in weight matrix")
#       plt.ylabel("Input feature")
#       plt.colorbar()
# 
# 
# 
# 
# 12 You might have noticed at this point that many of the well-performing models achieved exactly the same
#    accuracy of 0.972. This means that all of the models make exactly the same number of mistakes, which is four.
#    If you compare the actual predictions, you can even see that they make exactly the same mistakes! This might
#    be a consequence of the dataset being very small, or it may be because these points are really different from
#    the rest.
# 
# 
# 
# 116   |   Chapter 2: Supervised Learning
# 
# Figure 2-54. Heat map of the first layer weights in a neural network learned on the
# Breast Cancer dataset
# 
# One possible inference we can make is that features that have very small weights for
# all of the hidden units are “less important” to the model. We can see that “mean
# smoothness” and “mean compactness,” in addition to the features found between
# “smoothness error” and “fractal dimension error,” have relatively low weights com‐
# pared to other features. This could mean that these are less important features or pos‐
# sibly that we didn’t represent them in a way that the neural network could use.
# We could also visualize the weights connecting the hidden layer to the output layer,
# but those are even harder to interpret.
# While the MLPClassifier and MLPRegressor provide easy-to-use interfaces for the
# most common neural network architectures, they only capture a small subset of what
# is possible with neural networks. If you are interested in working with more flexible
# or larger models, we encourage you to look beyond scikit-learn into the fantastic
# deep learning libraries that are out there. For Python users, the most well-established
# are keras, lasagna, and tensor-flow. lasagna builds on the theano library, while
# keras can use either tensor-flow or theano. These libraries provide a much more
# flexible interface to build neural networks and track the rapid progress in deep learn‐
# ing research. All of the popular deep learning libraries also allow the use of high-
# performance graphics processing units (GPUs), which scikit-learn does not
# support. Using GPUs allows us to accelerate computations by factors of 10x to 100x,
# and they are essential for applying deep learning methods to large-scale datasets.
# 
# Strengths, weaknesses, and parameters
# Neural networks have reemerged as state-of-the-art models in many applications of
# machine learning. One of their main advantages is that they are able to capture infor‐
# mation contained in large amounts of data and build incredibly complex models.
# Given enough computation time, data, and careful tuning of the parameters, neural
# networks often beat other machine learning algorithms (for classification and regres‐
# sion tasks).
# 
# 
# 
#                                                    Supervised Machine Learning Algorithms   |   117
# 
# This brings us to the downsides. Neural networks—particularly the large and power‐
# ful ones—often take a long time to train. They also require careful preprocessing of
# the data, as we saw here. Similarly to SVMs, they work best with “homogeneous”
# data, where all the features have similar meanings. For data that has very different
# kinds of features, tree-based models might work better. Tuning neural network
# parameters is also an art unto itself. In our experiments, we barely scratched the sur‐
# face of possible ways to adjust neural network models and how to train them.
# 
# Estimating complexity in neural networks. The most important parameters are the num‐
# ber of layers and the number of hidden units per layer. You should start with one or
# two hidden layers, and possibly expand from there. The number of nodes per hidden
# layer is often similar to the number of input features, but rarely higher than in the low
# to mid-thousands.
# A helpful measure when thinking about the model complexity of a neural network is
# the number of weights or coefficients that are learned. If you have a binary classifica‐
# tion dataset with 100 features, and you have 100 hidden units, then there are 100 *
# 100 = 10,000 weights between the input and the first hidden layer. There are also
# 100 * 1 = 100 weights between the hidden layer and the output layer, for a total of
# around 10,100 weights. If you add a second hidden layer with 100 hidden units, there
# will be another 100 * 100 = 10,000 weights from the first hidden layer to the second
# hidden layer, resulting in a total of 20,100 weights. If instead you use one layer with
# 1,000 hidden units, you are learning 100 * 1,000 = 100,000 weights from the input to
# the hidden layer and 1,000 x 1 weights from the hidden layer to the output layer, for a
# total of 101,000. If you add a second hidden layer you add 1,000 * 1,000 = 1,000,000
# weights, for a whopping total of 1,101,000—50 times larger than the model with two
# hidden layers of size 100.
# A common way to adjust parameters in a neural network is to first create a network
# that is large enough to overfit, making sure that the task can actually be learned by
# the network. Then, once you know the training data can be learned, either shrink the
# network or increase alpha to add regularization, which will improve generalization
# performance.
# In our experiments, we focused mostly on the definition of the model: the number of
# layers and nodes per layer, the regularization, and the nonlinearity. These define the
# model we want to learn. There is also the question of how to learn the model, or the
# algorithm that is used for learning the parameters, which is set using the algorithm
# parameter. There are two easy-to-use choices for algorithm. The default is 'adam',
# which works well in most situations but is quite sensitive to the scaling of the data (so
# it is important to always scale your data to 0 mean and unit variance). The other one
# is 'l-bfgs', which is quite robust but might take a long time on larger models or
# larger datasets. There is also the more advanced 'sgd' option, which is what many
# deep learning researchers use. The 'sgd' option comes with many additional param‐
# 
# 118   | Chapter 2: Supervised Learning
# 
# eters that need to be tuned for best results. You can find all of these parameters and
# their definitions in the user guide. When starting to work with MLPs, we recommend
# sticking to 'adam' and 'l-bfgs'.
# 
#                 fit Resets a Model
#                 An important property of scikit-learn models is that calling fit
#                 will always reset everything a model previously learned. So if you
#                 build a model on one dataset, and then call fit again on a different
#                 dataset, the model will “forget” everything it learned from the first
#                 dataset. You can call fit as often as you like on a model, and the
#                 outcome will be the same as calling fit on a “new” model.
# 
# 
# Uncertainty Estimates from Classifiers
# Another useful part of the scikit-learn interface that we haven’t talked about yet is
# the ability of classifiers to provide uncertainty estimates of predictions. Often, you are
# not only interested in which class a classifier predicts for a certain test point, but also
# how certain it is that this is the right class. In practice, different kinds of mistakes lead
# to very different outcomes in real-world applications. Imagine a medical application
# testing for cancer. Making a false positive prediction might lead to a patient undergo‐
# ing additional tests, while a false negative prediction might lead to a serious disease
# not being treated. We will go into this topic in more detail in Chapter 6.
# There are two different functions in scikit-learn that can be used to obtain uncer‐
# tainty estimates from classifiers: decision_function and predict_proba. Most (but
# not all) classifiers have at least one of them, and many classifiers have both. Let’s look
# at what these two functions do on a synthetic two-dimensional dataset, when build‐
# ing a GradientBoostingClassifier classifier, which has both a decision_function
# and a predict_proba method:
# In[105]:
#     from sklearn.ensemble import GradientBoostingClassifier
#     from sklearn.datasets import make_blobs, make_circles
#     X, y = make_circles(noise=0.25, factor=0.5, random_state=1)
# 
#     # we rename the classes "blue" and "red" for illustration purposes
#     y_named = np.array(["blue", "red"])[y]
# 
#     # we can call train_test_split with arbitrarily many arrays;
#     # all will be split in a consistent manner
#     X_train, X_test, y_train_named, y_test_named, y_train, y_test = \
#         train_test_split(X, y_named, y, random_state=0)
# 
#     # build the gradient boosting model
#     gbrt = GradientBoostingClassifier(random_state=0)
#     gbrt.fit(X_train, y_train_named)
# 
# 
#                                                         Uncertainty Estimates from Classifiers |   119
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Neural Networks (Deep Learning)",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class NeuralNetworks(HierNode):
    def __init__(self):
        super().__init__("Neural Networks (Deep Learning)")
        self.add(Content(), "content")

# eof
