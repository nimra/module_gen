# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           Download from finelybook www.finelybook.com
#                        If you already know all the Machine Learning basics, you may want
#                        to skip directly to Chapter 2. If you are not sure, try to answer all
#                        the questions listed at the end of the chapter before moving on.
# 
# 
# 
# 
# What Is Machine Learning?
# Machine Learning is the science (and art) of programming computers so they can
# learn from data.
# Here is a slightly more general definition:
#          [Machine Learning is the] field of study that gives computers the ability to learn
#          without being explicitly programmed.
#             —Arthur Samuel, 1959
# 
# And a more engineering-oriented one:
#          A computer program is said to learn from experience E with respect to some task T
#          and some performance measure P, if its performance on T, as measured by P, improves
#          with experience E.
#             —Tom Mitchell, 1997
# 
# For example, your spam filter is a Machine Learning program that can learn to flag
# spam given examples of spam emails (e.g., flagged by users) and examples of regular
# (nonspam, also called “ham”) emails. The examples that the system uses to learn are
# called the training set. Each training example is called a training instance (or sample).
# In this case, the task T is to flag spam for new emails, the experience E is the training
# data, and the performance measure P needs to be defined; for example, you can use
# the ratio of correctly classified emails. This particular performance measure is called
# accuracy and it is often used in classification tasks.
# If you just download a copy of Wikipedia, your computer has a lot more data, but it is
# not suddenly better at any task. Thus, it is not Machine Learning.
# 
# Why Use Machine Learning?
# Consider how you would write a spam filter using traditional programming techni‐
# ques (Figure 1-1):
# 
#     1. First you would look at what spam typically looks like. You might notice that
#        some words or phrases (such as “4U,” “credit card,” “free,” and “amazing”) tend to
#        come up a lot in the subject. Perhaps you would also notice a few other patterns
#        in the sender’s name, the email’s body, and so on.
# 
# 
# 
# 
# 4    |    Chapter 1: The Machine Learning Landscape
# 
#                Download from finelybook www.finelybook.com
#  2. You would write a detection algorithm for each of the patterns that you noticed,
#     and your program would flag emails as spam if a number of these patterns are
#     detected.
#  3. You would test your program, and repeat steps 1 and 2 until it is good enough.
# 
# 
# 
# 
# Figure 1-1. The traditional approach
# 
# Since the problem is not trivial, your program will likely become a long list of com‐
# plex rules—pretty hard to maintain.
# In contrast, a spam filter based on Machine Learning techniques automatically learns
# which words and phrases are good predictors of spam by detecting unusually fre‐
# quent patterns of words in the spam examples compared to the ham examples
# (Figure 1-2). The program is much shorter, easier to maintain, and most likely more
# accurate.
# 
# 
# 
# 
# Figure 1-2. Machine Learning approach
# 
# 
#                                                             Why Use Machine Learning?   |   5
# 
#                  Download from finelybook www.finelybook.com
# Moreover, if spammers notice that all their emails containing “4U” are blocked, they
# might start writing “For U” instead. A spam filter using traditional programming
# techniques would need to be updated to flag “For U” emails. If spammers keep work‐
# ing around your spam filter, you will need to keep writing new rules forever.
# In contrast, a spam filter based on Machine Learning techniques automatically noti‐
# ces that “For U” has become unusually frequent in spam flagged by users, and it starts
# flagging them without your intervention (Figure 1-3).
# 
# 
# 
# 
# Figure 1-3. Automatically adapting to change
# 
# Another area where Machine Learning shines is for problems that either are too com‐
# plex for traditional approaches or have no known algorithm. For example, consider
# speech recognition: say you want to start simple and write a program capable of dis‐
# tinguishing the words “one” and “two.” You might notice that the word “two” starts
# with a high-pitch sound (“T”), so you could hardcode an algorithm that measures
# high-pitch sound intensity and use that to distinguish ones and twos. Obviously this
# technique will not scale to thousands of words spoken by millions of very different
# people in noisy environments and in dozens of languages. The best solution (at least
# today) is to write an algorithm that learns by itself, given many example recordings
# for each word.
# Finally, Machine Learning can help humans learn (Figure 1-4): ML algorithms can be
# inspected to see what they have learned (although for some algorithms this can be
# tricky). For instance, once the spam filter has been trained on enough spam, it can
# easily be inspected to reveal the list of words and combinations of words that it
# believes are the best predictors of spam. Sometimes this will reveal unsuspected cor‐
# relations or new trends, and thereby lead to a better understanding of the problem.
# Applying ML techniques to dig into large amounts of data can help discover patterns
# that were not immediately apparent. This is called data mining.
# 
# 
# 
# 
# 6   |   Chapter 1: The Machine Learning Landscape
# 
#                  Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 1-4. Machine Learning can help humans learn
# 
# To summarize, Machine Learning is great for:
# 
#   • Problems for which existing solutions require a lot of hand-tuning or long lists of
#     rules: one Machine Learning algorithm can often simplify code and perform bet‐
#     ter.
#   • Complex problems for which there is no good solution at all using a traditional
#     approach: the best Machine Learning techniques can find a solution.
#   • Fluctuating environments: a Machine Learning system can adapt to new data.
#   • Getting insights about complex problems and large amounts of data.
# 
# 
# Types of Machine Learning Systems
# There are so many different types of Machine Learning systems that it is useful to
# classify them in broad categories based on:
# 
#   • Whether or not they are trained with human supervision (supervised, unsuper‐
#     vised, semisupervised, and Reinforcement Learning)
#   • Whether or not they can learn incrementally on the fly (online versus batch
#     learning)
#   • Whether they work by simply comparing new data points to known data points,
#     or instead detect patterns in the training data and build a predictive model, much
#     like scientists do (instance-based versus model-based learning)
# 
# These criteria are not exclusive; you can combine them in any way you like. For
# example, a state-of-the-art spam filter may learn on the fly using a deep neural net‐
# 
# 
# 
#                                                         Types of Machine Learning Systems   |   7
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Why Use Machine Learning?",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Why Use Machine Learning?"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class WhyUse(HierNode):
    def __init__(self):
        super().__init__("Why Use Machine Learning?")
        self.add(Content())

# eof
