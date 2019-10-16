# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
#                   Download from finelybook www.finelybook.com
# instance, and it will also be very large if the model estimates a probability close to 1
# for a negative instance. On the other hand, – log(t) is close to 0 when t is close to 1, so
# the cost will be close to 0 if the estimated probability is close to 0 for a negative
# instance or close to 1 for a positive instance, which is precisely what we want.
# The cost function over the whole training set is simply the average cost over all train‐
# ing instances. It can be written in a single expression (as you can verify easily), called
# the log loss, shown in Equation 4-17.
# 
#       Equation 4-17. Logistic Regression cost function (log loss)
# 
#                   1 m
#                   mi∑
#       Jθ = −           y i log p i + 1 − y i log 1 − p i
#                     =1
# 
# 
# The bad news is that there is no known closed-form equation to compute the value of
# θ that minimizes this cost function (there is no equivalent of the Normal Equation).
# But the good news is that this cost function is convex, so Gradient Descent (or any
# other optimization algorithm) is guaranteed to find the global minimum (if the learn‐
# ing rate is not too large and you wait long enough). The partial derivatives of the cost
# function with regards to the jth model parameter θj is given by Equation 4-18.
# 
#       Equation 4-18. Logistic cost function partial derivatives
# 
#        ∂        1 m
#                 mi∑
#                              i
#            Jθ =      σ θT · � − y i x ji
#       ∂θ j        =1
# 
# 
# This equation looks very much like Equation 4-5: for each instance it computes the
# prediction error and multiplies it by the jth feature value, and then it computes the
# average over all training instances. Once you have the gradient vector containing all
# the partial derivatives you can use it in the Batch Gradient Descent algorithm. That’s
# it: you now know how to train a Logistic Regression model. For Stochastic GD you
# would of course just take one instance at a time, and for Mini-batch GD you would
# use a mini-batch at a time.
# 
# Decision Boundaries
# Let’s use the iris dataset to illustrate Logistic Regression. This is a famous dataset that
# contains the sepal and petal length and width of 150 iris flowers of three different
# species: Iris-Setosa, Iris-Versicolor, and Iris-Virginica (see Figure 4-22).
# 
# 
# 
# 
# 136    |   Chapter 4: Training Models
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Training and Cost Function",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Training and Cost Function"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Trainingand(HierNode):
    def __init__(self):
        super().__init__("Training and Cost Function")
        self.add(Content())

# eof
