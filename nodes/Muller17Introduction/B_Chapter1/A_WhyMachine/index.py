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

from .A_ProblemsMachine.index import ProblemsMachine as A_ProblemsMachine
from .B_KnowingYour.index import KnowingYour as B_KnowingYour

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                                                                            CHAPTER 1
#                                                                Introduction
# 
# 
# 
# 
# Machine learning is about extracting knowledge from data. It is a research field at the
# intersection of statistics, artificial intelligence, and computer science and is also
# known as predictive analytics or statistical learning. The application of machine
# learning methods has in recent years become ubiquitous in everyday life. From auto‐
# matic recommendations of which movies to watch, to what food to order or which
# products to buy, to personalized online radio and recognizing your friends in your
# photos, many modern websites and devices have machine learning algorithms at their
# core. When you look at a complex website like Facebook, Amazon, or Netflix, it is
# very likely that every part of the site contains multiple machine learning models.
# Outside of commercial applications, machine learning has had a tremendous influ‐
# ence on the way data-driven research is done today. The tools introduced in this book
# have been applied to diverse scientific problems such as understanding stars, finding
# distant planets, discovering new particles, analyzing DNA sequences, and providing
# personalized cancer treatments.
# Your application doesn’t need to be as large-scale or world-changing as these exam‐
# ples in order to benefit from machine learning, though. In this chapter, we will
# explain why machine learning has become so popular and discuss what kinds of
# problems can be solved using machine learning. Then, we will show you how to build
# your first machine learning model, introducing important concepts along the way.
# 
# Why Machine Learning?
# In the early days of “intelligent” applications, many systems used handcoded rules of
# “if ” and “else” decisions to process data or adjust to user input. Think of a spam filter
# whose job is to move the appropriate incoming email messages to a spam folder. You
# could make up a blacklist of words that would result in an email being marked as
# 
# 
#                                                                                          1
# 
# spam. This would be an example of using an expert-designed rule system to design an
# “intelligent” application. Manually crafting decision rules is feasible for some applica‐
# tions, particularly those in which humans have a good understanding of the process
# to model. However, using handcoded rules to make decisions has two major disad‐
# vantages:
# 
#     • The logic required to make a decision is specific to a single domain and task.
#       Changing the task even slightly might require a rewrite of the whole system.
#     • Designing rules requires a deep understanding of how a decision should be made
#       by a human expert.
# 
# One example of where this handcoded approach will fail is in detecting faces in
# images. Today, every smartphone can detect a face in an image. However, face detec‐
# tion was an unsolved problem until as recently as 2001. The main problem is that the
# way in which pixels (which make up an image in a computer) are “perceived” by the
# computer is very different from how humans perceive a face. This difference in repre‐
# sentation makes it basically impossible for a human to come up with a good set of
# rules to describe what constitutes a face in a digital image.
# Using machine learning, however, simply presenting a program with a large collec‐
# tion of images of faces is enough for an algorithm to determine what characteristics
# are needed to identify a face.
# 
# Problems Machine Learning Can Solve
# The most successful kinds of machine learning algorithms are those that automate
# decision-making processes by generalizing from known examples. In this setting,
# which is known as supervised learning, the user provides the algorithm with pairs of
# inputs and desired outputs, and the algorithm finds a way to produce the desired out‐
# put given an input. In particular, the algorithm is able to create an output for an input
# it has never seen before without any help from a human. Going back to our example
# of spam classification, using machine learning, the user provides the algorithm with a
# large number of emails (which are the input), together with information about
# whether any of these emails are spam (which is the desired output). Given a new
# email, the algorithm will then produce a prediction as to whether the new email is
# spam.
# Machine learning algorithms that learn from input/output pairs are called supervised
# learning algorithms because a “teacher” provides supervision to the algorithms in the
# form of the desired outputs for each example that they learn from. While creating a
# dataset of inputs and outputs is often a laborious manual process, supervised learning
# algorithms are well understood and their performance is easy to measure. If your
# application can be formulated as a supervised learning problem, and you are able to
# 
# 
# 
# 2   |   Chapter 1: Introduction
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Why Machine Learning?",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class WhyMachine(HierNode):
    def __init__(self):
        super().__init__("Why Machine Learning?")
        self.add(Content(), "content")
        self.add(A_ProblemsMachine())
        self.add(B_KnowingYour())

# eof
