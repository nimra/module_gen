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
# Figure 5-63. The effect of the C parameter on the support vector fit
# 
# The optimal value of the C parameter will depend on your dataset, and should be
# tuned via cross-validation or a similar procedure (refer back to “Hyperparameters
# and Model Validation” on page 359 for further information).
# 
# Example: Face Recognition
# As an example of support vector machines in action, let’s take a look at the facial rec‐
# ognition problem. We will use the Labeled Faces in the Wild dataset, which consists
# of several thousand collated photos of various public figures. A fetcher for the dataset
# is built into Scikit-Learn:
#       In[18]: from sklearn.datasets import fetch_lfw_people
#               faces = fetch_lfw_people(min_faces_per_person=60)
#               print(faces.target_names)
#               print(faces.images.shape)
#       ['Ariel Sharon' 'Colin Powell' 'Donald Rumsfeld' 'George W Bush'
#        'Gerhard Schroeder' 'Hugo Chavez' 'Junichiro Koizumi' 'Tony Blair']
#       (1348, 62, 47)
# Let’s plot a few of these faces to see what we’re working with (Figure 5-64):
#       In[19]: fig, ax = plt.subplots(3, 5)
#               for i, axi in enumerate(ax.flat):
#                   axi.imshow(faces.images[i], cmap='bone')
#                   axi.set(xticks=[], yticks=[],
#                           xlabel=faces.target_names[faces.target[i]])
# 
# 
# 
# 
# 416   |   Chapter 5: Machine Learning
# 
# Figure 5-64. Examples from the Labeled Faces in the Wild dataset
# 
# Each image contains [62×47] or nearly 3,000 pixels. We could proceed by simply
# using each pixel value as a feature, but often it is more effective to use some sort of
# preprocessor to extract more meaningful features; here we will use a principal com‐
# ponent analysis (see “In Depth: Principal Component Analysis” on page 433) to
# extract 150 fundamental components to feed into our support vector machine classi‐
# fier. We can do this most straightforwardly by packaging the preprocessor and the
# classifier into a single pipeline:
#     In[20]: from sklearn.svm import SVC
#             from sklearn.decomposition import RandomizedPCA
#             from sklearn.pipeline import make_pipeline
# 
#             pca = RandomizedPCA(n_components=150, whiten=True, random_state=42)
#             svc = SVC(kernel='rbf', class_weight='balanced')
#             model = make_pipeline(pca, svc)
# For the sake of testing our classifier output, we will split the data into a training and
# testing set:
#     In[21]: from sklearn.cross_validation import train_test_split
#             Xtrain, Xtest, ytrain, ytest = train_test_split(faces.data, faces.target,
#                                                             random_state=42)
# Finally, we can use a grid search cross-validation to explore combinations of parame‐
# ters. Here we will adjust C (which controls the margin hardness) and gamma (which
# controls the size of the radial basis function kernel), and determine the best model:
#     In[22]: from sklearn.grid_search import GridSearchCV
#             param_grid = {'svc__C': [1, 5, 10, 50],
#                           'svc__gamma': [0.0001, 0.0005, 0.001, 0.005]}
#             grid = GridSearchCV(model, param_grid)
# 
# 
# 
#                                                        In-Depth: Support Vector Machines   |   417
# 
#                 %time grid.fit(Xtrain, ytrain)
#                 print(grid.best_params_)
#       CPU times: user 47.8 s, sys: 4.08 s, total: 51.8 s
#       Wall time: 26 s
#       {'svc__gamma': 0.001, 'svc__C': 10}
# The optimal values fall toward the middle of our grid; if they fell at the edges, we
# would want to expand the grid to make sure we have found the true optimum.
# Now with this cross-validated model, we can predict the labels for the test data, which
# the model has not yet seen:
#       In[23]: model = grid.best_estimator_
#               yfit = model.predict(Xtest)
# Let’s take a look at a few of the test images along with their predicted values
# (Figure 5-65):
#       In[24]: fig, ax = plt.subplots(4, 6)
#               for i, axi in enumerate(ax.flat):
#                   axi.imshow(Xtest[i].reshape(62, 47), cmap='bone')
#                   axi.set(xticks=[], yticks=[])
#                   axi.set_ylabel(faces.target_names[yfit[i]].split()[-1],
#                                  color='black' if yfit[i] == ytest[i] else 'red')
#               fig.suptitle('Predicted Names; Incorrect Labels in Red', size=14);
# 
# 
# 
# 
# Figure 5-65. Labels predicted by our model
# 
# Out of this small sample, our optimal estimator mislabeled only a single face (Bush’s
# face in the bottom row was mislabeled as Blair). We can get a better sense of our esti‐
# mator’s performance using the classification report, which lists recovery statistics
# label by label:
# 
# 
# 
# 418   |   Chapter 5: Machine Learning
# 
#     In[25]: from sklearn.metrics import classification_report
#             print(classification_report(ytest, yfit,
#                                         target_names=faces.target_names))
#                         precision    recall    f1-score     support
# 
#          Ariel Sharon        0.65       0.73       0.69           15
#          Colin Powell        0.81       0.87       0.84           68
#       Donald Rumsfeld        0.75       0.87       0.81           31
#         George W Bush        0.93       0.83       0.88          126
#     Gerhard Schroeder        0.86       0.78       0.82           23
#           Hugo Chavez        0.93       0.70       0.80           20
#     Junichiro Koizumi        0.80       1.00       0.89           12
#            Tony Blair        0.83       0.93       0.88           42
# 
#           avg / total        0.85       0.85       0.85          337
# We might also display the confusion matrix between these classes (Figure 5-66):
#     In[26]: from sklearn.metrics import confusion_matrix
#             mat = confusion_matrix(ytest, yfit)
#             sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
#                         xticklabels=faces.target_names,
#                         yticklabels=faces.target_names)
#             plt.xlabel('true label')
#             plt.ylabel('predicted label');
# 
# 
# 
# 
# Figure 5-66. Confusion matrix for the faces data
# 
# This helps us get a sense of which labels are likely to be confused by the estimator.
# 
# 
# 
#                                                           In-Depth: Support Vector Machines   |   419
# 
# For a real-world facial recognition task, in which the photos do not come precropped
# into nice grids, the only difference in the facial classification scheme is the feature
# selection: you would need to use a more sophisticated algorithm to find the faces, and
# extract features that are independent of the pixellation. For this kind of application,
# one good option is to make use of OpenCV, which among other things, includes pre‐
# trained implementations of state-of-the-art feature extraction tools for images in gen‐
# eral and faces in particular.
# 
# Support Vector Machine Summary
# We have seen here a brief intuitive introduction to the principals behind support vec‐
# tor machines. These methods are a powerful classification method for a number of
# reasons:
# 
#   • Their dependence on relatively few support vectors means that they are very
#     compact models, and take up very little memory.
#   • Once the model is trained, the prediction phase is very fast.
#   • Because they are affected only by points near the margin, they work well with
#     high-dimensional data—even data with more dimensions than samples, which is
#     a challenging regime for other algorithms.
#   • Their integration with kernel methods makes them very versatile, able to adapt to
#     many types of data.
# 
# However, SVMs have several disadvantages as well:
# 
#   • The scaling with the number of samples N is � N 3 at worst, or � N 2 for effi‐
#     cient implementations. For large numbers of training samples, this computa‐
#     tional cost can be prohibitive.
#   • The results are strongly dependent on a suitable choice for the softening parame‐
#     ter C. This must be carefully chosen via cross-validation, which can be expensive
#     as datasets grow in size.
#   • The results do not have a direct probabilistic interpretation. This can be estima‐
#     ted via an internal cross-validation (see the probability parameter of SVC), but
#     this extra estimation is costly.
# 
# With those traits in mind, I generally only turn to SVMs once other simpler, faster,
# and less tuning-intensive methods have been shown to be insufficient for my needs.
# Nevertheless, if you have the CPU cycles to commit to training and cross-validating
# an SVM on your data, the method can lead to excellent results.
# 
# 
# 
# 
# 420   |   Chapter 5: Machine Learning
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Example: Face Recognition",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ExampleFace(HierNode):
    def __init__(self):
        super().__init__("Example: Face Recognition")
        self.add(Content())

# eof
