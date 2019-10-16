# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                        Download from finelybook www.finelybook.com
#      final_predictions = final_model.predict(X_test_prepared)
# 
#      final_mse = mean_squared_error(y_test, final_predictions)
#      final_rmse = np.sqrt(final_mse)   # => evaluates to 48,209.6
# The performance will usually be slightly worse than what you measured using cross-
# validation if you did a lot of hyperparameter tuning (because your system ends up
# fine-tuned to perform well on the validation data, and will likely not perform as well
# on unknown datasets). It is not the case in this example, but when this happens you
# must resist the temptation to tweak the hyperparameters to make the numbers look
# good on the test set; the improvements would be unlikely to generalize to new data.
# Now comes the project prelaunch phase: you need to present your solution (high‐
# lighting what you have learned, what worked and what did not, what assumptions
# were made, and what your system’s limitations are), document everything, and create
# nice presentations with clear visualizations and easy-to-remember statements (e.g.,
# “the median income is the number one predictor of housing prices”).
# 
# Launch, Monitor, and Maintain Your System
# Perfect, you got approval to launch! You need to get your solution ready for produc‐
# tion, in particular by plugging the production input data sources into your system
# and writing tests.
# You also need to write monitoring code to check your system’s live performance at
# regular intervals and trigger alerts when it drops. This is important to catch not only
# sudden breakage, but also performance degradation. This is quite common because
# models tend to “rot” as data evolves over time, unless the models are regularly trained
# on fresh data.
# Evaluating your system’s performance will require sampling the system’s predictions
# and evaluating them. This will generally require a human analysis. These analysts
# may be field experts, or workers on a crowdsourcing platform (such as Amazon
# Mechanical Turk or CrowdFlower). Either way, you need to plug the human evalua‐
# tion pipeline into your system.
# You should also make sure you evaluate the system’s input data quality. Sometimes
# performance will degrade slightly because of a poor quality signal (e.g., a malfunc‐
# tioning sensor sending random values, or another team’s output becoming stale), but
# it may take a while before your system’s performance degrades enough to trigger an
# alert. If you monitor your system’s inputs, you may catch this earlier. Monitoring the
# inputs is particularly important for online learning systems.
# Finally, you will generally want to train your models on a regular basis using fresh
# data. You should automate this process as much as possible. If you don’t, you are very
# 
# 
# 76   |   Chapter 2: End-to-End Machine Learning Project
# 
#                    Download from finelybook www.finelybook.com
# likely to refresh your model only every six months (at best), and your system’s perfor‐
# mance may fluctuate severely over time. If your system is an online learning system,
# you should make sure you save snapshots of its state at regular intervals so you can
# easily roll back to a previously working state.
# 
# Try It Out!
# Hopefully this chapter gave you a good idea of what a Machine Learning project
# looks like, and showed you some of the tools you can use to train a great system. As
# you can see, much of the work is in the data preparation step, building monitoring
# tools, setting up human evaluation pipelines, and automating regular model training.
# The Machine Learning algorithms are also important, of course, but it is probably
# preferable to be comfortable with the overall process and know three or four algo‐
# rithms well rather than to spend all your time exploring advanced algorithms and not
# enough time on the overall process.
# So, if you have not already done so, now is a good time to pick up a laptop, select a
# dataset that you are interested in, and try to go through the whole process from A to
# Z. A good place to start is on a competition website such as http://kaggle.com/: you
# will have a dataset to play with, a clear goal, and people to share the experience with.
# 
# Exercises
# Using this chapter’s housing dataset:
# 
#  1. Try a Support Vector Machine regressor (sklearn.svm.SVR), with various hyper‐
#     parameters such as kernel="linear" (with various values for the C hyperpara‐
#     meter) or kernel="rbf" (with various values for the C and gamma
#     hyperparameters). Don’t worry about what these hyperparameters mean for now.
#     How does the best SVR predictor perform?
#  2. Try replacing GridSearchCV with RandomizedSearchCV.
#  3. Try adding a transformer in the preparation pipeline to select only the most
#     important attributes.
#  4. Try creating a single pipeline that does the full data preparation plus the final
#     prediction.
#  5. Automatically explore some preparation options using GridSearchCV.
# 
# Solutions to these exercises are available in the online Jupyter notebooks at https://
# github.com/ageron/handson-ml.
# 
# 
# 
# 
#                                                                           Try It Out!   |   77
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Launch, Monitor, and Maintain Your System",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Launch, Monitor, and Maintain Your System"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LaunchMonitor(HierNode):
    def __init__(self):
        super().__init__("Launch, Monitor, and Maintain Your System")
        self.add(Content())

# eof
