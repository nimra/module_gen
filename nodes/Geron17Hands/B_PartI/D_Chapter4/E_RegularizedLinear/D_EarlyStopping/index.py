# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                  Download from finelybook www.finelybook.com
# Early Stopping
# A very different way to regularize iterative learning algorithms such as Gradient
# Descent is to stop training as soon as the validation error reaches a minimum. This is
# called early stopping. Figure 4-20 shows a complex model (in this case a high-degree
# Polynomial Regression model) being trained using Batch Gradient Descent. As the
# epochs go by, the algorithm learns and its prediction error (RMSE) on the training set
# naturally goes down, and so does its prediction error on the validation set. However,
# after a while the validation error stops decreasing and actually starts to go back up.
# This indicates that the model has started to overfit the training data. With early stop‐
# ping you just stop training as soon as the validation error reaches the minimum. It is
# such a simple and efficient regularization technique that Geoffrey Hinton called it a
# “beautiful free lunch.”
# 
# 
# 
# 
# Figure 4-20. Early stopping regularization
# 
#                With Stochastic and Mini-batch Gradient Descent, the curves are
#                not so smooth, and it may be hard to know whether you have
#                reached the minimum or not. One solution is to stop only after the
#                validation error has been above the minimum for some time (when
#                you are confident that the model will not do any better), then roll
#                back the model parameters to the point where the validation error
#                was at a minimum.
# 
# Here is a basic implementation of early stopping:
#     from sklearn.base import clone
# 
# 
# 
# 
#                                                                Regularized Linear Models   |   133
# 
#                         Download from finelybook www.finelybook.com
#       sgd_reg = SGDRegressor(n_iter=1, warm_start=True, penalty=None,
#                              learning_rate="constant", eta0=0.0005)
# 
#       minimum_val_error = float("inf")
#       best_epoch = None
#       best_model = None
#       for epoch in range(1000):
#           sgd_reg.fit(X_train_poly_scaled, y_train) # continues where it left off
#           y_val_predict = sgd_reg.predict(X_val_poly_scaled)
#           val_error = mean_squared_error(y_val_predict, y_val)
#           if val_error < minimum_val_error:
#               minimum_val_error = val_error
#               best_epoch = epoch
#               best_model = clone(sgd_reg)
# 
# Note that with warm_start=True, when the fit() method is called, it just continues
# training where it left off instead of restarting from scratch.
# 
# Logistic Regression
# As we discussed in Chapter 1, some regression algorithms can be used for classifica‐
# tion as well (and vice versa). Logistic Regression (also called Logit Regression) is com‐
# monly used to estimate the probability that an instance belongs to a particular class
# (e.g., what is the probability that this email is spam?). If the estimated probability is
# greater than 50%, then the model predicts that the instance belongs to that class
# (called the positive class, labeled “1”), or else it predicts that it does not (i.e., it
# belongs to the negative class, labeled “0”). This makes it a binary classifier.
# 
# Estimating Probabilities
# So how does it work? Just like a Linear Regression model, a Logistic Regression
# model computes a weighted sum of the input features (plus a bias term), but instead
# of outputting the result directly like the Linear Regression model does, it outputs the
# logistic of this result (see Equation 4-13).
# 
#       Equation 4-13. Logistic Regression model estimated probability (vectorized form)
#       p = hθ � = σ θT · �
# 
# The logistic—also called the logit, noted σ(·)—is a sigmoid function (i.e., S-shaped)
# that outputs a number between 0 and 1. It is defined as shown in Equation 4-14 and
# Figure 4-21.
# 
# 
# 
# 
# 134    |   Chapter 4: Training Models
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Early Stopping",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Early Stopping"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class EarlyStopping(HierNode):
    def __init__(self):
        super().__init__("Early Stopping")
        self.add(Content())

# eof
