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
#                  Download from finelybook www.finelybook.com
# 17. What is the purpose of a validation set?
# 18. What can go wrong if you tune hyperparameters using the test set?
# 19. What is cross-validation and why would you prefer it to a validation set?
# 
# Solutions to these exercises are available in Appendix A.
# 
# 
# 
# 
# 32   |   Chapter 1: The Machine Learning Landscape
# 
#                        Download from finelybook www.finelybook.com
# 
# 
#                                                                                                 CHAPTER 2
#                 End-to-End Machine Learning Project
# 
# 
# 
# 
# In this chapter, you will go through an example project end to end, pretending to be a
# recently hired data scientist in a real estate company.1 Here are the main steps you will
# go through:
# 
#  1. Look at the big picture.
#  2. Get the data.
#  3. Discover and visualize the data to gain insights.
#  4. Prepare the data for Machine Learning algorithms.
#  5. Select a model and train it.
#  6. Fine-tune your model.
#  7. Present your solution.
#  8. Launch, monitor, and maintain your system.
# 
# 
# Working with Real Data
# When you are learning about Machine Learning it is best to actually experiment with
# real-world data, not just artificial datasets. Fortunately, there are thousands of open
# datasets to choose from, ranging across all sorts of domains. Here are a few places
# you can look to get data:
# 
#   • Popular open data repositories:
# 
# 
# 1 The example project is completely fictitious; the goal is just to illustrate the main steps of a Machine Learning
#   project, not to learn anything about the real estate business.
# 
# 
# 
#                                                                                                                  33
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Exercises",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Exercises(HierNode):
    def __init__(self):
        super().__init__("Exercises")
        self.add(Content(), "content")

# eof
