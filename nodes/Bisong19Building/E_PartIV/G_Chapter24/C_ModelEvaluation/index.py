# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.ListBlock import ListBlock as lbk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_RegressionEvaluation.index import RegressionEvaluation as A_RegressionEvaluation
from .B_ClassificationEvaluation.index import ClassificationEvaluation as B_ClassificationEvaluation

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
    mbk("This chapter has already used a couple of evaluation metrics for assessing the quality of the fitted models. In this section, we survey a couple of other metrics for regression and classification use cases and how to implement them using Scikit-learn. For each metric, we show how to use them as stand-alone implementations, as well as together with cross-validation using the cross_val_score method."),
    mbk("What we’ll cover here includes"),
    mbk("Regression evaluation metrics"),
    lbk([
        "Mean squared error (MSE): The average sum of squared difference between the predicted label, ŷ, and the true label, y. A score of 0 indicates a perfect prediction without errors.",
        "Mean absolute error (MAE): The average absolute difference between the predicted label, ŷ, and the true label, y. A score of 0 indicates a perfect prediction without errors.",
        "R2: The amount of variance or variability in the dataset explained by the model. The score of 1 means that the model perfectly captures the variability in the dataset.",
    ]),
    mbk("Classification evaluation metrics"),
    lbk([
        "Accuracy: Is the ratio of correct predictions to the total number of predictions. The bigger the accuracy, the better the model.",
        "Logarithmic loss (a.k.a logistic loss or cross-entropy loss): Is the probability that an observation is correctly assigned to a class label. By minimizing the log-loss, conversely, the accuracy is maximized. So with this metric, values closer to zero are good.",
        "Area under the ROC curve (AUC-ROC): Used in the binary classification case. Implementation is not provided, but very similar in style to the others.",
        "Confusion matrix: More intuitive in the binary classification case. Implementation is not provided, but very similar in style to the others.",
        "Classification report: It returns a text report of the main classification metrics.",
    ]),
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Model Evaluation",
            Stage.REMOVE_EXTRANEOUS,
            Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Model Evaluation"))
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ModelEvaluation(HierNode):
    def __init__(self):
        super().__init__("Model Evaluation")
        self.add(Content())
        self.add(A_RegressionEvaluation())
        self.add(B_ClassificationEvaluation())

# eof
