# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Trainingand.index import Trainingand as A_Trainingand
from .B_MakingPredictions.index import MakingPredictions as B_MakingPredictions
from .C_EstimatingClass.index import EstimatingClass as C_EstimatingClass
from .D_TheCART.index import TheCART as D_TheCART
from .E_ComputationalComplexity.index import ComputationalComplexity as E_ComputationalComplexity
from .F_GiniImpurity.index import GiniImpurity as F_GiniImpurity
from .G_RegularizationHyperparameters.index import RegularizationHyperparameters as G_RegularizationHyperparameters
from .H_Regression.index import Regression as H_Regression
from .I_Instability.index import Instability as I_Instability
from .J_Exercises.index import Exercises as J_Exercises

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                  Download from finelybook www.finelybook.com
# 
# 
#                                                                         CHAPTER 6
#                                                           Decision Trees
# 
# 
# 
# 
# Like SVMs, Decision Trees are versatile Machine Learning algorithms that can per‐
# form both classification and regression tasks, and even multioutput tasks. They are
# very powerful algorithms, capable of fitting complex datasets. For example, in Chap‐
# ter 2 you trained a DecisionTreeRegressor model on the California housing dataset,
# fitting it perfectly (actually overfitting it).
# Decision Trees are also the fundamental components of Random Forests (see Chap‐
# ter 7), which are among the most powerful Machine Learning algorithms available
# today.
# In this chapter we will start by discussing how to train, visualize, and make predic‐
# tions with Decision Trees. Then we will go through the CART training algorithm
# used by Scikit-Learn, and we will discuss how to regularize trees and use them for
# regression tasks. Finally, we will discuss some of the limitations of Decision Trees.
# 
# Training and Visualizing a Decision Tree
# To understand Decision Trees, let’s just build one and take a look at how it makes pre‐
# dictions. The following code trains a DecisionTreeClassifier on the iris dataset
# (see Chapter 4):
#     from sklearn.datasets import load_iris
#     from sklearn.tree import DecisionTreeClassifier
# 
#     iris = load_iris()
#     X = iris.data[:, 2:] # petal length and width
#     y = iris.target
# 
#     tree_clf = DecisionTreeClassifier(max_depth=2)
#     tree_clf.fit(X, y)
# 
# 
# 
#                                                                                     167
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 6. Decision Trees",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Chapter 6. Decision Trees"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter6(HierNode):
    def __init__(self):
        super().__init__("Chapter 6. Decision Trees")
        self.add(Content())
        self.add(A_Trainingand())
        self.add(B_MakingPredictions())
        self.add(C_EstimatingClass())
        self.add(D_TheCART())
        self.add(E_ComputationalComplexity())
        self.add(F_GiniImpurity())
        self.add(G_RegularizationHyperparameters())
        self.add(H_Regression())
        self.add(I_Instability())
        self.add(J_Exercises())

# eof
