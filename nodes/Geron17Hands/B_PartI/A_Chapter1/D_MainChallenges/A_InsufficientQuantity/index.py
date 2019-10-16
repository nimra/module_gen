# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                    Download from finelybook www.finelybook.com
# If all went well, your model will make good predictions. If not, you may need to use
# more attributes (employment rate, health, air pollution, etc.), get more or better qual‐
# ity training data, or perhaps select a more powerful model (e.g., a Polynomial Regres‐
# sion model).
# In summary:
# 
#      • You studied the data.
#      • You selected a model.
#      • You trained it on the training data (i.e., the learning algorithm searched for the
#        model parameter values that minimize a cost function).
#      • Finally, you applied the model to make predictions on new cases (this is called
#        inference), hoping that this model will generalize well.
# 
# This is what a typical Machine Learning project looks like. In Chapter 2 you will
# experience this first-hand by going through an end-to-end project.
# We have covered a lot of ground so far: you now know what Machine Learning is
# really about, why it is useful, what some of the most common categories of ML sys‐
# tems are, and what a typical project workflow looks like. Now let’s look at what can go
# wrong in learning and prevent you from making accurate predictions.
# 
# Main Challenges of Machine Learning
# In short, since your main task is to select a learning algorithm and train it on some
# data, the two things that can go wrong are “bad algorithm” and “bad data.” Let’s start
# with examples of bad data.
# 
# Insufficient Quantity of Training Data
# For a toddler to learn what an apple is, all it takes is for you to point to an apple and
# say “apple” (possibly repeating this procedure a few times). Now the child is able to
# recognize apples in all sorts of colors and shapes. Genius.
# Machine Learning is not quite there yet; it takes a lot of data for most Machine Learn‐
# ing algorithms to work properly. Even for very simple problems you typically need
# thousands of examples, and for complex problems such as image or speech recogni‐
# tion you may need millions of examples (unless you can reuse parts of an existing
# model).
# 
# 
# 
# 
# 22    |   Chapter 1: The Machine Learning Landscape
# 
#                        Download from finelybook www.finelybook.com
# 
#                           The Unreasonable Effectiveness of Data
#    In a famous paper published in 2001, Microsoft researchers Michele Banko and Eric
#    Brill showed that very different Machine Learning algorithms, including fairly simple
#    ones, performed almost identically well on a complex problem of natural language
#    disambiguation8 once they were given enough data (as you can see in Figure 1-20).
# 
# 
# 
# 
#    Figure 1-20. The importance of data versus algorithms9
# 
#    As the authors put it: “these results suggest that we may want to reconsider the trade-
#    off between spending time and money on algorithm development versus spending it
#    on corpus development.”
#    The idea that data matters more than algorithms for complex problems was further
#    popularized by Peter Norvig et al. in a paper titled “The Unreasonable Effectiveness
#    of Data” published in 2009.10 It should be noted, however, that small- and medium-
#    sized datasets are still very common, and it is not always easy or cheap to get extra
#    training data, so don’t abandon algorithms just yet.
# 
# 
# 
# 
#  8 For example, knowing whether to write “to,” “two,” or “too” depending on the context.
#  9 Figure reproduced with permission from Banko and Brill (2001), “Learning Curves for Confusion Set Disam‐
#    biguation.”
# 10 “The Unreasonable Effectiveness of Data,” Peter Norvig et al. (2009).
# 
# 
# 
#                                                                       Main Challenges of Machine Learning   |   23
# 
#                          Download from finelybook www.finelybook.com
# Nonrepresentative Training Data
# In order to generalize well, it is crucial that your training data be representative of the
# new cases you want to generalize to. This is true whether you use instance-based
# learning or model-based learning.
# For example, the set of countries we used earlier for training the linear model was not
# perfectly representative; a few countries were missing. Figure 1-21 shows what the
# data looks like when you add the missing countries.
# 
# 
# 
# 
# Figure 1-21. A more representative training sample
# 
# If you train a linear model on this data, you get the solid line, while the old model is
# represented by the dotted line. As you can see, not only does adding a few missing
# countries significantly alter the model, but it makes it clear that such a simple linear
# model is probably never going to work well. It seems that very rich countries are not
# happier than moderately rich countries (in fact they seem unhappier), and conversely
# some poor countries seem happier than many rich countries.
# By using a nonrepresentative training set, we trained a model that is unlikely to make
# accurate predictions, especially for very poor and very rich countries.
# It is crucial to use a training set that is representative of the cases you want to general‐
# ize to. This is often harder than it sounds: if the sample is too small, you will have
# sampling noise (i.e., nonrepresentative data as a result of chance), but even very large
# samples can be nonrepresentative if the sampling method is flawed. This is called
# sampling bias.
# 
# 
#                                A Famous Example of Sampling Bias
#      Perhaps the most famous example of sampling bias happened during the US presi‐
#      dential election in 1936, which pitted Landon against Roosevelt: the Literary Digest
#      conducted a very large poll, sending mail to about 10 million people. It got 2.4 million
#      answers, and predicted with high confidence that Landon would get 57% of the votes.
# 
# 
# 24     |   Chapter 1: The Machine Learning Landscape
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Insufficient Quantity of Training Data",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Insufficient Quantity of Training Data"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class InsufficientQuantity(HierNode):
    def __init__(self):
        super().__init__("Insufficient Quantity of Training Data")
        self.add(Content())

# eof
