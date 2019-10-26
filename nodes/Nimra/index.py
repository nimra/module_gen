# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
# from pathlib import Path
# import imp

# from lm.common.util.PrintAligner import PrintAligner as pa
# from lm.common.util.Utils import Utils

from modules.node.HierNode import HierNode
# from modules.node.LeafNode import LeafNode
# from modules.node.Stage import Stage
# from modules.node.block.CodeBlock import CodeBlock as cbk
# from modules.node.block.ImageBlock import ImageBlock as ibk
# from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .CurriculumNode import CurriculumNode
from .A_DataScience.index import DataScience
from .B_MachineLearning.index import MachineLearning
from .C_DeepLearningBasics.index import DeepLearningBasics
from .D_DeepLearningAdvanced.index import DeepLearningAdvanced
from .E_Performance.index import Performance

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class NimraNode(HierNode):
class NimraNode(CurriculumNode):
    def __init__(self):

        super().__init__("Nimra Curriculum")

        self.add(DataScience())
        self.add(MachineLearning())
        self.add(DeepLearningBasics())
        self.add(DeepLearningAdvanced())
        self.add(Performance())

        # # ~~~~~~~~ module filenames ~~~~~~~~
        # module_filenames = list(Path("modules/nodes/web").glob("**/index.py"))
        # module_filenames.remove(Path("modules/nodes/web/index.py"))
        # # pa().addx("index_filenames", index_filenames).ppprint()

        # # ~~~~~~~~ add nodes ~~~~~~~~
        # for module_filename in module_filenames:

        #     with open(module_filename, "rb") as f:
        #         module = imp.load_module(
        #             "leaf_node",
        #             f,
        #             "",
        #             ('.py', 'rb', imp.PY_SOURCE),
        #         )
        #         node = module.Index()

        #     # pa().add("node", node.Index()).ppprint()
        #     self.add(node)

        # # # ~~~~~~~~ debug ~~~~~~~~
        # # pa().addx("*web", self).ppprint()

# eof
