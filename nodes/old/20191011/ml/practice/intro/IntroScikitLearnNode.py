# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode

# from .IntroNode import IntroNode
from .LoadSampleDataNode import LoadSampleDataNode
from .SplitDataNode import SplitDataNode
from .PreprocessDataNode import PreprocessDataNode
# from .MLAlgosNode import MLAlgosNode

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class IntroScikitLearnNode(HierNode):
    def __init__(self):
        super().__init__("Scikit-Learn Introduction")
        # self.add(IntroNode())
        self.add(LoadSampleDataNode())
        self.add(SplitDataNode())
        self.add(PreprocessDataNode())
        # self.add(MLAlgosNode())

# eof
