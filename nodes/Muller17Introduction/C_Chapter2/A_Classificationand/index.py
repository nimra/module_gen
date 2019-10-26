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
#                                                                             CHAPTER 2
#                                                 Supervised Learning
# 
# 
# 
# 
# As we mentioned earlier, supervised machine learning is one of the most commonly
# used and successful types of machine learning. In this chapter, we will describe super‐
# vised learning in more detail and explain several popular supervised learning algo‐
# rithms. We already saw an application of supervised machine learning in Chapter 1:
# classifying iris flowers into several species using physical measurements of the
# flowers.
# Remember that supervised learning is used whenever we want to predict a certain
# outcome from a given input, and we have examples of input/output pairs. We build a
# machine learning model from these input/output pairs, which comprise our training
# set. Our goal is to make accurate predictions for new, never-before-seen data. Super‐
# vised learning often requires human effort to build the training set, but afterward
# automates and often speeds up an otherwise laborious or infeasible task.
# 
# Classification and Regression
# There are two major types of supervised machine learning problems, called classifica‐
# tion and regression.
# In classification, the goal is to predict a class label, which is a choice from a predefined
# list of possibilities. In Chapter 1 we used the example of classifying irises into one of
# three possible species. Classification is sometimes separated into binary classification,
# which is the special case of distinguishing between exactly two classes, and multiclass
# classification, which is classification between more than two classes. You can think of
# binary classification as trying to answer a yes/no question. Classifying emails as
# either spam or not spam is an example of a binary classification problem. In this
# binary classification task, the yes/no question being asked would be “Is this email
# spam?”
# 
# 
#                                                                                           25
# 
#                      In binary classification we often speak of one class being the posi‐
#                      tive class and the other class being the negative class. Here, positive
#                      doesn’t represent having benefit or value, but rather what the object
#                      of the study is. So, when looking for spam, “positive” could mean
#                      the spam class. Which of the two classes is called positive is often a
#                      subjective matter, and specific to the domain.
# 
# The iris example, on the other hand, is an example of a multiclass classification prob‐
# lem. Another example is predicting what language a website is in from the text on the
# website. The classes here would be a pre-defined list of possible languages.
# For regression tasks, the goal is to predict a continuous number, or a floating-point
# number in programming terms (or real number in mathematical terms). Predicting a
# person’s annual income from their education, their age, and where they live is an
# example of a regression task. When predicting income, the predicted value is an
# amount, and can be any number in a given range. Another example of a regression
# task is predicting the yield of a corn farm given attributes such as previous yields,
# weather, and number of employees working on the farm. The yield again can be an
# arbitrary number.
# An easy way to distinguish between classification and regression tasks is to ask
# whether there is some kind of continuity in the output. If there is continuity between
# possible outcomes, then the problem is a regression problem. Think about predicting
# annual income. There is a clear continuity in the output. Whether a person makes
# $40,000 or $40,001 a year does not make a tangible difference, even though these are
# different amounts of money; if our algorithm predicts $39,999 or $40,001 when it
# should have predicted $40,000, we don’t mind that much.
# By contrast, for the task of recognizing the language of a website (which is a classifi‐
# cation problem), there is no matter of degree. A website is in one language, or it is in
# another. There is no continuity between languages, and there is no language that is
# between English and French.1
# 
# Generalization, Overfitting, and Underfitting
# In supervised learning, we want to build a model on the training data and then be
# able to make accurate predictions on new, unseen data that has the same characteris‐
# tics as the training set that we used. If a model is able to make accurate predictions on
# unseen data, we say it is able to generalize from the training set to the test set. We
# want to build a model that is able to generalize as accurately as possible.
# 
# 
# 
# 
# 1 We ask linguists to excuse the simplified presentation of languages as distinct and fixed entities.
# 
# 
# 
# 26   |   Chapter 2: Supervised Learning
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Classification and Regression",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Classificationand(HierNode):
    def __init__(self):
        super().__init__("Classification and Regression")
        self.add(Content(), "content")

# eof
