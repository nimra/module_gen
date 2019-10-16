# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                  Download from finelybook www.finelybook.com
# you use batch learning or online learning techniques? Before you read on, pause and
# try to answer these questions for yourself.
# Have you found the answers? Let’s see: it is clearly a typical supervised learning task
# since you are given labeled training examples (each instance comes with the expected
# output, i.e., the district’s median housing price). Moreover, it is also a typical regres‐
# sion task, since you are asked to predict a value. More specifically, this is a multivari‐
# ate regression problem since the system will use multiple features to make a prediction
# (it will use the district’s population, the median income, etc.). In the first chapter, you
# predicted life satisfaction based on just one feature, the GDP per capita, so it was a
# univariate regression problem. Finally, there is no continuous flow of data coming in
# the system, there is no particular need to adjust to changing data rapidly, and the data
# is small enough to fit in memory, so plain batch learning should do just fine.
# 
#                     If the data was huge, you could either split your batch learning
#                     work across multiple servers (using the MapReduce technique, as
#                     we will see later), or you could use an online learning technique
#                     instead.
# 
# 
# Select a Performance Measure
# Your next step is to select a performance measure. A typical performance measure for
# regression problems is the Root Mean Square Error (RMSE). It measures the standard
# deviation4 of the errors the system makes in its predictions. For example, an RMSE
# equal to 50,000 means that about 68% of the system’s predictions fall within $50,000
# of the actual value, and about 95% of the predictions fall within $100,000 of the actual
# value.5 Equation 2-1 shows the mathematical formula to compute the RMSE.
# 
#     Equation 2-1. Root Mean Square Error (RMSE)
# 
#                          1 m                       2
#                          mi∑
#                                 i
#     RMSE �, h =               h� −yi
#                            =1
# 
# 
# 
# 
# 4 The standard deviation, generally denoted σ (the Greek letter sigma), is the square root of the variance, which
#   is the average of the squared deviation from the mean.
# 5 When a feature has a bell-shaped normal distribution (also called a Gaussian distribution), which is very com‐
#   mon, the “68-95-99.7” rule applies: about 68% of the values fall within 1σ of the mean, 95% within 2σ, and
#   99.7% within 3σ.
# 
# 
# 
#                                                                                    Look at the Big Picture   |   37
# 
#                             Download from finelybook www.finelybook.com
# 
#                                                      Notations
#      This equation introduces several very common Machine Learning notations that we
#      will use throughout this book:
# 
#        • m is the number of instances in the dataset you are measuring the RMSE on.
#           — For example, if you are evaluating the RMSE on a validation set of 2,000 dis‐
#             tricts, then m = 2,000.
#        • x(i) is a vector of all the feature values (excluding the label) of the ith instance in
#          the dataset, and y(i) is its label (the desired output value for that instance).
#           — For example, if the first district in the dataset is located at longitude –118.29°,
#             latitude 33.91°, and it has 1,416 inhabitants with a median income of $38,372,
#             and the median house value is $156,400 (ignoring the other features for now),
#             then:
# 
#                               −118 . 29
#                         1      33 . 91
#                     �       =
#                                 1, 416
#                                38, 372
# 
#              and:
# 
#                     y 1 = 156, 400
# 
#        • X is a matrix containing all the feature values (excluding labels) of all instances in
#          the dataset. There is one row per instance and the ith row is equal to the transpose
#          of x(i), noted (x(i))T.6
#           — For example, if the first district is as just described, then the matrix X looks
#             like this:
# 
#                                       1 T
#                                   �
#                                       2 T
#                                   �
#                                                 −118 . 29 33 . 91 1, 416 38, 372
#                     �=                ⋮     =
#                                                    ⋮         ⋮       ⋮      ⋮
#                                   1999 T
#                               �
#                                   2000 T
#                               �
# 
# 
# 6 Recall that the transpose operator flips a column vector into a row vector (and vice versa).
# 
# 
# 
# 38    |   Chapter 2: End-to-End Machine Learning Project
# 
#                    Download from finelybook www.finelybook.com
#     • h is your system’s prediction function, also called a hypothesis. When your system
#       is given an instance’s feature vector x(i), it outputs a predicted value ŷ(i) = h(x(i))
#       for that instance (ŷ is pronounced “y-hat”).
#       — For example, if your system predicts that the median housing price in the first
#         district is $158,400, then ŷ(1) = h(x(1)) = 158,400. The prediction error for this
#         district is ŷ(1) – y(1) = 2,000.
#     • RMSE(X,h) is the cost function measured on the set of examples using your
#       hypothesis h.
# 
#  We use lowercase italic font for scalar values (such as m or y(i)) and function names
#  (such as h), lowercase bold font for vectors (such as x(i)), and uppercase bold font for
#  matrices (such as X).
# 
# 
# Even though the RMSE is generally the preferred performance measure for regression
# tasks, in some contexts you may prefer to use another function. For example, suppose
# that there are many outlier districts. In that case, you may consider using the Mean
# Absolute Error (also called the Average Absolute Deviation; see Equation 2-2):
# 
#    Equation 2-2. Mean Absolute Error
# 
#                   1 m
#                   mi∑
#                          i
#    MAE �, h =          h� −yi
#                     =1
# 
# 
# Both the RMSE and the MAE are ways to measure the distance between two vectors:
# the vector of predictions and the vector of target values. Various distance measures,
# or norms, are possible:
# 
#   • Computing the root of a sum of squares (RMSE) corresponds to the Euclidian
#     norm: it is the notion of distance you are familiar with. It is also called the ℓ2
#     norm, noted ∥ · ∥2 (or just ∥ · ∥).
#   • Computing the sum of absolutes (MAE) corresponds to the ℓ1 norm, noted ∥ · ∥1.
#     It is sometimes called the Manhattan norm because it measures the distance
#     between two points in a city if you can only travel along orthogonal city blocks.
#   • More generally, the ℓk norm of a vector v containing n elements is defined as
#                                          1
#                   k       k            k k
#     ∥ � ∥k = v0 + v1 + ⋯ + vn         . ℓ 0 just gives the cardinality of the vector (i.e.,
#     the number of elements), and ℓ∞ gives the maximum absolute value in the vector.
#   • The higher the norm index, the more it focuses on large values and neglects small
#     ones. This is why the RMSE is more sensitive to outliers than the MAE. But when
# 
# 
# 
# 
#                                                                       Look at the Big Picture   |   39
# 
#                    Download from finelybook www.finelybook.com
#      outliers are exponentially rare (like in a bell-shaped curve), the RMSE performs
#      very well and is generally preferred.
# 
# 
# Check the Assumptions
# Lastly, it is good practice to list and verify the assumptions that were made so far (by
# you or others); this can catch serious issues early on. For example, the district prices
# that your system outputs are going to be fed into a downstream Machine Learning
# system, and we assume that these prices are going to be used as such. But what if the
# downstream system actually converts the prices into categories (e.g., “cheap,”
# “medium,” or “expensive”) and then uses those categories instead of the prices them‐
# selves? In this case, getting the price perfectly right is not important at all; your sys‐
# tem just needs to get the category right. If that’s so, then the problem should have
# been framed as a classification task, not a regression task. You don’t want to find this
# out after working on a regression system for months.
# Fortunately, after talking with the team in charge of the downstream system, you are
# confident that they do indeed need the actual prices, not just categories. Great! You’re
# all set, the lights are green, and you can start coding now!
# 
# Get the Data
# It’s time to get your hands dirty. Don’t hesitate to pick up your laptop and walk
# through the following code examples in a Jupyter notebook. The full Jupyter note‐
# book is available at https://github.com/ageron/handson-ml.
# 
# Create the Workspace
# First you will need to have Python installed. It is probably already installed on your
# system. If not, you can get it at https://www.python.org/.7
# Next you need to create a workspace directory for your Machine Learning code and
# datasets. Open a terminal and type the following commands (after the $ prompts):
#      $ export ML_PATH="$HOME/ml"                   # You can change the path if you prefer
#      $ mkdir -p $ML_PATH
# You will need a number of Python modules: Jupyter, NumPy, Pandas, Matplotlib, and
# Scikit-Learn. If you already have Jupyter running with all these modules installed,
# you can safely skip to “Download the Data” on page 43. If you don’t have them yet,
# there are many ways to install them (and their dependencies). You can use your sys‐
# tem’s packaging system (e.g., apt-get on Ubuntu, or MacPorts or HomeBrew on
# 
# 
# 7 The latest version of Python 3 is recommended. Python 2.7+ should work fine too, but it is deprecated.
# 
# 
# 
# 40   |   Chapter 2: End-to-End Machine Learning Project
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Select a Performance Measure",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Select a Performance Measure"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Selecta(HierNode):
    def __init__(self):
        super().__init__("Select a Performance Measure")
        self.add(Content())

# eof
