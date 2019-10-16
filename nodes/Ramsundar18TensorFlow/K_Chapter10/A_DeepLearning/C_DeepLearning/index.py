# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# where the effects of potential drugs are tested indirectly in test tubes and in animals,
# followed by the clinical phase where therapeutics are tested directly in human volun‐
# teers. Medicine that passes both nonhuman and human testing is approved for sale to
# consumers.
# Researchers have begun to construct models that optimize each part of the drug dis‐
# covery process. For example, molecular deep learning has been applied to problems
# such as predicting the potential toxicity of putative medications and to chemical
# problems involved in the synthesis and design of drug-like molecules. Other
# researchers and companies are using deep convolutional networks to design new
# experiments that closely track cellular behavior on massive scales to obtain stronger
# understanding of novel biology. These applications have had some impact on the
# pharmaceutical world, but nothing dramatic yet since it isn’t possible to build one
# drug discovery model that “designs” a novel drug. However, as more data gathering
# efforts continue and more biological and chemical deep learning models are
# designed, this state of affairs could change drastically in the next few years.
# 
# Deep Learning in Law
# The legal industry relies heavily on precedent in the legal literature to make argu‐
# ments about the legality or illegality of new cases. Traditionally, legions of paralegal
# researchers have been employed by large law firms to perform the needed lookups
# into the legal literature. In more recent years, legal search engines have become stan‐
# dard fare for most sophisticated firms.
# Such search algorithms are still relatively immature, and it’s likely that deep learning
# systems for neurolinguistic processing (NLP) can offer significant improvements. For
# example, a number of startups are working on building deep NLP systems that offer
# better querying of legal precedent. Other startups are working on predictive methods
# that use machine learning to predict the outcome of litigation, while a few are even
# experimenting with methods for automated generation of legal arguments.
# In general, these sophisticated applications of deep models will take time to mature,
# but the groundswell of legal AI innovation likely heralds a dramatic shift in the legal
# profession.
# 
# Deep Learning for Robotics
# The robotics industry has traditionally avoided deploying machine learning since it’s
# not easy to prove that machine-learned systems are safe to deploy. This lack of safety
# guarantees can become a major liability when building systems that need to be safe
# for deployment around human operators.
# In recent years, though, it’s become clear that deep reinforcement learning systems,
# combined with low data learning techniques, can offer dramatic improvements in
# 
# 
#                                                    Deep Learning Outside the Tech Industry   |   227
# 
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
            "Deep Learning for Robotics",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Deep Learning for Robotics"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DeepLearning(HierNode):
    def __init__(self):
        super().__init__("Deep Learning for Robotics")
        self.add(Content())

# eof
