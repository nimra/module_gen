# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
import nbformat as nbf
import os

from lm.common.util.PrintAligner import PrintAligner as pa
from lm.common.util.Types import Types
from lm.common.util.Utils import Utils

from modules.node.BaseNode import BaseNode

from .Stage import Stage
from .block.BaseBlock import BaseBlock

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LeafNode(BaseNode):

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, title, *stages):
        super().__init__(title)
        # self.nb = nbf.v4.create_notebookk()
        self.blocks = []
        self.stages = [Types.assertType(a, Stage) for a in stages]

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def xstr(self):
        return "blocks %d; %s" % (len(self.blocks), super().xstr())
    def xprint(self):
        return super().xprint().addx("blocks", self.blocks)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def add(self, block):
        self.blocks.append(Types.assertType(block, BaseBlock))

    def getPaths(self, crnt_path):
        return [crnt_path.pushLeaf(self)]

    def containsStage(self, stage):
        Types.assertType(stage, Stage)
        return stage in self.stages

    def toNbf(self, top_dirname, sub_prefix_index):

        # ~~~~~~~~ verify top dir ~~~~~~~~
        if not os.path.isdir(top_dirname):
            Utils.todo("Directory not found.")

        # ~~~~~~~~ remove existing file ~~~~~~~~
        sub_filename = os.path.join(
            top_dirname,
            # "%s_%s.ipynb" % (sub_prefix, self.getTitlePathname()),
            "%s.ipynb" % self.getPrefixname(sub_prefix_index),
        )
        # os.remove(sub_filename)
        # os.mkdir(sub_dirname)

        # ~~~~~~~~ write nb ~~~~~~~~
        nb = nbf.v4.new_notebook()
        [nb["cells"].extend(a.toNbf()) for a in self.blocks]
        nbf.write(nb, sub_filename)

        # # ~~~~~~~~ debug ~~~~~~~~
        # pa().add(
        #     "top_dirname", top_dirname,
        #     "sub_prefix", sub_prefix,
        #     "sub_filename", sub_filename,
        #     "nb", nb,
        # ).ppprint()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# eof
