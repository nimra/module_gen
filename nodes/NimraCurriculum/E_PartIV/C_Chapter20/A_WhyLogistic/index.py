# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 20
# 
# 
# 
# Logistic Regression
# Logistic regression is a supervised machine learning algorithm developed for learning
# classification problems. A classification learning problem is when the target variable is
# categorical. The goal of logistic regression is to map a function from the features of the
# dataset to the targets to predict the probability that a new example belongs to one of the
# target classes. Figure 20-1 is an example of a dataset with categorical targets.
# 
# 
# 
# 
# Figure 20-1. Dataset with qualitative variables as output
# 
# 
# Why Logistic Regression?
# To develop our understanding of classification with logistic regression and why linear
# regression is unsuitable for learning categorical outputs, let us consider a binary or
# two-­class classification problem. The dataset illustrated in Figure 20-2 has the output y
# (i.e., eye disease) = {disease, no-disease} is an example of dataset with binary targets.
# 
# 
# 
#                                                                                           243
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_20
# 
# Chapter 20   Logistic Regression
# 
# 
# 
# 
# Figure 20-2. Two-class classification problem
# 
#     From the illustration in Figure 20-3, the linear regression algorithm is susceptible
# to plot inaccurate decision boundaries especially in the presence of outliers (as seen
# toward the far right of the graph in Figure 20-3). Moreover, the linear regression model
# will be looking to learn a real-valued output, whereas a classification learning problem
# predicts the class membership of an observation using probability estimates.
# 
# 
# 
# 
# Figure 20-3. Linear regression on a classification dataset
# 
# 
# 
# 
# 244
# 
#                                                                   Chapter 20   Logistic Regression
# 
# 
# Introducing the Logit or Sigmoid Model
# The logistic function, also known as the logit or the sigmoid function, is responsible
# for constraining the output of the cost function so that it becomes a probability output
# between 0 and 1. The sigmoid function is formally written as
# 
#                                                         1
#                                         h (t ) =
#                                                      1 + e -t
# 
#     The logistic regression model is formally similar to the linear regression model
# except that it is acted upon by the sigmoid model. The following is the formal
# representation:
# 
#                                ŷ = q 0 + q1 x1 + q 2 x 2 +¼+ qn xn
# 
# 
#                                                        1
#                                         h ( yˆ ) =
#                                                      1+ e-y
#                                                           ˆ
# 
# 
# 
# 
# where 0 ≤ h(t) ≤ 1. The sigmoid function is graphically shown in Figure 20-4.
# 
# 
# 
# 
# Figure 20-4. Logistic function
# 
# 
# 
#                                                                                               245
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Why Logistic Regression?")
        self.add(MarkdownBlock("# Why Logistic Regression?"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class WhyLogistic(HierNode):
    def __init__(self):
        super().__init__("Why Logistic Regression?")
        self.add(Content())

# eof
