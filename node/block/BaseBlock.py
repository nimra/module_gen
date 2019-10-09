# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
import abc

from lm.common.object.Object import Object

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class BaseBlock(Object):
    @abc.abstractmethod
    def toNbf(self):
        pass

# eof
