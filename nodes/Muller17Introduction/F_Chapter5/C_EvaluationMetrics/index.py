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

from .A_Keepthe.index import Keepthe as A_Keepthe
from .B_Metricsfor.index import Metricsfor as B_Metricsfor
from .C_Metricsfor.index import Metricsfor as C_Metricsfor
from .D_RegressionMetrics.index import RegressionMetrics as D_RegressionMetrics
from .E_UsingEvaluation.index import UsingEvaluation as E_UsingEvaluation

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# model using a particular parameter setting on a particular cross-validation split can
# be done completely independently from the other parameter settings and models.
# This makes grid search and cross-validation ideal candidates for parallelization over
# multiple CPU cores or over a cluster. You can make use of multiple cores in Grid
# SearchCV and cross_val_score by setting the n_jobs parameter to the number of
# CPU cores you want to use. You can set n_jobs=-1 to use all available cores.
# You should be aware that scikit-learn does not allow nesting of parallel operations.
# So, if you are using the n_jobs option on your model (for example, a random forest),
# you cannot use it in GridSearchCV to search over this model. If your dataset and
# model are very large, it might be that using many cores uses up too much memory,
# and you should monitor your memory usage when building large models in parallel.
# It is also possible to parallelize grid search and cross-validation over multiple
# machines in a cluster, although at the time of writing this is not supported within
# scikit-learn. It is, however, possible to use the IPython parallel framework for par‐
# allel grid searches, if you don’t mind writing the for loop over parameters as we did
# in “Simple Grid Search” on page 261.
# For Spark users, there is also the recently developed spark-sklearn package, which
# allows running a grid search over an already established Spark cluster.
# 
# Evaluation Metrics and Scoring
# So far, we have evaluated classification performance using accuracy (the fraction of
# correctly classified samples) and regression performance using R2. However, these are
# only two of the many possible ways to summarize how well a supervised model per‐
# forms on a given dataset. In practice, these evaluation metrics might not be appropri‐
# ate for your application, and it is important to choose the right metric when selecting
# between models and adjusting parameters.
# 
# Keep the End Goal in Mind
# When selecting a metric, you should always have the end goal of the machine learn‐
# ing application in mind. In practice, we are usually interested not just in making
# accurate predictions, but in using these predictions as part of a larger decision-
# making process. Before picking a machine learning metric, you should think about
# the high-level goal of the application, often called the business metric. The conse‐
# quences of choosing a particular algorithm for a machine learning application are
# 
# 
# 
# 
#                                                          Evaluation Metrics and Scoring   |   275
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Evaluation Metrics and Scoring",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class EvaluationMetrics(HierNode):
    def __init__(self):
        super().__init__("Evaluation Metrics and Scoring")
        self.add(Content(), "content")
        self.add(A_Keepthe())
        self.add(B_Metricsfor())
        self.add(C_Metricsfor())
        self.add(D_RegressionMetrics())
        self.add(E_UsingEvaluation())

# eof
