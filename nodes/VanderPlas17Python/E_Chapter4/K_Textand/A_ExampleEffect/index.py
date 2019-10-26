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
# Example: Effect of Holidays on US Births
# Let’s return to some data we worked with earlier in “Example: Birthrate Data” on page
# 174, where we generated a plot of average births over the course of the calendar year;
# as already mentioned, this data can be downloaded at https://raw.githubusercon
# tent.com/jakevdp/data-CDCbirths/master/births.csv.
# We’ll start with the same cleaning procedure we used there, and plot the results
# (Figure 4-67):
#     In[2]:
#     births = pd.read_csv('births.csv')
# 
#     quartiles = np.percentile(births['births'], [25, 50, 75])
#     mu, sig = quartiles[1], 0.74 * (quartiles[2] - quartiles[0])
#     births = births.query('(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)')
# 
#     births['day'] = births['day'].astype(int)
# 
#     births.index = pd.to_datetime(10000 * births.year +
#                                   100 * births.month +
#                                   births.day, format='%Y%m%d')
#     births_by_date = births.pivot_table('births',
#                                         [births.index.month, births.index.day])
#     births_by_date.index = [pd.datetime(2012, month, day)
#                             for (month, day) in births_by_date.index]
#     In[3]: fig, ax = plt.subplots(figsize=(12, 4))
#            births_by_date.plot(ax=ax);
# 
# 
# 
# 
# Figure 4-67. Average daily births by date
# 
# When we’re communicating data like this, it is often useful to annotate certain fea‐
# tures of the plot to draw the reader’s attention. This can be done manually with the
# plt.text/ax.text command, which will place text at a particular x/y value
# (Figure 4-68):
# 
# 
# 
#                                                                 Text and Annotation   |   269
# 
#       In[4]: fig, ax = plt.subplots(figsize=(12, 4))
#              births_by_date.plot(ax=ax)
# 
#                # Add labels to the plot
#                style = dict(size=10, color='gray')
# 
#                ax.text('2012-1-1', 3950, "New Year's Day", **style)
#                ax.text('2012-7-4', 4250, "Independence Day", ha='center', **style)
#                ax.text('2012-9-4', 4850, "Labor Day", ha='center', **style)
#                ax.text('2012-10-31', 4600, "Halloween", ha='right', **style)
#                ax.text('2012-11-25', 4450, "Thanksgiving", ha='center', **style)
#                ax.text('2012-12-25', 3850, "Christmas ", ha='right', **style)
# 
#                # Label the axes
#                ax.set(title='USA births by day of year (1969-1988)',
#                       ylabel='average daily births')
# 
#                # Format the x axis with centered month labels
#                ax.xaxis.set_major_locator(mpl.dates.MonthLocator())
#                ax.xaxis.set_minor_locator(mpl.dates.MonthLocator(bymonthday=15))
#                ax.xaxis.set_major_formatter(plt.NullFormatter())
#                ax.xaxis.set_minor_formatter(mpl.dates.DateFormatter('%h'));
# 
# 
# 
# 
# Figure 4-68. Annotated average daily births by date
# 
# The ax.text method takes an x position, a y position, a string, and then optional key‐
# words specifying the color, size, style, alignment, and other properties of the text.
# Here we used ha='right' and ha='center', where ha is short for horizonal align‐
# ment. See the docstring of plt.text() and of mpl.text.Text() for more information
# on available options.
# 
# Transforms and Text Position
# In the previous example, we anchored our text annotations to data locations. Some‐
# times it’s preferable to anchor the text to a position on the axes or figure, independent
# of the data. In Matplotlib, we do this by modifying the transform.
# 
# 
# 270   |   Chapter 4: Visualization with Matplotlib
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Example: Effect of Holidays on US Births",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ExampleEffect(HierNode):
    def __init__(self):
        super().__init__("Example: Effect of Holidays on US Births")
        self.add(Content())

# eof
