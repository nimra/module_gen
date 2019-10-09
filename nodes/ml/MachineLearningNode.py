# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode

from .practice.PracticeNode import PracticeNode

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MachineLearningNode(HierNode):
    def __init__(self):
        super().__init__("Machine Learning")
        # self.add(IntroductionNode())
        self.add(PracticeNode())

# eof
