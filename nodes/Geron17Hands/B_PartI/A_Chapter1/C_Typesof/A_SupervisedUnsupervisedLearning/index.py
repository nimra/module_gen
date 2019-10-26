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
#                  Download from finelybook www.finelybook.com
# work model trained using examples of spam and ham; this makes it an online, model-
# based, supervised learning system.
# Let’s look at each of these criteria a bit more closely.
# 
# Supervised/Unsupervised Learning
# Machine Learning systems can be classified according to the amount and type of
# supervision they get during training. There are four major categories: supervised
# learning, unsupervised learning, semisupervised learning, and Reinforcement Learn‐
# ing.
# 
# Supervised learning
# In supervised learning, the training data you feed to the algorithm includes the desired
# solutions, called labels (Figure 1-5).
# 
# 
# 
# 
# Figure 1-5. A labeled training set for supervised learning (e.g., spam classification)
# 
# A typical supervised learning task is classification. The spam filter is a good example
# of this: it is trained with many example emails along with their class (spam or ham),
# and it must learn how to classify new emails.
# Another typical task is to predict a target numeric value, such as the price of a car,
# given a set of features (mileage, age, brand, etc.) called predictors. This sort of task is
# called regression (Figure 1-6).1 To train the system, you need to give it many examples
# of cars, including both their predictors and their labels (i.e., their prices).
# 
# 
# 
# 
# 1 Fun fact: this odd-sounding name is a statistics term introduced by Francis Galton while he was studying the
#     fact that the children of tall people tend to be shorter than their parents. Since children were shorter, he called
#     this regression to the mean. This name was then applied to the methods he used to analyze correlations
#     between variables.
# 
# 
# 
# 8    |   Chapter 1: The Machine Learning Landscape
# 
#                      Download from finelybook www.finelybook.com
#                    In Machine Learning an attribute is a data type (e.g., “Mileage”),
#                    while a feature has several meanings depending on the context, but
#                    generally means an attribute plus its value (e.g., “Mileage =
#                    15,000”). Many people use the words attribute and feature inter‐
#                    changeably, though.
# 
# 
# 
# 
# Figure 1-6. Regression
# 
# Note that some regression algorithms can be used for classification as well, and vice
# versa. For example, Logistic Regression is commonly used for classification, as it can
# output a value that corresponds to the probability of belonging to a given class (e.g.,
# 20% chance of being spam).
# Here are some of the most important supervised learning algorithms (covered in this
# book):
# 
#   • k-Nearest Neighbors
#   • Linear Regression
#   • Logistic Regression
#   • Support Vector Machines (SVMs)
#   • Decision Trees and Random Forests
#   • Neural networks2
# 
# 
# 
# 2 Some neural network architectures can be unsupervised, such as autoencoders and restricted Boltzmann
#   machines. They can also be semisupervised, such as in deep belief networks and unsupervised pretraining.
# 
# 
# 
#                                                                       Types of Machine Learning Systems   |   9
# 
#                          Download from finelybook www.finelybook.com
# Unsupervised learning
# In unsupervised learning, as you might guess, the training data is unlabeled
# (Figure 1-7). The system tries to learn without a teacher.
# 
# 
# 
# 
# Figure 1-7. An unlabeled training set for unsupervised learning
# 
# Here are some of the most important unsupervised learning algorithms (we will
# cover dimensionality reduction in Chapter 8):
# 
#      • Clustering
#           — k-Means
#           — Hierarchical Cluster Analysis (HCA)
#           — Expectation Maximization
#      • Visualization and dimensionality reduction
#           — Principal Component Analysis (PCA)
#           — Kernel PCA
#           — Locally-Linear Embedding (LLE)
#           — t-distributed Stochastic Neighbor Embedding (t-SNE)
#      • Association rule learning
#           — Apriori
#           — Eclat
# 
# For example, say you have a lot of data about your blog’s visitors. You may want to
# run a clustering algorithm to try to detect groups of similar visitors (Figure 1-8). At
# no point do you tell the algorithm which group a visitor belongs to: it finds those
# connections without your help. For example, it might notice that 40% of your visitors
# are males who love comic books and generally read your blog in the evening, while
# 20% are young sci-fi lovers who visit during the weekends, and so on. If you use a
# hierarchical clustering algorithm, it may also subdivide each group into smaller
# groups. This may help you target your posts for each group.
# 
# 
# 10    |    Chapter 1: The Machine Learning Landscape
# 
#                       Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 1-8. Clustering
# 
# Visualization algorithms are also good examples of unsupervised learning algorithms:
# you feed them a lot of complex and unlabeled data, and they output a 2D or 3D rep‐
# resentation of your data that can easily be plotted (Figure 1-9). These algorithms try
# to preserve as much structure as they can (e.g., trying to keep separate clusters in the
# input space from overlapping in the visualization), so you can understand how the
# data is organized and perhaps identify unsuspected patterns.
# 
# 
# 
# 
# Figure 1-9. Example of a t-SNE visualization highlighting semantic clusters3
# 
# 
# 
# 3 Notice how animals are rather well separated from vehicles, how horses are close to deer but far from birds,
#   and so on. Figure reproduced with permission from Socher, Ganjoo, Manning, and Ng (2013), “T-SNE visual‐
#   ization of the semantic word space.”
# 
# 
# 
#                                                                        Types of Machine Learning Systems   |     11
# 
#                    Download from finelybook www.finelybook.com
# A related task is dimensionality reduction, in which the goal is to simplify the data
# without losing too much information. One way to do this is to merge several correla‐
# ted features into one. For example, a car’s mileage may be very correlated with its age,
# so the dimensionality reduction algorithm will merge them into one feature that rep‐
# resents the car’s wear and tear. This is called feature extraction.
# 
#                     It is often a good idea to try to reduce the dimension of your train‐
#                     ing data using a dimensionality reduction algorithm before you
#                     feed it to another Machine Learning algorithm (such as a super‐
#                     vised learning algorithm). It will run much faster, the data will take
#                     up less disk and memory space, and in some cases it may also per‐
#                     form better.
# 
# Yet another important unsupervised task is anomaly detection—for example, detect‐
# ing unusual credit card transactions to prevent fraud, catching manufacturing defects,
# or automatically removing outliers from a dataset before feeding it to another learn‐
# ing algorithm. The system is trained with normal instances, and when it sees a new
# instance it can tell whether it looks like a normal one or whether it is likely an anom‐
# aly (see Figure 1-10).
# 
# 
# 
# 
# Figure 1-10. Anomaly detection
# 
# Finally, another common unsupervised task is association rule learning, in which the
# goal is to dig into large amounts of data and discover interesting relations between
# attributes. For example, suppose you own a supermarket. Running an association rule
# on your sales logs may reveal that people who purchase barbecue sauce and potato
# chips also tend to buy steak. Thus, you may want to place these items close to each
# other.
# 
# 
# 
# 
# 12   |   Chapter 1: The Machine Learning Landscape
# 
#                       Download from finelybook www.finelybook.com
# Semisupervised learning
# Some algorithms can deal with partially labeled training data, usually a lot of unla‐
# beled data and a little bit of labeled data. This is called semisupervised learning
# (Figure 1-11).
# Some photo-hosting services, such as Google Photos, are good examples of this. Once
# you upload all your family photos to the service, it automatically recognizes that the
# same person A shows up in photos 1, 5, and 11, while another person B shows up in
# photos 2, 5, and 7. This is the unsupervised part of the algorithm (clustering). Now all
# the system needs is for you to tell it who these people are. Just one label per person,4
# and it is able to name everyone in every photo, which is useful for searching photos.
# 
# 
# 
# 
# Figure 1-11. Semisupervised learning
# 
# Most semisupervised learning algorithms are combinations of unsupervised and
# supervised algorithms. For example, deep belief networks (DBNs) are based on unsu‐
# pervised components called restricted Boltzmann machines (RBMs) stacked on top of
# one another. RBMs are trained sequentially in an unsupervised manner, and then the
# whole system is fine-tuned using supervised learning techniques.
# 
# Reinforcement Learning
# Reinforcement Learning is a very different beast. The learning system, called an agent
# in this context, can observe the environment, select and perform actions, and get
# rewards in return (or penalties in the form of negative rewards, as in Figure 1-12). It
# must then learn by itself what is the best strategy, called a policy, to get the most
# reward over time. A policy defines what action the agent should choose when it is in a
# given situation.
# 
# 
# 
# 4 That’s when the system works perfectly. In practice it often creates a few clusters per person, and sometimes
#   mixes up two people who look alike, so you need to provide a few labels per person and manually clean up
#   some clusters.
# 
# 
# 
#                                                                         Types of Machine Learning Systems   |     13
# 
#                        Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 1-12. Reinforcement Learning
# 
# For example, many robots implement Reinforcement Learning algorithms to learn
# how to walk. DeepMind’s AlphaGo program is also a good example of Reinforcement
# Learning: it made the headlines in March 2016 when it beat the world champion Lee
# Sedol at the game of Go. It learned its winning policy by analyzing millions of games,
# and then playing many games against itself. Note that learning was turned off during
# the games against the champion; AlphaGo was just applying the policy it had learned.
# 
# Batch and Online Learning
# Another criterion used to classify Machine Learning systems is whether or not the
# system can learn incrementally from a stream of incoming data.
# 
# Batch learning
# In batch learning, the system is incapable of learning incrementally: it must be trained
# using all the available data. This will generally take a lot of time and computing
# resources, so it is typically done offline. First the system is trained, and then it is
# launched into production and runs without learning anymore; it just applies what it
# has learned. This is called offline learning.
# If you want a batch learning system to know about new data (such as a new type of
# spam), you need to train a new version of the system from scratch on the full dataset
# (not just the new data, but also the old data), then stop the old system and replace it
# with the new one.
# Fortunately, the whole process of training, evaluating, and launching a Machine
# Learning system can be automated fairly easily (as shown in Figure 1-3), so even a
# 
# 
# 14   |   Chapter 1: The Machine Learning Landscape
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Supervised/Unsupervised Learning",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class SupervisedUnsupervisedLearning(HierNode):
    def __init__(self):
        super().__init__("Supervised/Unsupervised Learning")
        self.add(Content(), "content")

# eof
