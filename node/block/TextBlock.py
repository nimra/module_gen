# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
import nbformat as nbf

from .LeafBlock import LeafBlock

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TextBlock(LeafBlock):
    def toNbf(self):
        return [nbf.v4.new_markdown_cell(self.text)]

# eof
