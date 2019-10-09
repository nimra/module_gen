# Lawrence McAfee

# git remote add origin https://github.com/nimra/modules.git
# git push -u origin master

# ~~~~~~~~ import ~~~~~~~~
import os
import sys
COMMON_PYTHON_PATH = os.environ["COMMON_PYTHON_PATH"]
sys.path.insert(0, COMMON_PYTHON_PATH)

import nbformat as nbf

from lm.common.object.Object import Object
from lm.common.util.PrintAligner import PrintAligner as pa
from lm.common.util.Utils import Utils

from modules.node.HierNode import HierNode
from modules.nodes.RootNode import RootNode

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Main:

    @classmethod
    def run(cls):

        # nb = nbformat.read(
        #     "/home/lcmcafee/Dropbox/Code/nimra/data/modules/test.ipynb",
        #     as_version = 4,
        # )

        root_node = RootNode()
        root_node.toNbf("/home/lcmcafee/Dropbox/Code/nimra/data/modules", "")

        text = """
# Lawrence McAfee

I was here.

I created.
        """

        code = """
# Lawrence McAfee

print("2 + 2 = " + (2 + 2))

# eof
        """

        nb = nbf.v4.new_notebook()
        nb["cells"] = [
            nbf.v4.new_markdown_cell(text),
            nbf.v4.new_code_cell(code),
        ]

        nbf.write(nb, "/home/lcmcafee/Dropbox/Code/nimra/data/modules/test.ipynb")

        pa().add("nb", nb).ppprint()

        Utils.todo("dot.   :)")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":

    Main.run()

    Utils.todo("dot.   :)")

# eof
