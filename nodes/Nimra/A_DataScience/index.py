# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
# from pathlib import Path
# import imp

# from lm.common.util.PrintAligner import PrintAligner as pa
# from lm.common.util.Utils import Utils

# from modules.node.HierNode import HierNode
# from modules.node.LeafNode import LeafNode
# from modules.node.Stage import Stage
# from modules.node.block.CodeBlock import CodeBlock as cbk
# from modules.node.block.ImageBlock import ImageBlock as ibk
# from modules.node.block.MarkdownBlock import MarkdownBlock as mbk
from modules.nodes.Nimra.ModuleNode import ModuleNode

from .A_BasicTools.index import BasicTools
from .B_Concepts.index import Concepts

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class DataScience(HierNode):
class DataScience(ModuleNode):
    def __init__(self):
        super().__init__("Data Science")
        self.add(BasicTools())
        self.add(Concepts())

# eof