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
# 
#                                                                        CHAPTER 10
#                               The Future of Deep Learning
# 
# 
# 
# 
# In this book, we have covered the foundations of modern deep learning. We’ve dis‐
# cussed a wide variety of algorithms, and delved deeply into a number of sophisticated
# case studies. Readers who’ve been working through the examples covered in this book
# are now well prepared to use deep learning on the job, and to start reading the large
# research literature on deep learning methods.
# It’s worth emphasizing how unique this skill set is. Deep learning has had tremendous
# impact in the technology industry already, but deep learning is beginning to dramati‐
# cally alter the state of essentially all nontech industries and to even shift the global
# geopolitical balance. Your understanding of this epochal technology will open many
# doors you may not have envisioned. In this final chapter, we will briefly survey some
# of the important applications of deep learning outside the software industry.
# We will also use this chapter to help you answer the question of how to use your new
# knowledge effectively and ethically. Deep learning is a technology of such power that
# it’s important for practitioners to think about how to use their skills properly. There
# have already been numerous misuses of deep learning, so it behooves new practition‐
# ers to pause before building sophisticated deep learning systems to ask whether the
# systems they are building are ethically sound. We will attempt to provide a brief dis‐
# cussion of ethical best practices, but caution the area of software ethics is complex
# enough that brief discussions are unlikely to do it full justice.
# Finally, we will examine where deep learning is going. Is deep learning the first step
# toward building artificially general intelligences, computational entities that have the
# full range of abilities of humans? There exist a wide range of expert opinions, which
# we survey.
# 
# 
# 
# 
#                                                                                      225
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Review",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(mbk("# Review"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Review(HierNode):
    def __init__(self):
        super().__init__("Review")
        self.add(Content())

# eof
