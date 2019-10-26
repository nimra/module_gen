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
# The process is illustrated in Figure 6-3 for two transformers, T1 and T2, and a
# classifier (called Classifier).
# 
# 
# 
# 
# Figure 6-3. Overview of the pipeline training and prediction process
# 
# The pipeline is actually even more general than this. There is no requirement for the
# last step in a pipeline to have a predict function, and we could create a pipeline just
# containing, for example, a scaler and PCA. Then, because the last step (PCA) has a
# transform method, we could call transform on the pipeline to get the output of
# PCA.transform applied to the data that was processed by the previous step. The last
# step of a pipeline is only required to have a fit method.
# 
# Convenient Pipeline Creation with make_pipeline
# Creating a pipeline using the syntax described earlier is sometimes a bit cumbersome,
# and we often don’t need user-specified names for each step. There is a convenience
# function, make_pipeline, that will create a pipeline for us and automatically name
# each step based on its class. The syntax for make_pipeline is as follows:
# In[17]:
#     from sklearn.pipeline import make_pipeline
#     # standard syntax
#     pipe_long = Pipeline([("scaler", MinMaxScaler()), ("svm", SVC(C=100))])
#     # abbreviated syntax
#     pipe_short = make_pipeline(MinMaxScaler(), SVC(C=100))
# 
# 
# 
# 
#                                                            The General Pipeline Interface   |   313
# 
# The pipeline objects pipe_long and pipe_short do exactly the same thing, but
# pipe_short has steps that were automatically named. We can see the names of the
# steps by looking at the steps attribute:
# In[18]:
#       print("Pipeline steps:\n{}".format(pipe_short.steps))
# 
# Out[18]:
#       Pipeline steps:
#       [('minmaxscaler', MinMaxScaler(copy=True, feature_range=(0, 1))),
#        ('svc', SVC(C=100, cache_size=200, class_weight=None, coef0=0.0,
#                    decision_function_shape=None, degree=3, gamma='auto',
#                    kernel='rbf', max_iter=-1, probability=False,
#                    random_state=None, shrinking=True, tol=0.001,
#                    verbose=False))]
# 
# The steps are named minmaxscaler and svc. In general, the step names are just low‐
# ercase versions of the class names. If multiple steps have the same class, a number is
# appended:
# In[19]:
#       from sklearn.preprocessing import StandardScaler
#       from sklearn.decomposition import PCA
# 
#       pipe = make_pipeline(StandardScaler(), PCA(n_components=2), StandardScaler())
#       print("Pipeline steps:\n{}".format(pipe.steps))
# 
# Out[19]:
#       Pipeline steps:
#       [('standardscaler-1', StandardScaler(copy=True, with_mean=True, with_std=True)),
#        ('pca', PCA(copy=True, iterated_power=4, n_components=2, random_state=None,
#                    svd_solver='auto', tol=0.0, whiten=False)),
#        ('standardscaler-2', StandardScaler(copy=True, with_mean=True, with_std=True))]
# 
# As you can see, the first StandardScaler step was named standardscaler-1 and the
# second standardscaler-2. However, in such settings it might be better to use the
# Pipeline construction with explicit names, to give more semantic names to each
# step.
# 
# Accessing Step Attributes
# Often you will want to inspect attributes of one of the steps of the pipeline—say, the
# coefficients of a linear model or the components extracted by PCA. The easiest way to
# access the steps in a pipeline is via the named_steps attribute, which is a dictionary
# from the step names to the estimators:
# 
# 
# 
# 
# 314   |   Chapter 6: Algorithm Chains and Pipelines
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Convenient Pipeline Creation with make_pipeline",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ConvenientPipeline(HierNode):
    def __init__(self):
        super().__init__("Convenient Pipeline Creation with make_pipeline")
        self.add(Content(), "content")

# eof
