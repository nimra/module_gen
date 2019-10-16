# Lawrence McAfee

# git remote add origin https://github.com/nimra/modules.git
# git push -u origin master

# ~~~~~~~~ import ~~~~~~~~
import os
import sys
COMMON_PYTHON_PATH = os.environ["COMMON_PYTHON_PATH"]
sys.path.insert(0, COMMON_PYTHON_PATH)

from lm.common.object.Object import Object
from lm.common.util.PrintAligner import PrintAligner as pa
from lm.common.util.Types import Types
from lm.common.util.Utils import Utils

from .node.LeafNode import LeafNode
from .node.Path import Path
from .node.Stage import Stage
from .nodes.BisongBook.index import BisongBook

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Main:

    @classmethod
    def listUncroppedText(cls, node):

        # ~~~~~~~~ paths ~~~~~~~~
        leaf_paths = list(filter(
            lambda a : Types.isType(a.getLeaf(), LeafNode),
            node.getPaths(Path()),
        ))
        uncropped_paths = list(filter(
            # lambda a : not a.getLeaf().containsStage(Stage.REMOVE_EXTRANEOUS),
            lambda a : not a.getLeaf().containsStage(Stage.ORIG_BLOCKS),
            leaf_paths,
        ))
        # leaf_nodes = [a.getLeaf() for a in leaf_paths]
        # uncropped_nodes = list(filter(
        #     lambda a : not a.containsStage(Stage.CROP_TEXT),
        #     leaf_nodes,
        # ))

        pa().addx("uncropped_paths", uncropped_paths[:10]).pprint()
        pa().add(
            "leaf_paths", leaf_paths,
            "uncropped_paths", uncropped_paths,
        ).ppprint()



    @classmethod
    def run(cls):

        root_node = BisongBook()

        # ~~~~~~~~ create jupyter notebooks ~~~~~~~~
        root_node.toNbf("/home/lcmcafee/Dropbox/Code/nimra/data/modules", None)

        # ~~~~~~~~ list uncropped text ~~~~~~~~
        cls.listUncroppedText(root_node)

        # pa().addx("root_node", root_node).ppprint()
        Utils.todo("dot.   :)")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":

    Main.run()

    Utils.todo("dot.   :)")

# eof
