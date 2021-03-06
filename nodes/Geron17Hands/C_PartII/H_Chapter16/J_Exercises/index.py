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
#                   Download from finelybook www.finelybook.com
#                Unfortunately, training is very slow: if you use your laptop for
#                training, it will take days before Ms. Pac-Man gets any good, and if
#                you look at the learning curve, measuring the average rewards per
#                episode, you will notice that it is extremely noisy. At some points
#                there may be no apparent progress for a very long time until sud‐
#                denly the agent learns to survive a reasonable amount of time. As
#                mentioned earlier, one solution is to inject as much prior knowl‐
#                edge as possible into the model (e.g., through preprocessing,
#                rewards, and so on), and you can also try to bootstrap the model by
#                first training it to imitate a basic strategy. In any case, RL still
#                requires quite a lot of patience and tweaking, but the end result is
#                very exciting.
# 
# 
# Exercises
#  1. How would you define Reinforcement Learning? How is it different from regular
#     supervised or unsupervised learning?
#  2. Can you think of three possible applications of RL that were not mentioned in
#     this chapter? For each of them, what is the environment? What is the agent?
#     What are possible actions? What are the rewards?
#  3. What is the discount rate? Can the optimal policy change if you modify the dis‐
#     count rate?
#  4. How do you measure the performance of a Reinforcement Learning agent?
#  5. What is the credit assignment problem? When does it occur? How can you allevi‐
#     ate it?
#  6. What is the point of using a replay memory?
#  7. What is an off-policy RL algorithm?
#  8. Use Deep Q-Learning to tackle OpenAI gym’s “BypedalWalker-v2.” The Q-
#     networks do not need to be very deep for this task.
#  9. Use policy gradients to train an agent to play Pong, the famous Atari game (Pong-
#     v0 in the OpenAI gym). Beware: an individual observation is insufficient to tell
#     the direction and speed of the ball. One solution is to pass two observations at a
#     time to the neural network policy. To reduce dimensionality and speed up train‐
#     ing, you should definitely preprocess these images (crop, resize, and convert
#     them to black and white), and possibly merge them into a single image (e.g., by
#     overlaying them).
# 10. If you have about $100 to spare, you can purchase a Raspberry Pi 3 plus some
#     cheap robotics components, install TensorFlow on the Pi, and go wild! For an
#     example, check out this fun post by Lukas Biewald, or take a look at GoPiGo or
#     BrickPi. Why not try to build a real-life cartpole by training the robot using pol‐
# 
# 
#                                                                              Exercises   |   469
# 
#                     Download from finelybook www.finelybook.com
#       icy gradients? Or build a robotic spider that learns to walk; give it rewards any
#       time it gets closer to some objective (you will need sensors to measure the dis‐
#       tance to the objective). The only limit is your imagination.
# 
# Solutions to these exercises are available in Appendix A.
# 
# Thank You!
# Before we close the last chapter of this book, I would like to thank you for reading it
# up to the last paragraph. I truly hope that you had as much pleasure reading this book
# as I had writing it, and that it will be useful for your projects, big or small.
# If you find errors, please send feedback. More generally, I would love to know what
# you think, so please don’t hesitate to contact me via O’Reilly, or through the ageron/
# handson-ml GitHub project.
# Going forward, my best advice to you is to practice and practice: try going through all
# the exercises if you have not done so already, play with the Jupyter notebooks, join
# Kaggle.com or some other ML community, watch ML courses, read papers, attend
# conferences, meet experts. You may also want to study some topics that we did not
# cover in this book, including recommender systems, clustering algorithms, anomaly
# detection algorithms, and genetic algorithms.
# My greatest hope is that this book will inspire you to build a wonderful ML applica‐
# tion that will benefit all of us! What will it be?
# Aurélien Géron, November 26th, 2016
# 
# 
# 
# 
# 470   |   Chapter 16: Reinforcement Learning
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Exercises",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Exercises(HierNode):
    def __init__(self):
        super().__init__("Exercises")
        self.add(Content(), "content")

# eof
