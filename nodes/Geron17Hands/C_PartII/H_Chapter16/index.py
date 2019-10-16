# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Learningto.index import Learningto as A_Learningto
from .B_PolicySearch.index import PolicySearch as B_PolicySearch
from .C_Introductionto.index import Introductionto as C_Introductionto
from .D_NeuralNetwork.index import NeuralNetwork as D_NeuralNetwork
from .E_EvaluatingActions.index import EvaluatingActions as E_EvaluatingActions
from .F_PolicyGradients.index import PolicyGradients as F_PolicyGradients
from .G_MarkovDecision.index import MarkovDecision as G_MarkovDecision
from .H_TemporalDifference.index import TemporalDifference as H_TemporalDifference
from .I_Learningto.index import Learningto as I_Learningto
from .J_Exercises.index import Exercises as J_Exercises
from .K_ThankYou.index import ThankYou as K_ThankYou

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                       Download from finelybook www.finelybook.com
# 
# 
#                                                                                            CHAPTER 16
#                                                  Reinforcement Learning
# 
# 
# 
# 
# Reinforcement Learning (RL) is one of the most exciting fields of Machine Learning
# today, and also one of the oldest. It has been around since the 1950s, producing many
# interesting applications over the years,1 in particular in games (e.g., TD-Gammon, a
# Backgammon playing program) and in machine control, but seldom making the
# headline news. But a revolution took place in 2013 when researchers from an English
# startup called DeepMind demonstrated a system that could learn to play just about
# any Atari game from scratch,2 eventually outperforming humans3 in most of them,
# using only raw pixels as inputs and without any prior knowledge of the rules of the
# games.4 This was the first of a series of amazing feats, culminating in March 2016
# with the victory of their system AlphaGo against Lee Sedol, the world champion of
# the game of Go. No program had ever come close to beating a master of this game, let
# alone the world champion. Today the whole field of RL is boiling with new ideas, with
# a wide range of applications. DeepMind was bought by Google for over 500 million
# dollars in 2014.
# So how did they do it? With hindsight it seems rather simple: they applied the power
# of Deep Learning to the field of Reinforcement Learning, and it worked beyond their
# wildest dreams. In this chapter we will first explain what Reinforcement Learning is
# and what it is good at, and then we will present two of the most important techniques
# in deep Reinforcement Learning: policy gradients and deep Q-networks (DQN),
# 
# 
# 1 For more details, be sure to check out Richard Sutton and Andrew Barto’s book on RL, Reinforcement Learn‐
#   ing: An Introduction (MIT Press), or David Silver’s free online RL course at University College London.
# 
# 2 “Playing Atari with Deep Reinforcement Learning,” V. Mnih et al. (2013).
# 3 “Human-level control through deep reinforcement learning,” V. Mnih et al. (2015).
# 4 Check out the videos of DeepMind’s system learning to play Space Invaders, Breakout, and more at https://
#   goo.gl/yTsH6X.
# 
# 
# 
#                                                                                                               437
# 
#                   Download from finelybook www.finelybook.com
# including a discussion of Markov decision processes (MDP). We will use these techni‐
# ques to train a model to balance a pole on a moving cart, and another to play Atari
# games. The same techniques can be used for a wide variety of tasks, from walking
# robots to self-driving cars.
# 
# Learning to Optimize Rewards
# In Reinforcement Learning, a software agent makes observations and takes actions
# within an environment, and in return it receives rewards. Its objective is to learn to act
# in a way that will maximize its expected long-term rewards. If you don’t mind a bit of
# anthropomorphism, you can think of positive rewards as pleasure, and negative
# rewards as pain (the term “reward” is a bit misleading in this case). In short, the agent
# acts in the environment and learns by trial and error to maximize its pleasure and
# minimize its pain.
# This is quite a broad setting, which can apply to a wide variety of tasks. Here are a few
# examples (see Figure 16-1):
# 
#  a. The agent can be the program controlling a walking robot. In this case, the envi‐
#     ronment is the real world, the agent observes the environment through a set of
#     sensors such as cameras and touch sensors, and its actions consist of sending sig‐
#     nals to activate motors. It may be programmed to get positive rewards whenever
#     it approaches the target destination, and negative rewards whenever it wastes
#     time, goes in the wrong direction, or falls down.
#  b. The agent can be the program controlling Ms. Pac-Man. In this case, the environ‐
#     ment is a simulation of the Atari game, the actions are the nine possible joystick
#     positions (upper left, down, center, and so on), the observations are screenshots,
#     and the rewards are just the game points.
#  c. Similarly, the agent can be the program playing a board game such as the game of
#     Go.
#  d. The agent does not have to control a physically (or virtually) moving thing. For
#     example, it can be a smart thermostat, getting rewards whenever it is close to the
#     target temperature and saves energy, and negative rewards when humans need to
#     tweak the temperature, so the agent must learn to anticipate human needs.
#  e. The agent can observe stock market prices and decide how much to buy or sell
#     every second. Rewards are obviously the monetary gains and losses.
# 
# 
# 
# 
# 438   |   Chapter 16: Reinforcement Learning
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 16. Reinforcement Learning",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Chapter 16. Reinforcement Learning"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter16(HierNode):
    def __init__(self):
        super().__init__("Chapter 16. Reinforcement Learning")
        self.add(Content())
        self.add(A_Learningto())
        self.add(B_PolicySearch())
        self.add(C_Introductionto())
        self.add(D_NeuralNetwork())
        self.add(E_EvaluatingActions())
        self.add(F_PolicyGradients())
        self.add(G_MarkovDecision())
        self.add(H_TemporalDifference())
        self.add(I_Learningto())
        self.add(J_Exercises())
        self.add(K_ThankYou())

# eof