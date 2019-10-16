# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_DataRescaling.index import DataRescaling as A_DataRescaling
from .B_Standardization.index import Standardization as B_Standardization
from .C_Normalization.index import Normalization as C_Normalization
from .D_Binarization.index import Binarization as D_Binarization
from .E_EncodingCategorical.index import EncodingCategorical as E_EncodingCategorical
from .F_InputMissing.index import InputMissing as F_InputMissing
from .G_GeneratingHigherOrder.index import GeneratingHigherOrder as G_GeneratingHigherOrder

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
    MarkdownBlock("Before a dataset is trained or fitted with a machine learning model, it necessarily undergoes some vital transformations. These transformations have a huge effect on the performance of the learning model. Transformations in Scikit-learn have a fit() and transform() method, or a fit_transform() method."),
    MarkdownBlock("Depending on the use case, the fit() method can be used to learn the parameters of the dataset, while the transform() method applies the data transform based on the learned parameters to the same dataset and also to the test or validation datasets before modeling. Also, the fit_transform() method can be used to learn and apply the transformation to the same dataset in a one-off fashion. Data transformation packages are found in the sklearn.preprocessing package."),
    MarkdownBlock("""
This section will cover some critical transformation for numeric and categorical variables. They include:",

- Data rescaling
- Standardization
- Normalization
- Binarization
- Encoding categorical variables
- Input missing data
- Generating higher-order polynomial features
        """),
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Preprocessing the Data for Model Fitting",
            Stage.REMOVE_EXTRANEOUS,
            Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Preprocessing the Data for Model Fitting"))
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Preprocessingthe(HierNode):
    def __init__(self):
        super().__init__("Preprocessing the Data for Model Fitting")
        self.add(Content())
        self.add(A_DataRescaling())
        self.add(B_Standardization())
        self.add(C_Normalization())
        self.add(D_Binarization())
        self.add(E_EncodingCategorical())
        self.add(F_InputMissing())
        self.add(G_GeneratingHigherOrder())

# eof
