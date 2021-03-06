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
# Figure 5-75. Decision boundaries for a random forest, which is an optimized ensemble of
# decision trees
# 
# We see that by averaging over 100 randomly perturbed models, we end up with an
# overall model that is much closer to our intuition about how the parameter space
# should be split.
# 
# Random Forest Regression
# In the previous section we considered random forests within the context of classifica‐
# tion. Random forests can also be made to work in the case of regression (that is, con‐
# tinuous rather than categorical variables). The estimator to use for this is the
# RandomForestRegressor, and the syntax is very similar to what we saw earlier.
# Consider the following data, drawn from the combination of a fast and slow oscilla‐
# tion (Figure 5-76):
#       In[10]: rng = np.random.RandomState(42)
#               x = 10 * rng.rand(200)
# 
#                 def model(x, sigma=0.3):
#                     fast_oscillation = np.sin(5 * x)
#                     slow_oscillation = np.sin(0.5 * x)
#                     noise = sigma * rng.randn(len(x))
# 
#                      return slow_oscillation + fast_oscillation + noise
# 
#                 y = model(x)
#                 plt.errorbar(x, y, 0.3, fmt='o');
# 
# 
# 
# 
# 428   |   Chapter 5: Machine Learning
# 
# Figure 5-76. Data for random forest regression
# 
# Using the random forest regressor, we can find the best-fit curve as follows
# (Figure 5-77):
#     In[11]: from sklearn.ensemble import RandomForestRegressor
#             forest = RandomForestRegressor(200)
#             forest.fit(x[:, None], y)
# 
#             xfit = np.linspace(0, 10, 1000)
#             yfit = forest.predict(xfit[:, None])
#             ytrue = model(xfit, sigma=0)
# 
#             plt.errorbar(x, y, 0.3, fmt='o', alpha=0.5)
#             plt.plot(xfit, yfit, '-r');
#             plt.plot(xfit, ytrue, '-k', alpha=0.5);
# Here the true model is shown by the smooth curve, while the random forest model is
# shown by the jagged curve. As you can see, the nonparametric random forest model
# is flexible enough to fit the multiperiod data, without us needing to specify a multi‐
# period model!
# 
# 
# 
# 
#                                                  In-Depth: Decision Trees and Random Forests   |   429
# 
# Figure 5-77. Random forest model fit to the data
# 
# Example: Random Forest for Classifying Digits
# Earlier we took a quick look at the handwritten digits data (see “Introducing Scikit-
# Learn” on page 343). Let’s use that again here to see how the random forest classifier
# can be used in this context.
#       In[12]: from sklearn.datasets import load_digits
#               digits = load_digits()
#               digits.keys()
#       Out[12]: dict_keys(['target', 'data', 'target_names', 'DESCR', 'images'])
# To remind us what we’re looking at, we’ll visualize the first few data points
# (Figure 5-78):
#       In[13]:
#       # set up the figure
#       fig = plt.figure(figsize=(6, 6)) # figure size in inches
#       fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
# 
#       # plot the digits: each image is 8x8 pixels
#       for i in range(64):
#           ax = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
#           ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')
# 
#           # label the image with the target value
#           ax.text(0, 7, str(digits.target[i]))
# 
# 
# 
# 
# 430   |   Chapter 5: Machine Learning
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Random Forest Regression",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class RandomForest(HierNode):
    def __init__(self):
        super().__init__("Random Forest Regression")
        self.add(Content())

# eof
