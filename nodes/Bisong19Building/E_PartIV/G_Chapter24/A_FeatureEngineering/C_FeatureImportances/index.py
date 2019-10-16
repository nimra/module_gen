# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Feature Importances
# Tree-based or ensemble methods in Scikit-learn have a feature_importances_ attribute
# which can be used to drop irrelevant features in the dataset using the SelectFromModel
# module contained in the sklearn.feature_selection package.
#    Let’s used the ensemble method AdaBoostClassifier in this example.
# 
# # import packages
# from sklearn.ensemble import AdaBoostClassifier
# from sklearn.feature_selection import SelectFromModel
# from sklearn import datasets
# 
# # load dataset
# data = datasets.load_iris()
# 
# # separate features and target
# X = data.data
# y = data.target
# 
# # original data shape
# X.shape
# 
# # feature engineering
# ada_boost_classifier = AdaBoostClassifier()
# ada_boost_classifier.fit(X, y)
# 
# 'Output':
# AdaBoostClassifier(algorithm='SAMME.R', base_estimator=None,
#           learning_rate=1.0, n_estimators=50, random_state=None)
# 
# # print the feature importances
# ada_boost_classifier.feature_importances_
# 'Output': array([0.  , 0.  , 0.58, 0.42])
# 
# # create a subset of data based on the relevant features
# model = SelectFromModel(ada_boost_classifier, prefit=True)
# new_data = model.transform(X)
# 
# # the irrelevant features have been removed
# new_data.shape
# 'Output': (150, 2)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Feature Importances",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Feature Importances"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class FeatureImportances(HierNode):
    def __init__(self):
        super().__init__("Feature Importances")
        self.add(Content())

# eof
