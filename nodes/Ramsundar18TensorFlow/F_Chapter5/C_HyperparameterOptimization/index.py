# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_SettingUp.index import SettingUp as A_SettingUp
from .B_GraduateStudent.index import GraduateStudent as B_GraduateStudent
from .C_GridSearch.index import GridSearch as C_GridSearch
from .D_RandomHyperparameter.index import RandomHyperparameter as D_RandomHyperparameter
from .E_Challengefor.index import Challengefor as E_Challengefor

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Regression Metrics
# You learned about regression metrics a few chapters ago. As a quick recap, the Pear‐
# son R2 and RMSE (root-mean-squared error) are good defaults.
# We only briefly covered the mathematical definition of R2 previously, but will delve
# into it more now. Let xi represent predictions and yi represent labels. Let x and y rep‐
# resent the mean of the predicted values and the labels, respectively. Then the Pearson
# R (note the lack of square) is
# 
#                   ∑N
#                    i = 1 xi − x y i − y
#       R=
#              ∑N
#               i = 1 xi − x
#                              2
#                                  ∑N
#                                   i = 1 yi − y
#                                                  2
# 
# 
# 
# This equation can be rewritten as
# 
#            cov x, y
#       R=
#            σxσ y
# 
# where cov represents the covariance and σ represents the standard deviation. Intui‐
# tively, the Pearson R measures the joint fluctuations of the predictions and labels
# from their means normalized by their respective ranges of fluctuations. If predictions
# and labels differ, these fluctuations will happen at different points and will tend to
# cancel, making R2 smaller. If predictions and labels tend to agree, the fluctuations will
# happen together and make R2 larger. We note that R2 is limited to a range between 0
# and 1.
# The RMSE measures the absolute quantity of the error between the predictions and
# the true quantities. It stands for root-mean-squared error, which is roughly analogous
# to the absolute value of the error between the true quantity and the predicted quan‐
# tity. Mathematically, the RMSE is defined as follows (using the same notation as
# before):
# 
#                    ∑N
#                     i = 1 xi − yi
#                                     2
#       RMSE =
#                           N
# 
# 
# Hyperparameter Optimization Algorithms
# As we mentioned earlier in the chapter, hyperparameter optimization methods are
# learning algorithms for finding values of the hyperparameters that optimize the
# chosen metric on the validation set. In general, this objective function cannot be dif‐
# ferentiated, so any optimization method must by necessity be a black box. In this
# section, we will show you some simple black-box learning algorithms for choosing
# 
# 110   |    Chapter 5: Hyperparameter Optimization
# 
# hyperparameter values. We will use the Tox21 dataset from Chapter 4 as a case study
# to demonstrate these black-box optimization methods. The Tox21 dataset is small
# enough to make experimentation easy, but complex enough that hyperparameter
# optimization isn’t trivial.
# We note before setting off that none of these black-box algorithms works perfectly. As
# you will soon see, in practice, much human input is required to optimize hyperpara‐
# meters.
# 
#                Can’t Hyperparameter Optimization Be Automated?
#                One of the long-running dreams of machine learning has been to
#                automate the process of selecting model hyperparameters. Projects
#                such as the “automated statistician” and others have sought to
#                remove some of the drudgery from the hyperparameter selection
#                process and make model construction more easily available to non-
#                experts. However, in practice, there has typically been a steep cost
#                in performance for the added convenience.
#                In recent years, there has been a surge of work focused on improv‐
#                ing the algorithmic foundations of model tuning. Gaussian pro‐
#                cesses, evolutionary algorithms, and reinforcement learning have
#                all been used to learn model hyperparameters and architectures
#                with very limited human input. Recent work has shown that with
#                large amounts of computing power, these algorithms can exceed
#                expert performance in model tuning! But the overhead is severe,
#                with dozens to hundreds of times greater computational power
#                required.
#                For now, automatic model tuning is still not practical. All algo‐
#                rithms we cover in this section require significant manual tuning
#                However, as hardware quality improves, we anticipate that hyper‐
#                parameter learning will become increasingly automated. In the
#                near term, we recommend strongly that all practitioners master the
#                intricacies of hyperparameter tuning. A strong ability to hyper‐
#                parameter tune is the skill that separates the expert from the
#                novice.
# 
# 
# Setting Up a Baseline
# The first step in hyperparameter tuning is finding a baseline. A baseline is perfor‐
# mance achievable by a robust (non–deep learning usually) algorithm. In general, ran‐
# dom forests are a superb choice for setting baselines. As shown in Figure 5-3, random
# forests are an ensemble method that train many decision tree models on subsets of
# the input data and input features. These individual trees then vote on the outcome.
# 
# 
# 
# 
#                                                    Hyperparameter Optimization Algorithms   |   111
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Hyperparameter Optimization Algorithms",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Hyperparameter Optimization Algorithms"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class HyperparameterOptimization(HierNode):
    def __init__(self):
        super().__init__("Hyperparameter Optimization Algorithms")
        self.add(Content())
        self.add(A_SettingUp())
        self.add(B_GraduateStudent())
        self.add(C_GridSearch())
        self.add(D_RandomHyperparameter())
        self.add(E_Challengefor())

# eof
