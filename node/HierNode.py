# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
import os
import shutil

from lm.common.util.PrintAligner import PrintAligner as pa
from lm.common.util.Types import Types

from .BaseNode import BaseNode

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class HierNode(BaseNode):

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, title):
        super().__init__(title)
        self.children = []

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def xstr(self):
        Utils.todo("dot.   :)")
    def xprint(self):
        Utils.todo("dot.   :)")

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def add(self, child):
        self.children.append(Types.assertType(child, BaseNode))

    def toNbf(self, top_dirname, sub_prefix):

        # ~~~~~~~~ verify top dir ~~~~~~~~
        if not os.path.isdir(top_dirname):
            Utils.todo("Directory not found.")

        # ~~~~~~~~ remove/create sub dir ~~~~~~~~
        sub_dirname = os.path.join(
            sub_prefix,
            top_dirname,
            self.getTitlePathname(),
        )
        shutil.rmtree(sub_dirname, True)
        os.mkdir(sub_dirname)

        # ~~~~~~~~ children ~~~~~~~~
        [a.toNbf(sub_dirname, str(i)) for i, a in enumerate(self.children)]

        # # ~~~~~~~~ debug ~~~~~~~~
        # pa().add(
        #     "top_dirname", top_dirname,
        #     "sub_dirname", sub_dirname,
        # ).ppprint()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# eof
