# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.nodes.Nimra.ChapterNode import ChapterNode
# from modules.nodes.Nimra.MetaChapterNode import MetaChapterNode

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Clustering(ChapterNode):
    def __init__(self):
        super().__init__("Clustering")
        # self.add(KMeans())
        # self.add(Hierarchical())
        # self.add(GaussianMixtureModel())
        # self.add(HiddenMarkovModel())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DimensionalityReduction(ChapterNode):
    def __init__(self):
        super().__init__("Dimensionality Reduction")
        # self.add(SingularValueDecomposition())
        # self.add(PrincipleComponentAnalysis())
        # self.add(LinearDiscriminantAnalysis())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Unsupervised(ChapterNode):
    def __init__(self):
        super().__init__("Unsupervised")
        self.add(Clustering())
        self.add(DimensionalityReduction())

# eof
