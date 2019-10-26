# Lawrence McAfee






? ? ?

# ~~~~~~~~ import ~~~~~~~~
# from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
# from modules.node.Stage import Stage
# from modules.node.block.CodeBlock import CodeBlock as cbk
# from modules.node.block.HierBlock import HierBlock
# from modules.node.block.ImageBlock import ImageBlock as ibk
# from modules.node.block.ListBlock import ListBlock as lbk
# from modules.node.block.YoutubeBlock import YoutubeBlock as ybk

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class WebNode(LeafNode):
    def __init__(self, title, *stages):
        super().__init__(title, *stages)
        self.add("# " + title)

# eof
