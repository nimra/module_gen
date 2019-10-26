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

from .A_WhatIs.index import WhatIs as A_WhatIs
from .B_IntroducingScikitLearn.index import IntroducingScikitLearn as B_IntroducingScikitLearn
from .C_Hyperparametersand.index import Hyperparametersand as C_Hyperparametersand
from .D_FeatureEngineering.index import FeatureEngineering as D_FeatureEngineering
from .E_InDepth.index import InDepth as E_InDepth
from .F_InDepth.index import InDepth as F_InDepth
from .G_InDepthSupport.index import InDepthSupport as G_InDepthSupport
from .H_InDepthDecision.index import InDepthDecision as H_InDepthDecision
from .I_InDepth.index import InDepth as I_InDepth
from .J_InDepthManifold.index import InDepthManifold as J_InDepthManifold
from .K_InDepth.index import InDepth as K_InDepth
from .L_InDepth.index import InDepth as L_InDepth
from .M_InDepthKernel.index import InDepthKernel as M_InDepthKernel
from .N_ApplicationA.index import ApplicationA as N_ApplicationA
from .O_FurtherMachine.index import FurtherMachine as O_FurtherMachine

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# In many ways, machine learning is the primary means by which data science mani‐
# fests itself to the broader world. Machine learning is where these computational and
# algorithmic skills of data science meet the statistical thinking of data science, and the
# result is a collection of approaches to inference and data exploration that are not
# about effective theory so much as effective computation.
# The term “machine learning” is sometimes thrown around as if it is some kind of
# magic pill: apply machine learning to your data, and all your problems will be solved!
# As you might expect, the reality is rarely this simple. While these methods can be
# incredibly powerful, to be effective they must be approached with a firm grasp of the
# strengths and weaknesses of each method, as well as a grasp of general concepts such
# as bias and variance, overfitting and underfitting, and more.
# This chapter will dive into practical aspects of machine learning, primarily using
# Python’s Scikit-Learn package. This is not meant to be a comprehensive introduction
# to the field of machine learning; that is a large subject and necessitates a more techni‐
# cal approach than we take here. Nor is it meant to be a comprehensive manual for the
# use of the Scikit-Learn package (for this, see “Further Machine Learning Resources”
# on page 514). Rather, the goals of this chapter are:
# 
#   • To introduce the fundamental vocabulary and concepts of machine learning.
#   • To introduce the Scikit-Learn API and show some examples of its use.
#   • To take a deeper dive into the details of several of the most important machine
#     learning approaches, and develop an intuition into how they work and when and
#     where they are applicable.
# 
# Much of this material is drawn from the Scikit-Learn tutorials and workshops I have
# given on several occasions at PyCon, SciPy, PyData, and other conferences. Any
# clarity in the following pages is likely due to the many workshop participants and co-
# instructors who have given me valuable feedback on this material over the years!
# Finally, if you are seeking a more comprehensive or technical treatment of any of
# these subjects, I’ve listed several resources and references in “Further Machine Learn‐
# ing Resources” on page 514.
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 5. Machine Learning",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter5(HierNode):
    def __init__(self):
        super().__init__("Chapter 5. Machine Learning")
        self.add(Content())
        # self.add(A_WhatIs())                 # What Is Machine Learning?
        # self.add(B_IntroducingScikitLearn()) # Introducing Scikit-Learn
        # self.add(C_Hyperparametersand())     # Hyperparameters and Model Validation
        # self.add(D_FeatureEngineering())     # Feature Engineering
        # self.add(E_InDepth())                # In Depth: Naive Bayes Classification
        self.add(F_InDepth())                  # In Depth: Linear Regression
        # self.add(G_InDepthSupport())         # In-Depth: Support Vector Machines
        # self.add(H_InDepthDecision())        # In-Depth: Decision Trees and Random Forests
        # self.add(I_InDepth())                # In Depth: Principal Component Analysis
        # self.add(J_InDepthManifold())        # In-Depth: Manifold Learning
        # self.add(K_InDepth())                # In Depth: k-Means Clustering
        # self.add(L_InDepth())                # In Depth: Gaussian Mixture Models
        # self.add(M_InDepthKernel())          # In-Depth: Kernel Density Estimation
        # self.add(N_ApplicationA())           # Application: A Face Detection Pipeline
        # self.add(O_FurtherMachine())         # Further Machine Learning Resources

# eof
