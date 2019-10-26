# Lawrence McAfee








? ? ?

# ~~~~~~~~ import ~~~~~~~~
from lm.common.util.Types import Types

from modules.node.HierNode import HierNode

from .ChapterNode import ChapterNode

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MetaChapterNode(HierNode):
    def add(self, child):
        return super().add(Types.assertType(child, [
            MetaChapterNode,
            ChapterNode,
        ]))
    # def toNbf(self, top_dirname, sub_prefix_index):
    #     Utils.todo("Dot.")

# eof
