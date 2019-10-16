# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                    Download from finelybook www.finelybook.com
# It is actually possible to train several different blenders this way (e.g., one using Lin‐
# ear Regression, another using Random Forest Regression, and so on): we get a whole
# layer of blenders. The trick is to split the training set into three subsets: the first one is
# used to train the first layer, the second one is used to create the training set used to
# train the second layer (using predictions made by the predictors of the first layer),
# and the third one is used to create the training set to train the third layer (using pre‐
# dictions made by the predictors of the second layer). Once this is done, we can make
# a prediction for a new instance by going through each layer sequentially, as shown in
# Figure 7-15.
# 
# 
# 
# 
# Figure 7-15. Predictions in a multilayer stacking ensemble
# 
# Unfortunately, Scikit-Learn does not support stacking directly, but it is not too hard
# to roll out your own implementation (see the following exercises). Alternatively, you
# can use an open source implementation such as brew (available at https://github.com/
# viisar/brew).
# 
# Exercises
#  1. If you have trained five different models on the exact same training data, and
#     they all achieve 95% precision, is there any chance that you can combine these
#     models to get better results? If so, how? If not, why?
#  2. What is the difference between hard and soft voting classifiers?
# 
# 
# 
# 202   |   Chapter 7: Ensemble Learning and Random Forests
# 
#                    Download from finelybook www.finelybook.com
#  3. Is it possible to speed up training of a bagging ensemble by distributing it across
#     multiple servers? What about pasting ensembles, boosting ensembles, random
#     forests, or stacking ensembles?
#  4. What is the benefit of out-of-bag evaluation?
#  5. What makes Extra-Trees more random than regular Random Forests? How can
#     this extra randomness help? Are Extra-Trees slower or faster than regular Ran‐
#     dom Forests?
#  6. If your AdaBoost ensemble underfits the training data, what hyperparameters
#     should you tweak and how?
#  7. If your Gradient Boosting ensemble overfits the training set, should you increase
#     or decrease the learning rate?
#  8. Load the MNIST data (introduced in Chapter 3), and split it into a training set, a
#     validation set, and a test set (e.g., use the first 40,000 instances for training, the
#     next 10,000 for validation, and the last 10,000 for testing). Then train various
#     classifiers, such as a Random Forest classifier, an Extra-Trees classifier, and an
#     SVM. Next, try to combine them into an ensemble that outperforms them all on
#     the validation set, using a soft or hard voting classifier. Once you have found one,
#     try it on the test set. How much better does it perform compared to the individ‐
#     ual classifiers?
#  9. Run the individual classifiers from the previous exercise to make predictions on
#     the validation set, and create a new training set with the resulting predictions:
#     each training instance is a vector containing the set of predictions from all your
#     classifiers for an image, and the target is the image’s class. Congratulations, you
#     have just trained a blender, and together with the classifiers they form a stacking
#     ensemble! Now let’s evaluate the ensemble on the test set. For each image in the
#     test set, make predictions with all your classifiers, then feed the predictions to the
#     blender to get the ensemble’s predictions. How does it compare to the voting clas‐
#     sifier you trained earlier?
# 
# Solutions to these exercises are available in Appendix A.
# 
# 
# 
# 
#                                                                            Exercises   |   203
# 
# Download from finelybook www.finelybook.com
# 
#                  Download from finelybook www.finelybook.com
# 
# 
#                                                                             CHAPTER 8
#                                     Dimensionality Reduction
# 
# 
# 
# 
# Many Machine Learning problems involve thousands or even millions of features for
# each training instance. Not only does this make training extremely slow, it can also
# make it much harder to find a good solution, as we will see. This problem is often
# referred to as the curse of dimensionality.
# Fortunately, in real-world problems, it is often possible to reduce the number of fea‐
# tures considerably, turning an intractable problem into a tractable one. For example,
# consider the MNIST images (introduced in Chapter 3): the pixels on the image bor‐
# ders are almost always white, so you could completely drop these pixels from the
# training set without losing much information. Figure 7-6 confirms that these pixels
# are utterly unimportant for the classification task. Moreover, two neighboring pixels
# are often highly correlated: if you merge them into a single pixel (e.g., by taking the
# mean of the two pixel intensities), you will not lose much information.
# 
#                Reducing dimensionality does lose some information (just like
#                compressing an image to JPEG can degrade its quality), so even
#                though it will speed up training, it may also make your system per‐
#                form slightly worse. It also makes your pipelines a bit more com‐
#                plex and thus harder to maintain. So you should first try to train
#                your system with the original data before considering using dimen‐
#                sionality reduction if training is too slow. In some cases, however,
#                reducing the dimensionality of the training data may filter out
#                some noise and unnecessary details and thus result in higher per‐
#                formance (but in general it won’t; it will just speed up training).
# 
# Apart from speeding up training, dimensionality reduction is also extremely useful
# for data visualization (or DataViz). Reducing the number of dimensions down to two
# 
# 
# 
#                                                                                       205
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Exercises",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Exercises"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Exercises(HierNode):
    def __init__(self):
        super().__init__("Exercises")
        self.add(Content())

# eof
