# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.LeafNode import LeafNode
from modules.node.block.CodeBlock import CodeBlock

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
load_imports_code = CodeBlock(
    "Load imports.",
    """
# load library
from sklearn import datasets
import numpy as np
    """,
)

load_iris_code = CodeBlock(
    "Load Iris dataset.",
    """
# load iris
iris = datasets.load_iris()
iris.data.shape

'Output': (150, 4)

iris.feature_names

'Output':
['sepal length (cm)',
'sepal width (cm)',
'petal length (cm)',
'petal width (cm)']
    """,
)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LoadSampleDataNode(LeafNode):
    def __init__(self):
        super().__init__("Loading Sample Datasets from Scikit-learn")
        self.add(load_imports_code)
        self.add(load_iris_code)

# eof
