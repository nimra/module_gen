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
#                                                                           Preface
# 
# 
# 
# 
# Machine learning is an integral part of many commercial applications and research
# projects today, in areas ranging from medical diagnosis and treatment to finding your
# friends on social networks. Many people think that machine learning can only be
# applied by large companies with extensive research teams. In this book, we want to
# show you how easy it can be to build machine learning solutions yourself, and how to
# best go about it. With the knowledge in this book, you can build your own system for
# finding out how people feel on Twitter, or making predictions about global warming.
# The applications of machine learning are endless and, with the amount of data avail‐
# able today, mostly limited by your imagination.
# 
# Who Should Read This Book
# This book is for current and aspiring machine learning practitioners looking to
# implement solutions to real-world machine learning problems. This is an introduc‐
# tory book requiring no previous knowledge of machine learning or artificial intelli‐
# gence (AI). We focus on using Python and the scikit-learn library, and work
# through all the steps to create a successful machine learning application. The meth‐
# ods we introduce will be helpful for scientists and researchers, as well as data scien‐
# tists working on commercial applications. You will get the most out of the book if you
# are somewhat familiar with Python and the NumPy and matplotlib libraries.
# We made a conscious effort not to focus too much on the math, but rather on the
# practical aspects of using machine learning algorithms. As mathematics (probability
# theory, in particular) is the foundation upon which machine learning is built, we
# won’t go into the analysis of the algorithms in great detail. If you are interested in the
# mathematics of machine learning algorithms, we recommend the book The Elements
# of Statistical Learning (Springer) by Trevor Hastie, Robert Tibshirani, and Jerome
# Friedman, which is available for free at the authors’ website. We will also not describe
# how to write machine learning algorithms from scratch, and will instead focus on
# 
# 
# 
#                                                                                         vii
# 
# how to use the large array of models already implemented in scikit-learn and other
# libraries.
# 
# Why We Wrote This Book
# There are many books on machine learning and AI. However, all of them are meant
# for graduate students or PhD students in computer science, and they’re full of
# advanced mathematics. This is in stark contrast with how machine learning is being
# used, as a commodity tool in research and commercial applications. Today, applying
# machine learning does not require a PhD. However, there are few resources out there
# that fully cover all the important aspects of implementing machine learning in prac‐
# tice, without requiring you to take advanced math courses. We hope this book will
# help people who want to apply machine learning without reading up on years’ worth
# of calculus, linear algebra, and probability theory.
# 
# Navigating This Book
# This book is organized roughly as follows:
# 
#    • Chapter 1 introduces the fundamental concepts of machine learning and its
#      applications, and describes the setup we will be using throughout the book.
#    • Chapters 2 and 3 describe the actual machine learning algorithms that are most
#      widely used in practice, and discuss their advantages and shortcomings.
#    • Chapter 4 discusses the importance of how we represent data that is processed by
#      machine learning, and what aspects of the data to pay attention to.
#    • Chapter 5 covers advanced methods for model evaluation and parameter tuning,
#      with a particular focus on cross-validation and grid search.
#    • Chapter 6 explains the concept of pipelines for chaining models and encapsulat‐
#      ing your workflow.
#    • Chapter 7 shows how to apply the methods described in earlier chapters to text
#      data, and introduces some text-specific processing techniques.
#    • Chapter 8 offers a high-level overview, and includes references to more advanced
#      topics.
# 
# While Chapters 2 and 3 provide the actual algorithms, understanding all of these
# algorithms might not be necessary for a beginner. If you need to build a machine
# learning system ASAP, we suggest starting with Chapter 1 and the opening sections of
# Chapter 2, which introduce all the core concepts. You can then skip to “Summary and
# Outlook” on page 127 in Chapter 2, which includes a list of all the supervised models
# that we cover. Choose the model that best fits your needs and flip back to read the
# 
# 
# 
# viii   |   Preface
# 
# section devoted to it for details. Then you can use the techniques in Chapter 5 to eval‐
# uate and tune your model.
# 
# Online Resources
# While studying this book, definitely refer to the scikit-learn website for more in-
# depth documentation of the classes and functions, and many examples. There is also
# a video course created by Andreas Müller, “Advanced Machine Learning with scikit-
# learn,” that supplements this book. You can find it at http://bit.ly/
# advanced_machine_learning_scikit-learn.
# 
# Conventions Used in This Book
# The following typographical conventions are used in this book:
# Italic
#      Indicates new terms, URLs, email addresses, filenames, and file extensions.
# Constant width
#     Used for program listings, as well as within paragraphs to refer to program ele‐
#     ments such as variable or function names, databases, data types, environment
#     variables, statements, and keywords. Also used for commands and module and
#     package names.
# Constant width bold
#     Shows commands or other text that should be typed literally by the user.
# Constant width italic
#     Shows text that should be replaced with user-supplied values or by values deter‐
#     mined by context.
# 
#                This element signifies a tip or suggestion.
# 
# 
# 
# 
#                This element signifies a general note.
# 
# 
# 
# 
#                                                                             Preface   |   ix
# 
#                   This icon indicates a warning or caution.
# 
# 
# 
# 
# Using Code Examples
# Supplemental material (code examples, IPython notebooks, etc.) is available for
# download at https://github.com/amueller/introduction_to_ml_with_python.
# This book is here to help you get your job done. In general, if example code is offered
# with this book, you may use it in your programs and documentation. You do not
# need to contact us for permission unless you’re reproducing a significant portion of
# the code. For example, writing a program that uses several chunks of code from this
# book does not require permission. Selling or distributing a CD-ROM of examples
# from O’Reilly books does require permission. Answering a question by citing this
# book and quoting example code does not require permission. Incorporating a signifi‐
# cant amount of example code from this book into your product’s documentation does
# require permission.
# We appreciate, but do not require, attribution. An attribution usually includes the
# title, author, publisher, and ISBN. For example: “An Introduction to Machine Learning
# with Python by Andreas C. Müller and Sarah Guido (O’Reilly). Copyright 2017 Sarah
# Guido and Andreas Müller, 978-1-449-36941-5.”
# If you feel your use of code examples falls outside fair use or the permission given
# above, feel free to contact us at permissions@oreilly.com.
# 
# Safari® Books Online
#                           Safari Books Online is an on-demand digital library that deliv‐
#                           ers expert content in both book and video form from the
#                           world’s leading authors in technology and business.
# 
# Technology professionals, software developers, web designers, and business and crea‐
# tive professionals use Safari Books Online as their primary resource for research,
# problem solving, learning, and certification training.
# Safari Books Online offers a range of plans and pricing for enterprise, government,
# education, and individuals.
# Members have access to thousands of books, training videos, and prepublication
# manuscripts in one fully searchable database from publishers like O’Reilly Media,
# Prentice Hall Professional, Addison-Wesley Professional, Microsoft Press, Sams, Que,
# 
# 
# x   |   Preface
# 
# Peachpit Press, Focal Press, Cisco Press, John Wiley & Sons, Syngress, Morgan Kauf‐
# mann, IBM Redbooks, Packt, Adobe Press, FT Press, Apress, Manning, New Riders,
# McGraw-Hill, Jones & Bartlett, Course Technology, and hundreds more. For more
# information about Safari Books Online, please visit us online.
# 
# How to Contact Us
# Please address comments and questions concerning this book to the publisher:
# 
#     O’Reilly Media, Inc.
#     1005 Gravenstein Highway North
#     Sebastopol, CA 95472
#     800-998-9938 (in the United States or Canada)
#     707-829-0515 (international or local)
#     707-829-0104 (fax)
# 
# We have a web page for this book, where we list errata, examples, and any additional
# information. You can access this page at http://bit.ly/intro-machine-learning-python.
# To comment or ask technical questions about this book, send email to bookques‐
# tions@oreilly.com.
# For more information about our books, courses, conferences, and news, see our web‐
# site at http://www.oreilly.com.
# Find us on Facebook: http://facebook.com/oreilly
# Follow us on Twitter: http://twitter.com/oreillymedia
# Watch us on YouTube: http://www.youtube.com/oreillymedia
# 
# Acknowledgments
# From Andreas
# Without the help and support of a large group of people, this book would never have
# existed.
# I would like to thank the editors, Meghan Blanchette, Brian MacDonald, and in par‐
# ticular Dawn Schanafelt, for helping Sarah and me make this book a reality.
# I want to thank my reviewers, Thomas Caswell, Olivier Grisel, Stefan van der Walt,
# and John Myles White, who took the time to read the early versions of this book and
# provided me with invaluable feedback—in addition to being some of the corner‐
# stones of the scientific open source ecosystem.
# 
# 
# 
# 
#                                                                          Preface   |   xi
# 
# I am forever thankful for the welcoming open source scientific Python community,
# especially the contributors to scikit-learn. Without the support and help from this
# community, in particular from Gael Varoquaux, Alex Gramfort, and Olivier Grisel, I
# would never have become a core contributor to scikit-learn or learned to under‐
# stand this package as well as I do now. My thanks also go out to all the other contrib‐
# utors who donate their time to improve and maintain this package.
# I’m also thankful for the discussions with many of my colleagues and peers that hel‐
# ped me understand the challenges of machine learning and gave me ideas for struc‐
# turing a textbook. Among the people I talk to about machine learning, I specifically
# want to thank Brian McFee, Daniela Huttenkoppen, Joel Nothman, Gilles Louppe,
# Hugo Bowne-Anderson, Sven Kreis, Alice Zheng, Kyunghyun Cho, Pablo Baberas,
# and Dan Cervone.
# My thanks also go out to Rachel Rakov, who was an eager beta tester and proofreader
# of an early version of this book, and helped me shape it in many ways.
# On the personal side, I want to thank my parents, Harald and Margot, and my sister,
# Miriam, for their continuing support and encouragement. I also want to thank the
# many people in my life whose love and friendship gave me the energy and support to
# undertake such a challenging task.
# 
# From Sarah
# I would like to thank Meg Blanchette, without whose help and guidance this project
# would not have even existed. Thanks to Celia La and Brian Carlson for reading in the
# early days. Thanks to the O’Reilly folks for their endless patience. And finally, thanks
# to DTS, for your everlasting and endless support.
# 
# 
# 
# 
# xii   |   Preface
# 
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
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Preface",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Preface(HierNode):
    def __init__(self):
        super().__init__("Preface")
        self.add(Content(), "content")

# eof
