# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# How Do We Know that Learning Has Occurred?
# This question is vital to determine if the learning algorithm can learn a useful pattern
# between the input features and the targets. Let’s create a scenario that will give us better
# insights into appraising the question of determining when learning has occurred.
#     Assume a teacher takes a physics class for 3 months, and at the end of each session,
# the teacher administers a test to ascertain if the student has learned anything.
#     Let’s consider two different scenarios the teacher might use in evaluating the students:
# 
#       1. The teacher evaluates the student with the exact word-for-word
#          questions that were used as sample problems while teaching.
# 
#       2. The teacher evaluates the student with an entirely different but
#          similar set of sample problems that are based on the principles
#          taught in class.
# 
#     In which of these subplots can the teacher ascertain that the student has learned? To
# figure this out, we must consider the two norms of learning:
# 
#       1. Memorization: In the first subplot, it will be incorrect for the
#          teacher to form a basis for learning because the student has
#          seen and most likely memorized the examples during the class
#          sessions. Memorization is when the exact snapshot of a sample
#          is stored for future recollection. Therefore, it is inaccurate to
#          use samples used in training to carry out learning evaluation. In
#          machine learning, this is known as data snooping.
# 
#       2. Generalization: In the second subplot, the teacher can be
#          confident that the assessment serves as an accurate test to
#          evaluate if the student has learned from the session. The ability to
#          use the principles learned to solve previously unseen samples is
#          known as generalization.
# 
#    Hence, we can conclude that learning is the ability to generalize to previously
# unseen samples.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "How Do We Know that Learning Has Occurred?",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# How Do We Know that Learning Has Occurred?"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class HowDo(HierNode):
    def __init__(self):
        super().__init__("How Do We Know that Learning Has Occurred?")
        self.add(Content())

# eof
