# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                    Download from finelybook www.finelybook.com
# you want.2 If you have several servers on one machine, you will need to ensure that
# they don’t all try to grab all the RAM of every GPU, as explained earlier. For example,
# in Figure 12-6 the "ps" task does not see the GPU devices, since presumably its pro‐
# cess was launched with CUDA_VISIBLE_DEVICES="". Note that the CPU is shared by
# all tasks located on the same machine.
# If you want the process to do nothing other than run the TensorFlow server, you can
# block the main thread by telling it to wait for the server to finish using the join()
# method (otherwise the server will be killed as soon as your main thread exits). Since
# there is currently no way to stop the server, this will actually block forever:
#      server.join()        # blocks until the server stops (i.e., never)
# 
# 
# Opening a Session
# Once all the tasks are up and running (doing nothing yet), you can open a session on
# any of the servers, from a client located in any process on any machine (even from a
# process running one of the tasks), and use that session like a regular local session. For
# example:
#      a = tf.constant(1.0)
#      b = a + 2
#      c = a * 3
# 
#      with tf.Session("grpc://machine-b.example.com:2222") as sess:
#          print(c.eval()) # 9.0
# This client code first creates a simple graph, then opens a session on the TensorFlow
# server located on machine B (which we will call the master), and instructs it to evalu‐
# ate c. The master starts by placing the operations on the appropriate devices. In this
# example, since we did not pin any operation on any device, the master simply places
# them all on its own default device—in this case, machine B’s GPU device. Then it just
# evaluates c as instructed by the client, and it returns the result.
# 
# The Master and Worker Services
# The client uses the gRPC protocol (Google Remote Procedure Call) to communicate
# with the server. This is an efficient open source framework to call remote functions
# and get their outputs across a variety of platforms and languages.3 It is based on
# HTTP2, which opens a connection and leaves it open during the whole session,
# allowing efficient bidirectional communication once the connection is established.
# 
# 
# 2 You can even start multiple tasks in the same process. It may be useful for tests, but it is not recommended in
#   production.
# 3 It is the next version of Google’s internal Stubby service, which Google has used successfully for over a decade.
#   See http://grpc.io/ for more details.
# 
# 
# 
#                                                                    Multiple Devices Across Multiple Servers   |   325
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Opening a Session",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Opening a Session"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Openinga(HierNode):
    def __init__(self):
        super().__init__("Opening a Session")
        self.add(Content())

# eof
