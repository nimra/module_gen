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
#                    Download from finelybook www.finelybook.com
# Loading Data Directly from the Graph
# So far we have assumed that the clients would load the training data and feed it to the
# cluster using placeholders. This is simple and works quite well for simple setups, but
# it is rather inefficient since it transfers the training data several times:
# 
#  1. From the filesystem to the client
#  2. From the client to the master task
#  3. Possibly from the master task to other tasks where the data is needed
# 
# It gets worse if you have several clients training various neural networks using the
# same training data (for example, for hyperparameter tuning): if every client loads the
# data simultaneously, you may end up even saturating your file server or the network’s
# bandwidth.
# 
# Preload the data into a variable
# For datasets that can fit in memory, a better option is to load the training data once
# and assign it to a variable, then just use that variable in your graph. This is called
# preloading the training set. This way the data will be transferred only once from the
# client to the cluster (but it may still need to be moved around from task to task
# depending on which operations need it). The following code shows how to load the
# full training set into a variable:
#     training_set_init = tf.placeholder(tf.float32, shape=(None, n_features))
#     training_set = tf.Variable(training_set_init, trainable=False, collections=[],
#                                name="training_set")
# 
#     with tf.Session([...]) as sess:
#         data = [...] # load the training data from the datastore
#         sess.run(training_set.initializer, feed_dict={training_set_init: data})
# 
# You must set trainable=False so the optimizers don’t try to tweak this variable. You
# should also set collections=[] to ensure that this variable won’t get added to the
# GraphKeys.GLOBAL_VARIABLES collection, which is used for saving and restoring
# checkpoints.
# 
#                  This example assumes that all of your training set (including the
#                  labels) consists only of float32 values. If that’s not the case, you
#                  will need one variable per type.
# 
# 
# 
# Reading the training data directly from the graph
# If the training set does not fit in memory, a good solution is to use reader operations:
# these are operations capable of reading data directly from the filesystem. This way the
# 
#                                                        Multiple Devices Across Multiple Servers   |   335
# 
#                    Download from finelybook www.finelybook.com
# training data never needs to flow through the clients at all. TensorFlow provides read‐
# ers for various file formats:
# 
#   • CSV
#   • Fixed-length binary records
#   • TensorFlow’s own TFRecords format, based on protocol buffers
# 
# Let’s look at a simple example reading from a CSV file (for other formats, please
# check out the API documentation). Suppose you have file named my_test.csv that
# contains training instances, and you want to create operations to read it. Suppose it
# has the following content, with two float features x1 and x2 and one integer target
# representing a binary class:
#       x1, x2, target
#       1. , 2. , 0
#       4. , 5 , 1
#       7. ,    , 0
# 
# First, let’s create a TextLineReader to read this file. A TextLineReader opens a file
# (once we tell it which one to open) and reads lines one by one. It is a stateful opera‐
# tion, like variables and queues: it preserves its state across multiple runs of the graph,
# keeping track of which file it is currently reading and what its current position is in
# this file.
#       reader = tf.TextLineReader(skip_header_lines=1)
# Next, we create a queue that the reader will pull from to know which file to read next.
# We also create an enqueue operation and a placeholder to push any filename we want
# to the queue, and we create an operation to close the queue once we have no more
# files to read:
#       filename_queue = tf.FIFOQueue(capacity=10, dtypes=[tf.string], shapes=[()])
#       filename = tf.placeholder(tf.string)
#       enqueue_filename = filename_queue.enqueue([filename])
#       close_filename_queue = filename_queue.close()
# 
# Now we are ready to create a read operation that will read one record (i.e., a line) at a
# time and return a key/value pair. The key is the record’s unique identifier—a string
# composed of the filename, a colon (:), and the line number—and the value is simply
# a string containing the content of the line:
#       key, value = reader.read(filename_queue)
# We have all we need to read the file line by line! But we are not quite done yet—we
# need to parse this string to get the features and target:
#       x1, x2, target = tf.decode_csv(value, record_defaults=[[-1.], [-1.], [-1]])
#       features = tf.stack([x1, x2])
# 
# 
# 
# 
# 336   |   Chapter 12: Distributing TensorFlow Across Devices and Servers
# 
#                     Download from finelybook www.finelybook.com
# The first line uses TensorFlow’s CSV parser to extract the values from the current
# line. The default values are used when a field is missing (in this example the third
# training instance’s x2 feature), and they are also used to determine the type of each
# field (in this case two floats and one integer).
# Finally, we can push this training instance and its target to a RandomShuffleQueue
# that we will share with the training graph (so it can pull mini-batches from it), and we
# create an operation to close that queue when we are done pushing instances to it:
#     instance_queue = tf.RandomShuffleQueue(
#         capacity=10, min_after_dequeue=2,
#         dtypes=[tf.float32, tf.int32], shapes=[[2],[]],
#         name="instance_q", shared_name="shared_instance_q")
#     enqueue_instance = instance_queue.enqueue([features, target])
#     close_instance_queue = instance_queue.close()
# Wow! That was a lot of work just to read a file. Plus we only created the graph, so now
# we need to run it:
#     with tf.Session([...]) as sess:
#         sess.run(enqueue_filename, feed_dict={filename: "my_test.csv"})
#         sess.run(close_filename_queue)
#         try:
#              while True:
#                  sess.run(enqueue_instance)
#         except tf.errors.OutOfRangeError as ex:
#              pass # no more records in the current file and no more files to read
#         sess.run(close_instance_queue)
# 
# First we open the session, and then we enqueue the filename "my_test.csv" and
# immediately close that queue since we will not enqueue any more filenames. Then we
# run an infinite loop to enqueue instances one by one. The enqueue_instance
# depends on the reader reading the next line, so at every iteration a new record is read
# until it reaches the end of the file. At that point it tries to read the filename queue to
# know which file to read next, and since the queue is closed it throws an OutOfRan
# geError exception (if we did not close the queue, it would just remain blocked until
# we pushed another filename or closed the queue). Lastly, we close the instance queue
# so that the training operations pulling from it won’t get blocked forever. Figure 12-9
# summarizes what we have learned; it represents a typical graph for reading training
# instances from a set of CSV files.
# 
# 
# 
# 
#                                                     Multiple Devices Across Multiple Servers   |   337
# 
#                        Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 12-9. A graph dedicated to reading training instances from CSV files
# 
# In the training graph, you need to create the shared instance queue and simply
# dequeue mini-batches from it:
#       instance_queue = tf.RandomShuffleQueue([...], shared_name="shared_instance_q")
#       mini_batch_instances, mini_batch_targets = instance_queue.dequeue_up_to(2)
#       [...] # use the mini_batch instances and targets to build the training graph
#       training_op = [...]
# 
#       with tf.Session([...]) as sess:
#           try:
#                for step in range(max_steps):
#                    sess.run(training_op)
#           except tf.errors.OutOfRangeError as ex:
#                pass # no more training instances
# In this example, the first mini-batch will contain the first two instances of the CSV
# file, and the second mini-batch will contain the last instance.
# 
#                      TensorFlow queues don’t handle sparse tensors well, so if your
#                      training instances are sparse you should parse the records after the
#                      instance queue.
# 
# 
# 
# This architecture will only use one thread to read records and push them to the
# instance queue. You can get a much higher throughput by having multiple threads
# read simultaneously from multiple files using multiple readers. Let’s see how.
# 
# Multithreaded readers using a Coordinator and a QueueRunner
# To have multiple threads read instances simultaneously, you could create Python
# threads (using the threading module) and manage them yourself. However, Tensor‐
# Flow provides some tools to make this simpler: the Coordinator class and the QueueR
# unner class.
# 
# 
# 
# 338   |   Chapter 12: Distributing TensorFlow Across Devices and Servers
# 
#                   Download from finelybook www.finelybook.com
# A Coordinator is a very simple object whose sole purpose is to coordinate stopping
# multiple threads. First you create a Coordinator:
#     coord = tf.train.Coordinator()
# Then you give it to all threads that need to stop jointly, and their main loop looks like
# this:
#     while not coord.should_stop():
#         [...] # do something
# 
# Any thread can request that every thread stop by calling the Coordinator’s
# request_stop() method:
#     coord.request_stop()
# Every thread will stop as soon as it finishes its current iteration. You can wait for all of
# the threads to finish by calling the Coordinator’s join() method, passing it the list of
# threads:
#     coord.join(list_of_threads)
# 
# A QueueRunner runs multiple threads that each run an enqueue operation repeatedly,
# filling up a queue as fast as possible. As soon as the queue is closed, the next thread
# that tries to push an item to the queue will get an OutOfRangeError; this thread
# catches the error and immediately tells other threads to stop using a Coordinator.
# The following code shows how you can use a QueueRunner to have five threads read‐
# ing instances simultaneously and pushing them to an instance queue:
#     [...] # same construction phase as earlier
#     queue_runner = tf.train.QueueRunner(instance_queue, [enqueue_instance] * 5)
# 
#     with tf.Session() as sess:
#         sess.run(enqueue_filename, feed_dict={filename: "my_test.csv"})
#         sess.run(close_filename_queue)
#         coord = tf.train.Coordinator()
#         enqueue_threads = queue_runner.create_threads(sess, coord=coord, start=True)
# 
# The first line creates the QueueRunner and tells it to run five threads, all running the
# same enqueue_instance operation repeatedly. Then we start a session and we
# enqueue the name of the files to read (in this case just "my_test.csv"). Next we cre‐
# ate a Coordinator that the QueueRunner will use to stop gracefully, as just explained.
# Finally, we tell the QueueRunner to create the threads and start them. The threads will
# read all training instances and push them to the instance queue, and then they will all
# stop gracefully.
# This will be a bit more efficient than earlier, but we can do better. Currently all
# threads are reading from the same file. We can make them read simultaneously from
# separate files instead (assuming the training data is sharded across multiple CSV files)
# by creating multiple readers (see Figure 12-10).
# 
# 
#                                                      Multiple Devices Across Multiple Servers   |   339
# 
#                        Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 12-10. Reading simultaneously from multiple files
# 
# For this we need to write a small function to create a reader and the nodes that will
# read and push one instance to the instance queue:
#       def read_and_push_instance(filename_queue, instance_queue):
#           reader = tf.TextLineReader(skip_header_lines=1)
#           key, value = reader.read(filename_queue)
#           x1, x2, target = tf.decode_csv(value, record_defaults=[[-1.], [-1.], [-1]])
#           features = tf.stack([x1, x2])
#           enqueue_instance = instance_queue.enqueue([features, target])
#           return enqueue_instance
# Next we define the queues:
#       filename_queue = tf.FIFOQueue(capacity=10, dtypes=[tf.string], shapes=[()])
#       filename = tf.placeholder(tf.string)
#       enqueue_filename = filename_queue.enqueue([filename])
#       close_filename_queue = filename_queue.close()
# 
#       instance_queue = tf.RandomShuffleQueue([...])
# 
# And finally we create the QueueRunner, but this time we give it a list of different
# enqueue operations. Each operation will use a different reader, so the threads will
# simultaneously read from different files:
#       read_and_enqueue_ops = [
#           read_and_push_instance(filename_queue, instance_queue)
#           for i in range(5)]
#       queue_runner = tf.train.QueueRunner(instance_queue, read_and_enqueue_ops)
# The execution phase is then the same as before: first push the names of the files to
# read, then create a Coordinator and create and start the QueueRunner threads. This
# time all threads will read from different files simultaneously until all files are read
# entirely, and then the QueueRunner will close the instance queue so that other ops
# pulling from it don’t get blocked.
# 
# 
# 
# 
# 340   |   Chapter 12: Distributing TensorFlow Across Devices and Servers
# 
#                   Download from finelybook www.finelybook.com
# Other convenience functions
# TensorFlow also offers a few convenience functions to simplify some common tasks
# when reading training instances. We will go over just a few (see the API documenta‐
# tion for the full list).
# The string_input_producer() takes a 1D tensor containing a list of filenames, cre‐
# ates a thread that pushes one filename at a time to the filename queue, and then
# closes the queue. If you specify a number of epochs, it will cycle through the file‐
# names once per epoch before closing the queue. By default, it shuffles the filenames at
# each epoch. It creates a QueueRunner to manage its thread, and adds it to the Graph
# Keys.QUEUE_RUNNERS collection. To start every QueueRunner in that collection, you
# can call the tf.train.start_queue_runners() function. Note that if you forget to
# start the QueueRunner, the filename queue will be open and empty, and your readers
# will be blocked forever.
# There are a few other producer functions that similarly create a queue and a corre‐
# sponding QueueRunner for running an enqueue operation (e.g., input_producer(),
# range_input_producer(), and slice_input_producer()).
# The shuffle_batch() function takes a list of tensors (e.g., [features, target]) and
# creates:
# 
#   • A RandomShuffleQueue
#   • A QueueRunner to enqueue the tensors to the queue (added to the Graph
#     Keys.QUEUE_RUNNERS collection)
#   • A dequeue_many operation to extract a mini-batch from the queue
# 
# This makes it easy to manage in a single process a multithreaded input pipeline feed‐
# ing a queue and a training pipeline reading mini-batches from that queue. Also check
# out the batch(), batch_join(), and shuffle_batch_join() functions that provide
# similar functionality.
# Okay! You now have all the tools you need to start training and running neural net‐
# works efficiently across multiple devices and servers on a TensorFlow cluster. Let’s
# review what you have learned:
# 
#   • Using multiple GPU devices
#   • Setting up and starting a TensorFlow cluster
#   • Distributing computations across multiple devices and servers
#   • Sharing variables (and other stateful ops such as queues and readers) across ses‐
#     sions using containers
#   • Coordinating multiple graphs working asynchronously using queues
# 
# 
#                                                    Multiple Devices Across Multiple Servers   |   341
# 
#                 Download from finelybook www.finelybook.com
#   • Reading inputs efficiently using readers, queue runners, and coordinators
# 
# Now let’s use all of this to parallelize neural networks!
# 
# Parallelizing Neural Networks on a TensorFlow Cluster
# In this section, first we will look at how to parallelize several neural networks by sim‐
# ply placing each one on a different device. Then we will look at the much trickier
# problem of training a single neural network across multiple devices and servers.
# 
# One Neural Network per Device
# The most trivial way to train and run neural networks on a TensorFlow cluster is to
# take the exact same code you would use for a single device on a single machine, and
# specify the master server’s address when creating the session. That’s it—you’re done!
# Your code will be running on the server’s default device. You can change the device
# that will run your graph simply by putting your code’s construction phase within a
# device block.
# By running several client sessions in parallel (in different threads or different pro‐
# cesses), connecting them to different servers, and configuring them to use different
# devices, you can quite easily train or run many neural networks in parallel, across all
# devices and all machines in your cluster (see Figure 12-11). The speedup is almost
# linear.4 Training 100 neural networks across 50 servers with 2 GPUs each will not take
# much longer than training just 1 neural network on 1 GPU.
# 
# 
# 
# 
# Figure 12-11. Training one neural network per device
# 
# 
# 4 Not 100% linear if you wait for all devices to finish, since the total time will be the time taken by the slowest
#   device.
# 
# 
# 
# 342   |     Chapter 12: Distributing TensorFlow Across Devices and Servers
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Loading Data Directly from the Graph",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LoadingData(HierNode):
    def __init__(self):
        super().__init__("Loading Data Directly from the Graph")
        self.add(Content(), "content")

# eof
