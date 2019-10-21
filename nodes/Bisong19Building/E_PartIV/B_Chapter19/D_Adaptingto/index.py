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
    mbk("Although linear regression has the premise that the underlying structure of the dataset features is linear, this is, however, not the case for most datasets. It is nevertheless possible to adapt linear regression to fit or build a model for non-linear datasets. This process of adding non-linearity to linear models is called polynomial regression."),
    mbk("Polynomial regression fits a non-linear relationship to the data by adding higher-­order polynomial terms of existing data features as new features in the dataset. More of this is visualized in Figure 19-5."),
    ibk("Figure 19-5. Adding polynomial features to the dataset"),
    mbk("It is important to note that from a statistical point of view, when approximating the optimal values of the weights to minimize the model, the underlying assumption of the interactions of the parameters is linear. Non-linear regression models may tend to overfit the data, but this can be mitigated by adding regularization to the model. Here is a formal example of the polynomial regression model."),
    mbk("$$ \\hat{y} = \\theta_0 + \\theta_1 x_1 + \\theta_2 x_1^2 + \\theta_3 x_2 + \\theta_4 x_2^2 + ... + \\theta_n x_n + \\theta_n x_n^2 $$"),
    mbk("An illustration of polynomial regression is shown in Figure 19-6."),
    ibk("Figure 19-6. Fitting a non-linear model with polynomial regression"),
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Adapting to Non-linearity",
            Stage.REMOVE_EXTRANEOUS,
            Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Adapting to Non-linearity"))
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Adaptingto(HierNode):
    def __init__(self):
        super().__init__("Adapting to Non-linearity")
        self.add(Content())

# eof
