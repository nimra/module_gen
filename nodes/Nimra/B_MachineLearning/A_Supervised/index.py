# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.nodes.Nimra.ChapterNode import ChapterNode
# from modules.nodes.Nimra.MetaChapterNode import MetaChapterNode

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from lm.common.util.PrintAligner import PrintAligner as pa
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.HierBlock import HierBlock as hbk
from modules.node.block.ListBlock import ListBlock as lbk
from modules.nodes.VanderPlas17Python.index import VanderPlas17Python
class LinearRegression(HierNode):
    def __init__(self):
        # super().__init__("Linear Regression")
        super().__init__("LinReg")

        vanderplas = VanderPlas17Python()
        lin_reg = vanderplas["Chapter 5. Machine Learning"]["In Depth: Linear Regression"]
        lin_reg["SimpleLinear"]["content"].prepend(hbk("Assigned Reading", [
            lbk([
                "**Geron**: Chapter 4",
                "**Bisong**: Chapter 19",
            ]),
        ]))
        for n in ["BasisFunction", "Regularization", "ExamplePredicting"]:
            lin_reg[n]["content"].prepend(hbk("Assigned Reading", [
                lbk([
                    "**Author #1**: Chapter/Section #1",
                    "**Author #2**: Chapter/Section #2",
                    "**Author #3**: Chapter/Section #3",
                ]),
            ]))

        [self.add(a) for a in lin_reg.children]
        # [self.add(a) for a in lin_reg.getBlocks()]

        # pa().addx("vanderplas", vanderplas).ppprint()
        # pa().addx("lin_reg", lin_reg).ppprint()
        # pa().addx("lin_reg.blocks", lin_reg.getBlocks()).ppprint()

        # pa().addx("*node", self).ppprint()

from modules.nodes.Geron17Hands.index import Geron17Hands
class DecisionTree(HierNode):
    def __init__(self):
        # super().__init__("Decision Tree")
        super().__init__("DTree")

        geron_dt = Geron17Hands()["PartI"]["Chapter 6. Decision Trees"]
        # [a["content"].prepend(hbk("Assigned Reading", [
        #     lbk([
        #         "**Author #1**: Chapter/Section #1",
        #         "**Author #2**: Chapter/Section #2",
        #         "**Author #3**: Chapter/Section #3",
        #     ]),
        # ])) for a in geron_dt.children]

        [self.add(a) for a in geron_dt.children]

        # pa().addx("geron_dt", geron_dt).ppprint()

from modules.nodes.Nimra.ChapterNode import ChapterNode
class Regression(ChapterNode):
    def __init__(self):
        super().__init__("Regression")
        self.add(LinearRegression())
        self.add(DecisionTree())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from modules.nodes.Muller17Introduction.index import Muller17Introduction
class KNearestNeighbor(HierNode):
    def __init__(self):
        super().__init__("kNN")
        muller_knn = Muller17Introduction()["Chapter 2. Supervised Learning"]["Supervised Machine Learning Algorithms"]["k-Nearest Neighbors"]
        # pa().addx("muller_knn", muller_knn).ppprint()
        [self.add(a) for a in muller_knn.children]

from modules.nodes.Bisong19Building.index import Bisong19Building
class LogisticRegression(HierNode):
    def __init__(self):
        super().__init__("LogReg")
        bisong_lr = Bisong19Building()["PartIV"]["Chapter20"]
        # pa().addx("bisong_lr", bisong_lr).ppprint()
        [self.add(a) for a in bisong_lr.children]

class Classification(ChapterNode):
    def __init__(self):
        super().__init__("Classification")
        self.add(KNearestNeighbor())
        self.add(LogisticRegression())
        # self.add(NaiveBayes())
        # self.add(SupportVectorMachine())
        # self.add(DecisionTree())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Ensemble(ChapterNode):
    def __init__(self):
        super().__init__("Ensemble")
        # self.add(RandomForest())
        # self.add(Boosting())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class Supervised(HierNode):
# class Supervised(MetaChapterNode):
class Supervised(ChapterNode):
    def __init__(self):
        super().__init__("Supervised")
        self.add(Regression())
        self.add(Classification())
        self.add(Ensemble())

# eof
