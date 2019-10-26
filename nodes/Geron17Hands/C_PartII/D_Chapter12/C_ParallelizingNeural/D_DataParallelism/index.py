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
#                  Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 12-16. Splitting a deep recurrent neural network
# 
# In short, model parallelism can speed up running or training some types of neural
# networks, but not all, and it requires special care and tuning, such as making sure
# that devices that need to communicate the most run on the same machine.
# 
# Data Parallelism
# Another way to parallelize the training of a neural network is to replicate it on each
# device, run a training step simultaneously on all replicas using a different mini-batch
# for each, and then aggregate the gradients to update the model parameters. This is
# called data parallelism (see Figure 12-17).
# 
# 
# 
# 
# Figure 12-17. Data parallelism
# 
# There are two variants of this approach: synchronous updates and asynchronous
# updates.
# 
# 
#                                          Parallelizing Neural Networks on a TensorFlow Cluster   |   347
# 
#                        Download from finelybook www.finelybook.com
# Synchronous updates
# With synchronous updates, the aggregator waits for all gradients to be available before
# computing the average and applying the result (i.e., using the aggregated gradients to
# update the model parameters). Once a replica has finished computing its gradients, it
# must wait for the parameters to be updated before it can proceed to the next mini-
# batch. The downside is that some devices may be slower than others, so all other
# devices will have to wait for them at every step. Moreover, the parameters will be
# copied to every device almost at the same time (immediately after the gradients are
# applied), which may saturate the parameter servers’ bandwidth.
# 
#                      To reduce the waiting time at each step, you could ignore the gradi‐
#                      ents from the slowest few replicas (typically ~10%). For example,
#                      you could run 20 replicas, but only aggregate the gradients from
#                      the fastest 18 replicas at each step, and just ignore the gradients
#                      from the last 2. As soon as the parameters are updated, the first 18
#                      replicas can start working again immediately, without having to
#                      wait for the 2 slowest replicas. This setup is generally described as
#                      having 18 replicas plus 2 spare replicas.5
# 
# Asynchronous updates
# With asynchronous updates, whenever a replica has finished computing the gradi‐
# ents, it immediately uses them to update the model parameters. There is no aggrega‐
# tion (remove the “mean” step in Figure 12-17), and no synchronization. Replicas just
# work independently of the other replicas. Since there is no waiting for the other repli‐
# cas, this approach runs more training steps per minute. Moreover, although the
# parameters still need to be copied to every device at every step, this happens at differ‐
# ent times for each replica so the risk of bandwidth saturation is reduced.
# Data parallelism with asynchronous updates is an attractive choice, because of its
# simplicity, the absence of synchronization delay, and a better use of the bandwidth.
# However, although it works reasonably well in practice, it is almost surprising that it
# works at all! Indeed, by the time a replica has finished computing the gradients based
# on some parameter values, these parameters will have been updated several times by
# other replicas (on average N – 1 times if there are N replicas) and there is no guaran‐
# tee that the computed gradients will still be pointing in the right direction (see
# Figure 12-18). When gradients are severely out-of-date, they are called stale gradients:
# they can slow down convergence, introducing noise and wobble effects (the learning
# 
# 
# 
# 
# 5 This name is slightly confusing since it sounds like some replicas are special, doing nothing. In reality, all rep‐
#   licas are equivalent: they all work hard to be among the fastest at each training step, and the losers vary at
#   every step (unless some devices are really slower than others).
# 
# 
# 
# 348   |   Chapter 12: Distributing TensorFlow Across Devices and Servers
# 
#                 Download from finelybook www.finelybook.com
# curve may contain temporary oscillations), or they can even make the training algo‐
# rithm diverge.
# 
# 
# 
# 
# Figure 12-18. Stale gradients when using asynchronous updates
# 
# There are a few ways to reduce the effect of stale gradients:
# 
#   • Reduce the learning rate.
#   • Drop stale gradients or scale them down.
#   • Adjust the mini-batch size.
#   • Start the first few epochs using just one replica (this is called the warmup phase).
#     Stale gradients tend to be more damaging at the beginning of training, when gra‐
#     dients are typically large and the parameters have not settled into a valley of the
#     cost function yet, so different replicas may push the parameters in quite different
#     directions.
# 
# A paper published by the Google Brain team in April 2016 benchmarked various
# approaches and found that data parallelism with synchronous updates using a few
# spare replicas was the most efficient, not only converging faster but also producing a
# better model. However, this is still an active area of research, so you should not rule
# out asynchronous updates quite yet.
# 
# Bandwidth saturation
# Whether you use synchronous or asynchronous updates, data parallelism still
# requires communicating the model parameters from the parameter servers to every
# replica at the beginning of every training step, and the gradients in the other direction
# at the end of each training step. Unfortunately, this means that there always comes a
# point where adding an extra GPU will not improve performance at all because the
# 
# 
#                                           Parallelizing Neural Networks on a TensorFlow Cluster   |   349
# 
#                 Download from finelybook www.finelybook.com
# time spent moving the data in and out of GPU RAM (and possibly across the net‐
# work) will outweigh the speedup obtained by splitting the computation load. At that
# point, adding more GPUs will just increase saturation and slow down training.
# 
#                      For some models, typically relatively small and trained on a very
#                      large training set, you are often better off training the model on a
#                      single machine with a single GPU.
# 
# 
# 
# Saturation is more severe for large dense models, since they have a lot of parameters
# and gradients to transfer. It is less severe for small models (but the parallelization gain
# is small) and also for large sparse models since the gradients are typically mostly
# zeros, so they can be communicated efficiently. Jeff Dean, initiator and lead of the
# Google Brain project, reported typical speedups of 25–40x when distributing compu‐
# tations across 50 GPUs for dense models, and 300x speedup for sparser models
# trained across 500 GPUs. As you can see, sparse models really do scale better. Here
# are a few concrete examples:
# 
#   • Neural Machine Translation: 6x speedup on 8 GPUs
#   • Inception/ImageNet: 32x speedup on 50 GPUs
#   • RankBrain: 300x speedup on 500 GPUs
# 
# These numbers represent the state of the art in Q1 2016. Beyond a few dozen GPUs
# for a dense model or few hundred GPUs for a sparse model, saturation kicks in and
# performance degrades. There is plenty of research going on to solve this problem
# (exploring peer-to-peer architectures rather than centralized parameter servers, using
# lossy model compression, optimizing when and what the replicas need to communi‐
# cate, and so on), so there will likely be a lot of progress in parallelizing neural net‐
# works in the next few years.
# In the meantime, here are a few simple steps you can take to reduce the saturation
# problem:
# 
#   • Group your GPUs on a few servers rather than scattering them across many
#     servers. This will avoid unnecessary network hops.
#   • Shard the parameters across multiple parameter servers (as discussed earlier).
#   • Drop the model parameters’ float precision from 32 bits (tf.float32) to 16 bits
#     (tf.bfloat16). This will cut in half the amount of data to transfer, without much
#     impact on the convergence rate or the model’s performance.
# 
# 
# 
# 
# 350   |   Chapter 12: Distributing TensorFlow Across Devices and Servers
# 
#                  Download from finelybook www.finelybook.com
#                Although 16-bit precision is the minimum for training neural net‐
#                work, you can actually drop down to 8-bit precision after training
#                to reduce the size of the model and speed up computations. This is
#                called quantizing the neural network. It is particularly useful for
#                deploying and running pretrained models on mobile phones. See
#                Pete Warden’s great post on the subject.
# 
# TensorFlow implementation
# To implement data parallelism using TensorFlow, you first need to choose whether
# you want in-graph replication or between-graph replication, and whether you want
# synchronous updates or asynchronous updates. Let’s look at how you would imple‐
# ment each combination (see the exercises and the Jupyter notebooks for complete
# code examples).
# With in-graph replication + synchronous updates, you build one big graph contain‐
# ing all the model replicas (placed on different devices), and a few nodes to aggregate
# all their gradients and feed them to an optimizer. Your code opens a session to the
# cluster and simply runs the training operation repeatedly.
# With in-graph replication + asynchronous updates, you also create one big graph, but
# with one optimizer per replica, and you run one thread per replica, repeatedly run‐
# ning the replica’s optimizer.
# With between-graph replication + asynchronous updates, you run multiple inde‐
# pendent clients (typically in separate processes), each training the model replica as if
# it were alone in the world, but the parameters are actually shared with other replicas
# (using a resource container).
# With between-graph replication + synchronous updates, once again you run multiple
# clients, each training a model replica based on shared parameters, but this time you
# wrap the optimizer (e.g., a MomentumOptimizer) within a SyncReplicasOptimizer.
# Each replica uses this optimizer as it would use any other optimizer, but under the
# hood this optimizer sends the gradients to a set of queues (one per variable), which is
# read by one of the replica’s SyncReplicasOptimizer, called the chief. The chief aggre‐
# gates the gradients and applies them, then writes a token to a token queue for each
# replica, signaling it that it can go ahead and compute the next gradients. This
# approach supports having spare replicas.
# If you go through the exercises, you will implement each of these four solutions. You
# will easily be able to apply what you have learned to train large deep neural networks
# across dozens of servers and GPUs! In the following chapters we will go through a
# few more important neural network architectures before we tackle Reinforcement
# Learning.
# 
# 
# 
# 
#                                           Parallelizing Neural Networks on a TensorFlow Cluster   |   351
# 
#                        Download from finelybook www.finelybook.com
# Exercises
#  1. If you get a CUDA_ERROR_OUT_OF_MEMORY when starting your TensorFlow pro‐
#     gram, what is probably going on? What can you do about it?
#  2. What is the difference between pinning an operation on a device and placing an
#     operation on a device?
#  3. If you are running on a GPU-enabled TensorFlow installation, and you just use
#     the default placement, will all operations be placed on the first GPU?
#  4. If you pin a variable to "/gpu:0", can it be used by operations placed on /gpu:1?
#     Or by operations placed on "/cpu:0"? Or by operations pinned to devices loca‐
#     ted on other servers?
#  5. Can two operations placed on the same device run in parallel?
#  6. What is a control dependency and when would you want to use one?
#  7. Suppose you train a DNN for days on a TensorFlow cluster, and immediately
#     after your training program ends you realize that you forgot to save the model
#     using a Saver. Is your trained model lost?
#  8. Train several DNNs in parallel on a TensorFlow cluster, using different hyper‐
#     parameter values. This could be DNNs for MNIST classification or any other task
#     you are interested in. The simplest option is to write a single client program that
#     trains only one DNN, then run this program in multiple processes in parallel,
#     with different hyperparameter values for each client. The program should have
#     command-line options to control what server and device the DNN should be
#     placed on, and what resource container and hyperparameter values to use (make
#     sure to use a different resource container for each DNN). Use a validation set or
#     cross-validation to select the top three models.
#  9. Create an ensemble using the top three models from the previous exercise.
#     Define it in a single graph, ensuring that each DNN runs on a different device.
#     Evaluate it on the validation set: does the ensemble perform better than the indi‐
#     vidual DNNs?
# 10. Train a DNN using between-graph replication and data parallelism with asyn‐
#     chronous updates, timing how long it takes to reach a satisfying performance.
#     Next, try again using synchronous updates. Do synchronous updates produce a
#     better model? Is training faster? Split the DNN vertically and place each vertical
#     slice on a different device, and train the model again. Is training any faster? Is the
#     performance any different?
# 
# Solutions to these exercises are available in Appendix A.
# 
# 
# 
# 
# 352   |   Chapter 12: Distributing TensorFlow Across Devices and Servers
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Data Parallelism",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DataParallelism(HierNode):
    def __init__(self):
        super().__init__("Data Parallelism")
        self.add(Content(), "content")

# eof
