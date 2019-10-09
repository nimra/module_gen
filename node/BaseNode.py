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
        Utils.todo("dot.   :)")
    def xprint(self):
        Utils.todo("dot.   :)")

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getTitlePathname(self):
        pattern = re.compile('[\W_]+')
        pathname = pattern.sub('', self.title)
        # pa().add(
        #     "title", self.title,
        #     "pathname", pathname,
        # ).ppprint()
        return pathname
    
    @abc.abstractmethod
    def toNbf(self, top_dirname, sub_prefix):
        pass

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# eof
