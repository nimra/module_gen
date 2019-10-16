# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from enum import Enum

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Stage(Enum):

    REMOVE_EXTRANEOUS = 0
    ORIG_BLOCKS       = 1
    CUSTOM_BLOCKS     = 2
    ORIG_FIGURES      = 3
    CUSTOM_FIGURES    = 4
    EXERCISES         = 5

# eof
