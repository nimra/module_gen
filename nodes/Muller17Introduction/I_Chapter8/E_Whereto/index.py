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

from .A_Theory.index import Theory as A_Theory
from .B_OtherMachine.index import OtherMachine as B_OtherMachine
from .C_RankingRecommender.index import RankingRecommender as C_RankingRecommender
from .D_ProbabilisticModeling.index import ProbabilisticModeling as D_ProbabilisticModeling
from .E_NeuralNetworks.index import NeuralNetworks as E_NeuralNetworks
from .F_Scalingto.index import Scalingto as F_Scalingto
from .G_HoningYour.index import HoningYour as G_HoningYour

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# In[1]:
#     from sklearn.base import BaseEstimator, TransformerMixin
# 
#     class MyTransformer(BaseEstimator, TransformerMixin):
#         def __init__(self, first_parameter=1, second_parameter=2):
#             # All parameters must be specified in the __init__ function
#             self.first_parameter = 1
#             self.second_parameter = 2
# 
#          def fit(self, X, y=None):
#              # fit should only take X and y as parameters
#              # Even if your model is unsupervised, you need to accept a y argument!
# 
#              # Model fitting code goes here
#              print("fitting the model right here")
#              # fit returns self
#              return self
# 
#          def transform(self, X):
#              # transform takes as parameter only X
# 
#              # Apply some transformation to X
#              X_transformed = X + 1
#              return X_transformed
# 
# Implementing a classifier or regressor works similarly, only instead of Transformer
# Mixin you need to inherit from ClassifierMixin or RegressorMixin. Also, instead
# of implementing transform, you would implement predict.
# As you can see from the example given here, implementing your own estimator
# requires very little code, and most scikit-learn users build up a collection of cus‐
# tom models over time.
# 
# Where to Go from Here
# This book provides an introduction to machine learning and will make you an effec‐
# tive practitioner. However, if you want to further your machine learning skills, here
# are some suggestions of books and more specialized resources to investigate to dive
# deeper.
# 
# Theory
# In this book, we tried to provide an intuition of how the most common machine
# learning algorithms work, without requiring a strong foundation in mathematics or
# computer science. However, many of the models we discussed use principles from
# probability theory, linear algebra, and optimization. While it is not necessary to
# understand all the details of how these algorithms are implemented, we think that
# 
# 
#                                                                Where to Go from Here   |   361
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Where to Go from Here",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Whereto(HierNode):
    def __init__(self):
        super().__init__("Where to Go from Here")
        self.add(Content(), "content")
        self.add(A_Theory())
        self.add(B_OtherMachine())
        self.add(C_RankingRecommender())
        self.add(D_ProbabilisticModeling())
        self.add(E_NeuralNetworks())
        self.add(F_Scalingto())
        self.add(G_HoningYour())

# eof
