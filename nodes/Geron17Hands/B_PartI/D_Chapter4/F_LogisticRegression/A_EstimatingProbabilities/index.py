# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
#                 Download from finelybook www.finelybook.com
#    Equation 4-14. Logistic function
#                 1
#    σt =
#           1 + exp − t
# 
# 
# 
# 
# Figure 4-21. Logistic function
# 
# Once the Logistic Regression model has estimated the probability p = hθ(x) that an
# instance x belongs to the positive class, it can make its prediction ŷ easily (see Equa‐
# tion 4-15).
# 
#    Equation 4-15. Logistic Regression model prediction
#         0 if p < 0 . 5,
#    y=
#         1 if p ≥ 0 . 5 .
# 
# Notice that σ(t) < 0.5 when t < 0, and σ(t) ≥ 0.5 when t ≥ 0, so a Logistic Regression
# model predicts 1 if θT · x is positive, and 0 if it is negative.
# 
# Training and Cost Function
# Good, now you know how a Logistic Regression model estimates probabilities and
# makes predictions. But how is it trained? The objective of training is to set the param‐
# eter vector θ so that the model estimates high probabilities for positive instances (y =
# 1) and low probabilities for negative instances (y = 0). This idea is captured by the
# cost function shown in Equation 4-16 for a single training instance x.
# 
#    Equation 4-16. Cost function of a single training instance
#            − log p         if y = 1,
#    cθ =
#            − log 1 − p if y = 0 .
# 
# This cost function makes sense because – log(t) grows very large when t approaches
# 0, so the cost will be large if the model estimates a probability close to 0 for a positive
# 
# 
#                                                                     Logistic Regression   |   135
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Estimating Probabilities",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Estimating Probabilities"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class EstimatingProbabilities(HierNode):
    def __init__(self):
        super().__init__("Estimating Probabilities")
        self.add(Content())

# eof
