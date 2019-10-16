# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
import abc
import re

from lm.common.object.Object import Object
from lm.common.util.PrintAligner import PrintAligner as pa
from lm.common.util.Types import Types

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class BaseNode(Object):

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, title):
        super().__init__()
        self.title = Types.assertType(title, str)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def xstr(self):
        return "'%s'" % self.title
    def xprint(self):
        return pa().add("title", self.title)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # def getTitlePathname(self):
    #     pattern = re.compile('[\W_]+')
    #     pathname = pattern.sub('', self.title)
    #     # pa().add(
    #     #     "title", self.title,
    #     #     "pathname", pathname,
    #     # ).ppprint()
    #     return pathname
    def getPathname(self):
        short_title = " ".join(self.title.split()[:2])
        # short_title = self.title
        pattern = re.compile('[\W_]+')
        pathname = pattern.sub('', short_title)
        # if len(self.title.split()) > 2:
        #     pa().add(
        #         "title", self.title,
        #         "short_title", short_title,
        #         "pathname", pathname,
        #     ).ppprint()
        return pathname

    def getPrefixname(self, prefix_index):
        Types.assertType(prefix_index, [int, Types.NoneType])
        return (
            self.getPathname()
            if prefix_index is None
            # else "%s_%s" % (ascii_uppercase[prefix_index], self.getPathname())
            else "%d_%s" % (prefix_index, self.getPathname())
        )

    @abc.abstractmethod
    def getPaths(self, crnt_path):
        pass
    
    @abc.abstractmethod
    def toNbf(self, top_dirname, sub_prefix):
        pass

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# eof
