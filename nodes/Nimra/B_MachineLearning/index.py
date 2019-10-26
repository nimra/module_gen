# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.nodes.Nimra.ModuleNode import ModuleNode

from .A_Supervised.index import Supervised
from .B_Unsupervised.index import Unsupervised
from .C_Reinforcement.index import Reinforcement

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class MachineLearning(HierNode):
class MachineLearning(ModuleNode):
    def __init__(self):
        super().__init__("Machine Learning")
        self.add(Supervised())
        self.add(Unsupervised())
        self.add(Reinforcement())

# eof
