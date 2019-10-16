# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                  Download from finelybook www.finelybook.com
# However, in general you will want to reuse only part of the original model (as we will
# discuss in a moment). A simple solution is to configure the Saver to restore only a
# subset of the variables from the original model. For example, the following code
# restores only hidden layers 1, 2, and 3:
#       [...] # build new model with the same definition as before for hidden layers 1-3
# 
#       init = tf.global_variables_initializer()
# 
#       reuse_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES,
#                                      scope="hidden[123]")
#       reuse_vars_dict = dict([(var.name, var.name) for var in reuse_vars])
#       original_saver = tf.Saver(reuse_vars_dict) # saver to restore the original model
# 
#       new_saver = tf.Saver() # saver to save the new model
# 
#       with tf.Session() as sess:
#           sess.run(init)
#           original_saver.restore("./my_original_model.ckpt") # restore layers 1 to 3
#           [...] # train the new model
#           new_saver.save("./my_new_model.ckpt") # save the whole model
# First we build the new model, making sure to copy the original model’s hidden layers
# 1 to 3. We also create a node to initialize all variables. Then we get the list of all vari‐
# ables that were just created with "trainable=True" (which is the default), and we
# keep only the ones whose scope matches the regular expression "hidden[123]" (i.e.,
# we get all trainable variables in hidden layers 1 to 3). Next we create a dictionary
# mapping the name of each variable in the original model to its name in the new
# model (generally you want to keep the exact same names). Then we create a Saver
# that will restore only these variables, and we create another Saver to save the entire
# new model, not just layers 1 to 3. We then start a session and initialize all variables in
# the model, then restore the variable values from the original model’s layers 1 to 3.
# Finally, we train the model on the new task and save it.
# 
#                      The more similar the tasks are, the more layers you want to reuse
#                      (starting with the lower layers). For very similar tasks, you can try
#                      keeping all the hidden layers and just replace the output layer.
# 
# 
# 
# Reusing Models from Other Frameworks
# If the model was trained using another framework, you will need to load the weights
# manually (e.g., using Theano code if it was trained with Theano), then assign them to
# the appropriate variables. This can be quite tedious. For example, the following code
# shows how you would copy the weight and biases from the first hidden layer of a
# model trained using another framework:
# 
# 
# 288   |   Chapter 11: Training Deep Neural Nets
# 
#                   Download from finelybook www.finelybook.com
#     original_w = [...] # Load the weights from the other framework
#     original_b = [...] # Load the biases from the other framework
# 
#     X = tf.placeholder(tf.float32, shape=(None, n_inputs), name="X")
#     hidden1 = fully_connected(X, n_hidden1, scope="hidden1")
#     [...] # # Build the rest of the model
# 
#     # Get a handle on the variables created by fully_connected()
#     with tf.variable_scope("", default_name="", reuse=True): # root scope
#         hidden1_weights = tf.get_variable("hidden1/weights")
#         hidden1_biases = tf.get_variable("hidden1/biases")
# 
#     # Create nodes to assign arbitrary values to the weights and biases
#     original_weights = tf.placeholder(tf.float32, shape=(n_inputs, n_hidden1))
#     original_biases = tf.placeholder(tf.float32, shape=(n_hidden1))
#     assign_hidden1_weights = tf.assign(hidden1_weights, original_weights)
#     assign_hidden1_biases = tf.assign(hidden1_biases, original_biases)
# 
#     init = tf.global_variables_initializer()
# 
#     with tf.Session() as sess:
#         sess.run(init)
#         sess.run(assign_hidden1_weights, feed_dict={original_weights: original_w})
#         sess.run(assign_hidden1_biases, feed_dict={original_biases: original_b})
#         [...] # Train the model on your new task
# 
# 
# Freezing the Lower Layers
# It is likely that the lower layers of the first DNN have learned to detect low-level fea‐
# tures in pictures that will be useful across both image classification tasks, so you can
# just reuse these layers as they are. It is generally a good idea to “freeze” their weights
# when training the new DNN: if the lower-layer weights are fixed, then the higher-
# layer weights will be easier to train (because they won’t have to learn a moving target).
# To freeze the lower layers during training, the simplest solution is to give the opti‐
# mizer the list of variables to train, excluding the variables from the lower layers:
#     train_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES,
#                                    scope="hidden[34]|outputs")
#     training_op = optimizer.minimize(loss, var_list=train_vars)
# The first line gets the list of all trainable variables in hidden layers 3 and 4 and in the
# output layer. This leaves out the variables in the hidden layers 1 and 2. Next we pro‐
# vide this restricted list of trainable variables to the optimizer’s minimize() function.
# Ta-da! Layers 1 and 2 are now frozen: they will not budge during training (these are
# often called frozen layers).
# 
# 
# 
# 
#                                                                Reusing Pretrained Layers   |   289
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Reusing Models from Other Frameworks",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Reusing Models from Other Frameworks"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ReusingModels(HierNode):
    def __init__(self):
        super().__init__("Reusing Models from Other Frameworks")
        self.add(Content())

# eof
