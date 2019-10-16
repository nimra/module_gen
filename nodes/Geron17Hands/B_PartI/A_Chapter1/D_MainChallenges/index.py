# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_InsufficientQuantity.index import InsufficientQuantity as A_InsufficientQuantity
from .B_NonrepresentativeTraining.index import NonrepresentativeTraining as B_NonrepresentativeTraining
from .C_PoorQualityData.index import PoorQualityData as C_PoorQualityData
from .D_IrrelevantFeatures.index import IrrelevantFeatures as D_IrrelevantFeatures
from .E_Overfittingthe.index import Overfittingthe as E_Overfittingthe
from .F_Underfittingthe.index import Underfittingthe as F_Underfittingthe
from .G_SteppingBack.index import SteppingBack as G_SteppingBack

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                    Download from finelybook www.finelybook.com
# If all went well, your model will make good predictions. If not, you may need to use
# more attributes (employment rate, health, air pollution, etc.), get more or better qual‐
# ity training data, or perhaps select a more powerful model (e.g., a Polynomial Regres‐
# sion model).
# In summary:
# 
#      • You studied the data.
#      • You selected a model.
#      • You trained it on the training data (i.e., the learning algorithm searched for the
#        model parameter values that minimize a cost function).
#      • Finally, you applied the model to make predictions on new cases (this is called
#        inference), hoping that this model will generalize well.
# 
# This is what a typical Machine Learning project looks like. In Chapter 2 you will
# experience this first-hand by going through an end-to-end project.
# We have covered a lot of ground so far: you now know what Machine Learning is
# really about, why it is useful, what some of the most common categories of ML sys‐
# tems are, and what a typical project workflow looks like. Now let’s look at what can go
# wrong in learning and prevent you from making accurate predictions.
# 
# Main Challenges of Machine Learning
# In short, since your main task is to select a learning algorithm and train it on some
# data, the two things that can go wrong are “bad algorithm” and “bad data.” Let’s start
# with examples of bad data.
# 
# Insufficient Quantity of Training Data
# For a toddler to learn what an apple is, all it takes is for you to point to an apple and
# say “apple” (possibly repeating this procedure a few times). Now the child is able to
# recognize apples in all sorts of colors and shapes. Genius.
# Machine Learning is not quite there yet; it takes a lot of data for most Machine Learn‐
# ing algorithms to work properly. Even for very simple problems you typically need
# thousands of examples, and for complex problems such as image or speech recogni‐
# tion you may need millions of examples (unless you can reuse parts of an existing
# model).
# 
# 
# 
# 
# 22    |   Chapter 1: The Machine Learning Landscape
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Main Challenges of Machine Learning",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Main Challenges of Machine Learning"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MainChallenges(HierNode):
    def __init__(self):
        super().__init__("Main Challenges of Machine Learning")
        self.add(Content())
        self.add(A_InsufficientQuantity())
        self.add(B_NonrepresentativeTraining())
        self.add(C_PoorQualityData())
        self.add(D_IrrelevantFeatures())
        self.add(E_Overfittingthe())
        self.add(F_Underfittingthe())
        self.add(G_SteppingBack())

# eof
