# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                 Download from finelybook www.finelybook.com
# moment) control additional stopping conditions (min_samples_split, min_sam
# ples_leaf, min_weight_fraction_leaf, and max_leaf_nodes).
# 
#                      As you can see, the CART algorithm is a greedy algorithm: it greed‐
#                      ily searches for an optimum split at the top level, then repeats the
#                      process at each level. It does not check whether or not the split will
#                      lead to the lowest possible impurity several levels down. A greedy
#                      algorithm often produces a reasonably good solution, but it is not
#                      guaranteed to be the optimal solution.
# 
# Unfortunately, finding the optimal tree is known to be an NP-Complete problem:2 it
# requires O(exp(m)) time, making the problem intractable even for fairly small train‐
# ing sets. This is why we must settle for a “reasonably good” solution.
# 
# Computational Complexity
# Making predictions requires traversing the Decision Tree from the root to a leaf.
# Decision Trees are generally approximately balanced, so traversing the Decision Tree
# requires going through roughly O(log2(m)) nodes.3 Since each node only requires
# checking the value of one feature, the overall prediction complexity is just O(log2(m)),
# independent of the number of features. So predictions are very fast, even when deal‐
# ing with large training sets.
# However, the training algorithm compares all features (or less if max_features is set)
# on all samples at each node. This results in a training complexity of O(n × m log(m)).
# For small training sets (less than a few thousand instances), Scikit-Learn can speed up
# training by presorting the data (set presort=True), but this slows down training con‐
# siderably for larger training sets.
# 
# Gini Impurity or Entropy?
# By default, the Gini impurity measure is used, but you can select the entropy impurity
# measure instead by setting the criterion hyperparameter to "entropy". The concept
# of entropy originated in thermodynamics as a measure of molecular disorder:
# entropy approaches zero when molecules are still and well ordered. It later spread to a
# wide variety of domains, including Shannon’s information theory, where it measures
# 
# 
# 2 P is the set of problems that can be solved in polynomial time. NP is the set of problems whose solutions can
#   be verified in polynomial time. An NP-Hard problem is a problem to which any NP problem can be reduced
#   in polynomial time. An NP-Complete problem is both NP and NP-Hard. A major open mathematical ques‐
#   tion is whether or not P = NP. If P ≠ NP (which seems likely), then no polynomial algorithm will ever be
#   found for any NP-Complete problem (except perhaps on a quantum computer).
# 3 log2 is the binary logarithm. It is equal to log2(m) = log(m) / log(2).
# 
# 
# 
# 172   |   Chapter 6: Decision Trees
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Computational Complexity",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Computational Complexity"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ComputationalComplexity(HierNode):
    def __init__(self):
        super().__init__("Computational Complexity")
        self.add(Content())

# eof
