# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode

from .ml.MachineLearningNode import MachineLearningNode

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class RootNode(HierNode):
    def __init__(self):
        super().__init__("Nimra Curriculum")
        # self.add(BackgroundNode())
        # self.add(IntroductionNode())
        self.add(MachineLearningNode())
        # self.add(DeepLearningNode())
        # self.add(DataScienceNode())
        # self.add(CloudNode())
        # self.add(ProjectsNode())

# eof
