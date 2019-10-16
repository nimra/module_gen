# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.LeafNode import LeafNode
from modules.node.block.CodeBlock import CodeBlock

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
imports_code = CodeBlock(
    "Imports.",
    """
# import module
from sklearn.model_selection import train_test_split
    """,
)

split_code = CodeBlock(
    "Split train/test sets.",
    """
# split in train and test sets
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target,
shuffle=True)
X_train.shape
'Output': (112, 4)
X_test.shape
'Output': (38, 4)
y_train.shape
'Output': (112,)
y_test.shape
'Output': (38,)
    """,
)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class SplitDataNode(LeafNode):
    def __init__(self):
        super().__init__("Splitting the Dataset into Training and Test Sets")
        self.add(imports_code)
        self.add(split_code)

# eof
