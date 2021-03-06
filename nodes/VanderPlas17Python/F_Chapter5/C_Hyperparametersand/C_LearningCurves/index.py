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
# Notice that finding this optimal model did not actually require us to compute the
# training score, but examining the relationship between the training score and valida‐
# tion score can give us useful insight into the performance of the model.
# 
# Learning Curves
# One important aspect of model complexity is that the optimal model will generally
# depend on the size of your training data. For example, let’s generate a new dataset
# with a factor of five more points (Figure 5-30):
#       In[15]: X2, y2 = make_data(200)
#               plt.scatter(X2.ravel(), y2);
# 
# 
# 
# 
# Figure 5-30. Data to demonstrate learning curves
# 
# We will duplicate the preceding code to plot the validation curve for this larger data‐
# set; for reference let’s over-plot the previous results as well (Figure 5-31):
#       In[16]:
#       degree = np.arange(21)
#       train_score2, val_score2 = validation_curve(PolynomialRegression(), X2, y2,
#                                                   'polynomialfeatures__degree',
#                                                   degree, cv=7)
# 
#       plt.plot(degree, np.median(train_score2, 1), color='blue',
#                label='training score')
#       plt.plot(degree, np.median(val_score2, 1), color='red', label='validation score')
#       plt.plot(degree, np.median(train_score, 1), color='blue', alpha=0.3,
#                linestyle='dashed')
#       plt.plot(degree, np.median(val_score, 1), color='red', alpha=0.3,
#                linestyle='dashed')
#       plt.legend(loc='lower center')
#       plt.ylim(0, 1)
# 
# 
# 
# 370   |   Chapter 5: Machine Learning
# 
#     plt.xlabel('degree')
#     plt.ylabel('score');
# 
# 
# 
# 
# Figure 5-31. Learning curves for the polynomial model fit to data in Figure 5-30
# 
# The solid lines show the new results, while the fainter dashed lines show the results of
# the previous smaller dataset. It is clear from the validation curve that the larger data‐
# set can support a much more complicated model: the peak here is probably around a
# degree of 6, but even a degree-20 model is not seriously overfitting the data—the vali‐
# dation and training scores remain very close.
# Thus we see that the behavior of the validation curve has not one, but two, important
# inputs: the model complexity and the number of training points. It is often useful to
# explore the behavior of the model as a function of the number of training points,
# which we can do by using increasingly larger subsets of the data to fit our model. A
# plot of the training/validation score with respect to the size of the training set is
# known as a learning curve.
# The general behavior we would expect from a learning curve is this:
# 
#   • A model of a given complexity will overfit a small dataset: this means the training
#     score will be relatively high, while the validation score will be relatively low.
#   • A model of a given complexity will underfit a large dataset: this means that the
#     training score will decrease, but the validation score will increase.
#   • A model will never, except by chance, give a better score to the validation set than
#     the training set: this means the curves should keep getting closer together but
#     never cross.
# 
# 
# 
# 
#                                                     Hyperparameters and Model Validation   |   371
# 
# With these features in mind, we would expect a learning curve to look qualitatively
# like that shown in Figure 5-32.
# 
# 
# 
# 
# Figure 5-32. Schematic showing the typical interpretation of learning curves
# 
# The notable feature of the learning curve is the convergence to a particular score as
# the number of training samples grows. In particular, once you have enough points
# that a particular model has converged, adding more training data will not help you!
# The only way to increase model performance in this case is to use another (often
# more complex) model.
# 
# Learning curves in Scikit-Learn
# Scikit-Learn offers a convenient utility for computing such learning curves from your
# models; here we will compute a learning curve for our original dataset with a second-
# order polynomial model and a ninth-order polynomial (Figure 5-33):
#       In[17]:
#       from sklearn.learning_curve import learning_curve
# 
#       fig, ax = plt.subplots(1, 2, figsize=(16, 6))
#       fig.subplots_adjust(left=0.0625, right=0.95, wspace=0.1)
# 
#       for i, degree in enumerate([2, 9]):
#           N, train_lc, val_lc = learning_curve(PolynomialRegression(degree),
#                                                X, y, cv=7,
#                                                train_sizes=np.linspace(0.3, 1, 25))
# 
#           ax[i].plot(N, np.mean(train_lc, 1), color='blue', label='training score')
#           ax[i].plot(N, np.mean(val_lc, 1), color='red', label='validation score')
#           ax[i].hlines(np.mean([train_lc[-1], val_lc[-1]]), N[0], N[-1], color='gray',
#                        linestyle='dashed')
# 
# 
# 
# 372   |   Chapter 5: Machine Learning
# 
#         ax[i].set_ylim(0, 1)
#         ax[i].set_xlim(N[0], N[-1])
#         ax[i].set_xlabel('training size')
#         ax[i].set_ylabel('score')
#         ax[i].set_title('degree = {0}'.format(degree), size=14)
#         ax[i].legend(loc='best')
# 
# 
# 
# 
# Figure 5-33. Learning curves for a low-complexity model (left) and a high-complexity
# model (right)
# 
# This is a valuable diagnostic, because it gives us a visual depiction of how our model
# responds to increasing training data. In particular, when your learning curve has
# already converged (i.e., when the training and validation curves are already close to
# each other), adding more training data will not significantly improve the fit! This situa‐
# tion is seen in the left panel, with the learning curve for the degree-2 model.
# The only way to increase the converged score is to use a different (usually more com‐
# plicated) model. We see this in the right panel: by moving to a much more compli‐
# cated model, we increase the score of convergence (indicated by the dashed line), but
# at the expense of higher model variance (indicated by the difference between the
# training and validation scores). If we were to add even more data points, the learning
# curve for the more complicated model would eventually converge.
# Plotting a learning curve for your particular choice of model and dataset can help you
# to make this type of decision about how to move forward in improving your analysis.
# 
# Validation in Practice: Grid Search
# The preceding discussion is meant to give you some intuition into the trade-off
# between bias and variance, and its dependence on model complexity and training set
# size. In practice, models generally have more than one knob to turn, and thus plots of
# validation and learning curves change from lines to multidimensional surfaces. In
# these cases, such visualizations are difficult and we would rather simply find the par‐
# ticular model that maximizes the validation score.
# 
# 
#                                                      Hyperparameters and Model Validation   |   373
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Learning Curves",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LearningCurves(HierNode):
    def __init__(self):
        super().__init__("Learning Curves")
        self.add(Content())

# eof
