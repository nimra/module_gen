# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
import os
import shutil

from lm.common.util.PrintAligner import PrintAligner as pa
from lm.common.util.Types import Types
from lm.common.util.Utils import Utils

from .BaseNode import BaseNode

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class HierNode(BaseNode):

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, title):
        super().__init__(title)
        self.children = []

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def xstr(self):
        return "child %d; %s" % (len(self.children), super().xstr())
    def xprint(self):
        return super().xprint().addx("children", self.children)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def add(self, child):
        self.children.append(Types.assertType(child, BaseNode))

    def getPaths(self, crnt_path):

        # ~~~~~~~~ update path ~~~~~~~~
        crnt_path = crnt_path.pushLeaf(self)

        # ~~~~~~~~ add paths ~~~~~~~~
        paths = [crnt_path]
        [paths.extend(a.getPaths(crnt_path)) for a in self.children]

        # # ~~~~~~~~ debug ~~~~~~~~
        # pa().addx("paths", paths).ppprint()

        # ~~~~~~~~ return ~~~~~~~~
        return paths

    def toNbf(self, top_dirname, sub_prefix_index):

        # ~~~~~~~~ verify top dir ~~~~~~~~
        if not os.path.isdir(top_dirname):
            Utils.todo("Directory not found.")

        # ~~~~~~~~ remove/create sub dir ~~~~~~~~
        # Utils.todo("sub_prefix before top_dirname?")
        # sub_dirname = os.path.join(
        #     sub_prefix,
        #     top_dirname,
        #     self.getTitlePathname(),
        # )
        sub_dirname = os.path.join(
            top_dirname,
            self.getPrefixname(sub_prefix_index),
        )
        # if sub_prefix_index is not None:
        #     pa().add(
        #         "sub_prefix_index", sub_prefix_index,
        #         "top_dirname", top_dirname,
        #         "sub_dirname", sub_dirname,
        #     ).ppprint()
        shutil.rmtree(sub_dirname, True)
        os.mkdir(sub_dirname)

        print("processing '%s'" % sub_dirname)

        # ~~~~~~~~ children ~~~~~~~~
        [a.toNbf(sub_dirname, i) for i, a in enumerate(self.children)]

        # # ~~~~~~~~ debug ~~~~~~~~
        # pa().add(
        #     "top_dirname", top_dirname,
        #     "sub_dirname", sub_dirname,
        # ).ppprint()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# eof
