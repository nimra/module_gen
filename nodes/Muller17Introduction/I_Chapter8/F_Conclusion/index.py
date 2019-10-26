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
# hosts over 20,000 datasets with over 50,000 associated machine learning tasks. Work‐
# ing with these datasets can provide a great opportunity to practice your machine
# learning skills. A disadvantage of competitions is that they already provide a particu‐
# lar metric to optimize, and usually a fixed, preprocessed dataset. Keep in mind that
# defining the problem and collecting the data are also important aspects of real-world
# problems, and that representing the problem in the right way might be much more
# important than squeezing the last percent of accuracy out of a classifier.
# 
# Conclusion
# We hope we have convinced you of the usefulness of machine learning in a wide vari‐
# ety of applications, and how easily machine learning can be implemented in practice.
# Keep digging into the data, and don’t lose sight of the larger picture.
# 
# 
# 
# 
# 366   |   Chapter 8: Wrapping Up
# 
#                                                                                    Index
# 
# 
# 
# 
# A                                                    supervised, classification
# A/B testing, 359                                         decision trees, 70-83
# accuracy, 22, 282                                        gradient boosting, 88-91, 119, 124
# acknowledgments, xi                                      k-nearest neighbors, 35-44
# adjusted rand index (ARI), 191                           kernelized support vector machines,
# agglomerative clustering                                     92-104
#    evaluating and comparing, 191                         linear SVMs, 56
#    example of, 183                                       logistic regression, 56
#    hierarchical clustering, 184                          naive Bayes, 68-70
#    linkage choices, 182                                  neural networks, 104-119
#    principle of, 182                                     random forests, 84-88
# algorithm chains and pipelines, 305-321              supervised, regression
#    building pipelines, 308                               decision trees, 70-83
#    building pipelines with make_pipeline,                gradient boosting, 88-91
#        313-316                                           k-nearest neighbors, 40
#    grid search preprocessing steps, 317                  Lasso, 53-55
#    grid-searching for model selection, 319               linear regression (OLS), 47, 220-229
#    importance of, 305                                    neural networks, 104-119
#    overview of, 320                                      random forests, 84-88
#    parameter selection with preprocessing, 306           Ridge, 49-55, 67, 112, 231, 234, 310,
#    pipeline interface, 312                                   317-319
#    using pipelines in grid searches, 309-311         unsupervised, clustering
# algorithm parameter, 118                                 agglomerative clustering, 182-187,
# algorithms (see also models; problem solving)                191-195, 203-207
#    evaluating, 28                                        DBSCAN, 187-190
#    minimal code to apply to algorithm, 24                k-means, 168-181
#    sample datasets, 30-34                            unsupervised, manifold learning
#    scaling                                               t-SNE, 163-168
#        MinMaxScaler, 102, 135-139, 190, 230,         unsupervised, signal decomposition
#           308, 319                                       non-negative matrix factorization,
#        Normalizer, 134                                       156-163
#        RobustScaler, 133                                 principal component analysis, 140-155
#        StandardScaler, 114, 133, 138, 144, 150,   alpha parameter in linear models, 50
#           190-195, 314-320                        Anaconda, 6
# 
# 
# 
#                                                                                              367
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Conclusion",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Conclusion(HierNode):
    def __init__(self):
        super().__init__("Conclusion")
        self.add(Content(), "content")

# eof