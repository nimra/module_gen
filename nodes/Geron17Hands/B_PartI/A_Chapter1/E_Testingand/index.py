# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                  Download from finelybook www.finelybook.com
#   • Machine Learning is about making machines get better at some task by learning
#     from data, instead of having to explicitly code rules.
#   • There are many different types of ML systems: supervised or not, batch or online,
#     instance-based or model-based, and so on.
#   • In a ML project you gather data in a training set, and you feed the training set to
#     a learning algorithm. If the algorithm is model-based it tunes some parameters to
#     fit the model to the training set (i.e., to make good predictions on the training set
#     itself), and then hopefully it will be able to make good predictions on new cases
#     as well. If the algorithm is instance-based, it just learns the examples by heart and
#     uses a similarity measure to generalize to new instances.
#   • The system will not perform well if your training set is too small, or if the data is
#     not representative, noisy, or polluted with irrelevant features (garbage in, garbage
#     out). Lastly, your model needs to be neither too simple (in which case it will
#     underfit) nor too complex (in which case it will overfit).
# 
# There’s just one last important topic to cover: once you have trained a model, you
# don’t want to just “hope” it generalizes to new cases. You want to evaluate it, and fine-
# tune it if necessary. Let’s see how.
# 
# Testing and Validating
# The only way to know how well a model will generalize to new cases is to actually try
# it out on new cases. One way to do that is to put your model in production and moni‐
# tor how well it performs. This works well, but if your model is horribly bad, your
# users will complain—not the best idea.
# A better option is to split your data into two sets: the training set and the test set. As
# these names imply, you train your model using the training set, and you test it using
# the test set. The error rate on new cases is called the generalization error (or out-of-
# sample error), and by evaluating your model on the test set, you get an estimation of
# this error. This value tells you how well your model will perform on instances it has
# never seen before.
# If the training error is low (i.e., your model makes few mistakes on the training set)
# but the generalization error is high, it means that your model is overfitting the train‐
# ing data.
# 
#                 It is common to use 80% of the data for training and hold out 20%
#                 for testing.
# 
# 
# 
# 
#                                                                   Testing and Validating   |   29
# 
#                  Download from finelybook www.finelybook.com
# So evaluating a model is simple enough: just use a test set. Now suppose you are hesi‐
# tating between two models (say a linear model and a polynomial model): how can
# you decide? One option is to train both and compare how well they generalize using
# the test set.
# Now suppose that the linear model generalizes better, but you want to apply some
# regularization to avoid overfitting. The question is: how do you choose the value of
# the regularization hyperparameter? One option is to train 100 different models using
# 100 different values for this hyperparameter. Suppose you find the best hyperparame‐
# ter value that produces a model with the lowest generalization error, say just 5% error.
# So you launch this model into production, but unfortunately it does not perform as
# well as expected and produces 15% errors. What just happened?
# The problem is that you measured the generalization error multiple times on the test
# set, and you adapted the model and hyperparameters to produce the best model for
# that set. This means that the model is unlikely to perform as well on new data.
# A common solution to this problem is to have a second holdout set called the valida‐
# tion set. You train multiple models with various hyperparameters using the training
# set, you select the model and hyperparameters that perform best on the validation set,
# and when you’re happy with your model you run a single final test against the test set
# to get an estimate of the generalization error.
# To avoid “wasting” too much training data in validation sets, a common technique is
# to use cross-validation: the training set is split into complementary subsets, and each
# model is trained against a different combination of these subsets and validated
# against the remaining parts. Once the model type and hyperparameters have been
# selected, a final model is trained using these hyperparameters on the full training set,
# and the generalized error is measured on the test set.
# 
# 
#                                          No Free Lunch Theorem
#      A model is a simplified version of the observations. The simplifications are meant to
#      discard the superfluous details that are unlikely to generalize to new instances. How‐
#      ever, to decide what data to discard and what data to keep, you must make assump‐
#      tions. For example, a linear model makes the assumption that the data is
#      fundamentally linear and that the distance between the instances and the straight line
#      is just noise, which can safely be ignored.
#      In a famous 1996 paper,11 David Wolpert demonstrated that if you make absolutely
#      no assumption about the data, then there is no reason to prefer one model over any
#      other. This is called the No Free Lunch (NFL) theorem. For some datasets the best
# 
# 
# 11 “The Lack of A Priori Distinctions Between Learning Algorithms,” D. Wolperts (1996).
# 
# 
# 
# 30     |   Chapter 1: The Machine Learning Landscape
# 
#                   Download from finelybook www.finelybook.com
#  model is a linear model, while for other datasets it is a neural network. There is no
#  model that is a priori guaranteed to work better (hence the name of the theorem). The
#  only way to know for sure which model is best is to evaluate them all. Since this is not
#  possible, in practice you make some reasonable assumptions about the data and you
#  evaluate only a few reasonable models. For example, for simple tasks you may evalu‐
#  ate linear models with various levels of regularization, and for a complex problem you
#  may evaluate various neural networks.
# 
# 
# 
# Exercises
# In this chapter we have covered some of the most important concepts in Machine
# Learning. In the next chapters we will dive deeper and write more code, but before we
# do, make sure you know how to answer the following questions:
# 
#  1. How would you define Machine Learning?
#  2. Can you name four types of problems where it shines?
#  3. What is a labeled training set?
#  4. What are the two most common supervised tasks?
#  5. Can you name four common unsupervised tasks?
#  6. What type of Machine Learning algorithm would you use to allow a robot to
#     walk in various unknown terrains?
#  7. What type of algorithm would you use to segment your customers into multiple
#     groups?
#  8. Would you frame the problem of spam detection as a supervised learning prob‐
#     lem or an unsupervised learning problem?
#  9. What is an online learning system?
# 10. What is out-of-core learning?
# 11. What type of learning algorithm relies on a similarity measure to make predic‐
#     tions?
# 12. What is the difference between a model parameter and a learning algorithm’s
#     hyperparameter?
# 13. What do model-based learning algorithms search for? What is the most common
#     strategy they use to succeed? How do they make predictions?
# 14. Can you name four of the main challenges in Machine Learning?
# 15. If your model performs great on the training data but generalizes poorly to new
#     instances, what is happening? Can you name three possible solutions?
# 16. What is a test set and why would you want to use it?
# 
# 
#                                                                              Exercises   |   31
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Testing and Validating",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Testing and Validating"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Testingand(HierNode):
    def __init__(self):
        super().__init__("Testing and Validating")
        self.add(Content())

# eof
