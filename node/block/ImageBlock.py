# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
import base64
import nbformat as nbf
import os

from lm.common.util.PrintAligner import PrintAligner as pa
from lm.common.util.Types import Types

from .LeafBlock import LeafBlock

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ImageBlock(LeafBlock):
    def __init__(self, filename):
        super().__init__('<img src="a.png" />')
        self.filename = Types.assertType(filename, str)
    def toNbf(self):
        
        filename = os.path.join(
            "/home/lcmcafee/Dropbox/Code/nimra/data/modules/BisongBook_images",
            self.filename,
        )
        with open(filename, "rb") as f:
            # image_str = f.read().decode("utf-8")
            image_str = base64.b64encode(f.read()).decode("utf-8")

        # pa().add(
        #     "filename", filename,
        #     "image_str", image_str,
        # ).ppprint()

        # return [nbf.v4.new_markdown_cell(self.text, **{
        #     "attachments" : {
        #         "a.png" : {
        #             "image/png" : image_str,
        #         },
        #     },
        # })]
        return [nbf.v4.new_markdown_cell(self.text, attachments = {
            "a.png" : {
                "image/png" : image_str,
            },
        })]

# eof
