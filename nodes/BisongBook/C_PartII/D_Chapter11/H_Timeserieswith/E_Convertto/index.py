# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Convert to Datetime Datatype Using ‘to_datetime’
# Pandas uses the to_datetime method to convert strings to Pandas datetime datatype.
# The to_datetime method is smart enough to infer a datetime representation from a
# string of dates passed with different formats. The default output format of to_datetime is
# in the following order: year, month, day, minute, second, millisecond, microsecond,
# nanosecond.
#     The input to to_datetime is recognized as month, day, year. Although, it can easily
# be modified by setting the attributes dayfirst or yearfirst to True.
#     For example, if dayfirst is set to True, the input is recognized as day, month, year.
#     Let’s see an example of this.
# 
# # create list of dates
# my_dates = ['Friday, May 11, 2018', '11/5/2018', '11-5-2018', '5/11/2018',
#             '2018.5.11']
# pd.to_datetime(my_dates)
# 'Output':
# DatetimeIndex(['2018-05-11', '2018-11-05', '2018-11-05', '2018-05-11',
#                '2018-05-11'],
#               dtype='datetime64[ns]', freq=None)
# 
#     Let’s set dayfirst to True. Observe that the first input in the string is treated as a day in
# the output.
# 
# # set dayfirst to True
# pd.to_datetime('5-11-2018', dayfirst = True)
# 'Output':
# Timestamp('2018-11-05 00:00:00')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Convert to Datetime Datatype Using ‘to_datetime’",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Convert to Datetime Datatype Using ‘to_datetime’"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Convertto(HierNode):
    def __init__(self):
        super().__init__("Convert to Datetime Datatype Using ‘to_datetime’")
        self.add(Content())

# eof
