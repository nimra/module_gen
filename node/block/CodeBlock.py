# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
import nbformat as nbf

from .HierBlock import HierBlock
from .TextBlock import TextBlock

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .LeafBlock import LeafBlock
class _CodeBlock(LeafBlock):
    def toNbf(self):
        return [nbf.v4.new_code_cell(self.text)]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class CodeBlock(HierBlock):
    def __init__(self, text, code):
        super().__init__()
        self.add(TextBlock(text))
        self.add(_CodeBlock(code))

# eof
