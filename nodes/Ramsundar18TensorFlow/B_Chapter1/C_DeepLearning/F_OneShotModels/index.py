# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Figure 1-9. The Google neural machine translation system uses a deep recurrent archi‐
# tecture to process the input sentence and a second deep recurrent architecture to generate
# the translated output sentence.
# 
# One-Shot Models
# One-shot learning is perhaps the most interesting new idea in machine/deep learn‐
# ing. Most deep learning techniques typically require very large amounts of data to
# learn meaningful behavior. The AlexNet architecture, for example, made use of the
# large ILSVRC dataset to learn a visual object detector. However, much work in cogni‐
# tive science has indicated that humans can learn complex concepts from just a few
# examples. Take the example of baby learning about giraffes for the first time. A baby
# shown a single giraffe at the zoo might be capable of learning to recognize all giraffes
# she sees from then on.
# Recent progress in deep learning has started to invent architectures capable of similar
# learning feats. Given only a few examples of a concept (but given ample sources of
# side information), such systems can learn to make meaningful predictions with very
# few datapoints. One recent paper (by an author of this book) used this idea to demon‐
# strate that one-shot architectures can learn even in contexts babies can’t, such as in
# medical drug discovery. A one-shot architecture for drug discovery is illustrated in
# Figure 1-10.
# 
# 
# 
# 
# 10   |   Chapter 1: Introduction to Deep Learning
# 
# Figure 1-10. The one-shot architecture uses a type of convolutional network to transform
# each molecule into a vector. The vector for styrene oxide is compared with vectors from
# the experimental dataset. The label for the most similar datapoint (tosylic acid) is impu‐
# ted for the query.
#                                                               Deep Learning Architectures   |   11
# 
# AlphaGo
# Go is an ancient board game, widely influential in Asia. Computer Go has been a
# major challenge for computer science since the late 1960s. Techniques that enabled
# the computer chess system Deep Blue to beat chess grandmaster Garry Kasparov in
# 1997 don’t scale to Go. Part of the issue is that Go has a much bigger board than
# chess; Go boards are of size 19 × 19 as opposed to 8 × 8 for chess. Since far more
# moves are possible per step, the game tree of possible Go moves expands much more
# quickly, rendering brute force search with contemporary computer hardware insuffi‐
# cient for adequate Go gameplay. Figure 1-11 illustrates a Go board.
# 
# 
# 
# 
# Figure 1-11. An illustration of a Go board. Players alternately place white and black
# pieces on a 19 × 19 grid.
# 
# Master level computer Go was finally achieved by AlphaGo from Google DeepMind.
# AlphaGo proved capable of defeating one of the world’s strongest Go champions, Lee
# Sedol, in a five-game match. Some of the key ideas from AlphaGo include the use of a
# deep value network and deep policy network. The value network provides an esti‐
# mate of the value of a board position. Unlike chess, it’s very difficult to guess whether
# white or black is winning in Go from the board state. The value network solves this
# problem by learning to make this prediction from game outcomes. The policy net‐
# work, on the other hand, helps estimate the best move to take given a current board
# state. The combination of these two techniques with Monte Carlo Tree search (a clas‐
# sical search method) helped overcome the large branching factor in Go games. The
# basic AlphaGo architecture is illustrated in Figure 1-12.
# 
# 
# 
# 
# 12   |   Chapter 1: Introduction to Deep Learning
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "One-Shot Models",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(mbk("# One-Shot Models"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class OneShotModels(HierNode):
    def __init__(self):
        super().__init__("One-Shot Models")
        self.add(Content())

# eof
