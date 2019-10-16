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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "What Is Machine Learning?",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# What Is Machine Learning?"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class WhatIs(HierNode):
    def __init__(self):
        super().__init__("What Is Machine Learning?")
        self.add(Content())

# eof
