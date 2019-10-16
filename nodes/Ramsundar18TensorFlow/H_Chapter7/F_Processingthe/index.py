# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Codefor.index import Codefor as A_Codefor
from .B_LoadingData.index import LoadingData as B_LoadingData
from .C_TheBasic.index import TheBasic as C_TheBasic
from .D_Challengefor.index import Challengefor as D_Challengefor

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                Recurrent Networks Are Turing Complete
#                Perhaps unsurprisingly, NTMs are capable of performing any com‐
#                putation a Turing machine can and are consequently Turing com‐
#                plete. However, a less known fact is that vanilla recurrent neural
#                networks are themselves Turing complete! Put another way, in
#                principle, a recurrent neural network is capable of learning to per‐
#                form arbitrary computation.
#                The basic idea is that the transition operator can learn to perform
#                basic reading, writing, and storage operations. The unrolling of the
#                recurrent network over time allows for the performance of com‐
#                plex computations. In some sense, this fact shouldn’t be too
#                surprising. The universal approximation theorem already demon‐
#                strates that fully connected networks are capable of learning arbi‐
#                trary functions. Chaining arbitrary functions together over time
#                leads to arbitrary computations. (The technical details required to
#                formally prove this are formidable, though.)
# 
# 
# Working with Recurrent Neural Networks in Practice
# In this section, you will learn about the use of recurrent neural networks for language
# modeling on the Penn Treebank dataset, a natural language dataset built from Wall
# Street Journal articles. We will introduce the TensorFlow primitives needed to per‐
# form this modeling and will also walk you through the data handling and preprocess‐
# ing steps needed to prepare data for training. We encourage you to follow along and
# try running the code in the GitHub repo associated with the book.
# 
# Processing the Penn Treebank Corpus
# The Penn Treebank contains a million-word corpus of Wall Street Journal articles.
# This corpus can be used for either character-level or word-level modeling (the tasks
# of predicting the next character or word in a sentence given those preceding). The
# efficacy of models is measured using the perplexity of trained models (more on this
# metric later).
# The Penn Treebank corpus consists of sentences. How can we transform sentences
# into a form that can be fed to machine learning systems such as recurrent language
# models? Recall that machine learning models accept tensors (with recurrent models
# accepting sequences of tensors) as input. Consequently, we need to transform words
# into tensors for machine learning.
# The simplest method of transforming words into vectors is to use “one-hot” encod‐
# ing. In this encoding, let’s suppose that our language dataset uses a vocabulary that
# has V words. Then each word is transformed into a vector of shape V . All the
# 
# 
# 
#                                            Working with Recurrent Neural Networks in Practice   |   159
# 
# entries of this vector are zero, except for one entry, at the index that corresponds to
# the current word. For an example of this embedding, see Figure 7-10.
# 
# 
# 
# 
# Figure 7-10. One-hot encodings transform words into vectors with only one nonzero
# entry (which is typically set to one). Different indices in the vector uniquely represent
# words in a language corpus.
# 
# It’s also possible to use more sophisticated embeddings. The basic idea is similar to
# that for the one-hot encoding. Each word is associated with a unique vector. How‐
# ever, the key difference is that it’s possible to learn this encoding vector directly from
# data to obtain a “word embedding” for the word in question that’s meaningful for the
# dataset at hand. We will show you how to learn word embeddings later in this
# chapter.
# In order to process the Penn Treebank data, we need to find the vocabulary of words
# used in the corpus, then transform each word into its associated word vector. We will
# then show how to feed the processed data into a TensorFlow model.
# 
#                     Penn Treebank Limitations
#                     The Penn Treebank is a very useful dataset for language modeling,
#                     but it no longer poses a challenge for state-of-the-art language
#                     models; researchers have already overfit models on the peculiarities
#                     of this collection. State-of-the-art research would use larger data‐
#                     sets such as the billion-word-corpus language benchmark. How‐
#                     ever, for our exploratory purposes, the Penn Treebank easily
#                     suffices.
# 
# 
# Code for Preprocessing
# The snippet of code in Example 7-1 reads in the raw files associated with the Penn
# Treebank corpus. The corpus is stored with one sentence per line. Some Python
# string handling is done to replace "\n" newline markers with fixed-token "<eos>"
# and then split the file into a list of tokens.
# 
# 
# 
# 160   |   Chapter 7: Recurrent Neural Networks
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Processing the Penn Treebank Corpus",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Processing the Penn Treebank Corpus"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Processingthe(HierNode):
    def __init__(self):
        super().__init__("Processing the Penn Treebank Corpus")
        self.add(Content())
        self.add(A_Codefor())
        self.add(B_LoadingData())
        self.add(C_TheBasic())
        self.add(D_Challengefor())

# eof
