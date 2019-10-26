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
# Note that by default, the text is aligned above and to the left of the specified coordi‐
# nates; here the “.” at the beginning of each string will approximately mark the given
# coordinate location.
# The transData coordinates give the usual data coordinates associated with the x- and
# y-axis labels. The transAxes coordinates give the location from the bottom-left cor‐
# ner of the axes (here the white box) as a fraction of the axes size. The transFigure
# coordinates are similar, but specify the position from the bottom left of the figure
# (here the gray box) as a fraction of the figure size.
# Notice now that if we change the axes limits, it is only the transData coordinates that
# will be affected, while the others remain stationary (Figure 4-70):
#       In[6]: ax.set_xlim(0, 2)
#              ax.set_ylim(-6, 6)
#              fig
# 
# 
# 
# 
# Figure 4-70. Comparing Matplotlib’s coordinate systems
# 
# You can see this behavior more clearly by changing the axes limits interactively; if you
# are executing this code in a notebook, you can make that happen by changing %mat
# plotlib inline to %matplotlib notebook and using each plot’s menu to interact
# with the plot.
# 
# Arrows and Annotation
# Along with tick marks and text, another useful annotation mark is the simple arrow.
# Drawing arrows in Matplotlib is often much harder than you might hope. While
# there is a plt.arrow() function available, I wouldn’t suggest using it; the arrows it
# creates are SVG objects that will be subject to the varying aspect ratio of your plots,
# and the result is rarely what the user intended. Instead, I’d suggest using the plt.anno
# tate() function. This function creates some text and an arrow, and the arrows can be
# very flexibly specified.
# 
# 
# 
# 272   |   Chapter 4: Visualization with Matplotlib
# 
# Here we’ll use annotate with several of its options (Figure 4-71):
#     In[7]: %matplotlib inline
# 
#            fig, ax = plt.subplots()
# 
#            x = np.linspace(0, 20, 1000)
#            ax.plot(x, np.cos(x))
#            ax.axis('equal')
# 
#            ax.annotate('local maximum', xy=(6.28, 1), xytext=(10, 4),
#                        arrowprops=dict(facecolor='black', shrink=0.05))
# 
#            ax.annotate('local minimum', xy=(5 * np.pi, -1), xytext=(2, -6),
#                        arrowprops=dict(arrowstyle="->",
#                                        connectionstyle="angle3,angleA=0,angleB=-90"));
# 
# 
# 
# 
# Figure 4-71. Annotation examples
# 
# The arrow style is controlled through the arrowprops dictionary, which has numer‐
# ous options available. These options are fairly well documented in Matplotlib’s online
# documentation, so rather than repeating them here I’ll quickly show some of the pos‐
# sibilities. Let’s demonstrate several of the possible options using the birthrate plot
# from before (Figure 4-72):
#     In[8]:
#     fig, ax = plt.subplots(figsize=(12, 4))
#     births_by_date.plot(ax=ax)
# 
#     # Add labels to the plot
#     ax.annotate("New Year's Day", xy=('2012-1-1', 4100), xycoords='data',
#                 xytext=(50, -30), textcoords='offset points',
#                 arrowprops=dict(arrowstyle="->",
#                                 connectionstyle="arc3,rad=-0.2"))
# 
# 
#     ax.annotate("Independence Day", xy=('2012-7-4', 4250), xycoords='data',
#                 bbox=dict(boxstyle="round", fc="none", ec="gray"),
# 
# 
# 
#                                                                  Text and Annotation   |   273
# 
#                       xytext=(10, -40), textcoords='offset points', ha='center',
#                       arrowprops=dict(arrowstyle="->"))
# 
#       ax.annotate('Labor Day', xy=('2012-9-4', 4850), xycoords='data', ha='center',
#                   xytext=(0, -20), textcoords='offset points')
#       ax.annotate('', xy=('2012-9-1', 4850), xytext=('2012-9-7', 4850),
#                   xycoords='data', textcoords='data',
#                   arrowprops={'arrowstyle': '|-|,widthA=0.2,widthB=0.2', })
# 
#       ax.annotate('Halloween', xy=('2012-10-31', 4600), xycoords='data',
#                   xytext=(-80, -40), textcoords='offset points',
#                   arrowprops=dict(arrowstyle="fancy",
#                                   fc="0.6", ec="none",
#                                   connectionstyle="angle3,angleA=0,angleB=-90"))
# 
#       ax.annotate('Thanksgiving', xy=('2012-11-25', 4500), xycoords='data',
#                   xytext=(-120, -60), textcoords='offset points',
#                   bbox=dict(boxstyle="round4,pad=.5", fc="0.9"),
#                   arrowprops=dict(arrowstyle="->",
#                                   connectionstyle="angle,angleA=0,angleB=80,rad=20"))
# 
# 
#       ax.annotate('Christmas', xy=('2012-12-25', 3850), xycoords='data',
#                    xytext=(-30, 0), textcoords='offset points',
#                    size=13, ha='right', va="center",
#                    bbox=dict(boxstyle="round", alpha=0.1),
#                    arrowprops=dict(arrowstyle="wedge,tail_width=0.5", alpha=0.1));
# 
#       # Label the axes
#       ax.set(title='USA births by day of year (1969-1988)',
#              ylabel='average daily births')
# 
#       # Format the x axis with centered month labels
#       ax.xaxis.set_major_locator(mpl.dates.MonthLocator())
#       ax.xaxis.set_minor_locator(mpl.dates.MonthLocator(bymonthday=15))
#       ax.xaxis.set_major_formatter(plt.NullFormatter())
#       ax.xaxis.set_minor_formatter(mpl.dates.DateFormatter('%h'));
# 
#       ax.set_ylim(3600, 5400);
# 
# 
# 
# 
# 274   |   Chapter 4: Visualization with Matplotlib
# 
# Figure 4-72. Annotated average birth rates by day
# 
# You’ll notice that the specifications of the arrows and text boxes are very detailed: this
# gives you the power to create nearly any arrow style you wish. Unfortunately, it also
# means that these sorts of features often must be manually tweaked, a process that can
# be very time-consuming when one is producing publication-quality graphics! Finally,
# I’ll note that the preceding mix of styles is by no means best practice for presenting
# data, but rather included as a demonstration of some of the available options.
# More discussion and examples of available arrow and annotation styles can be found
# in the Matplotlib gallery, in particular http://matplotlib.org/examples/pylab_examples/
# annotation_demo2.html.
# 
# Customizing Ticks
# Matplotlib’s default tick locators and formatters are designed to be generally sufficient
# in many common situations, but are in no way optimal for every plot. This section
# will give several examples of adjusting the tick locations and formatting for the par‐
# ticular plot type you’re interested in.
# Before we go into examples, it will be best for us to understand further the object
# hierarchy of Matplotlib plots. Matplotlib aims to have a Python object representing
# everything that appears on the plot: for example, recall that the figure is the bound‐
# ing box within which plot elements appear. Each Matplotlib object can also act as a
# container of sub-objects; for example, each figure can contain one or more axes
# objects, each of which in turn contain other objects representing plot contents.
# The tick marks are no exception. Each axes has attributes xaxis and yaxis, which in
# turn have attributes that contain all the properties of the lines, ticks, and labels that
# make up the axes.
# 
# 
# 
# 
#                                                                      Customizing Ticks   |   275
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Arrows and Annotation",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Arrowsand(HierNode):
    def __init__(self):
        super().__init__("Arrows and Annotation")
        self.add(Content())

# eof
