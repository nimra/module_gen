# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode

from .intro.IntroScikitLearnNode import IntroScikitLearnNode

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PracticeNode(HierNode):
    def __init__(self):
        super().__init__("Practice")
        self.add(IntroScikitLearnNode())
        # self.add(LinRegNode())
        # self.add(LogRegNode())
        # self.add(RegularizationNode())
        # self.add(SVMNode())
        # self.add(EnsembleNode())
        # self.add(MoreTechniquesNode())
        # self.add(ClusteringNode())
        # self.add(PCANode())

# eof
