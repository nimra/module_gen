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
# The ROC Curve
# The receiver operating characteristic (ROC) curve is another common tool used with
# binary classifiers. It is very similar to the precision/recall curve, but instead of plot‐
# ting precision versus recall, the ROC curve plots the true positive rate (another name
# for recall) against the false positive rate. The FPR is the ratio of negative instances that
# are incorrectly classified as positive. It is equal to one minus the true negative rate,
# which is the ratio of negative instances that are correctly classified as negative. The
# TNR is also called specificity. Hence the ROC curve plots sensitivity (recall) versus
# 1 – specificity.
# To plot the ROC curve, you first need to compute the TPR and FPR for various thres‐
# hold values, using the roc_curve() function:
#     from sklearn.metrics import roc_curve
# 
#     fpr, tpr, thresholds = roc_curve(y_train_5, y_scores)
# Then you can plot the FPR against the TPR using Matplotlib. This code produces the
# plot in Figure 3-6:
#     def plot_roc_curve(fpr, tpr, label=None):
#         plt.plot(fpr, tpr, linewidth=2, label=label)
#         plt.plot([0, 1], [0, 1], 'k--')
#         plt.axis([0, 1, 0, 1])
#         plt.xlabel('False Positive Rate')
#         plt.ylabel('True Positive Rate')
# 
#     plot_roc_curve(fpr, tpr)
#     plt.show()
# 
# 
# 
# 
# Figure 3-6. ROC curve
# 
#                                                                    Performance Measures   |   91
# 
#                   Download from finelybook www.finelybook.com
# Once again there is a tradeoff: the higher the recall (TPR), the more false positives
# (FPR) the classifier produces. The dotted line represents the ROC curve of a purely
# random classifier; a good classifier stays as far away from that line as possible (toward
# the top-left corner).
# One way to compare classifiers is to measure the area under the curve (AUC). A per‐
# fect classifier will have a ROC AUC equal to 1, whereas a purely random classifier will
# have a ROC AUC equal to 0.5. Scikit-Learn provides a function to compute the ROC
# AUC:
#      >>> from sklearn.metrics import roc_auc_score
#      >>> roc_auc_score(y_train_5, y_scores)
#      0.97061072797174941
# 
#                       Since the ROC curve is so similar to the precision/recall (or PR)
#                       curve, you may wonder how to decide which one to use. As a rule
#                       of thumb, you should prefer the PR curve whenever the positive
#                       class is rare or when you care more about the false positives than
#                       the false negatives, and the ROC curve otherwise. For example,
#                       looking at the previous ROC curve (and the ROC AUC score), you
#                       may think that the classifier is really good. But this is mostly
#                       because there are few positives (5s) compared to the negatives
#                       (non-5s). In contrast, the PR curve makes it clear that the classifier
#                       has room for improvement (the curve could be closer to the top-
#                       right corner).
# 
# Let’s train a RandomForestClassifier and compare its ROC curve and ROC AUC
# score to the SGDClassifier. First, you need to get scores for each instance in the
# training set. But due to the way it works (see Chapter 7), the RandomForestClassi
# fier class does not have a decision_function() method. Instead it has a pre
# dict_proba() method. Scikit-Learn classifiers generally have one or the other. The
# predict_proba() method returns an array containing a row per instance and a col‐
# umn per class, each containing the probability that the given instance belongs to the
# given class (e.g., 70% chance that the image represents a 5):
#      from sklearn.ensemble import RandomForestClassifier
# 
#      forest_clf = RandomForestClassifier(random_state=42)
#      y_probas_forest = cross_val_predict(forest_clf, X_train, y_train_5, cv=3,
#                                          method="predict_proba")
# But to plot a ROC curve, you need scores, not probabilities. A simple solution is to
# use the positive class’s probability as the score:
#      y_scores_forest = y_probas_forest[:, 1] # score = proba of positive class
#      fpr_forest, tpr_forest, thresholds_forest = roc_curve(y_train_5,y_scores_forest)
# 
# 
# 
# 
# 92   |   Chapter 3: Classification
# 
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
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "The ROC Curve",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TheROC(HierNode):
    def __init__(self):
        super().__init__("The ROC Curve")
        self.add(Content(), "content")

# eof
