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
# Tables of Pandas String Methods
# If you have a good understanding of string manipulation in Python, most of Pandas’
# string syntax is intuitive enough that it’s probably sufficient to just list a table of avail‐
# able methods; we will start with that here, before diving deeper into a few of the sub‐
# tleties. The examples in this section use the following series of names:
#       In[6]: monte = pd.Series(['Graham Chapman', 'John Cleese', 'Terry Gilliam',
#                                 'Eric Idle', 'Terry Jones', 'Michael Palin'])
# 
# Methods similar to Python string methods
# Nearly all Python’s built-in string methods are mirrored by a Pandas vectorized string
# method. Here is a list of Pandas str methods that mirror Python string methods:
# 
# len()         lower()            translate()         islower()
# ljust()       upper()            startswith() isupper()
# rjust()       find()             endswith()          isnumeric()
# center() rfind()                 isalnum()           isdecimal()
# zfill()       index()            isalpha()           split()
# strip()       rindex()           isdigit()           rsplit()
# rstrip() capitalize() isspace()                      partition()
# lstrip() swapcase()              istitle()           rpartition()
# 
# 
# Notice that these have various return values. Some, like lower(), return a series of
# strings:
#       In[7]: monte.str.lower()
#       Out[7]: 0    graham chapman
#               1       john cleese
#               2     terry gilliam
#               3         eric idle
#               4       terry jones
#               5     michael palin
#               dtype: object
# But some others return numbers:
#       In[8]: monte.str.len()
#       Out[8]: 0    14
#               1    11
#               2    13
#               3     9
#               4    11
#               5    13
#               dtype: int64
# 
# 
# 
# 180   |   Chapter 3: Data Manipulation with Pandas
# 
# Or Boolean values:
#     In[9]: monte.str.startswith('T')
#     Out[9]: 0    False
#             1    False
#             2     True
#             3    False
#             4     True
#             5    False
#             dtype: bool
# Still others return lists or other compound values for each element:
#     In[10]: monte.str.split()
#     Out[10]: 0    [Graham, Chapman]
#              1       [John, Cleese]
#              2     [Terry, Gilliam]
#              3         [Eric, Idle]
#              4       [Terry, Jones]
#              5     [Michael, Palin]
#              dtype: object
# We’ll see further manipulations of this kind of series-of-lists object as we continue
# our discussion.
# 
# Methods using regular expressions
# In addition, there are several methods that accept regular expressions to examine the
# content of each string element, and follow some of the API conventions of Python’s
# built-in re module (see Table 3-4).
# 
# Table 3-4. Mapping between Pandas methods and functions in Python’s re module
# Method        Description
# match()       Call re.match() on each element, returning a Boolean.
# extract()     Call re.match() on each element, returning matched groups as strings.
# findall()     Call re.findall() on each element.
# replace()     Replace occurrences of pattern with some other string.
# contains() Call re.search() on each element, returning a Boolean.
# count()       Count occurrences of pattern.
# split()       Equivalent to str.split(), but accepts regexps.
# rsplit()      Equivalent to str.rsplit(), but accepts regexps.
# 
# With these, you can do a wide range of interesting operations. For example, we can
# extract the first name from each by asking for a contiguous group of characters at the
# beginning of each element:
# 
# 
# 
#                                                                              Vectorized String Operations   |   181
# 
#       In[11]: monte.str.extract('([A-Za-z]+)')
#       Out[11]: 0     Graham
#                1       John
#                2      Terry
#                3       Eric
#                4      Terry
#                5    Michael
#                dtype: object
# Or we can do something more complicated, like finding all names that start and end
# with a consonant, making use of the start-of-string (^) and end-of-string ($) regular
# expression characters:
#       In[12]: monte.str.findall(r'^[^AEIOU].*[^aeiou]$')
#       Out[12]: 0    [Graham Chapman]
#                1                  []
#                2     [Terry Gilliam]
#                3                  []
#                4       [Terry Jones]
#                5     [Michael Palin]
#                dtype: object
# 
# The ability to concisely apply regular expressions across Series or DataFrame entries
# opens up many possibilities for analysis and cleaning of data.
# 
# Miscellaneous methods
# Finally, there are some miscellaneous methods that enable other convenient opera‐
# tions (see Table 3-5).
# 
# Table 3-5. Other Pandas string methods
# Method                 Description
# get()                  Index each element
# slice()                Slice each element
# slice_replace() Replace slice in each element with passed value
# cat()                  Concatenate strings
# repeat()               Repeat values
# normalize()            Return Unicode form of string
# pad()                  Add whitespace to left, right, or both sides of strings
# wrap()                 Split long strings into lines with length less than a given width
# join()                 Join strings in each element of the Series with passed separator
# get_dummies()          Extract dummy variables as a DataFrame
# 
# 
# 
# 
# 182   |   Chapter 3: Data Manipulation with Pandas
# 
# Vectorized item access and slicing. The get() and slice() operations, in particular,
# enable vectorized element access from each array. For example, we can get a slice of
# the first three characters of each array using str.slice(0, 3). Note that this behav‐
# ior is also available through Python’s normal indexing syntax—for example,
# df.str.slice(0, 3) is equivalent to df.str[0:3]:
#     In[13]: monte.str[0:3]
#     Out[13]: 0    Gra
#              1    Joh
#              2    Ter
#              3    Eri
#              4    Ter
#              5    Mic
#              dtype: object
# 
# Indexing via df.str.get(i) and df.str[i] is similar.
# These get() and slice() methods also let you access elements of arrays returned by
# split(). For example, to extract the last name of each entry, we can combine
# split() and get():
#     In[14]: monte.str.split().str.get(-1)
#     Out[14]: 0    Chapman
#              1     Cleese
#              2    Gilliam
#              3       Idle
#              4      Jones
#              5      Palin
#              dtype: object
# 
# Indicator variables. Another method that requires a bit of extra explanation is the
# get_dummies() method. This is useful when your data has a column containing some
# sort of coded indicator. For example, we might have a dataset that contains informa‐
# tion in the form of codes, such as A=“born in America,” B=“born in the United King‐
# dom,” C=“likes cheese,” D=“likes spam”:
#     In[15]:
#     full_monte = pd.DataFrame({'name': monte,
#                                'info': ['B|C|D', 'B|D', 'A|C', 'B|D', 'B|C',
#                                'B|C|D']})
#     full_monte
#     Out[15]:        info             name
#                0   B|C|D   Graham Chapman
#                1     B|D      John Cleese
#                2     A|C    Terry Gilliam
#                3     B|D        Eric Idle
#                4     B|C      Terry Jones
#                5   B|C|D    Michael Palin
# 
# 
# 
#                                                          Vectorized String Operations   |   183
# 
# The get_dummies() routine lets you quickly split out these indicator variables into a
# DataFrame:
#       In[16]: full_monte['info'].str.get_dummies('|')
#       Out[16]:       A   B   C    D
#                  0   0   1   1    1
#                  1   0   1   0    1
#                  2   1   0   1    0
#                  3   0   1   0    1
#                  4   0   1   1    0
#                  5   0   1   1    1
# With these operations as building blocks, you can construct an endless range of string
# processing procedures when cleaning your data.
# We won’t dive further into these methods here, but I encourage you to read through
# “Working with Text Data” in the pandas online documentation, or to refer to the
# resources listed in “Further Resources” on page 215.
# 
# Example: Recipe Database
# These vectorized string operations become most useful in the process of cleaning up
# messy, real-world data. Here I’ll walk through an example of that, using an open
# recipe database compiled from various sources on the Web. Our goal will be to parse
# the recipe data into ingredient lists, so we can quickly find a recipe based on some
# ingredients we have on hand.
# The scripts used to compile this can be found at https://github.com/fictivekin/openre
# cipes, and the link to the current version of the database is found there as well.
# As of spring 2016, this database is about 30 MB, and can be downloaded and unzip‐
# ped with these commands:
#       In[17]: # !curl -O http://openrecipes.s3.amazonaws.com/recipeitems-latest.json.gz
#               # !gunzip recipeitems-latest.json.gz
# 
# The database is in JSON format, so we will try pd.read_json to read it:
#       In[18]: try:
#                      recipes = pd.read_json('recipeitems-latest.json')
#                  except ValueError as e:
#                      print("ValueError:", e)
#       ValueError: Trailing data
# 
# Oops! We get a ValueError mentioning that there is “trailing data.” Searching for this
# error on the Internet, it seems that it’s due to using a file in which each line is itself a
# valid JSON, but the full file is not. Let’s check if this interpretation is true:
# 
# 
# 
# 
# 184   |   Chapter 3: Data Manipulation with Pandas
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Tables of Pandas String Methods",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Tablesof(HierNode):
    def __init__(self):
        super().__init__("Tables of Pandas String Methods")
        self.add(Content())

# eof
