# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                 Download from finelybook www.finelybook.com
# 
# 
#                                                                            APPENDIX A
#                                                      Exercise Solutions
# 
# 
# 
# 
#               Solutions to the coding exercises are available in the online Jupyter
#               notebooks at https://github.com/ageron/handson-ml.
# 
# 
# 
# 
# Chapter 1: The Machine Learning Landscape
# 1. Machine Learning is about building systems that can learn from data. Learning
#    means getting better at some task, given some performance measure.
# 2. Machine Learning is great for complex problems for which we have no algorith‐
#    mic solution, to replace long lists of hand-tuned rules, to build systems that adapt
#    to fluctuating environments, and finally to help humans learn (e.g., data mining).
# 3. A labeled training set is a training set that contains the desired solution (a.k.a. a
#    label) for each instance.
# 4. The two most common supervised tasks are regression and classification.
# 5. Common unsupervised tasks include clustering, visualization, dimensionality
#    reduction, and association rule learning.
# 6. Reinforcement Learning is likely to perform best if we want a robot to learn to
#    walk in various unknown terrains since this is typically the type of problem that
#    Reinforcement Learning tackles. It might be possible to express the problem as a
#    supervised or semisupervised learning problem, but it would be less natural.
# 7. If you don’t know how to define the groups, then you can use a clustering algo‐
#    rithm (unsupervised learning) to segment your customers into clusters of similar
#    customers. However, if you know what groups you would like to have, then you
# 
# 
# 
#                                                                                       471
# 
#                    Download from finelybook www.finelybook.com
#       can feed many examples of each group to a classification algorithm (supervised
#       learning), and it will classify all your customers into these groups.
#  8. Spam detection is a typical supervised learning problem: the algorithm is fed
#     many emails along with their label (spam or not spam).
#  9. An online learning system can learn incrementally, as opposed to a batch learn‐
#     ing system. This makes it capable of adapting rapidly to both changing data and
#     autonomous systems, and of training on very large quantities of data.
# 10. Out-of-core algorithms can handle vast quantities of data that cannot fit in a
#     computer’s main memory. An out-of-core learning algorithm chops the data into
#     mini-batches and uses online learning techniques to learn from these mini-
#     batches.
# 11. An instance-based learning system learns the training data by heart; then, when
#     given a new instance, it uses a similarity measure to find the most similar learned
#     instances and uses them to make predictions.
# 12. A model has one or more model parameters that determine what it will predict
#     given a new instance (e.g., the slope of a linear model). A learning algorithm tries
#     to find optimal values for these parameters such that the model generalizes well
#     to new instances. A hyperparameter is a parameter of the learning algorithm
#     itself, not of the model (e.g., the amount of regularization to apply).
# 13. Model-based learning algorithms search for an optimal value for the model
#     parameters such that the model will generalize well to new instances. We usually
#     train such systems by minimizing a cost function that measures how bad the sys‐
#     tem is at making predictions on the training data, plus a penalty for model com‐
#     plexity if the model is regularized. To make predictions, we feed the new
#     instance’s features into the model’s prediction function, using the parameter val‐
#     ues found by the learning algorithm.
# 14. Some of the main challenges in Machine Learning are the lack of data, poor data
#     quality, nonrepresentative data, uninformative features, excessively simple mod‐
#     els that underfit the training data, and excessively complex models that overfit
#     the data.
# 15. If a model performs great on the training data but generalizes poorly to new
#     instances, the model is likely overfitting the training data (or we got extremely
#     lucky on the training data). Possible solutions to overfitting are getting more
#     data, simplifying the model (selecting a simpler algorithm, reducing the number
#     of parameters or features used, or regularizing the model), or reducing the noise
#     in the training data.
# 16. A test set is used to estimate the generalization error that a model will make on
#     new instances, before the model is launched in production.
# 
# 
# 
# 
# 472   | Appendix A: Exercise Solutions
# 
#                  Download from finelybook www.finelybook.com
# 17. A validation set is used to compare models. It makes it possible to select the best
#     model and tune the hyperparameters.
# 18. If you tune hyperparameters using the test set, you risk overfitting the test set,
#     and the generalization error you measure will be optimistic (you may launch a
#     model that performs worse than you expect).
# 19. Cross-validation is a technique that makes it possible to compare models (for
#     model selection and hyperparameter tuning) without the need for a separate vali‐
#     dation set. This saves precious training data.
# 
# 
# Chapter 2: End-to-End Machine Learning Project
# See the Jupyter notebooks available at https://github.com/ageron/handson-ml.
# 
# Chapter 3: Classification
# See the Jupyter notebooks available at https://github.com/ageron/handson-ml.
# 
# Chapter 4: Training Linear Models
#  1. If you have a training set with millions of features you can use Stochastic Gradi‐
#     ent Descent or Mini-batch Gradient Descent, and perhaps Batch Gradient
#     Descent if the training set fits in memory. But you cannot use the Normal Equa‐
#     tion because the computational complexity grows quickly (more than quadrati‐
#     cally) with the number of features.
#  2. If the features in your training set have very different scales, the cost function will
#     have the shape of an elongated bowl, so the Gradient Descent algorithms will take
#     a long time to converge. To solve this you should scale the data before training
#     the model. Note that the Normal Equation will work just fine without scaling.
#  3. Gradient Descent cannot get stuck in a local minimum when training a Logistic
#     Regression model because the cost function is convex.1
#  4. If the optimization problem is convex (such as Linear Regression or Logistic
#     Regression), and assuming the learning rate is not too high, then all Gradient
#     Descent algorithms will approach the global optimum and end up producing
#     fairly similar models. However, unless you gradually reduce the learning rate,
#     Stochastic GD and Mini-batch GD will never truly converge; instead, they will
#     keep jumping back and forth around the global optimum. This means that even
# 
# 
# 
# 1 If you draw a straight line between any two points on the curve, the line never crosses the curve.
# 
# 
# 
#                                                                                        Exercise Solutions   |   473
# 
#                     Download from finelybook www.finelybook.com
#       if you let them run for a very long time, these Gradient Descent algorithms will
#       produce slightly different models.
#  5. If the validation error consistently goes up after every epoch, then one possibility
#     is that the learning rate is too high and the algorithm is diverging. If the training
#     error also goes up, then this is clearly the problem and you should reduce the
#     learning rate. However, if the training error is not going up, then your model is
#     overfitting the training set and you should stop training.
#  6. Due to their random nature, neither Stochastic Gradient Descent nor Mini-batch
#     Gradient Descent is guaranteed to make progress at every single training itera‐
#     tion. So if you immediately stop training when the validation error goes up, you
#     may stop much too early, before the optimum is reached. A better option is to
#     save the model at regular intervals, and when it has not improved for a long time
#     (meaning it will probably never beat the record), you can revert to the best saved
#     model.
#  7. Stochastic Gradient Descent has the fastest training iteration since it considers
#     only one training instance at a time, so it is generally the first to reach the vicinity
#     of the global optimum (or Mini-batch GD with a very small mini-batch size).
#     However, only Batch Gradient Descent will actually converge, given enough
#     training time. As mentioned, Stochastic GD and Mini-batch GD will bounce
#     around the optimum, unless you gradually reduce the learning rate.
#  8. If the validation error is much higher than the training error, this is likely because
#     your model is overfitting the training set. One way to try to fix this is to reduce
#     the polynomial degree: a model with fewer degrees of freedom is less likely to
#     overfit. Another thing you can try is to regularize the model—for example, by
#     adding an ℓ2 penalty (Ridge) or an ℓ1 penalty (Lasso) to the cost function. This
#     will also reduce the degrees of freedom of the model. Lastly, you can try to
#     increase the size of the training set.
#  9. If both the training error and the validation error are almost equal and fairly
#     high, the model is likely underfitting the training set, which means it has a high
#     bias. You should try reducing the regularization hyperparameter α.
# 10. Let’s see:
#       • A model with some regularization typically performs better than a model
#         without any regularization, so you should generally prefer Ridge Regression
#         over plain Linear Regression.2
#       • Lasso Regression uses an ℓ1 penalty, which tends to push the weights down to
#         exactly zero. This leads to sparse models, where all weights are zero except for
# 
# 
# 2 Moreover, the Normal Equation requires computing the inverse of a matrix, but that matrix is not always
#   invertible. In contrast, the matrix for Ridge Regression is always invertible.
# 
# 
# 
# 474   |   Appendix A: Exercise Solutions
# 
#                  Download from finelybook www.finelybook.com
#       the most important weights. This is a way to perform feature selection auto‐
#       matically, which is good if you suspect that only a few features actually matter.
#       When you are not sure, you should prefer Ridge Regression.
#     • Elastic Net is generally preferred over Lasso since Lasso may behave erratically
#       in some cases (when several features are strongly correlated or when there are
#       more features than training instances). However, it does add an extra hyper‐
#       parameter to tune. If you just want Lasso without the erratic behavior, you can
#       just use Elastic Net with an l1_ratio close to 1.
# 
# 11. If you want to classify pictures as outdoor/indoor and daytime/nighttime, since
#     these are not exclusive classes (i.e., all four combinations are possible) you should
#     train two Logistic Regression classifiers.
# 12. See the Jupyter notebooks available at https://github.com/ageron/handson-ml.
# 
# 
# Chapter 5: Support Vector Machines
#  1. The fundamental idea behind Support Vector Machines is to fit the widest possi‐
#     ble “street” between the classes. In other words, the goal is to have the largest pos‐
#     sible margin between the decision boundary that separates the two classes and
#     the training instances. When performing soft margin classification, the SVM
#     searches for a compromise between perfectly separating the two classes and hav‐
#     ing the widest possible street (i.e., a few instances may end up on the street).
#     Another key idea is to use kernels when training on nonlinear datasets.
#  2. After training an SVM, a support vector is any instance located on the “street” (see
#     the previous answer), including its border. The decision boundary is entirely
#     determined by the support vectors. Any instance that is not a support vector (i.e.,
#     off the street) has no influence whatsoever; you could remove them, add more
#     instances, or move them around, and as long as they stay off the street they won’t
#     affect the decision boundary. Computing the predictions only involves the sup‐
#     port vectors, not the whole training set.
#  3. SVMs try to fit the largest possible “street” between the classes (see the first
#     answer), so if the training set is not scaled, the SVM will tend to neglect small
#     features (see Figure 5-2).
#  4. An SVM classifier can output the distance between the test instance and the deci‐
#     sion boundary, and you can use this as a confidence score. However, this score
#     cannot be directly converted into an estimation of the class probability. If you set
#     probability=True when creating an SVM in Scikit-Learn, then after training it
#     will calibrate the probabilities using Logistic Regression on the SVM’s scores
#     (trained by an additional five-fold cross-validation on the training data). This
#     will add the predict_proba() and predict_log_proba() methods to the SVM.
# 
# 
#                                                                      Exercise Solutions   |   475
# 
#                  Download from finelybook www.finelybook.com
#  5. This question applies only to linear SVMs since kernelized can only use the dual
#     form. The computational complexity of the primal form of the SVM problem is
#     proportional to the number of training instances m, while the computational
#     complexity of the dual form is proportional to a number between m2 and m3. So
#     if there are millions of instances, you should definitely use the primal form,
#     because the dual form will be much too slow.
#  6. If an SVM classifier trained with an RBF kernel underfits the training set, there
#     might be too much regularization. To decrease it, you need to increase gamma or C
#     (or both).
#  7. Let’s call the QP parameters for the hard-margin problem H′, f′, A′ and b′ (see
#     “Quadratic Programming” on page 159). The QP parameters for the soft-margin
#     problem have m additional parameters (np = n + 1 + m) and m additional con‐
#     straints (nc = 2m). They can be defined like so:
#       • H is equal to H′, plus m columns of 0s on the right and m rows of 0s at the
#                         �′ 0 ⋯
#         bottom: � = 0 0
#                          ⋮    ⋱
#       • f is equal to f′ with m additional elements, all equal to the value of the hyper‐
#         parameter C.
#       • b is equal to b′ with m additional elements, all equal to 0.
#       • A is equal to A′, with an extra m × m identity matrix Im appended to the right,
#                                                                 �′ �m
#         – Im just below it, and the rest filled with zeros: � =
#                                                                 0 −�m
# 
# For the solutions to exercises 8, 9, and 10, please see the Jupyter notebooks available
# at https://github.com/ageron/handson-ml.
# 
# Chapter 6: Decision Trees
#  1. The depth of a well-balanced binary tree containing m leaves is equal to log2(m)3,
#     rounded up. A binary Decision Tree (one that makes only binary decisions, as is
#     the case of all trees in Scikit-Learn) will end up more or less well balanced at the
#     end of training, with one leaf per training instance if it is trained without restric‐
#     tions. Thus, if the training set contains one million instances, the Decision Tree
#     will have a depth of log2(106) ≈ 20 (actually a bit more since the tree will generally
#     not be perfectly well balanced).
# 
# 
# 3 log2 is the binary log, log2(m) = log(m) / log(2).
# 
# 
# 
# 476   |   Appendix A: Exercise Solutions
# 
#                  Download from finelybook www.finelybook.com
#  2. A node’s Gini impurity is generally lower than its parent’s. This is ensured by the
#     CART training algorithm’s cost function, which splits each node in a way that
#     minimizes the weighted sum of its children’s Gini impurities. However, if one
#     child is smaller than the other, it is possible for it to have a higher Gini impurity
#     than its parent, as long as this increase is more than compensated for by a
#     decrease of the other child’s impurity. For example, consider a node containing
#                                                                             12     42
#     four instances of class A and 1 of class B. Its Gini impurity is 1 − 5 − 5 = 0.32.
#     Now suppose the dataset is one-dimensional and the instances are lined up in the
#     following order: A, B, A, A, A. You can verify that the algorithm will split this
#     node after the second instance, producing one child node with instances A, B,
#     and the other child node with instances A, A, A. The first child node’s Gini
#                     12   12
#     impurity is 1 − 2 − 2 = 0.5, which is higher than its parent. This is compensated
#     for by the fact that the other node is pure, so the overall weighted Gini impurity
#        2         3
#     is 5 × 0.5 + 5 × 0 = 0.2 , which is lower than the parent’s Gini impurity.
#  3. If a Decision Tree is overfitting the training set, it may be a good idea to decrease
#     max_depth, since this will constrain the model, regularizing it.
#  4. Decision Trees don’t care whether or not the training data is scaled or centered;
#     that’s one of the nice things about them. So if a Decision Tree underfits the train‐
#     ing set, scaling the input features will just be a waste of time.
#  5. The computational complexity of training a Decision Tree is O(n × m log(m)). So
#     if you multiply the training set size by 10, the training time will be multiplied by
#     K = (n × 10m × log(10m)) / (n × m × log(m)) = 10 × log(10m) / log(m). If m =
#     106, then K ≈ 11.7, so you can expect the training time to be roughly 11.7 hours.
#  6. Presorting the training set speeds up training only if the dataset is smaller than a
#     few thousand instances. If it contains 100,000 instances, setting presort=True
#     will considerably slow down training.
# 
# For the solutions to exercises 7 and 8, please see the Jupyter notebooks available at
# https://github.com/ageron/handson-ml.
# 
# Chapter 7: Ensemble Learning and Random Forests
#  1. If you have trained five different models and they all achieve 95% precision, you
#     can try combining them into a voting ensemble, which will often give you even
#     better results. It works better if the models are very different (e.g., an SVM classi‐
#     fier, a Decision Tree classifier, a Logistic Regression classifier, and so on). It is
#     even better if they are trained on different training instances (that’s the whole
#     point of bagging and pasting ensembles), but if not it will still work as long as the
#     models are very different.
# 
# 
#                                                                      Exercise Solutions   |   477
# 
#                  Download from finelybook www.finelybook.com
#  2. A hard voting classifier just counts the votes of each classifier in the ensemble
#     and picks the class that gets the most votes. A soft voting classifier computes the
#     average estimated class probability for each class and picks the class with the
#     highest probability. This gives high-confidence votes more weight and often per‐
#     forms better, but it works only if every classifier is able to estimate class probabil‐
#     ities (e.g., for the SVM classifiers in Scikit-Learn you must set
#     probability=True).
#  3. It is quite possible to speed up training of a bagging ensemble by distributing it
#     across multiple servers, since each predictor in the ensemble is independent of
#     the others. The same goes for pasting ensembles and Random Forests, for the
#     same reason. However, each predictor in a boosting ensemble is built based on
#     the previous predictor, so training is necessarily sequential, and you will not gain
#     anything by distributing training across multiple servers. Regarding stacking
#     ensembles, all the predictors in a given layer are independent of each other, so
#     they can be trained in parallel on multiple servers. However, the predictors in one
#     layer can only be trained after the predictors in the previous layer have all been
#     trained.
#  4. With out-of-bag evaluation, each predictor in a bagging ensemble is evaluated
#     using instances that it was not trained on (they were held out). This makes it pos‐
#     sible to have a fairly unbiased evaluation of the ensemble without the need for an
#     additional validation set. Thus, you have more instances available for training,
#     and your ensemble can perform slightly better.
#  5. When you are growing a tree in a Random Forest, only a random subset of the
#     features is considered for splitting at each node. This is true as well for Extra-
#     Trees, but they go one step further: rather than searching for the best possible
#     thresholds, like regular Decision Trees do, they use random thresholds for each
#     feature. This extra randomness acts like a form of regularization: if a Random
#     Forest overfits the training data, Extra-Trees might perform better. Moreover,
#     since Extra-Trees don’t search for the best possible thresholds, they are much
#     faster to train than Random Forests. However, they are neither faster nor slower
#     than Random Forests when making predictions.
#  6. If your AdaBoost ensemble underfits the training data, you can try increasing the
#     number of estimators or reducing the regularization hyperparameters of the base
#     estimator. You may also try slightly increasing the learning rate.
#  7. If your Gradient Boosting ensemble overfits the training set, you should try
#     decreasing the learning rate. You could also use early stopping to find the right
#     number of predictors (you probably have too many).
# 
# For the solutions to exercises 8 and 9, please see the Jupyter notebooks available at
# https://github.com/ageron/handson-ml.
# 
# 
# 
# 478   |   Appendix A: Exercise Solutions
# 
#                 Download from finelybook www.finelybook.com
# Chapter 8: Dimensionality Reduction
# 1. Motivations and drawbacks:
#    • The main motivations for dimensionality reduction are:
#      — To speed up a subsequent training algorithm (in some cases it may even
#        remove noise and redundant features, making the training algorithm per‐
#        form better).
#      — To visualize the data and gain insights on the most important features.
#      — Simply to save space (compression).
#    • The main drawbacks are:
#      — Some information is lost, possibly degrading the performance of subse‐
#        quent training algorithms.
#      — It can be computationally intensive.
#      — It adds some complexity to your Machine Learning pipelines.
#      — Transformed features are often hard to interpret.
# 
# 2. The curse of dimensionality refers to the fact that many problems that do not
#    exist in low-dimensional space arise in high-dimensional space. In Machine
#    Learning, one common manifestation is the fact that randomly sampled high-
#    dimensional vectors are generally very sparse, increasing the risk of overfitting
#    and making it very difficult to identify patterns in the data without having plenty
#    of training data.
# 3. Once a dataset’s dimensionality has been reduced using one of the algorithms we
#    discussed, it is almost always impossible to perfectly reverse the operation,
#    because some information gets lost during dimensionality reduction. Moreover,
#    while some algorithms (such as PCA) have a simple reverse transformation pro‐
#    cedure that can reconstruct a dataset relatively similar to the original, other algo‐
#    rithms (such as T-SNE) do not.
# 4. PCA can be used to significantly reduce the dimensionality of most datasets, even
#    if they are highly nonlinear, because it can at least get rid of useless dimensions.
#    However, if there are no useless dimensions—for example, the Swiss roll—then
#    reducing dimensionality with PCA will lose too much information. You want to
#    unroll the Swiss roll, not squash it.
# 5. That’s a trick question: it depends on the dataset. Let’s look at two extreme exam‐
#    ples. First, suppose the dataset is composed of points that are almost perfectly
#    aligned. In this case, PCA can reduce the dataset down to just one dimension
#    while still preserving 95% of the variance. Now imagine that the dataset is com‐
#    posed of perfectly random points, scattered all around the 1,000 dimensions. In
# 
# 
#                                                                    Exercise Solutions   |   479
# 
#                      Download from finelybook www.finelybook.com
#       this case all 1,000 dimensions are required to preserve 95% of the variance. So the
#       answer is, it depends on the dataset, and it could be any number between 1 and
#       1,000. Plotting the explained variance as a function of the number of dimensions
#       is one way to get a rough idea of the dataset’s intrinsic dimensionality.
#  6. Regular PCA is the default, but it works only if the dataset fits in memory. Incre‐
#     mental PCA is useful for large datasets that don’t fit in memory, but it is slower
#     than regular PCA, so if the dataset fits in memory you should prefer regular
#     PCA. Incremental PCA is also useful for online tasks, when you need to apply
#     PCA on the fly, every time a new instance arrives. Randomized PCA is useful
#     when you want to considerably reduce dimensionality and the dataset fits in
#     memory; in this case, it is much faster than regular PCA. Finally, Kernel PCA is
#     useful for nonlinear datasets.
#  7. Intuitively, a dimensionality reduction algorithm performs well if it eliminates a
#     lot of dimensions from the dataset without losing too much information. One
#     way to measure this is to apply the reverse transformation and measure the
#     reconstruction error. However, not all dimensionality reduction algorithms pro‐
#     vide a reverse transformation. Alternatively, if you are using dimensionality
#     reduction as a preprocessing step before another Machine Learning algorithm
#     (e.g., a Random Forest classifier), then you can simply measure the performance
#     of that second algorithm; if dimensionality reduction did not lose too much
#     information, then the algorithm should perform just as well as when using the
#     original dataset.
#  8. It can absolutely make sense to chain two different dimensionality reduction
#     algorithms. A common example is using PCA to quickly get rid of a large num‐
#     ber of useless dimensions, then applying another much slower dimensionality
#     reduction algorithm, such as LLE. This two-step approach will likely yield the
#     same performance as using LLE only, but in a fraction of the time.
# 
# For the solutions to exercises 9 and 10, please see the Jupyter notebooks available at
# https://github.com/ageron/handson-ml.
# 
# Chapter 9: Up and Running with TensorFlow
#  1. Main benefits and drawbacks of creating a computation graph rather than
#     directly executing the computations:
#       • Main benefits:
#           — TensorFlow can automatically compute the gradients for you (using
#             reverse-mode autodiff).
#           — TensorFlow can take care of running the operations in parallel in different
#             threads.
# 
# 
# 480   |   Appendix A: Exercise Solutions
# 
#                Download from finelybook www.finelybook.com
#       — It makes it easier to run the same model across different devices.
#       — It simplifies introspection—for example, to view the model in TensorBoard.
#    • Main drawbacks:
#       — It makes the learning curve steeper.
#       — It makes step-by-step debugging harder.
# 
# 2. Yes, the statement a_val = a.eval(session=sess) is indeed equivalent to a_val
#    = sess.run(a).
# 3. No, the statement a_val, b_val = a.eval(session=sess), b.eval(ses
#    sion=sess) is not equivalent to a_val, b_val = sess.run([a, b]). Indeed, the
#    first statement runs the graph twice (once to compute a, once to compute b),
#    while the second statement runs the graph only once. If any of these operations
#    (or the ops they depend on) have side effects (e.g., a variable is modified, an item
#    is inserted in a queue, or a reader reads a file), then the effects will be different. If
#    they don’t have side effects, both statements will return the same result, but the
#    second statement will be faster than the first.
# 4. No, you cannot run two graphs in the same session. You would have to merge the
#    graphs into a single graph first.
# 5. In local TensorFlow, sessions manage variable values, so if you create a graph g
#    containing a variable w, then start two threads and open a local session in each
#    thread, both using the same graph g, then each session will have its own copy of
#    the variable w. However, in distributed TensorFlow, variable values are stored in
#    containers managed by the cluster, so if both sessions connect to the same cluster
#    and use the same container, then they will share the same variable value for w.
# 6. A variable is initialized when you call its initializer, and it is destroyed when the
#    session ends. In distributed TensorFlow, variables live in containers on the clus‐
#    ter, so closing a session will not destroy the variable. To destroy a variable, you
#    need to clear its container.
# 7. Variables and placeholders are extremely different, but beginners often confuse
#    them:
#    • A variable is an operation that holds a value. If you run the variable, it returns
#      that value. Before you can run it, you need to initialize it. You can change the
#      variable’s value (for example, by using an assignment operation). It is stateful:
#      the variable keeps the same value upon successive runs of the graph. It is typi‐
#      cally used to hold model parameters but also for other purposes (e.g., to count
#      the global training step).
#    • Placeholders technically don’t do much: they just hold information about the
#      type and shape of the tensor they represent, but they have no value. In fact, if
# 
# 
#                                                                       Exercise Solutions   |   481
# 
#                      Download from finelybook www.finelybook.com
#           you try to evaluate an operation that depends on a placeholder, you must feed
#           TensorFlow the value of the placeholder (using the feed_dict argument) or
#           else you will get an exception. Placeholders are typically used to feed training
#           or test data to TensorFlow during the execution phase. They are also useful to
#           pass a value to an assignment node, to change the value of a variable (e.g.,
#           model weights).
# 
#  8. If you run the graph to evaluate an operation that depends on a placeholder but
#     you don’t feed its value, you get an exception. If the operation does not depend
#     on the placeholder, then no exception is raised.
#  9. When you run a graph, you can feed the output value of any operation, not just
#     the value of placeholders. In practice, however, this is rather rare (it can be useful,
#     for example, when you are caching the output of frozen layers; see Chapter 11).
# 10. You can specify a variable’s initial value when constructing the graph, and it will
#     be initialized later when you run the variable’s initializer during the execution
#     phase. If you want to change that variable’s value to anything you want during the
#     execution phase, then the simplest option is to create an assignment node (dur‐
#     ing the graph construction phase) using the tf.assign() function, passing the
#     variable and a placeholder as parameters. During the execution phase, you can
#     run the assignment operation and feed the variable’s new value using the place‐
#     holder.
#            import tensorflow as tf
# 
#            x = tf.Variable(tf.random_uniform(shape=(), minval=0.0, maxval=1.0))
#            x_new_val = tf.placeholder(shape=(), dtype=tf.float32)
#            x_assign = tf.assign(x, x_new_val)
# 
#            with tf.Session():
#                x.initializer.run() # random number is sampled *now*
#                print(x.eval()) # 0.646157 (some random number)
#                x_assign.eval(feed_dict={x_new_val: 5.0})
#                print(x.eval()) # 5.0
# 11. Reverse-mode autodiff (implemented by TensorFlow) needs to traverse the graph
#     only twice in order to compute the gradients of the cost function with regards to
#     any number of variables. On the other hand, forward-mode autodiff would need
#     to run once for each variable (so 10 times if we want the gradients with regards to
#     10 different variables). As for symbolic differentiation, it would build a different
#     graph to compute the gradients, so it would not traverse the original graph at all
#     (except when building the new gradients graph). A highly optimized symbolic
#     differentiation system could potentially run the new gradients graph only once to
#     compute the gradients with regards to all variables, but that new graph may be
#     horribly complex and inefficient compared to the original graph.
# 
# 
# 
# 482   |   Appendix A: Exercise Solutions
# 
#                  Download from finelybook www.finelybook.com
# 12. See the Jupyter notebooks available at https://github.com/ageron/handson-ml.
# 
# 
# Chapter 10: Introduction to Artificial Neural Networks
#  1. Here is a neural network based on the original artificial neurons that computes A
#     ⊕ B (where ⊕ represents the exclusive OR), using the fact that A ⊕ B = (A ∧ ¬ B)
#     ∨ (¬ A ∧ B). There are other solutions—for example, using the fact that A ⊕ B =
#     (A ∨ B) ∧ ¬(A ∧ B), or the fact that A ⊕ B = (A ∨ B) ∧ (¬ A ∨ ∧ B), and so on.
# 
# 
# 
# 
#  2. A classical Perceptron will converge only if the dataset is linearly separable, and it
#     won’t be able to estimate class probabilities. In contrast, a Logistic Regression
#     classifier will converge to a good solution even if the dataset is not linearly sepa‐
#     rable, and it will output class probabilities. If you change the Perceptron’s activa‐
#     tion function to the logistic activation function (or the softmax activation
#     function if there are multiple neurons), and if you train it using Gradient Descent
#     (or some other optimization algorithm minimizing the cost function, typically
#     cross entropy), then it becomes equivalent to a Logistic Regression classifier.
#  3. The logistic activation function was a key ingredient in training the first MLPs
#     because its derivative is always nonzero, so Gradient Descent can always roll
#     down the slope. When the activation function is a step function, Gradient
#     Descent cannot move, as there is no slope at all.
#  4. The step function, the logistic function, the hyperbolic tangent, the rectified lin‐
#     ear unit (see Figure 10-8). See Chapter 11 for other examples, such as ELU and
#     variants of the ReLU.
#  5. Considering the MLP described in the question: suppose you have an MLP com‐
#     posed of one input layer with 10 passthrough neurons, followed by one hidden
#     layer with 50 artificial neurons, and finally one output layer with 3 artificial neu‐
#     rons. All artificial neurons use the ReLU activation function.
# 
#                                                                      Exercise Solutions   |   483
# 
#                     Download from finelybook www.finelybook.com
#       • The shape of the input matrix X is m × 10, where m represents the training
#         batch size.
#       • The shape of the hidden layer’s weight vector Wh is 10 × 50 and the length of
#         its bias vector bh is 50.
#       • The shape of the output layer’s weight vector Wo is 50 × 3, and the length of its
#         bias vector bo is 3.
#       • The shape of the network’s output matrix Y is m × 3.
#       • Y = (X · Wh + bh) · Wo + bo. Note that when you are adding a bias vector to a
#         matrix, it is added to every single row in the matrix, which is called broadcast‐
#         ing.
# 
#  6. To classify email into spam or ham, you just need one neuron in the output layer
#     of a neural network—for example, indicating the probability that the email is
#     spam. You would typically use the logistic activation function in the output layer
#     when estimating a probability. If instead you want to tackle MNIST, you need 10
#     neurons in the output layer, and you must replace the logistic function with the
#     softmax activation function, which can handle multiple classes, outputting one
#     probability per class. Now, if you want your neural network to predict housing
#     prices like in Chapter 2, then you need one output neuron, using no activation
#     function at all in the output layer.4
#  7. Backpropagation is a technique used to train artificial neural networks. It first
#     computes the gradients of the cost function with regards to every model parame‐
#     ter (all the weights and biases), and then it performs a Gradient Descent step
#     using these gradients. This backpropagation step is typically performed thou‐
#     sands or millions of times, using many training batches, until the model parame‐
#     ters converge to values that (hopefully) minimize the cost function. To compute
#     the gradients, backpropagation uses reverse-mode autodiff (although it wasn’t
#     called that when backpropagation was invented, and it has been reinvented sev‐
#     eral times). Reverse-mode autodiff performs a forward pass through a computa‐
#     tion graph, computing every node’s value for the current training batch, and then
#     it performs a reverse pass, computing all the gradients at once (see Appendix D
#     for more details). So what’s the difference? Well, backpropagation refers to the
#     whole process of training an artificial neural network using multiple backpropa‐
#     gation steps, each of which computes gradients and uses them to perform a Gra‐
#     dient Descent step. In contrast, reverse-mode autodiff is a simply a technique to
#     compute gradients efficiently, and it happens to be used by backpropagation.
# 
# 
# 4 When the values to predict can vary by many orders of magnitude, then you may want to predict the loga‐
#   rithm of the target value rather than the target value directly. Simply computing the exponential of the neural
#   network’s output will give you the estimated value (since exp(log v) = v).
# 
# 
# 
# 484   |   Appendix A: Exercise Solutions
# 
#                    Download from finelybook www.finelybook.com
#  8. Here is a list of all the hyperparameters you can tweak in a basic MLP: the num‐
#     ber of hidden layers, the number of neurons in each hidden layer, and the activa‐
#     tion function used in each hidden layer and in the output layer.5 In general, the
#     ReLU activation function (or one of its variants; see Chapter 11) is a good default
#     for the hidden layers. For the output layer, in general you will want the logistic
#     activation function for binary classification, the softmax activation function for
#     multiclass classification, or no activation function for regression.
#      If the MLP overfits the training data, you can try reducing the number of hidden
#      layers and reducing the number of neurons per hidden layer.
#  9. See the Jupyter notebooks available at https://github.com/ageron/handson-ml.
# 
# 
# Chapter 11: Training Deep Neural Nets
#  1. No, all weights should be sampled independently; they should not all have the
#     same initial value. One important goal of sampling weights randomly is to break
#     symmetries: if all the weights have the same initial value, even if that value is not
#     zero, then symmetry is not broken (i.e., all neurons in a given layer are equiva‐
#     lent), and backpropagation will be unable to break it. Concretely, this means that
#     all the neurons in any given layer will always have the same weights. It’s like hav‐
#     ing just one neuron per layer, and much slower. It is virtually impossible for such
#     a configuration to converge to a good solution.
#  2. It is perfectly fine to initialize the bias terms to zero. Some people like to initialize
#     them just like weights, and that’s okay too; it does not make much difference.
#  3. A few advantages of the ELU function over the ReLU function are:
#      • It can take on negative values, so the average output of the neurons in any
#        given layer is typically closer to 0 than when using the ReLU activation func‐
#        tion (which never outputs negative values). This helps alleviate the vanishing
#        gradients problem.
#      • It always has a nonzero derivative, which avoids the dying units issue that can
#        affect ReLU units.
# 
# 
# 
# 
# 5 In Chapter 11 we discuss many techniques that introduce additional hyperparameters: type of weight initiali‐
#   zation, activation function hyperparameters (e.g., amount of leak in leaky ReLU), Gradient Clipping thres‐
#   hold, type of optimizer and its hyperparameters (e.g., the momentum hyperparameter when using a
#   MomentumOptimizer), type of regularization for each layer, and the regularization hyperparameters (e.g., drop‐
#   out rate when using dropout) and so on.
# 
# 
# 
#                                                                                      Exercise Solutions   |   485
# 
#                    Download from finelybook www.finelybook.com
#       • It is smooth everywhere, whereas the ReLU’s slope abruptly jumps from 0 to 1
#         at z = 0. Such an abrupt change can slow down Gradient Descent because it
#         will bounce around z = 0.
# 
#  4. The ELU activation function is a good default. If you need the neural network to
#     be as fast as possible, you can use one of the leaky ReLU variants instead (e.g., a
#     simple leaky ReLU using the default hyperparameter value). The simplicity of the
#     ReLU activation function makes it many people’s preferred option, despite the
#     fact that they are generally outperformed by the ELU and leaky ReLU. However,
#     the ReLU activation function’s capability of outputting precisely zero can be use‐
#     ful in some cases (e.g., see Chapter 15). The hyperbolic tangent (tanh) can be use‐
#     ful in the output layer if you need to output a number between –1 and 1, but
#     nowadays it is not used much in hidden layers. The logistic activation function is
#     also useful in the output layer when you need to estimate a probability (e.g., for
#     binary classification), but it is also rarely used in hidden layers (there are excep‐
#     tions—for example, for the coding layer of variational autoencoders; see Chap‐
#     ter 15). Finally, the softmax activation function is useful in the output layer to
#     output probabilities for mutually exclusive classes, but other than that it is rarely
#     (if ever) used in hidden layers.
#  5. If you set the momentum hyperparameter too close to 1 (e.g., 0.99999) when using
#     a MomentumOptimizer, then the algorithm will likely pick up a lot of speed, hope‐
#     fully roughly toward the global minimum, but then it will shoot right past the
#     minimum, due to its momentum. Then it will slow down and come back, accel‐
#     erate again, overshoot again, and so on. It may oscillate this way many times
#     before converging, so overall it will take much longer to converge than with a
#     smaller momentum value.
#  6. One way to produce a sparse model (i.e., with most weights equal to zero) is to
#     train the model normally, then zero out tiny weights. For more sparsity, you can
#     apply ℓ1 regularization during training, which pushes the optimizer toward spar‐
#     sity. A third option is to combine ℓ1 regularization with dual averaging, using
#     TensorFlow’s FTRLOptimizer class.
#  7. Yes, dropout does slow down training, in general roughly by a factor of two.
#     However, it has no impact on inference since it is only turned on during training.
# 
# For the solutions to exercises 8, 9, and 10, please see the Jupyter notebooks available
# at https://github.com/ageron/handson-ml.
# 
# 
# 
# 
# 486   |   Appendix A: Exercise Solutions
# 
#                 Download from finelybook www.finelybook.com
# Chapter 12: Distributing TensorFlow Across Devices and
# Servers
# 1. When a TensorFlow process starts, it grabs all the available memory on all GPU
#    devices that are visible to it, so if you get a CUDA_ERROR_OUT_OF_MEMORY when
#    starting your TensorFlow program, it probably means that other processes are
#    running that have already grabbed all the memory on at least one visible GPU
#    device (most likely it is another TensorFlow process). To fix this problem, a triv‐
#    ial solution is to stop the other processes and try again. However, if you need all
#    processes to run simultaneously, a simple option is to dedicate different devices
#    to each process, by setting the CUDA_VISIBLE_DEVICES environment variable
#    appropriately for each device. Another option is to configure TensorFlow to grab
#    only part of the GPU memory, instead of all of it, by creating a ConfigProto, set‐
#    ting its gpu_options.per_process_gpu_memory_fraction to the proportion of
#    the total memory that it should grab (e.g., 0.4), and using this ConfigProto when
#    opening a session. The last option is to tell TensorFlow to grab memory only
#    when it needs it by setting the gpu_options.allow_growth to True. However,
#    this last option is usually not recommended because any memory that Tensor‐
#    Flow grabs is never released, and it is harder to guarantee a repeatable behavior
#    (there may be race conditions depending on which processes start first, how
#    much memory they need during training, and so on).
# 2. By pinning an operation on a device, you are telling TensorFlow that this is
#    where you would like this operation to be placed. However, some constraints may
#    prevent TensorFlow from honoring your request. For example, the operation
#    may have no implementation (called a kernel) for that particular type of device.
#    In this case, TensorFlow will raise an exception by default, but you can configure
#    it to fall back to the CPU instead (this is called soft placement). Another example
#    is an operation that can modify a variable; this operation and the variable need to
#    be collocated. So the difference between pinning an operation and placing an
#    operation is that pinning is what you ask TensorFlow (“Please place this opera‐
#    tion on GPU #1”) while placement is what TensorFlow actually ends up doing
#    (“Sorry, falling back to the CPU”).
# 3. If you are running on a GPU-enabled TensorFlow installation, and you just use
#    the default placement, then if all operations have a GPU kernel (i.e., a GPU
#    implementation), yes, they will all be placed on the first GPU. However, if one or
#    more operations do not have a GPU kernel, then by default TensorFlow will raise
#    an exception. If you configure TensorFlow to fall back to the CPU instead (soft
#    placement), then all operations will be placed on the first GPU except the ones
#    without a GPU kernel and all the operations that must be collocated with them
#    (see the answer to the previous exercise).
# 
# 
# 
#                                                                  Exercise Solutions   |   487
# 
#                  Download from finelybook www.finelybook.com
#  4. Yes, if you pin a variable to "/gpu:0", it can be used by operations placed
#     on /gpu:1. TensorFlow will automatically take care of adding the appropriate
#     operations to transfer the variable’s value across devices. The same goes for devi‐
#     ces located on different servers (as long as they are part of the same cluster).
#  5. Yes, two operations placed on the same device can run in parallel: TensorFlow
#     automatically takes care of running operations in parallel (on different CPU
#     cores or different GPU threads), as long as no operation depends on another
#     operation’s output. Moreover, you can start multiple sessions in parallel threads
#     (or processes), and evaluate operations in each thread. Since sessions are inde‐
#     pendent, TensorFlow will be able to evaluate any operation from one session in
#     parallel with any operation from another session.
#  6. Control dependencies are used when you want to postpone the evaluation of an
#     operation X until after some other operations are run, even though these opera‐
#     tions are not required to compute X. This is useful in particular when X would
#     occupy a lot of memory and you only need it later in the computation graph, or if
#     X uses up a lot of I/O (for example, it requires a large variable value located on a
#     different device or server) and you don’t want it to run at the same time as other
#     I/O-hungry operations, to avoid saturating the bandwidth.
#  7. You’re in luck! In distributed TensorFlow, the variable values live in containers
#     managed by the cluster, so even if you close the session and exit the client pro‐
#     gram, the model parameters are still alive and well on the cluster. You simply
#     need to open a new session to the cluster and save the model (make sure you
#     don’t call the variable initializers or restore a previous model, as this would
#     destroy your precious new model!).
# 
# For the solutions to exercises 8, 9, and 10, please see the Jupyter notebooks available
# at https://github.com/ageron/handson-ml.
# 
# Chapter 13: Convolutional Neural Networks
#  1. These are the main advantages of a CNN over a fully connected DNN for image
#     classification:
#       • Because consecutive layers are only partially connected and because it heavily
#         reuses its weights, a CNN has many fewer parameters than a fully connected
#         DNN, which makes it much faster to train, reduces the risk of overfitting, and
#         requires much less training data.
#       • When a CNN has learned a kernel that can detect a particular feature, it can
#         detect that feature anywhere on the image. In contrast, when a DNN learns a
#         feature in one location, it can detect it only in that particular location. Since
#         images typically have very repetitive features, CNNs are able to generalize
# 
# 
# 488   |   Appendix A: Exercise Solutions
# 
#                 Download from finelybook www.finelybook.com
#      much better than DNNs for image processing tasks such as classification, using
#      fewer training examples.
#    • Finally, a DNN has no prior knowledge of how pixels are organized; it does not
#      know that nearby pixels are close. A CNN’s architecture embeds this prior
#      knowledge. Lower layers typically identify features in small areas of the images,
#      while higher layers combine the lower-level features into larger features. This
#      works well with most natural images, giving CNNs a decisive head start com‐
#      pared to DNNs.
# 
# 2. Let’s compute how many parameters the CNN has. Since its first convolutional
#    layer has 3 × 3 kernels, and the input has three channels (red, green, and blue),
#    then each feature map has 3 × 3 × 3 weights, plus a bias term. That’s 28 parame‐
#    ters per feature map. Since this first convolutional layer has 100 feature maps, it
#    has a total of 2,800 parameters. The second convolutional layer has 3 × 3 kernels,
#    and its input is the set of 100 feature maps of the previous layer, so each feature
#    map has 3 × 3 × 100 = 900 weights, plus a bias term. Since it has 200 feature
#    maps, this layer has 901 × 200 = 180,200 parameters. Finally, the third and last
#    convolutional layer also has 3 × 3 kernels, and its input is the set of 200 feature
#    maps of the previous layers, so each feature map has 3 × 3 × 200 = 1,800 weights,
#    plus a bias term. Since it has 400 feature maps, this layer has a total of 1,801 × 400
#    = 720,400 parameters. All in all, the CNN has 2,800 + 180,200 + 720,400 =
#    903,400 parameters.
#    Now let’s compute how much RAM this neural network will require (at least)
#    when making a prediction for a single instance. First let’s compute the feature
#    map size for each layer. Since we are using a stride of 2 and SAME padding, the
#    horizontal and vertical size of the feature maps are divided by 2 at each layer
#    (rounding up if necessary), so as the input channels are 200 × 300 pixels, the first
#    layer’s feature maps are 100 × 150, the second layer’s feature maps are 50 × 75,
#    and the third layer’s feature maps are 25 × 38. Since 32 bits is 4 bytes and the first
#    convolutional layer has 100 feature maps, this first layer takes up 4 x 100 × 150 ×
#    100 = 6 million bytes (about 5.7 MB, considering that 1 MB = 1,024 KB and 1 KB
#    = 1,024 bytes). The second layer takes up 4 × 50 × 75 × 200 = 3 million bytes
#    (about 2.9 MB). Finally, the third layer takes up 4 × 25 × 38 × 400 = 1,520,000
#    bytes (about 1.4 MB). However, once a layer has been computed, the memory
#    occupied by the previous layer can be released, so if everything is well optimized,
#    only 6 + 9 = 15 million bytes (about 14.3 MB) of RAM will be required (when the
#    second layer has just been computed, but the memory occupied by the first layer
#    is not released yet). But wait, you also need to add the memory occupied by the
#    CNN’s parameters. We computed earlier that it has 903,400 parameters, each
#    using up 4 bytes, so this adds 3,613,600 bytes (about 3.4 MB). The total RAM
#    required is (at least) 18,613,600 bytes (about 17.8 MB).
# 
# 
# 
#                                                                     Exercise Solutions   |   489
# 
#                      Download from finelybook www.finelybook.com
#       Lastly, let’s compute the minimum amount of RAM required when training the
#       CNN on a mini-batch of 50 images. During training TensorFlow uses backpropa‐
#       gation, which requires keeping all values computed during the forward pass until
#       the reverse pass begins. So we must compute the total RAM required by all layers
#       for a single instance and multiply that by 50! At that point let’s start counting in
#       megabytes rather than bytes. We computed before that the three layers require
#       respectively 5.7, 2.9, and 1.4 MB for each instance. That’s a total of 10.0 MB per
#       instance. So for 50 instances the total RAM is 500 MB. Add to that the RAM
#       required by the input images, which is 50 × 4 × 200 × 300 × 3 = 36 million bytes
#       (about 34.3 MB), plus the RAM required for the model parameters, which is
#       about 3.4 MB (computed earlier), plus some RAM for the gradients (we will
#       neglect them since they can be released gradually as backpropagation goes down
#       the layers during the reverse pass). We are up to a total of roughly 500.0 + 34.3 +
#       3.4 = 537.7 MB. And that’s really an optimistic bare minimum.
#  3. If your GPU runs out of memory while training a CNN, here are five things you
#     could try to solve the problem (other than purchasing a GPU with more RAM):
#       • Reduce the mini-batch size.
#       • Reduce dimensionality using a larger stride in one or more layers.
#       • Remove one or more layers.
#       • Use 16-bit floats instead of 32-bit floats.
#       • Distribute the CNN across multiple devices.
# 
#  4. A max pooling layer has no parameters at all, whereas a convolutional layer has
#     quite a few (see the previous questions).
#  5. A local response normalization layer makes the neurons that most strongly acti‐
#     vate inhibit neurons at the same location but in neighboring feature maps, which
#     encourages different feature maps to specialize and pushes them apart, forcing
#     them to explore a wider range of features. It is typically used in the lower layers to
#     have a larger pool of low-level features that the upper layers can build upon.
#  6. The main innovations in AlexNet compared to LeNet-5 are (1) it is much larger
#     and deeper, and (2) it stacks convolutional layers directly on top of each other,
#     instead of stacking a pooling layer on top of each convolutional layer. The main
#     innovation in GoogLeNet is the introduction of inception modules, which make it
#     possible to have a much deeper net than previous CNN architectures, with fewer
#     parameters. Finally, ResNet’s main innovation is the introduction of skip connec‐
#     tions, which make it possible to go well beyond 100 layers. Arguably, its simplic‐
#     ity and consistency are also rather innovative.
# 
# For the solutions to exercises 7, 8, 9, and 10, please see the Jupyter notebooks avail‐
# able at https://github.com/ageron/handson-ml.
# 
# 
# 490   |   Appendix A: Exercise Solutions
# 
#                 Download from finelybook www.finelybook.com
# Chapter 14: Recurrent Neural Networks
# 1. Here are a few RNN applications:
#    • For a sequence-to-sequence RNN: predicting the weather (or any other time
#      series), machine translation (using an encoder–decoder architecture), video
#      captioning, speech to text, music generation (or other sequence generation),
#      identifying the chords of a song.
#    • For a sequence-to-vector RNN: classifying music samples by music genre, ana‐
#      lyzing the sentiment of a book review, predicting what word an aphasic patient
#      is thinking of based on readings from brain implants, predicting the probabil‐
#      ity that a user will want to watch a movie based on her watch history (this is
#      one of many possible implementations of collaborative filtering).
#    • For a vector-to-sequence RNN: image captioning, creating a music playlist
#      based on an embedding of the current artist, generating a melody based on a
#      set of parameters, locating pedestrians in a picture (e.g., a video frame from a
#      self-driving car’s camera).
# 
# 2. In general, if you translate a sentence one word at a time, the result will be terri‐
#    ble. For example, the French sentence “Je vous en prie” means “You are welcome,”
#    but if you translate it one word at a time, you get “I you in pray.” Huh? It is much
#    better to read the whole sentence first and then translate it. A plain sequence-to-
#    sequence RNN would start translating a sentence immediately after reading the
#    first word, while an encoder–decoder RNN will first read the whole sentence and
#    then translate it. That said, one could imagine a plain sequence-to-sequence
#    RNN that would output silence whenever it is unsure about what to say next (just
#    like human translators do when they must translate a live broadcast).
# 3. To classify videos based on the visual content, one possible architecture could be
#    to take (say) one frame per second, then run each frame through a convolutional
#    neural network, feed the output of the CNN to a sequence-to-vector RNN, and
#    finally run its output through a softmax layer, giving you all the class probabili‐
#    ties. For training you would just use cross entropy as the cost function. If you
#    wanted to use the audio for classification as well, you could convert every second
#    of audio to a spectrograph, feed this spectrograph to a CNN, and feed the output
#    of this CNN to the RNN (along with the corresponding output of the other
#    CNN).
# 4. Building an RNN using dynamic_rnn() rather than static_rnn() offers several
#    advantages:
# 
#    • It is based on a while_loop() operation that is able to swap the GPU’s memory
#      to the CPU’s memory during backpropagation, avoiding out-of-memory
#      errors.
# 
#                                                                    Exercise Solutions   |   491
# 
#                    Download from finelybook www.finelybook.com
#       • It is arguably easier to use, as it can directly take a single tensor as input and
#         output (covering all time steps), rather than a list of tensors (one per time
#         step). No need to stack, unstack, or transpose.
#       • It generates a smaller graph, easier to visualize in TensorBoard.
# 
#  5. To handle variable length input sequences, the simplest option is to set the
#     sequence_length parameter when calling the static_rnn() or dynamic_rnn()
#     functions. Another option is to pad the smaller inputs (e.g., with zeros) to make
#     them the same size as the largest input (this may be faster than the first option if
#     the input sequences all have very similar lengths). To handle variable-length out‐
#     put sequences, if you know in advance the length of each output sequence, you
#     can use the sequence_length parameter (for example, consider a sequence-to-
#     sequence RNN that labels every frame in a video with a violence score: the output
#     sequence will be exactly the same length as the input sequence). If you don’t
#     know in advance the length of the output sequence, you can use the padding
#     trick: always output the same size sequence, but ignore any outputs that come
#     after the end-of-sequence token (by ignoring them when computing the cost
#     function).
#  6. To distribute training and execution of a deep RNN across multiple GPUs, a
#     common technique is simply to place each layer on a different GPU (see Chap‐
#     ter 12).
# 
# For the solutions to exercises 7, 8, and 9, please see the Jupyter notebooks available at
# https://github.com/ageron/handson-ml.
# 
# Chapter 15: Autoencoders
#  1. Here are some of the main tasks that autoencoders are used for:
#       • Feature extraction
#       • Unsupervised pretraining
#       • Dimensionality reduction
#       • Generative models
#       • Anomaly detection (an autoencoder is generally bad at reconstructing outliers)
# 
#  2. If you want to train a classifier and you have plenty of unlabeled training data,
#     but only a few thousand labeled instances, then you could first train a deep
#     autoencoder on the full dataset (labeled + unlabeled), then reuse its lower half for
#     the classifier (i.e., reuse the layers up to the codings layer, included) and train the
#     classifier using the labeled data. If you have little labeled data, you probably want
#     to freeze the reused layers when training the classifier.
# 
# 
# 492   |   Appendix A: Exercise Solutions
# 
#                  Download from finelybook www.finelybook.com
# 3. The fact that an autoencoder perfectly reconstructs its inputs does not necessarily
#    mean that it is a good autoencoder; perhaps it is simply an overcomplete autoen‐
#    coder that learned to copy its inputs to the codings layer and then to the outputs.
#    In fact, even if the codings layer contained a single neuron, it would be possible
#    for a very deep autoencoder to learn to map each training instance to a different
#    coding (e.g., the first instance could be mapped to 0.001, the second to 0.002, the
#    third to 0.003, and so on), and it could learn “by heart” to reconstruct the right
#    training instance for each coding. It would perfectly reconstruct its inputs
#    without really learning any useful pattern in the data. In practice such a mapping
#    is unlikely to happen, but it illustrates the fact that perfect reconstructions are not
#    a guarantee that the autoencoder learned anything useful. However, if it produces
#    very bad reconstructions, then it is almost guaranteed to be a bad autoencoder.
#    To evaluate the performance of an autoencoder, one option is to measure the
#    reconstruction loss (e.g., compute the MSE, the mean square of the outputs
#    minus the inputs). Again, a high reconstruction loss is a good sign that the
#    autoencoder is bad, but a low reconstruction loss is not a guarantee that it is
#    good. You should also evaluate the autoencoder according to what it will be used
#    for. For example, if you are using it for unsupervised pretraining of a classifier,
#    then you should also evaluate the classifier’s performance.
# 4. An undercomplete autoencoder is one whose codings layer is smaller than the
#    input and output layers. If it is larger, then it is an overcomplete autoencoder.
#    The main risk of an excessively undercomplete autoencoder is that it may fail to
#    reconstruct the inputs. The main risk of an overcomplete autoencoder is that it
#    may just copy the inputs to the outputs, without learning any useful feature.
# 5. To tie the weights of an encoder layer and its corresponding decoder layer, you
#    simply make the decoder weights equal to the transpose of the encoder weights.
#    This reduces the number of parameters in the model by half, often making train‐
#    ing converge faster with less training data, and reducing the risk of overfitting the
#    training set.
# 6. To visualize the features learned by the lower layer of a stacked autoencoder, a
#    common technique is simply to plot the weights of each neuron, by reshaping
#    each weight vector to the size of an input image (e.g., for MNIST, reshaping a
#    weight vector of shape [784] to [28, 28]). To visualize the features learned by
#    higher layers, one technique is to display the training instances that most activate
#    each neuron.
# 7. A generative model is a model capable of randomly generating outputs that
#    resemble the training instances. For example, once trained successfully on the
#    MNIST dataset, a generative model can be used to randomly generate realistic
#    images of digits. The output distribution is typically similar to the training data.
#    For example, since MNIST contains many images of each digit, the generative
#    model would output roughly the same number of images of each digit. Some
# 
# 
#                                                                     Exercise Solutions   |   493
# 
#                    Download from finelybook www.finelybook.com
#       generative models can be parametrized—for example, to generate only some
#       kinds of outputs. An example of a generative autoencoder is the variational
#       autoencoder.
# 
# For the solutions to exercises 8, 9, and 10, please see the Jupyter notebooks available
# at https://github.com/ageron/handson-ml.
# 
# Chapter 16: Reinforcement Learning
#  1. Reinforcement Learning is an area of Machine Learning aimed at creating agents
#     capable of taking actions in an environment in a way that maximizes rewards
#     over time. There are many differences between RL and regular supervised and
#     unsupervised learning. Here are a few:
#       • In supervised and unsupervised learning, the goal is generally to find patterns
#         in the data. In Reinforcement Learning, the goal is to find a good policy.
#       • Unlike in supervised learning, the agent is not explicitly given the “right”
#         answer. It must learn by trial and error.
#       • Unlike in unsupervised learning, there is a form of supervision, through
#         rewards. We do not tell the agent how to perform the task, but we do tell it
#         when it is making progress or when it is failing.
#       • A Reinforcement Learning agent needs to find the right balance between
#         exploring the environment, looking for new ways of getting rewards, and
#         exploiting sources of rewards that it already knows. In contrast, supervised and
#         unsupervised learning systems generally don’t need to worry about explora‐
#         tion; they just feed on the training data they are given.
#       • In supervised and unsupervised learning, training instances are typically inde‐
#         pendent (in fact, they are generally shuffled). In Reinforcement Learning, con‐
#         secutive observations are generally not independent. An agent may remain in
#         the same region of the environment for a while before it moves on, so consecu‐
#         tive observations will be very correlated. In some cases a replay memory is
#         used to ensure that the training algorithm gets fairly independent observa‐
#         tions.
# 
#  2. Here are a few possible applications of Reinforcement Learning, other than those
#     mentioned in Chapter 16:
#       Music personalization
#          The environment is a user’s personalized web radio. The agent is the software
#          deciding what song to play next for that user. Its possible actions are to play
#          any song in the catalog (it must try to choose a song the user will enjoy) or to
#          play an advertisement (it must try to choose an ad that the user will be inter‐
# 
# 
# 494   |   Appendix A: Exercise Solutions
# 
#                 Download from finelybook www.finelybook.com
#        ested in). It gets a small reward every time the user listens to a song, a larger
#        reward every time the user listens to an ad, a negative reward when the user
#        skips a song or an ad, and a very negative reward if the user leaves.
#    Marketing
#       The environment is your company’s marketing department. The agent is the
#       software that defines which customers a mailing campaign should be sent to,
#       given their profile and purchase history (for each customer it has two possi‐
#       ble actions: send or don’t send). It gets a negative reward for the cost of the
#       mailing campaign, and a positive reward for estimated revenue generated
#       from this campaign.
#    Product delivery
#        Let the agent control a fleet of delivery trucks, deciding what they should
#        pick up at the depots, where they should go, what they should drop off, and
#        so on. They would get positive rewards for each product delivered on time,
#        and negative rewards for late deliveries.
# 3. When estimating the value of an action, Reinforcement Learning algorithms typ‐
#    ically sum all the rewards that this action led to, giving more weight to immediate
#    rewards, and less weight to later rewards (considering that an action has more
#    influence on the near future than on the distant future). To model this, a discount
#    rate is typically applied at each time step. For example, with a discount rate of 0.9,
#    a reward of 100 that is received two time steps later is counted as only 0.92 × 100
#    = 81 when you are estimating the value of the action. You can think of the dis‐
#    count rate as a measure of how much the future is valued relative to the present:
#    if it is very close to 1, then the future is valued almost as much as the present. If it
#    is close to 0, then only immediate rewards matter. Of course, this impacts the
#    optimal policy tremendously: if you value the future, you may be willing to put
#    up with a lot of immediate pain for the prospect of eventual rewards, while if you
#    don’t value the future, you will just grab any immediate reward you can find,
#    never investing in the future.
# 4. To measure the performance of a Reinforcement Learning agent, you can simply
#    sum up the rewards it gets. In a simulated environment, you can run many epi‐
#    sodes and look at the total rewards it gets on average (and possibly look at the
#    min, max, standard deviation, and so on).
# 5. The credit assignment problem is the fact that when a Reinforcement Learning
#    agent receives a reward, it has no direct way of knowing which of its previous
#    actions contributed to this reward. It typically occurs when there is a large delay
#    between an action and the resulting rewards (e.g., during a game of Atari’s Pong,
#    there may be a few dozen time steps between the moment the agent hits the ball
#    and the moment it wins the point). One way to alleviate it is to provide the agent
#    with shorter-term rewards, when possible. This usually requires prior knowledge
# 
# 
#                                                                      Exercise Solutions   |   495
# 
#                    Download from finelybook www.finelybook.com
#       about the task. For example, if we want to build an agent that will learn to play
#       chess, instead of giving it a reward only when it wins the game, we could give it a
#       reward every time it captures one of the opponent’s pieces.
#  6. An agent can often remain in the same region of its environment for a while, so
#     all of its experiences will be very similar for that period of time. This can intro‐
#     duce some bias in the learning algorithm. It may tune its policy for this region of
#     the environment, but it will not perform well as soon as it moves out of this
#     region. To solve this problem, you can use a replay memory; instead of using
#     only the most immediate experiences for learning, the agent will learn based on a
#     buffer of its past experiences, recent and not so recent (perhaps this is why we
#     dream at night: to replay our experiences of the day and better learn from them?).
#  7. An off-policy RL algorithm learns the value of the optimal policy (i.e., the sum of
#     discounted rewards that can be expected for each state if the agent acts opti‐
#     mally), independently of how the agent actually acts. Q-Learning is a good exam‐
#     ple of such an algorithm. In contrast, an on-policy algorithm learns the value of
#     the policy that the agent actually executes, including both exploration and exploi‐
#     tation.
# 
# For the solutions to exercises 8, 9, and 10, please see the Jupyter notebooks available
# at https://github.com/ageron/handson-ml.
# 
# 
# 
# 
# 496   |   Appendix A: Exercise Solutions
# 
#                     Download from finelybook www.finelybook.com
# 
# 
#                                                                          APPENDIX B
#                     Machine Learning Project Checklist
# 
# 
# 
# 
# This checklist can guide you through your Machine Learning projects. There are
# eight main steps:
# 
#  1. Frame the problem and look at the big picture.
#  2. Get the data.
#  3. Explore the data to gain insights.
#  4. Prepare the data to better expose the underlying data patterns to Machine Learn‐
#     ing algorithms.
#  5. Explore many different models and short-list the best ones.
#  6. Fine-tune your models and combine them into a great solution.
#  7. Present your solution.
#  8. Launch, monitor, and maintain your system.
# 
# Obviously, you should feel free to adapt this checklist to your needs.
# 
# Frame the Problem and Look at the Big Picture
#  1. Define the objective in business terms.
#  2. How will your solution be used?
#  3. What are the current solutions/workarounds (if any)?
#  4. How should you frame this problem (supervised/unsupervised, online/offline,
#     etc.)?
#  5. How should performance be measured?
#  6. Is the performance measure aligned with the business objective?
# 
#                                                                                  497
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Appendix A. Exercise Solutions",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Appendix A. Exercise Solutions"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class AppendixA(HierNode):
    def __init__(self):
        super().__init__("Appendix A. Exercise Solutions")
        self.add(Content())

# eof
