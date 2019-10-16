# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_FeatureEngineering.index import FeatureEngineering as A_FeatureEngineering
from .B_ResamplingMethods.index import ResamplingMethods as B_ResamplingMethods
from .C_ModelEvaluation.index import ModelEvaluation as C_ModelEvaluation
from .D_PipelinesStreamlining.index import PipelinesStreamlining as D_PipelinesStreamlining
from .E_ModelTuning.index import ModelTuning as E_ModelTuning

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 24
# 
# 
# 
# More Supervised Machine
# Learning Techniques
# with Scikit-learn
# This chapter will cover using Scikit-learn to implement machine learning models using
# techniques such as
# 
#        •    Feature engineering
# 
#        •    Resampling methods
# 
#        •    Model evaluation methods
# 
#        •    Pipelines for streamlining machine learning workflows
# 
#        •    Techniques for model tuning

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 24: More Supervised Machine Learning Techniques with Scikit-learn",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Chapter 24: More Supervised Machine Learning Techniques with Scikit-learn"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter24(HierNode):
    def __init__(self):
        super().__init__("Chapter 24: More Supervised Machine Learning Techniques with Scikit-learn")
        self.add(Content())
        self.add(A_FeatureEngineering())
        self.add(B_ResamplingMethods())
        self.add(C_ModelEvaluation())
        self.add(D_PipelinesStreamlining())
        self.add(E_ModelTuning())

# eof
