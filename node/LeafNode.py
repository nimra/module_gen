# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
import nbformat as nbf
import os

from lm.common.util.PrintAligner import PrintAligner as pa
from lm.common.util.Types import Types

from modules.node.BaseNode import BaseNode

from .block.BaseBlock import BaseBlock

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LeafNode(BaseNode):

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, title):
        super().__init__(title)
        # self.nb = nbf.v4.create_notebookk()
        self.blocks = []

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def xstr(self):
        Utils.todo("dot.   :)")
    def xprint(self):
        Utils.todo("dot.   :)")

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def add(self, block):
        self.blocks.append(Types.assertType(block, BaseBlock))

    def toNbf(self, top_dirname, sub_prefix):

        # ~~~~~~~~ verify top dir ~~~~~~~~
        if not os.path.isdir(top_dirname):
            Utils.todo("Directory not found.")

        # ~~~~~~~~ remove existing file ~~~~~~~~
        sub_filename = os.path.join(
            top_dirname,
            "%s_%s.ipynb" % (sub_prefix, self.getTitlePathname()),
        )
        # os.remove(sub_filename)
        # os.mkdir(sub_dirname)

        # ~~~~~~~~ write nb ~~~~~~~~
        nb = nbf.v4.new_notebook()
        [nb["cells"].extend(a.toNbf()) for a in self.blocks]
        nbf.write(nb, sub_filename)

        # ~~~~~~~~ debug ~~~~~~~~
        pa().add(
            "top_dirname", top_dirname,
            "sub_prefix", sub_prefix,
            "sub_filename", sub_filename,
            "nb", nb,
        ).ppprint()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# eof
