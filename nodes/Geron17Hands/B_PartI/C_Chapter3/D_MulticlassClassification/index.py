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
#                   Download from finelybook www.finelybook.com
# Now you are ready to plot the ROC curve. It is useful to plot the first ROC curve as
# well to see how they compare (Figure 3-7):
#     plt.plot(fpr, tpr, "b:", label="SGD")
#     plot_roc_curve(fpr_forest, tpr_forest, "Random Forest")
#     plt.legend(loc="bottom right")
#     plt.show()
# 
# 
# 
# 
# Figure 3-7. Comparing ROC curves
# 
# As you can see in Figure 3-7, the RandomForestClassifier’s ROC curve looks much
# better than the SGDClassifier’s: it comes much closer to the top-left corner. As a
# result, its ROC AUC score is also significantly better:
#     >>> roc_auc_score(y_train_5, y_scores_forest)
#     0.99312433660038291
# Try measuring the precision and recall scores: you should find 98.5% precision and
# 82.8% recall. Not too bad!
# Hopefully you now know how to train binary classifiers, choose the appropriate met‐
# ric for your task, evaluate your classifiers using cross-validation, select the precision/
# recall tradeoff that fits your needs, and compare various models using ROC curves
# and ROC AUC scores. Now let’s try to detect more than just the 5s.
# 
# Multiclass Classification
# Whereas binary classifiers distinguish between two classes, multiclass classifiers (also
# called multinomial classifiers) can distinguish between more than two classes.
# 
# 
# 
#                                                                  Multiclass Classification   |   93
# 
#                    Download from finelybook www.finelybook.com
# Some algorithms (such as Random Forest classifiers or naive Bayes classifiers) are
# capable of handling multiple classes directly. Others (such as Support Vector Machine
# classifiers or Linear classifiers) are strictly binary classifiers. However, there are vari‐
# ous strategies that you can use to perform multiclass classification using multiple
# binary classifiers.
# For example, one way to create a system that can classify the digit images into 10
# classes (from 0 to 9) is to train 10 binary classifiers, one for each digit (a 0-detector, a
# 1-detector, a 2-detector, and so on). Then when you want to classify an image, you get
# the decision score from each classifier for that image and you select the class whose
# classifier outputs the highest score. This is called the one-versus-all (OvA) strategy
# (also called one-versus-the-rest).
# Another strategy is to train a binary classifier for every pair of digits: one to distin‐
# guish 0s and 1s, another to distinguish 0s and 2s, another for 1s and 2s, and so on.
# This is called the one-versus-one (OvO) strategy. If there are N classes, you need to
# train N × (N – 1) / 2 classifiers. For the MNIST problem, this means training 45
# binary classifiers! When you want to classify an image, you have to run the image
# through all 45 classifiers and see which class wins the most duels. The main advan‐
# tage of OvO is that each classifier only needs to be trained on the part of the training
# set for the two classes that it must distinguish.
# Some algorithms (such as Support Vector Machine classifiers) scale poorly with the
# size of the training set, so for these algorithms OvO is preferred since it is faster to
# train many classifiers on small training sets than training few classifiers on large
# training sets. For most binary classification algorithms, however, OvA is preferred.
# Scikit-Learn detects when you try to use a binary classification algorithm for a multi‐
# class classification task, and it automatically runs OvA (except for SVM classifiers for
# which it uses OvO). Let’s try this with the SGDClassifier:
#      >>> sgd_clf.fit(X_train, y_train)    # y_train, not y_train_5
#      >>> sgd_clf.predict([some_digit])
#      array([ 5.])
# 
# That was easy! This code trains the SGDClassifier on the training set using the origi‐
# nal target classes from 0 to 9 (y_train), instead of the 5-versus-all target classes
# (y_train_5). Then it makes a prediction (a correct one in this case). Under the hood,
# Scikit-Learn actually trained 10 binary classifiers, got their decision scores for the
# image, and selected the class with the highest score.
# To see that this is indeed the case, you can call the decision_function() method.
# Instead of returning just one score per instance, it now returns 10 scores, one per
# class:
#      >>> some_digit_scores = sgd_clf.decision_function([some_digit])
#      >>> some_digit_scores
# 
# 
# 
# 94   |   Chapter 3: Classification
# 
#                   Download from finelybook www.finelybook.com
#     array([[-311402.62954431, -363517.28355739, -446449.5306454 ,
#             -183226.61023518, -414337.15339485, 161855.74572176,
#             -452576.39616343, -471957.14962573, -518542.33997148,
#             -536774.63961222]])
# The highest score is indeed the one corresponding to class 5:
#     >>> np.argmax(some_digit_scores)
#     5
#     >>> sgd_clf.classes_
#     array([ 0., 1., 2., 3., 4., 5.,             6.,   7.,   8.,   9.])
#     >>> sgd_clf.classes[5]
#     5.0
# 
#                 When a classifier is trained, it stores the list of target classes in its
#                 classes_ attribute, ordered by value. In this case, the index of each
#                 class in the classes_ array conveniently matches the class itself
#                 (e.g., the class at index 5 happens to be class 5), but in general you
#                 won’t be so lucky.
# 
# If you want to force ScikitLearn to use one-versus-one or one-versus-all, you can use
# the OneVsOneClassifier or OneVsRestClassifier classes. Simply create an instance
# and pass a binary classifier to its constructor. For example, this code creates a multi‐
# class classifier using the OvO strategy, based on a SGDClassifier:
#     >>> from sklearn.multiclass import OneVsOneClassifier
#     >>> ovo_clf = OneVsOneClassifier(SGDClassifier(random_state=42))
#     >>> ovo_clf.fit(X_train, y_train)
#     >>> ovo_clf.predict([some_digit])
#     array([ 5.])
#     >>> len(ovo_clf.estimators_)
#     45
# 
# Training a RandomForestClassifier is just as easy:
#     >>> forest_clf.fit(X_train, y_train)
#     >>> forest_clf.predict([some_digit])
#     array([ 5.])
# This time Scikit-Learn did not have to run OvA or OvO because Random Forest
# classifiers can directly classify instances into multiple classes. You can call
# predict_proba() to get the list of probabilities that the classifier assigned to each
# instance for each class:
#     >>> forest_clf.predict_proba([some_digit])
#     array([[ 0.1, 0. , 0. , 0.1, 0. , 0.8,              0. ,   0. ,   0. ,      0. ]])
# You can see that the classifier is fairly confident about its prediction: the 0.8 at the 5th
# index in the array means that the model estimates an 80% probability that the image
# 
# 
# 
# 
#                                                                          Multiclass Classification   |   95
# 
#                   Download from finelybook www.finelybook.com
# represents a 5. It also thinks that the image could instead be a 0 or a 3 (10% chance
# each).
# Now of course you want to evaluate these classifiers. As usual, you want to use cross-
# validation. Let’s evaluate the SGDClassifier’s accuracy using the cross_val_score()
# function:
#      >>> cross_val_score(sgd_clf, X_train, y_train, cv=3, scoring="accuracy")
#      array([ 0.84063187, 0.84899245, 0.86652998])
# It gets over 84% on all test folds. If you used a random classifier, you would get 10%
# accuracy, so this is not such a bad score, but you can still do much better. For exam‐
# ple, simply scaling the inputs (as discussed in Chapter 2) increases accuracy above
# 90%:
#      >>> from sklearn.preprocessing import StandardScaler
#      >>> scaler = StandardScaler()
#      >>> X_train_scaled = scaler.fit_transform(X_train.astype(np.float64))
#      >>> cross_val_score(sgd_clf, X_train_scaled, y_train, cv=3, scoring="accuracy")
#      array([ 0.91011798, 0.90874544, 0.906636 ])
# 
# 
# Error Analysis
# Of course, if this were a real project, you would follow the steps in your Machine
# Learning project checklist (see Appendix B): exploring data preparation options, try‐
# ing out multiple models, shortlisting the best ones and fine-tuning their hyperpara‐
# meters using GridSearchCV, and automating as much as possible, as you did in the
# previous chapter. Here, we will assume that you have found a promising model and
# you want to find ways to improve it. One way to do this is to analyze the types of
# errors it makes.
# First, you can look at the confusion matrix. You need to make predictions using the
# cross_val_predict() function, then call the confusion_matrix() function, just like
# you did earlier:
#      >>> y_train_pred = cross_val_predict(sgd_clf, X_train_scaled, y_train, cv=3)
#      >>> conf_mx = confusion_matrix(y_train, y_train_pred)
#      >>> conf_mx
#      array([[5725,     3,   24,   9,   10,   49,   50,   10,   39,    4],
#             [    2, 6493,   43,  25,    7,   40,    5,   10, 109,     8],
#             [ 51,     41, 5321, 104,   89,   26,   87,   60, 166,    13],
#             [ 47,     46, 141, 5342,    1, 231,    40,   50, 141,    92],
#             [ 19,     29,   41,  10, 5366,    9,   56,   37,   86, 189],
#             [ 73,     45,   36, 193,   64, 4582, 111,    30, 193,    94],
#             [ 29,     34,   44,   2,   42,   85, 5627,   10,   45,    0],
#             [ 25,     24,   74,  32,   54,   12,    6, 5787,   15, 236],
#             [ 52, 161,      73, 156,   10, 163,    61,   25, 5027, 123],
#             [ 43,     35,   26,  92, 178,    28,    2, 223,    82, 5240]])
# 
# 
# 
# 
# 96   |   Chapter 3: Classification
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Multiclass Classification",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MulticlassClassification(HierNode):
    def __init__(self):
        super().__init__("Multiclass Classification")
        self.add(Content(), "content")

# eof
