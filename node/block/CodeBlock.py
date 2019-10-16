# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
import nbformat as nbf

from .HierBlock import HierBlock
from .MarkdownBlock import MarkdownBlock

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .LeafBlock import LeafBlock
class _CodeBlock(LeafBlock):
    def toNbf(self):
        return [nbf.v4.new_code_cell(self.text)]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class CodeBlock(HierBlock):
    def __init__(self, markdown, code, output):
        super().__init__()
        if markdown is not None:
            self.add(MarkdownBlock(markdown))
        self.add(_CodeBlock(code))
        if output is not None:
            self.add(MarkdownBlock("Output:<br>`%s`" % output))

# eof
