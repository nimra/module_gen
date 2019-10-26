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
#                      Download from finelybook www.finelybook.com
#                    He initialization considers only the fan-in, not the average between
#                    fan-in and fan-out like in Xavier initialization. This is also the
#                    default for the variance_scaling_initializer() function, but
#                    you can change this by setting the argument mode="FAN_AVG".
# 
# 
# Nonsaturating Activation Functions
# One of the insights in the 2010 paper by Glorot and Bengio was that the vanishing/
# exploding gradients problems were in part due to a poor choice of activation func‐
# tion. Until then most people had assumed that if Mother Nature had chosen to use
# roughly sigmoid activation functions in biological neurons, they must be an excellent
# choice. But it turns out that other activation functions behave much better in deep
# neural networks, in particular the ReLU activation function, mostly because it does
# not saturate for positive values (and also because it is quite fast to compute).
# Unfortunately, the ReLU activation function is not perfect. It suffers from a problem
# known as the dying ReLUs: during training, some neurons effectively die, meaning
# they stop outputting anything other than 0. In some cases, you may find that half of
# your network’s neurons are dead, especially if you used a large learning rate. During
# training, if a neuron’s weights get updated such that the weighted sum of the neuron’s
# inputs is negative, it will start outputting 0. When this happen, the neuron is unlikely
# to come back to life since the gradient of the ReLU function is 0 when its input is
# negative.
# To solve this problem, you may want to use a variant of the ReLU function, such as
# the leaky ReLU. This function is defined as LeakyReLUα(z) = max(αz, z) (see
# Figure 11-2). The hyperparameter α defines how much the function “leaks”: it is the
# slope of the function for z < 0, and is typically set to 0.01. This small slope ensures
# that leaky ReLUs never die; they can go into a long coma, but they have a chance to
# eventually wake up. A recent paper5 compared several variants of the ReLU activation
# function and one of its conclusions was that the leaky variants always outperformed
# the strict ReLU activation function. In fact, setting α = 0.2 (huge leak) seemed to
# result in better performance than α = 0.01 (small leak). They also evaluated the
# randomized leaky ReLU (RReLU), where α is picked randomly in a given range during
# training, and it is fixed to an average value during testing. It also performed fairly well
# and seemed to act as a regularizer (reducing the risk of overfitting the training set).
# Finally, they also evaluated the parametric leaky ReLU (PReLU), where α is authorized
# to be learned during training (instead of being a hyperparameter, it becomes a
# parameter that can be modified by backpropagation like any other parameter). This
# 
# 
# 
# 
# 5 “Empirical Evaluation of Rectified Activations in Convolution Network,” B. Xu et al. (2015).
# 
# 
# 
#                                                                  Vanishing/Exploding Gradients Problems   |   279
# 
#                    Download from finelybook www.finelybook.com
# was reported to strongly outperform ReLU on large image datasets, but on smaller
# datasets it runs the risk of overfitting the training set.
# 
# 
# 
# 
# Figure 11-2. Leaky ReLU
# 
# Last but not least, a 2015 paper by Djork-Arné Clevert et al.6 proposed a new activa‐
# tion function called the exponential linear unit (ELU) that outperformed all the ReLU
# variants in their experiments: training time was reduced and the neural network per‐
# formed better on the test set. It is represented in Figure 11-3, and Equation 11-2
# shows its definition.
# 
#       Equation 11-2. ELU activation function
#                       α exp z − 1 if z < 0
#       ELUα z =
#                       z           ifz ≥ 0
# 
# 
# 
# 
# Figure 11-3. ELU activation function
# 
# 
# 6 “Fast and Accurate Deep Network Learning by Exponential Linear Units (ELUs),” D. Clevert, T. Unterthiner,
#   S. Hochreiter (2015).
# 
# 
# 
# 280    |   Chapter 11: Training Deep Neural Nets
# 
#                     Download from finelybook www.finelybook.com
# It looks a lot like the ReLU function, with a few major differences:
# 
#   • First it takes on negative values when z < 0, which allows the unit to have an
#     average output closer to 0. This helps alleviate the vanishing gradients problem,
#     as discussed earlier. The hyperparameter α defines the value that the ELU func‐
#     tion approaches when z is a large negative number. It is usually set to 1, but you
#     can tweak it like any other hyperparameter if you want.
#   • Second, it has a nonzero gradient for z < 0, which avoids the dying units issue.
#   • Third, the function is smooth everywhere, including around z = 0, which helps
#     speed up Gradient Descent, since it does not bounce as much left and right of z =
#     0.
# 
# The main drawback of the ELU activation function is that it is slower to compute
# than the ReLU and its variants (due to the use of the exponential function), but dur‐
# ing training this is compensated by the faster convergence rate. However, at test time
# an ELU network will be slower than a ReLU network.
# 
#                So which activation function should you use for the hidden layers
#                of your deep neural networks? Although your mileage will vary, in
#                general ELU > leaky ReLU (and its variants) > ReLU > tanh > logis‐
#                tic. If you care a lot about runtime performance, then you may pre‐
#                fer leaky ReLUs over ELUs. If you don’t want to tweak yet another
#                hyperparameter, you may just use the default α values suggested
#                earlier (0.01 for the leaky ReLU, and 1 for ELU). If you have spare
#                time and computing power, you can use cross-validation to evalu‐
#                ate other activation functions, in particular RReLU if your network
#                is overfitting, or PReLU if you have a huge training set.
# 
# TensorFlow offers an elu() function that you can use to build your neural network.
# Simply set the activation_fn argument when calling the fully_connected() func‐
# tion, like this:
#     hidden1 = fully_connected(X, n_hidden1, activation_fn=tf.nn.elu)
# TensorFlow does not have a predefined function for leaky ReLUs, but it is easy
# enough to define:
#     def leaky_relu(z, name=None):
#         return tf.maximum(0.01 * z, z, name=name)
# 
#     hidden1 = fully_connected(X, n_hidden1, activation_fn=leaky_relu)
# 
# 
# 
# 
#                                                     Vanishing/Exploding Gradients Problems   |   281
# 
#                               Download from finelybook www.finelybook.com
# Batch Normalization
# Although using He initialization along with ELU (or any variant of ReLU) can signifi‐
# cantly reduce the vanishing/exploding gradients problems at the beginning of train‐
# ing, it doesn’t guarantee that they won’t come back during training.
# In a 2015 paper,7 Sergey Ioffe and Christian Szegedy proposed a technique called
# Batch Normalization (BN) to address the vanishing/exploding gradients problems,
# and more generally the problem that the distribution of each layer’s inputs changes
# during training, as the parameters of the previous layers change (which they call the
# Internal Covariate Shift problem).
# The technique consists of adding an operation in the model just before the activation
# function of each layer, simply zero-centering and normalizing the inputs, then scaling
# and shifting the result using two new parameters per layer (one for scaling, the other
# for shifting). In other words, this operation lets the model learn the optimal scale and
# mean of the inputs for each layer.
# In order to zero-center and normalize the inputs, the algorithm needs to estimate the
# inputs’ mean and standard deviation. It does so by evaluating the mean and standard
# deviation of the inputs over the current mini-batch (hence the name “Batch Normal‐
# ization”). The whole operation is summarized in Equation 11-3.
# 
#       Equation 11-3. Batch Normalization algorithm
#                                     m
#                   1 B i
#                   mB i ∑
#       1.     μB =         �
#                        =1
#                                     m
#                            1 B i             2
#                            mB i ∑
#                      2
#       2.     σB          =         � − μB
#                                 =1
#                                 i
#                  i           � − μB
#       3.     �           =
#                              σ B2 + �
#                  i              i
#       4.     �           = γ�       +β
# 
# 
#   • μB is the empirical mean, evaluated over the whole mini-batch B.
#   • σB is the empirical standard deviation, also evaluated over the whole mini-batch.
#   • mB is the number of instances in the mini-batch.
# 
# 
# 
# 7 “Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift,” S. Ioffe
#   and C. Szegedy (2015).
# 
# 
# 
# 282    |   Chapter 11: Training Deep Neural Nets
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Nonsaturating Activation Functions",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class NonsaturatingActivation(HierNode):
    def __init__(self):
        super().__init__("Nonsaturating Activation Functions")
        self.add(Content(), "content")

# eof
