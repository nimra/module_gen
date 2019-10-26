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

from .A_Reusinga.index import Reusinga as A_Reusinga
from .B_ReusingModels.index import ReusingModels as B_ReusingModels
from .C_Freezingthe.index import Freezingthe as C_Freezingthe
from .D_Cachingthe.index import Cachingthe as D_Cachingthe
from .E_TweakingDropping.index import TweakingDropping as E_TweakingDropping
from .F_ModelZoos.index import ModelZoos as F_ModelZoos
from .G_UnsupervisedPretraining.index import UnsupervisedPretraining as G_UnsupervisedPretraining
from .H_Pretrainingon.index import Pretrainingon as H_Pretrainingon

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                        Download from finelybook www.finelybook.com
#       with tf.Session() as sess:
#           sess.run(init)
# 
#            for epoch in range(n_epochs):
#                [...]
#                for X_batch, y_batch in zip(X_batches, y_batches):
#                    sess.run(training_op,
#                             feed_dict={is_training: True, X: X_batch, y: y_batch})
#                accuracy_score = accuracy.eval(
#                    feed_dict={is_training: False, X: X_test_scaled, y: y_test}))
#                print(accuracy_score)
# That’s all! In this tiny example with just two layers, it’s unlikely that Batch Normaliza‐
# tion will have a very positive impact, but for deeper networks it can make a tremen‐
# dous difference.
# 
# Gradient Clipping
# A popular technique to lessen the exploding gradients problem is to simply clip the
# gradients during backpropagation so that they never exceed some threshold (this is
# mostly useful for recurrent neural networks; see Chapter 14). This is called Gradient
# Clipping.8 In general people now prefer Batch Normalization, but it’s still useful to
# know about Gradient Clipping and how to implement it.
# In TensorFlow, the optimizer’s minimize() function takes care of both computing the
# gradients and applying them, so you must instead call the optimizer’s compute_gradi
# ents() method first, then create an operation to clip the gradients using the
# clip_by_value() function, and finally create an operation to apply the clipped gradi‐
# ents using the optimizer’s apply_gradients() method:
#       threshold = 1.0
#       optimizer = tf.train.GradientDescentOptimizer(learning_rate)
#       grads_and_vars = optimizer.compute_gradients(loss)
#       capped_gvs = [(tf.clip_by_value(grad, -threshold, threshold), var)
#                     for grad, var in grads_and_vars]
#       training_op = optimizer.apply_gradients(capped_gvs)
# 
# You would then run this training_op at every training step, as usual. It will compute
# the gradients, clip them between –1.0 and 1.0, and apply them. The threshold is a
# hyperparameter you can tune.
# 
# Reusing Pretrained Layers
# It is generally not a good idea to train a very large DNN from scratch: instead, you
# should always try to find an existing neural network that accomplishes a similar task
# 
# 
# 8 “On the difficulty of training recurrent neural networks,” R. Pascanu et al. (2013).
# 
# 
# 
# 286   |   Chapter 11: Training Deep Neural Nets
# 
#                    Download from finelybook www.finelybook.com
# to the one you are trying to tackle, then just reuse the lower layers of this network:
# this is called transfer learning. It will not only speed up training considerably, but will
# also require much less training data.
# For example, suppose that you have access to a DNN that was trained to classify pic‐
# tures into 100 different categories, including animals, plants, vehicles, and everyday
# objects. You now want to train a DNN to classify specific types of vehicles. These
# tasks are very similar, so you should try to reuse parts of the first network (see
# Figure 11-4).
# 
# 
# 
# 
# Figure 11-4. Reusing pretrained layers
# 
#                 If the input pictures of your new task don’t have the same size as
#                 the ones used in the original task, you will have to add a prepro‐
#                 cessing step to resize them to the size expected by the original
#                 model. More generally, transfer learning will work only well if the
#                 inputs have similar low-level features.
# 
# 
# Reusing a TensorFlow Model
# If the original model was trained using TensorFlow, you can simply restore it and
# train it on the new task:
#     [...] # construct the original model
# 
#     with tf.Session() as sess:
#         saver.restore(sess, "./my_original_model.ckpt")
#         [...] # Train it on your new task
# 
# 
# 
# 
#                                                                 Reusing Pretrained Layers   |   287
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Reusing Pretrained Layers",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ReusingPretrained(HierNode):
    def __init__(self):
        super().__init__("Reusing Pretrained Layers")
        self.add(Content(), "content")
        self.add(A_Reusinga())
        self.add(B_ReusingModels())
        self.add(C_Freezingthe())
        self.add(D_Cachingthe())
        self.add(E_TweakingDropping())
        self.add(F_ModelZoos())
        self.add(G_UnsupervisedPretraining())
        self.add(H_Pretrainingon())

# eof
