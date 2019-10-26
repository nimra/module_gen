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
# Related Magic Commands
# For accessing a batch of previous inputs at once, the %history magic command is
# very helpful. Here is how you can print the first four inputs:
#      In [16]: %history -n 1-4
#         1: import math
#         2: math.sin(2)
#         3: math.cos(2)
#         4: print(In)
# 
# As usual, you can type %history? for more information and a description of options
# available. Other similar magic commands are %rerun (which will re-execute some
# portion of the command history) and %save (which saves some set of the command
# history to a file). For more information, I suggest exploring these using the ? help
# functionality discussed in “Help and Documentation in IPython” on page 3.
# 
# IPython and Shell Commands
# When working interactively with the standard Python interpreter, one of the frustra‐
# tions you’ll face is the need to switch between multiple windows to access Python
# tools and system command-line tools. IPython bridges this gap, and gives you a syn‐
# tax for executing shell commands directly from within the IPython terminal. The
# magic happens with the exclamation point: anything appearing after ! on a line will
# be executed not by the Python kernel, but by the system command line.
# The following assumes you’re on a Unix-like system, such as Linux or Mac OS X.
# Some of the examples that follow will fail on Windows, which uses a different type of
# shell by default (though with the 2016 announcement of native Bash shells on Win‐
# dows, soon this may no longer be an issue!). If you’re unfamiliar with shell com‐
# mands, I’d suggest reviewing the Shell Tutorial put together by the always excellent
# Software Carpentry Foundation.
# 
# Quick Introduction to the Shell
# A full intro to using the shell/terminal/command line is well beyond the scope of this
# chapter, but for the uninitiated we will offer a quick introduction here. The shell is a
# way to interact textually with your computer. Ever since the mid-1980s, when Micro‐
# soft and Apple introduced the first versions of their now ubiquitous graphical operat‐
# ing systems, most computer users have interacted with their operating system
# through familiar clicking of menus and drag-and-drop movements. But operating
# systems existed long before these graphical user interfaces, and were primarily con‐
# trolled through sequences of text input: at the prompt, the user would type a com‐
# mand, and the computer would do what the user told it to. Those early prompt
# 
# 
# 
# 16   |   Chapter 1: IPython: Beyond Normal Python
# 
# systems are the precursors of the shells and terminals that most active data scientists
# still use today.
# Someone unfamiliar with the shell might ask why you would bother with this, when
# you can accomplish many results by simply clicking on icons and menus. A shell user
# might reply with another question: why hunt icons and click menus when you can
# accomplish things much more easily by typing? While it might sound like a typical
# tech preference impasse, when moving beyond basic tasks it quickly becomes clear
# that the shell offers much more control of advanced tasks, though admittedly the
# learning curve can intimidate the average computer user.
# As an example, here is a sample of a Linux/OS X shell session where a user explores,
# creates, and modifies directories and files on their system (osx:~ $ is the prompt,
# and everything after the $ sign is the typed command; text that is preceded by a # is
# meant just as description, rather than something you would actually type in):
#     osx:~ $ echo "hello world"               # echo is like Python's print function
#     hello world
# 
#     osx:~ $ pwd                              # pwd = print working directory
#     /home/jake                               # this is the "path" that we're in
# 
#     osx:~ $ ls                               # ls = list working directory contents
#     notebooks projects
# 
#     osx:~ $ cd projects/                     # cd = change directory
# 
#     osx:projects $ pwd
#     /home/jake/projects
# 
#     osx:projects $ ls
#     datasci_book   mpld3   myproject.txt
# 
#     osx:projects $ mkdir myproject           # mkdir = make new directory
# 
#     osx:projects $ cd myproject/
# 
#     osx:myproject $ mv ../myproject.txt ./   # mv = move file. Here we're moving the
#                                              # file myproject.txt from one directory
#                                              # up (../) to the current directory (./)
#     osx:myproject $ ls
#     myproject.txt
# Notice that all of this is just a compact way to do familiar operations (navigating a
# directory structure, creating a directory, moving a file, etc.) by typing commands
# rather than clicking icons and menus. Note that with just a few commands (pwd, ls,
# cd, mkdir, and cp) you can do many of the most common file operations. It’s when
# you go beyond these basics that the shell approach becomes really powerful.
# 
# 
# 
#                                                            IPython and Shell Commands   |   17
# 
# Shell Commands in IPython
# You can use any command that works at the command line in IPython by prefixing it
# with the ! character. For example, the ls, pwd, and echo commands can be run as
# follows:
#      In [1]: !ls
#      myproject.txt
# 
#      In [2]: !pwd
#      /home/jake/projects/myproject
# 
#      In [3]: !echo "printing from the shell"
#      printing from the shell
# 
# 
# Passing Values to and from the Shell
# Shell commands can not only be called from IPython, but can also be made to inter‐
# act with the IPython namespace. For example, you can save the output of any shell
# command to a Python list using the assignment operator:
#      In [4]: contents = !ls
# 
#      In [5]: print(contents)
#      ['myproject.txt']
# 
#      In [6]: directory = !pwd
# 
#      In [7]: print(directory)
#      ['/Users/jakevdp/notebooks/tmp/myproject']
# Note that these results are not returned as lists, but as a special shell return type
# defined in IPython:
#      In [8]: type(directory)
#      IPython.utils.text.SList
# This looks and acts a lot like a Python list, but has additional functionality, such as
# the grep and fields methods and the s, n, and p properties that allow you to search,
# filter, and display the results in convenient ways. For more information on these, you
# can use IPython’s built-in help features.
# Communication in the other direction—passing Python variables into the shell—is
# possible through the {varname} syntax:
#      In [9]: message = "hello from Python"
# 
#      In [10]: !echo {message}
#      hello from Python
# 
# 
# 
# 
# 18   |   Chapter 1: IPython: Beyond Normal Python
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Quick Introduction to the Shell",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class QuickIntroduction(HierNode):
    def __init__(self):
        super().__init__("Quick Introduction to the Shell")
        self.add(Content())

# eof
