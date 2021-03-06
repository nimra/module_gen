# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from lm.common.object.Object import Object

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Path(Object):

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, *nodes):
        super().__init__()
        self.nodes = list(nodes)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def xstr(self):
        return "len %d; '%s'" % (
            len(self.nodes),
            "/".join([a.getPathname() for a in self.nodes]),
        )
    def xprint(self):
        Utils.todo("dot.   :)")

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getLeaf(self):
        return self.nodes[-1]

    def pushLeaf(self, node):
        return Path(*self.nodes, node)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# eof
