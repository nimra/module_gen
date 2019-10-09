# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode

from .LoadSampleDataNode import LoadSampleDataNode

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class IntroScikitLearnNode(HierNode):
    def __init__(self):
        super().__init__("Scikit-Learn Introduction")
        # self.add(IntroNode())
        self.add(LoadSampleDataNode())
        # self.add(SplitDataNode())
        # self.add(PreprocessDataNode())
        # self.add(MLAlgosNode())

# eof
