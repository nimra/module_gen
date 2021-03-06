# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# robotic manipulation tasks. Google has demonstrated that reinforcement learning
# can be deployed to learn robotic object control, using a factory of robotic arms to
# enable large-scale training on real robots (see Figure 10-1). It’s likely that such
# enhanced learning techniques for robots will begin filtering into the larger robotics
# industry over the next few years.
# 
# 
# 
# 
# Figure 10-1. Google maintains a number of robotic arms that it uses to test deep rein‐
# forcement learning methods for robotic control. This fundamental research will likely
# find its way to the factory floor in the next few years.
# 
# Deep Learning in Agriculture
# Industrial farming is already heavily mechanized, with sophisticated tractors
# deployed to plant and even pick crops. Advances in robotics and in computer vision
# are accelerating this trend toward automation. Convolutional networks have already
# been employed to identify weeds for removal with less pesticide. Other companies
# have experimented with self-driving tractors, automated fruit picking, and algorith‐
# mic crop yield optimization. These are mainly research projects for the time being,
# but these efforts will likely blossom into major deployments over the next decade.
# 
# Using Deep Learning Ethically
# Most of this book has focused on the effective use of deep learning. We’ve covered
# many techniques for building deep models that generalize well on different data
# types. However, it’s also worth spending spending some time thinking about the soci‐
# etal effects of the systems we build as engineers. Deep learning systems unleash a host
# of potentially unsettling applications.
# 
# 228   |   Chapter 10: The Future of Deep Learning
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Deep Learning in Agriculture",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(mbk("# Deep Learning in Agriculture"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DeepLearning(HierNode):
    def __init__(self):
        super().__init__("Deep Learning in Agriculture")
        self.add(Content())

# eof
