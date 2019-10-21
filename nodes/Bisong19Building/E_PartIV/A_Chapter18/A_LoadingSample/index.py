# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
    mbk("Scikit-learn comes with a set of small standard datasets for quickly testing and prototyping machine learning models. These datasets are ideal for learning purposes when starting off working with machine learning or even trying out the performance of some new model. They save a bit of the time required to identify, download, and clean up a dataset obtained from the wild. However, these datasets are small and well curated, they do not represent real-world scenarios."),

    mbk("""
Five popular sample datasets are
- Boston house-prices dataset
- Diabetes dataset
- Iris dataset
- Wisconsin breast cancer dataset
- Wine dataset

Table 18-1 summarizes the properties of these datasets.
    """),

    mbk("""
[ Caption: Table 18-1. Scikit-learn Sample Dataset Properties ]

| Dataset name | Observations | Dimensions | Features | Targets |
|--------------|--------------|------------|----------|---------|
| Boston house-prices dataset (regression) | 506 | 13 | real, positive | real 5.–50. |
| Diabetes dataset (regression) | 442 | 10 | real, -.2 < x < .2 | integer 25–346 |
| Iris dataset (classification) | 150 | 4 | real, positive | 3 classes |
| Wisconsin breast cancer dataset (classification) | 569 | 30 | real, positive | 2 classes |
| Wine dataset (classification) | 178 | 13 | real, positive | 3 classes |
    """),
    cbk("To load the sample dataset, we’ll run:", """
# load library
from sklearn import datasets
import numpy as np
    """, None),
    cbk("Load the Iris dataset:", """
# load iris
iris = datasets.load_iris()
iris.data.shape
    """, "(150, 4)"),
    cbk(None, """
iris.feature_names
    """, """
['sepal length (cm)',
 'sepal width (cm)',
 'petal length (cm)',
 'petal width (cm)']
    """),
    mbk("""
Methods for loading other datasets:

- Boston house-prices dataset – `datasets.load_boston()`
- Diabetes dataset – `datasets.load_diabetes()`
- Wisconsin breast cancer dataset – `datasets.load_breast_cancer()`
- Wine dataset – `datasets.load_wine()`
    """),
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Loading Sample Datasets from Scikit-learn",
            Stage.REMOVE_EXTRANEOUS,
            Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Loading Sample Datasets from Scikit-learn"))
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LoadingSample(HierNode):
    def __init__(self):
        super().__init__("Loading Sample Datasets from Scikit-learn")
        self.add(Content())

# eof
