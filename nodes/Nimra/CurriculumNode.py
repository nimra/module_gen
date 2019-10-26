# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from lm.common.util.PrintAligner import PrintAligner as pa
from lm.common.util.Types import Types

from modules.node.HierNode import HierNode

from .ModuleNode import ModuleNode

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class CurriculumNode(HierNode):
    def add(self, child):
        return super().add(Types.assertType(child, [
            ModuleNode,
        ]))
    def liftChapters(self):
        # [a.liftChapters() for a in self.children]
        # new_node = type(self)() # self.title)
        # new_node = CurriculumNode(self.title) # infinite recursion
        new_node = HierNode(self.title)
        # pa().add("new_node", new_node).ppprint()
        for child in self.children:
            [new_node.add(a) for a in child.liftChapters()]
        return [new_node]
    def toNbf(self, top_dirname, sub_prefix_index):
        new_node = self.liftChapters()[0]
        # pa().addx("new_node", new_node).ppprint()
        return new_node.toNbf(top_dirname, sub_prefix_index)

# eof