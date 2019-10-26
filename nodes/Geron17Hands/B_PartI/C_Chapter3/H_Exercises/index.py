# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.HierBlock import HierBlock as hbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.ListBlock import ListBlock as lbk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                         Download from finelybook www.finelybook.com
# 
# 
# 
# 
# On the left is the noisy input image, and on the right is the clean target image. Now
# let’s train the classifier and make it clean this image:
#       knn_clf.fit(X_train_mod, y_train_mod)
#       clean_digit = knn_clf.predict([X_test_mod[some_index]])
#       plot_digit(clean_digit)
# 
# 
# 
# 
# Looks close enough to the target! This concludes our tour of classification. Hopefully
# you should now know how to select good metrics for classification tasks, pick the
# appropriate precision/recall tradeoff, compare classifiers, and more generally build
# good classification systems for a variety of tasks.
# 
# Exercises
#  1. Try to build a classifier for the MNIST dataset that achieves over 97% accuracy
#     on the test set. Hint: the KNeighborsClassifier works quite well for this task;
#     you just need to find good hyperparameter values (try a grid search on the
#     weights and n_neighbors hyperparameters).
#  2. Write a function that can shift an MNIST image in any direction (left, right, up,
#     or down) by one pixel.5 Then, for each image in the training set, create four shif‐
#     ted copies (one per direction) and add them to the training set. Finally, train your
#     best model on this expanded training set and measure its accuracy on the test set.
#     You should observe that your model performs even better now! This technique of
# 
# 
# 
# 5 You can use the shift() function from the scipy.ndimage.interpolation module. For example,
#   shift(image, [2, 1], cval=0) shifts the image 2 pixels down and 1 pixel to the right.
# 
# 
# 
# 102   |   Chapter 3: Classification
# 
#                    Download from finelybook www.finelybook.com
#     artificially growing the training set is called data augmentation or training set
#     expansion.
#  3. Tackle the Titanic dataset. A great place to start is on Kaggle.
#  4. Build a spam classifier (a more challenging exercise):
#     • Download examples of spam and ham from Apache SpamAssassin’s public
#       datasets.
#     • Unzip the datasets and familiarize yourself with the data format.
#     • Split the datasets into a training set and a test set.
#     • Write a data preparation pipeline to convert each email into a feature vector.
#       Your preparation pipeline should transform an email into a (sparse) vector
#       indicating the presence or absence of each possible word. For example, if all
#       emails only ever contain four words, “Hello,” “how,” “are,” “you,” then the email
#       “Hello you Hello Hello you” would be converted into a vector [1, 0, 0, 1]
#       (meaning [“Hello” is present, “how” is absent, “are” is absent, “you” is
#       present]), or [3, 0, 0, 2] if you prefer to count the number of occurrences of
#       each word.
#     • You may want to add hyperparameters to your preparation pipeline to control
#       whether or not to strip off email headers, convert each email to lowercase,
#       remove punctuation, replace all URLs with “URL,” replace all numbers with
#       “NUMBER,” or even perform stemming (i.e., trim off word endings; there are
#       Python libraries available to do this).
#     • Then try out several classifiers and see if you can build a great spam classifier,
#       with both high recall and high precision.
# 
# Solutions to these exercises are available in the online Jupyter notebooks at https://
# github.com/ageron/handson-ml.
# 
# 
# 
# 
#                                                                           Exercises   |   103
# 
# Download from finelybook www.finelybook.com
# 
#                  Download from finelybook www.finelybook.com
# 
# 
#                                                                          CHAPTER 4
#                                                        Training Models
# 
# 
# 
# 
# So far we have treated Machine Learning models and their training algorithms mostly
# like black boxes. If you went through some of the exercises in the previous chapters,
# you may have been surprised by how much you can get done without knowing any‐
# thing about what’s under the hood: you optimized a regression system, you improved
# a digit image classifier, and you even built a spam classifier from scratch—all this
# without knowing how they actually work. Indeed, in many situations you don’t really
# need to know the implementation details.
# However, having a good understanding of how things work can help you quickly
# home in on the appropriate model, the right training algorithm to use, and a good set
# of hyperparameters for your task. Understanding what’s under the hood will also help
# you debug issues and perform error analysis more efficiently. Lastly, most of the top‐
# ics discussed in this chapter will be essential in understanding, building, and training
# neural networks (discussed in Part II of this book).
# In this chapter, we will start by looking at the Linear Regression model, one of the
# simplest models there is. We will discuss two very different ways to train it:
# 
#   • Using a direct “closed-form” equation that directly computes the model parame‐
#     ters that best fit the model to the training set (i.e., the model parameters that
#     minimize the cost function over the training set).
#   • Using an iterative optimization approach, called Gradient Descent (GD), that
#     gradually tweaks the model parameters to minimize the cost function over the
#     training set, eventually converging to the same set of parameters as the first
#     method. We will look at a few variants of Gradient Descent that we will use again
#     and again when we study neural networks in Part II: Batch GD, Mini-batch GD,
#     and Stochastic GD.
# 
# 
# 
#                                                                                      105
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Exercises",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Exercises(HierNode):
    def __init__(self):
        super().__init__("Exercises")
        self.add(Content(), "content")

# eof
