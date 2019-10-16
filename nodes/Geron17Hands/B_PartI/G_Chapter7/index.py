# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_VotingClassifiers.index import VotingClassifiers as A_VotingClassifiers
from .B_Baggingand.index import Baggingand as B_Baggingand
from .C_RandomPatches.index import RandomPatches as C_RandomPatches
from .D_RandomForests.index import RandomForests as D_RandomForests
from .E_Boosting.index import Boosting as E_Boosting
from .F_Stacking.index import Stacking as F_Stacking
from .G_Exercises.index import Exercises as G_Exercises

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                   Download from finelybook www.finelybook.com
# 
# 
#                                                                             CHAPTER 7
#        Ensemble Learning and Random Forests
# 
# 
# 
# 
# Suppose you ask a complex question to thousands of random people, then aggregate
# their answers. In many cases you will find that this aggregated answer is better than
# an expert’s answer. This is called the wisdom of the crowd. Similarly, if you aggregate
# the predictions of a group of predictors (such as classifiers or regressors), you will
# often get better predictions than with the best individual predictor. A group of pre‐
# dictors is called an ensemble; thus, this technique is called Ensemble Learning, and an
# Ensemble Learning algorithm is called an Ensemble method.
# For example, you can train a group of Decision Tree classifiers, each on a different
# random subset of the training set. To make predictions, you just obtain the predic‐
# tions of all individual trees, then predict the class that gets the most votes (see the last
# exercise in Chapter 6). Such an ensemble of Decision Trees is called a Random Forest,
# and despite its simplicity, this is one of the most powerful Machine Learning algo‐
# rithms available today.
# Moreover, as we discussed in Chapter 2, you will often use Ensemble methods near
# the end of a project, once you have already built a few good predictors, to combine
# them into an even better predictor. In fact, the winning solutions in Machine Learn‐
# ing competitions often involve several Ensemble methods (most famously in the Net‐
# flix Prize competition).
# In this chapter we will discuss the most popular Ensemble methods, including bag‐
# ging, boosting, stacking, and a few others. We will also explore Random Forests.
# 
# Voting Classifiers
# Suppose you have trained a few classifiers, each one achieving about 80% accuracy.
# You may have a Logistic Regression classifier, an SVM classifier, a Random Forest
# classifier, a K-Nearest Neighbors classifier, and perhaps a few more (see Figure 7-1).
# 
# 
#                                                                                          181
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 7. Ensemble Learning and Random Forests",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Chapter 7. Ensemble Learning and Random Forests"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter7(HierNode):
    def __init__(self):
        super().__init__("Chapter 7. Ensemble Learning and Random Forests")
        self.add(Content())
        self.add(A_VotingClassifiers())
        self.add(B_Baggingand())
        self.add(C_RandomPatches())
        self.add(D_RandomForests())
        self.add(E_Boosting())
        self.add(F_Stacking())
        self.add(G_Exercises())

# eof
