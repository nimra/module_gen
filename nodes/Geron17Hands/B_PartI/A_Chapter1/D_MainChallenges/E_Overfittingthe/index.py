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
#                     Download from finelybook www.finelybook.com
#      • Feature selection: selecting the most useful features to train on among existing
#        features.
#      • Feature extraction: combining existing features to produce a more useful one (as
#        we saw earlier, dimensionality reduction algorithms can help).
#      • Creating new features by gathering new data.
# 
# Now that we have looked at many examples of bad data, let’s look at a couple of exam‐
# ples of bad algorithms.
# 
# Overfitting the Training Data
# Say you are visiting a foreign country and the taxi driver rips you off. You might be
# tempted to say that all taxi drivers in that country are thieves. Overgeneralizing is
# something that we humans do all too often, and unfortunately machines can fall into
# the same trap if we are not careful. In Machine Learning this is called overfitting: it
# means that the model performs well on the training data, but it does not generalize
# well.
# Figure 1-22 shows an example of a high-degree polynomial life satisfaction model
# that strongly overfits the training data. Even though it performs much better on the
# training data than the simple linear model, would you really trust its predictions?
# 
# 
# 
# 
# Figure 1-22. Overfitting the training data
# 
# Complex models such as deep neural networks can detect subtle patterns in the data,
# but if the training set is noisy, or if it is too small (which introduces sampling noise),
# then the model is likely to detect patterns in the noise itself. Obviously these patterns
# will not generalize to new instances. For example, say you feed your life satisfaction
# model many more attributes, including uninformative ones such as the country’s
# name. In that case, a complex model may detect patterns like the fact that all coun‐
# tries in the training data with a w in their name have a life satisfaction greater than 7:
# New Zealand (7.3), Norway (7.4), Sweden (7.2), and Switzerland (7.5). How confident
# 
# 
# 26    |   Chapter 1: The Machine Learning Landscape
# 
#                   Download from finelybook www.finelybook.com
# are you that the W-satisfaction rule generalizes to Rwanda or Zimbabwe? Obviously
# this pattern occurred in the training data by pure chance, but the model has no way
# to tell whether a pattern is real or simply the result of noise in the data.
# 
#                 Overfitting happens when the model is too complex relative to the
#                 amount and noisiness of the training data. The possible solutions
#                 are:
# 
#                   • To simplify the model by selecting one with fewer parameters
#                     (e.g., a linear model rather than a high-degree polynomial
#                     model), by reducing the number of attributes in the training
#                     data or by constraining the model
#                   • To gather more training data
#                   • To reduce the noise in the training data (e.g., fix data errors
#                     and remove outliers)
# 
# 
# Constraining a model to make it simpler and reduce the risk of overfitting is called
# regularization. For example, the linear model we defined earlier has two parameters,
# θ0 and θ1. This gives the learning algorithm two degrees of freedom to adapt the model
# to the training data: it can tweak both the height (θ0) and the slope (θ1) of the line. If
# we forced θ1 = 0, the algorithm would have only one degree of freedom and would
# have a much harder time fitting the data properly: all it could do is move the line up
# or down to get as close as possible to the training instances, so it would end up
# around the mean. A very simple model indeed! If we allow the algorithm to modify θ1
# but we force it to keep it small, then the learning algorithm will effectively have some‐
# where in between one and two degrees of freedom. It will produce a simpler model
# than with two degrees of freedom, but more complex than with just one. You want to
# find the right balance between fitting the data perfectly and keeping the model simple
# enough to ensure that it will generalize well.
# Figure 1-23 shows three models: the dotted line represents the original model that
# was trained with a few countries missing, the dashed line is our second model trained
# with all countries, and the solid line is a linear model trained with the same data as
# the first model but with a regularization constraint. You can see that regularization
# forced the model to have a smaller slope, which fits a bit less the training data that the
# model was trained on, but actually allows it to generalize better to new examples.
# 
# 
# 
# 
#                                                         Main Challenges of Machine Learning   |   27
# 
#                         Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 1-23. Regularization reduces the risk of overfitting
# 
# The amount of regularization to apply during learning can be controlled by a hyper‐
# parameter. A hyperparameter is a parameter of a learning algorithm (not of the
# model). As such, it is not affected by the learning algorithm itself; it must be set prior
# to training and remains constant during training. If you set the regularization hyper‐
# parameter to a very large value, you will get an almost flat model (a slope close to
# zero); the learning algorithm will almost certainly not overfit the training data, but it
# will be less likely to find a good solution. Tuning hyperparameters is an important
# part of building a Machine Learning system (you will see a detailed example in the
# next chapter).
# 
# Underfitting the Training Data
# As you might guess, underfitting is the opposite of overfitting: it occurs when your
# model is too simple to learn the underlying structure of the data. For example, a lin‐
# ear model of life satisfaction is prone to underfit; reality is just more complex than
# the model, so its predictions are bound to be inaccurate, even on the training exam‐
# ples.
# The main options to fix this problem are:
# 
#      • Selecting a more powerful model, with more parameters
#      • Feeding better features to the learning algorithm (feature engineering)
#      • Reducing the constraints on the model (e.g., reducing the regularization hyper‐
#        parameter)
# 
# 
# Stepping Back
# By now you already know a lot about Machine Learning. However, we went through
# so many concepts that you may be feeling a little lost, so let’s step back and look at the
# big picture:
# 
# 
# 28    |   Chapter 1: The Machine Learning Landscape
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Overfitting the Training Data",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Overfittingthe(HierNode):
    def __init__(self):
        super().__init__("Overfitting the Training Data")
        self.add(Content(), "content")

# eof
