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

from .A_OneHotEncodingDummy.index import OneHotEncodingDummy as A_OneHotEncodingDummy
from .B_NumbersCan.index import NumbersCan as B_NumbersCan

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# learning practitioners trying to solve real-world problems. Representing your data in
# the right way can have a bigger influence on the performance of a supervised model
# than the exact parameters you choose.
# In this chapter, we will first go over the important and very common case of categori‐
# cal features, and then give some examples of helpful transformations for specific
# combinations of features and models.
# 
# Categorical Variables
# As an example, we will use the dataset of adult incomes in the United States, derived
# from the 1994 census database. The task of the adult dataset is to predict whether a
# worker has an income of over $50,000 or under $50,000. The features in this dataset
# include the workers’ ages, how they are employed (self employed, private industry
# employee, government employee, etc.), their education, their gender, their working
# hours per week, occupation, and more. Table 4-1 shows the first few entries in the
# dataset.
# 
# Table 4-1. The first few entries in the adult dataset
#       age workclass           education     gender hours-per-week occupation         income
# 0     39 State-gov            Bachelors     Male   40             Adm-clerical       <=50K
# 1     50    Self-emp-not-inc Bachelors      Male     13            Exec-managerial   <=50K
# 2     38    Private           HS-grad       Male     40            Handlers-cleaners <=50K
# 3     53    Private           11th          Male     40            Handlers-cleaners <=50K
# 4     28    Private           Bachelors     Female 40              Prof-specialty    <=50K
# 5     37    Private           Masters       Female 40              Exec-managerial   <=50K
# 6     49    Private           9th           Female 16              Other-service     <=50K
# 7     52    Self-emp-not-inc HS-grad        Male     45            Exec-managerial   >50K
# 8     31    Private           Masters       Female 50              Prof-specialty    >50K
# 9     42    Private           Bachelors     Male     40            Exec-managerial   >50K
# 10 37       Private           Some-college Male      80            Exec-managerial   >50K
# 
# The task is phrased as a classification task with the two classes being income <=50k
# and >50k. It would also be possible to predict the exact income, and make this a
# regression task. However, that would be much more difficult, and the 50K division is
# interesting to understand on its own.
# In this dataset, age and hours-per-week are continuous features, which we know
# how to treat. The workclass, education, sex, and occupation features are categori‐
# cal, however. All of them come from a fixed list of possible values, as opposed to a
# range, and denote a qualitative property, as opposed to a quantity.
# 
# 
# 
# 212   |    Chapter 4: Representing Data and Engineering Features
# 
# As a starting point, let’s say we want to learn a logistic regression classifier on this
# data. We know from Chapter 2 that a logistic regression makes predictions, ŷ, using
# the following formula:
# 
#     ŷ = w[0] * x[0] + w[1] * x[1] + ... + w[p] * x[p] + b > 0
# 
# where w[i] and b are coefficients learned from the training set and x[i] are the input
# features. This formula makes sense when x[i] are numbers, but not when x[2] is
# "Masters" or "Bachelors". Clearly we need to represent our data in some different
# way when applying logistic regression. The next section will explain how we can
# overcome this problem.
# 
# One-Hot-Encoding (Dummy Variables)
# By far the most common way to represent categorical variables is using the one-hot-
# encoding or one-out-of-N encoding, also known as dummy variables. The idea behind
# dummy variables is to replace a categorical variable with one or more new features
# that can have the values 0 and 1. The values 0 and 1 make sense in the formula for
# linear binary classification (and for all other models in scikit-learn), and we can
# represent any number of categories by introducing one new feature per category, as
# described here.
# Let’s say for the workclass feature we have possible values of "Government
# Employee", "Private Employee", "Self Employed", and "Self Employed Incorpo
# rated". To encode these four possible values, we create four new features, called "Gov
# ernment Employee", "Private Employee", "Self Employed", and "Self Employed
# Incorporated". A feature is 1 if workclass for this person has the corresponding
# value and 0 otherwise, so exactly one of the four new features will be 1 for each data
# point. This is why this is called one-hot or one-out-of-N encoding.
# The principle is illustrated in Table 4-2. A single feature is encoded using four new
# features. When using this data in a machine learning algorithm, we would drop the
# original workclass feature and only keep the 0–1 features.
# 
# Table 4-2. Encoding the workclass feature using one-hot encoding
# workclass                 Government Employee Private Employee Self Employed Self Employed Incorporated
# Government Employee       1                   0                0             0
# Private Employee          0                    1                0              0
# Self Employed             0                    0                1              0
# Self Employed Incorporated 0                   0                0              1
# 
# 
# 
# 
#                                                                              Categorical Variables   |   213
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Categorical Variables",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class CategoricalVariables(HierNode):
    def __init__(self):
        super().__init__("Categorical Variables")
        self.add(Content(), "content")
        self.add(A_OneHotEncodingDummy())
        self.add(B_NumbersCan())

# eof
