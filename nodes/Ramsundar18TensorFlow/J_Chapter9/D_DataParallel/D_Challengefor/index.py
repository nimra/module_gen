# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                       'sec/batch)')
#         print (format_str % (datetime.now(), step, loss_value,
#                              examples_per_sec, sec_per_batch))
# 
#       if step % 100 == 0:
#         summary_str = sess.run(summary_op)
#         summary_writer.add_summary(summary_str, step)
#       # Save the model checkpoint periodically.
# 
#       if step % 1000 == 0 or (step + 1) == FLAGS.max_steps:
#         checkpoint_path = os.path.join(FLAGS.train_dir, 'model.ckpt')
#         saver.save(sess, checkpoint_path, global_step=step)
# 
# 
# Challenge for the Reader
# You now have all the pieces required to train this model in practice. Try running it on
# a suitable GPU server! You may want to use tools such as nvidia-smi to ensure that
# all GPUs are actually being used.
# 
# Review
# In this chapter, you learned about various types of hardware commonly used to train
# deep architectures. You also learned about data parallel and model parallel designs for
# training deep architectures on multiple CPUs or GPUs. We ended the chapter by
# walking through a case study on how to implement data parallel training of convolu‐
# tional networks in TensorFlow.
# In Chapter 10, we will discuss the future of deep learning and how you can use the
# skills you’ve learned in this book effectively and ethically.
# 
# 
# 
# 
#                                                                           Review   |   223
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Challenge for the Reader",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(mbk("# Challenge for the Reader"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Challengefor(HierNode):
    def __init__(self):
        super().__init__("Challenge for the Reader")
        self.add(Content())

# eof
