# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_PipelinesUsing.index import PipelinesUsing as A_PipelinesUsing
from .B_PipelinesUsing.index import PipelinesUsing as B_PipelinesUsing

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
    mbk("The concept of pipelines in Scikit-learn is a compelling tool for chaining a bunch of operations together to form a tidy process flow of data transforms from one state to another. The operations that constitute a pipeline can be any of Scikit-learn’s transformers (i.e., modules with a fit and transform method, or a fit_transform method) or classifiers (i.e., modules with a fit and predict method, or a fit_predict method). Classifiers are also called predictors."),
    mbk("For a typical machine learning workflow, the steps taken may involve cleaning the data, feature engineering, scaling the dataset, and then fitting a model. Pipelines can be used in this case to chain these operations together into a coherent workflow. They have the advantage of providing a convenient and consistent interface for calling at once a sequence of operations."),
    mbk("These transformers or predictors are collectively called estimators in Scikit-learn terminology. In the last two paragraphs, we called them operations."),
    mbk("Another advantage of pipelines is that it safeguards against accidentally fitting a transform on the entire dataset and thereby leaking statistics influenced by the test data to the machine learning model while training. For example, if a standardizer is fitted on the whole dataset, the test set will be compromised because the test observations have contributed in estimating the mean and standard deviation for scaling the training set before fitting the model."),
    mbk("Finally, only the last step of the pipeline can be a classifier or predictor. All the stages of the pipeline must contain a transform method except the final stage, which can be a transformer or a classifier."),
    mbk("To begin using Scikit-learn pipelines, first import"),
    cbk(None, "from sklearn.pipeline import Pipeline", None),
    mbk("Let’s see some examples of working with Pipelines in Scikit-learn. In the following example, we’ll apply a scaling transform to standardize our dataset and then use a support vector classifier to train the model."),
    cbk(None, """
# import packages
from sklearn.svm import SVC
from sklearn import datasets
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler

from sklearn.pipeline import Pipeline

# load dataset
data = datasets.load_iris()

# separate features and target
X = data.data
y = data.target

# create the pipeline
estimators = [
    ('standardize' , StandardScaler()),
    ('svc', SVC())
]

# build the pipeline model
pipe = Pipeline(estimators)

# run the pipeline
kfold = KFold(n_splits=3, shuffle=True)
cv_result = cross_val_score(pipe, X, y, cv=kfold)

# evaluate the model performance
print("Accuracy: %.3f%% (%.3f%%)" % (cv_result.mean()*100.0, cv_result.
std()*100.0))
    """, """
Accuracy: 94.667% (0.943%)
    """),
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Pipelines: Streamlining Machine Learning Workflows",
            Stage.REMOVE_EXTRANEOUS,
            Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Pipelines: Streamlining Machine Learning Workflows"))
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PipelinesStreamlining(HierNode):
    def __init__(self):
        super().__init__("Pipelines: Streamlining Machine Learning Workflows")
        self.add(Content())
        self.add(A_PipelinesUsing())
        self.add(B_PipelinesUsing())

# eof
