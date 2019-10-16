# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                         Download from finelybook www.finelybook.com
# Policy Search
# The algorithm used by the software agent to determine its actions is called its policy.
# For example, the policy could be a neural network taking observations as inputs and
# outputting the action to take (see Figure 16-2).
# 
# 
# 
# 
# Figure 16-2. Reinforcement Learning using a neural network policy
# 
# The policy can be any algorithm you can think of, and it does not even have to be
# deterministic. For example, consider a robotic vacuum cleaner whose reward is the
# amount of dust it picks up in 30 minutes. Its policy could be to move forward with
# some probability p every second, or randomly rotate left or right with probability 1 –
# p. The rotation angle would be a random angle between –r and +r. Since this policy
# involves some randomness, it is called a stochastic policy. The robot will have an
# erratic trajectory, which guarantees that it will eventually get to any place it can reach
# and pick up all the dust. The question is: how much dust will it pick up in 30
# minutes?
# How would you train such a robot? There are just two policy parameters you can
# tweak: the probability p and the angle range r. One possible learning algorithm could
# be to try out many different values for these parameters, and pick the combination
# that performs best (see Figure 16-3). This is an example of policy search, in this case
# using a brute force approach. However, when the policy space is too large (which is
# generally the case), finding a good set of parameters this way is like searching for a
# needle in a gigantic haystack.
# Another way to explore the policy space is to use genetic algorithms. For example, you
# could randomly create a first generation of 100 policies and try them out, then “kill”
# the 80 worst policies6 and make the 20 survivors produce 4 offspring each. An off‐
# 
# 
# 
# 6 It is often better to give the poor performers a slight chance of survival, to preserve some diversity in the “gene
#   pool.”
# 
# 
# 
# 440   |    Chapter 16: Reinforcement Learning
# 
#                    Download from finelybook www.finelybook.com
# spring is just a copy of its parent7 plus some random variation. The surviving policies
# plus their offspring together constitute the second generation. You can continue to
# iterate through generations this way, until you find a good policy.
# 
# 
# 
# 
# Figure 16-3. Four points in policy space and the agent’s corresponding behavior
# 
# Yet another approach is to use optimization techniques, by evaluating the gradients of
# the rewards with regards to the policy parameters, then tweaking these parameters by
# following the gradient toward higher rewards (gradient ascent). This approach is
# called policy gradients (PG), which we will discuss in more detail later in this chapter.
# For example, going back to the vacuum cleaner robot, you could slightly increase p
# and evaluate whether this increases the amount of dust picked up by the robot in 30
# minutes; if it does, then increase p some more, or else reduce p. We will implement a
# popular PG algorithm using TensorFlow, but before we do we need to create an envi‐
# ronment for the agent to live in, so it’s time to introduce OpenAI gym.
# 
# Introduction to OpenAI Gym
# One of the challenges of Reinforcement Learning is that in order to train an agent,
# you first need to have a working environment. If you want to program an agent that
# will learn to play an Atari game, you will need an Atari game simulator. If you want to
# program a walking robot, then the environment is the real world and you can directly
# train your robot in that environment, but this has its limits: if the robot falls off a cliff,
# you can’t just click “undo.” You can’t speed up time either; adding more computing
# 
# 
# 
# 7 If there is a single parent, this is called asexual reproduction. With two (or more) parents, it is called sexual
#   reproduction. An offspring’s genome (in this case a set of policy parameters) is randomly composed of parts of
#   its parents’ genomes.
# 
# 
# 
#                                                                                  Introduction to OpenAI Gym     |     441
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Policy Search",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Policy Search"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PolicySearch(HierNode):
    def __init__(self):
        super().__init__("Policy Search")
        self.add(Content())

# eof
