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
# Text Entry Shortcuts
# While everyone is familiar with using the Backspace key to delete the previous char‐
# acter, reaching for the key often requires some minor finger gymnastics, and it only
# deletes a single character at a time. In IPython there are several shortcuts for remov‐
# ing some portion of the text you’re typing. The most immediately useful of these are
# the commands to delete entire lines of text. You’ll know these have become second
# nature if you find yourself using a combination of Ctrl-b and Ctrl-d instead of reach‐
# ing for the Backspace key to delete the previous character!
# 
# Keystroke     Action
# Backspace key Delete previous character in line
# Ctrl-d           Delete next character in line
# Ctrl-k           Cut text from cursor to end of line
# Ctrl-u           Cut text from beginning fo line to cursor
# Ctrl-y           Yank (i.e., paste) text that was previously cut
# Ctrl-t           Transpose (i.e., switch) previous two characters
# 
# 
# Command History Shortcuts
# Perhaps the most impactful shortcuts discussed here are the ones IPython provides
# for navigating the command history. This command history goes beyond your cur‐
# rent IPython session: your entire command history is stored in a SQLite database in
# your IPython profile directory. The most straightforward way to access these is with
# the up and down arrow keys to step through the history, but other options exist as
# well:
# 
# Keystroke                         Action
# Ctrl-p (or the up arrow key)      Access previous command in history
# Ctrl-n (or the down arrow key) Access next command in history
# Ctrl-r                            Reverse-search through command history
# 
# The reverse-search can be particularly useful. Recall that in the previous section we
# defined a function called square. Let’s reverse-search our Python history from a new
# IPython shell and find this definition again. When you press Ctrl-r in the IPython
# terminal, you’ll see the following prompt:
#      In [1]:
#      (reverse-i-search)`':
# If you start typing characters at this prompt, IPython will auto-fill the most recent
# command, if any, that matches those characters:
# 
# 
# 
#                                                                            Keyboard Shortcuts in the IPython Shell   |   9
# 
#      In [1]:
#      (reverse-i-search)`sqa': square??
# At any point, you can add more characters to refine the search, or press Ctrl-r again
# to search further for another command that matches the query. If you followed along
# in the previous section, pressing Ctrl-r twice more gives:
#      In [1]:
#      (reverse-i-search)`sqa': def square(a):
#          """Return the square of a"""
#          return a ** 2
# Once you have found the command you’re looking for, press Return and the search
# will end. We can then use the retrieved command, and carry on with our session:
#      In [1]: def square(a):
#          """Return the square of a"""
#          return a ** 2
# 
#      In [2]: square(2)
#      Out[2]: 4
# Note that you can also use Ctrl-p/Ctrl-n or the up/down arrow keys to search
# through history, but only by matching characters at the beginning of the line. That is,
# if you type def and then press Ctrl-p, it would find the most recent command (if any)
# in your history that begins with the characters def.
# 
# Miscellaneous Shortcuts
# Finally, there are a few miscellaneous shortcuts that don’t fit into any of the preceding
# categories, but are nevertheless useful to know:
# 
# Keystroke Action
# Ctrl-l    Clear terminal screen
# Ctrl-c       Interrupt current Python command
# Ctrl-d       Exit IPython session
# 
# The Ctrl-c shortcut in particular can be useful when you inadvertently start a very
# long-running job.
# While some of the shortcuts discussed here may seem a bit tedious at first, they
# quickly become automatic with practice. Once you develop that muscle memory, I
# suspect you will even find yourself wishing they were available in other contexts.
# 
# IPython Magic Commands
# The previous two sections showed how IPython lets you use and explore Python effi‐
# ciently and interactively. Here we’ll begin discussing some of the enhancements that
# 
# 10   |   Chapter 1: IPython: Beyond Normal Python
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Command History Shortcuts",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class CommandHistory(HierNode):
    def __init__(self):
        super().__init__("Command History Shortcuts")
        self.add(Content())

# eof
