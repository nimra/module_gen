# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


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
# For one, convolutional networks will enable the widespread deployment of face
# detection technologies. China has taken a lead in real-world deployment of such sys‐
# tems (Figure 10-2).
# 
# 
# 
# 
# Figure 10-2. The Chinese government has broadly deployed face detection algorithms
# based on convolutional networks. The ability of these systems to track individuals will
# likely mean that anonymity in public settings will be a thing of the past in China.
# 
# Note that omnipresent facial detection will mean that public anonymity will belong to
# the past. Any actions taken in the public sphere will be logged and tracked by corpo‐
# rations and governments. This vision of the future should sound unsettling to anyone
# concerned with the ethical implications of deep learning.
# 
# 
# 
#                                                             Using Deep Learning Ethically   |   229
# 
# The broader lesson here is that when algorithms can understand visual and percep‐
# tual information, nearly all aspects of human life will fall under algorithmic sway.
# This is a macroscopic trend, and it’s not clear that any one engineer will have the
# power to prevent this future from coming into existence. Nonetheless, engineers
# retain the ability to vote with their feet. Your skills are valuable and in demand; don’t
# work for companies following unethical practices and building potentially dangerous
# systems.
# 
#                     Bias in AI
#                     Machine learning and deep learning provide the capabilities to
#                     learn interesting models from data without too much effort. This
#                     solidly mathematical process can provide the mirage of objectivity.
#                     However, it is strongly worth noting that all sorts of bias can creep
#                     into such analyses. Biases in the underlying data, drawn from his‐
#                     torical, prejudiced records, can induce models to learn fundamen‐
#                     tally unfair models. Google infamously once learned that a flawed
#                     visual prediction model had labeled black consumers as gorillas,
#                     likely due to biased training data that lacked adequate representa‐
#                     tion of people of color. While this system was rapidly corrected
#                     once brought to Google’s notice, such failures are deeply troubling
#                     and are emblematic of more fundamental problems of exclusion in
#                     the technology industry.
#                     As AI is increasingly used in applications such as prisoner parole
#                     granting and loan approval processes, it becomes increasingly
#                     important for us to ensure that our models aren’t making racist
#                     assumptions or learning biases already present in historical data. If
#                     you are working on sensitive data, making predictions that may
#                     alter the course of human lives, check twice and check thrice to
#                     make sure that your systems aren’t falling prey to biases.
# 
# 
# Is Artificial General Intelligence Imminent?
# There are widespread discussions about whether artificial general intelligence (AGI)
# will soon come into existence. Experts disagree strongly over whether AGI is worth
# seriously planning for. Our view is that while there’s no harm in doing research on
# “AI value alignment” and “safe reward function” design, the artificial intelligence sys‐
# tems of today and the foreseeable future are unlikely to rapidly achieve sentience. As
# you will have learned first hand, most deep learning systems are simply sophisticated
# numerical engines, prone to many finicky numerical stability issues. It will likely take
# decades of fundamental advances before general intelligence becomes an issue. At the
# same time, as we’ve discussed in the previous section, artificial intelligence is already
# having dramatic impact on human societies and industries. It is absolutely worth
# 
# 
# 
# 230   | Chapter 10: The Future of Deep Learning
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Using Deep Learning Ethically",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Using Deep Learning Ethically"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class UsingDeep(HierNode):
    def __init__(self):
        super().__init__("Using Deep Learning Ethically")
        self.add(Content())

# eof
