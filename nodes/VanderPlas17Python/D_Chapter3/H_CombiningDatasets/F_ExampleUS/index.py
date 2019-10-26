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
#                   df9 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
#                                       'rank': [3, 1, 4, 2]})
#                   print(df8); print(df9); print(pd.merge(df8, df9, on="name"))
#       df8                        df9                   pd.merge(df8, df9, on="name")
#          name        rank           name       rank       name rank_x rank_y
#       0  Bob           1         0  Bob          3     0   Bob       1       3
#       1 Jake           2         1 Jake          1     1 Jake        2       1
#       2 Lisa           3         2 Lisa          4     2 Lisa        3       4
#       3  Sue           4         3  Sue          2     3   Sue       4       2
# Because the output would have two conflicting column names, the merge function
# automatically appends a suffix _x or _y to make the output columns unique. If these
# defaults are inappropriate, it is possible to specify a custom suffix using the suffixes
# keyword:
#       In[18]:
#       print(df8); print(df9);
#       print(pd.merge(df8, df9, on="name", suffixes=["_L", "_R"]))
#       df8                        df9
#              name    rank               name   rank
#       0      Bob       1         0      Bob      3
#       1     Jake       2         1     Jake      1
#       2     Lisa       3         2     Lisa      4
#       3      Sue       4         3      Sue      2
# 
# 
#       pd.merge(df8, df9, on="name", suffixes=["_L", "_R"])
#          name rank_L rank_R
#       0   Bob       1       3
#       1 Jake        2       1
#       2 Lisa        3       4
#       3   Sue       4       2
# These suffixes work in any of the possible join patterns, and work also if there are
# multiple overlapping columns.
# For more information on these patterns, see “Aggregation and Grouping” on page
# 158, where we dive a bit deeper into relational algebra. Also see the “Merge, Join, and
# Concatenate” section of the Pandas documentation for further discussion of these
# topics.
# 
# Example: US States Data
# Merge and join operations come up most often when one is combining data from dif‐
# ferent sources. Here we will consider an example of some data about US states and
# their populations. The data files can be found at http://github.com/jakevdp/data-
# USstates/:
#       In[19]:
#       # Following are shell commands to download the data
# 
# 
# 154   |     Chapter 3: Data Manipulation with Pandas
# 
#     # !curl -O https://raw.githubusercontent.com/jakevdp/
#     #    data-USstates/master/state-population.csv
#     # !curl -O https://raw.githubusercontent.com/jakevdp/
#     #    data-USstates/master/state-areas.csv
#     # !curl -O https://raw.githubusercontent.com/jakevdp/
#     #    data-USstates/master/state-abbrevs.csv
# 
# Let’s take a look at the three datasets, using the Pandas read_csv() function:
#     In[20]: pop = pd.read_csv('state-population.csv')
#             areas = pd.read_csv('state-areas.csv')
#             abbrevs = pd.read_csv('state-abbrevs.csv')
# 
#             print(pop.head()); print(areas.head()); print(abbrevs.head())
#     pop.head()                                       areas.head()
#       state/region        ages   year   population           state      area (sq. mi)
#     0           AL     under18   2012    1117489.0   0     Alabama              52423
#     1           AL       total   2012    4817528.0   1      Alaska             656425
#     2           AL     under18   2010    1130966.0   2     Arizona             114006
#     3           AL       total   2010    4785570.0   3    Arkansas              53182
#     4           AL     under18   2011    1125763.0   3    Arkansas              53182
#                                                      4 California              163707
# 
#     abbrevs.head()
#             state abbreviation
#     0     Alabama           AL
#     1      Alaska           AK
#     2     Arizona           AZ
#     3    Arkansas           AR
#     4 California            CA
# Given this information, say we want to compute a relatively straightforward result:
# rank US states and territories by their 2010 population density. We clearly have the
# data here to find this result, but we’ll have to combine the datasets to get it.
# We’ll start with a many-to-one merge that will give us the full state name within the
# population DataFrame. We want to merge based on the state/region column of pop,
# and the abbreviation column of abbrevs. We’ll use how='outer' to make sure no
# data is thrown away due to mismatched labels.
#     In[21]: merged = pd.merge(pop, abbrevs, how='outer',
#                               left_on='state/region', right_on='abbreviation')
#             merged = merged.drop('abbreviation', 1) # drop duplicate info
#             merged.head()
#     Out[21]:       state/region    ages year population   state
#                0             AL under18 2012  1117489.0 Alabama
#                1             AL   total 2012  4817528.0 Alabama
#                2             AL under18 2010 1130966.0 Alabama
#                3             AL   total 2010 4785570.0 Alabama
#                4             AL under18 2011 1125763.0 Alabama
# 
# 
# 
# 
#                                                        Combining Datasets: Merge and Join   |   155
# 
# Let’s double-check whether there were any mismatches here, which we can do by
# looking for rows with nulls:
#       In[22]: merged.isnull().any()
#       Out[22]: state/region          False
#                ages                  False
#                year                  False
#                population             True
#                state                  True
#                dtype: bool
# 
# Some of the population info is null; let’s figure out which these are!
#       In[23]: merged[merged['population'].isnull()].head()
#       Out[23]:          state/region    ages year population state
#                  2448             PR under18 1990        NaN   NaN
#                  2449             PR   total 1990        NaN   NaN
#                  2450             PR   total 1991        NaN   NaN
#                  2451             PR under18 1991        NaN   NaN
#                  2452             PR   total 1993        NaN   NaN
# It appears that all the null population values are from Puerto Rico prior to the year
# 2000; this is likely due to this data not being available from the original source.
# More importantly, we see also that some of the new state entries are also null, which
# means that there was no corresponding entry in the abbrevs key! Let’s figure out
# which regions lack this match:
#       In[24]: merged.loc[merged['state'].isnull(), 'state/region'].unique()
#       Out[24]: array(['PR', 'USA'], dtype=object)
# We can quickly infer the issue: our population data includes entries for Puerto Rico
# (PR) and the United States as a whole (USA), while these entries do not appear in the
# state abbreviation key. We can fix these quickly by filling in appropriate entries:
#       In[25]: merged.loc[merged['state/region'] == 'PR', 'state'] = 'Puerto Rico'
#               merged.loc[merged['state/region'] == 'USA', 'state'] = 'United States'
#               merged.isnull().any()
#       Out[25]: state/region          False
#                ages                  False
#                year                  False
#                population             True
#                state                 False
#                dtype: bool
# 
# No more nulls in the state column: we’re all set!
# Now we can merge the result with the area data using a similar procedure. Examining
# our results, we will want to join on the state column in both:
# 
# 
# 
# 156   | Chapter 3: Data Manipulation with Pandas
# 
#     In[26]: final = pd.merge(merged, areas, on='state', how='left')
#             final.head()
#     Out[26]:       state/region      ages year population     state area (sq. mi)
#                0             AL   under18 2012  1117489.0   Alabama       52423.0
#                1             AL     total 2012  4817528.0   Alabama       52423.0
#                2             AL   under18 2010  1130966.0   Alabama       52423.0
#                3             AL     total 2010  4785570.0   Alabama       52423.0
#                4             AL   under18 2011  1125763.0   Alabama       52423.0
# Again, let’s check for nulls to see if there were any mismatches:
#     In[27]: final.isnull().any()
#     Out[27]: state/region         False
#              ages                 False
#              year                 False
#              population            True
#              state                False
#              area (sq. mi)         True
#              dtype: bool
# 
# There are nulls in the area column; we can take a look to see which regions were
# ignored here:
#     In[28]: final['state'][final['area (sq. mi)'].isnull()].unique()
#     Out[28]: array(['United States'], dtype=object)
# 
# We see that our areas DataFrame does not contain the area of the United States as a
# whole. We could insert the appropriate value (using the sum of all state areas, for
# instance), but in this case we’ll just drop the null values because the population den‐
# sity of the entire United States is not relevant to our current discussion:
#     In[29]: final.dropna(inplace=True)
#             final.head()
#     Out[29]:       state/region    ages   year population   state area (sq. mi)
#                0             AL under18   2012  1117489.0 Alabama       52423.0
#                1             AL   total   2012  4817528.0 Alabama       52423.0
#                2             AL under18   2010 1130966.0 Alabama        52423.0
#                3             AL   total   2010  4785570.0 Alabama       52423.0
#                4             AL under18   2011  1125763.0 Alabama       52423.0
# Now we have all the data we need. To answer the question of interest, let’s first select
# the portion of the data corresponding with the year 2000, and the total population.
# We’ll use the query() function to do this quickly (this requires the numexpr package
# to be installed; see “High-Performance Pandas: eval() and query()” on page 208):
#     In[30]: data2010 = final.query("year == 2010 & ages == 'total'")
#             data2010.head()
#     Out[30]:         state/region  ages year population           state area (sq. mi)
#                3               AL total 2010  4785570.0         Alabama       52423.0
#                91              AK total 2010   713868.0          Alaska      656425.0
# 
# 
#                                                        Combining Datasets: Merge and Join   |   157
# 
#                 101                AZ   total       2010    6408790.0      Arizona   114006.0
#                 189                AR   total       2010    2922280.0     Arkansas    53182.0
#                 197                CA   total       2010   37333601.0   California   163707.0
# Now let’s compute the population density and display it in order. We’ll start by rein‐
# dexing our data on the state, and then compute the result:
#       In[31]: data2010.set_index('state', inplace=True)
#               density = data2010['population'] / data2010['area (sq. mi)']
#       In[32]: density.sort_values(ascending=False, inplace=True)
#               density.head()
#       Out[32]: state
#                District of Columbia                8898.897059
#                Puerto Rico                         1058.665149
#                New Jersey                          1009.253268
#                Rhode Island                         681.339159
#                Connecticut                          645.600649
#                dtype: float64
# The result is a ranking of US states plus Washington, DC, and Puerto Rico in order of
# their 2010 population density, in residents per square mile. We can see that by far the
# densest region in this dataset is Washington, DC (i.e., the District of Columbia);
# among states, the densest is New Jersey.
# We can also check the end of the list:
#       In[33]: density.tail()
#       Out[33]: state
#                South Dakota   10.583512
#                North Dakota    9.537565
#                Montana         6.736171
#                Wyoming         5.768079
#                Alaska          1.087509
#                dtype: float64
# We see that the least dense state, by far, is Alaska, averaging slightly over one resident
# per square mile.
# This type of messy data merging is a common task when one is trying to answer
# questions using real-world data sources. I hope that this example has given you an
# idea of the ways you can combine tools we’ve covered in order to gain insight from
# your data!
# 
# Aggregation and Grouping
# An essential piece of analysis of large data is efficient summarization: computing
# aggregations like sum(), mean(), median(), min(), and max(), in which a single num‐
# ber gives insight into the nature of a potentially large dataset. In this section, we’ll
# 
# 
# 
# 158   | Chapter 3: Data Manipulation with Pandas
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Example: US States Data",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ExampleUS(HierNode):
    def __init__(self):
        super().__init__("Example: US States Data")
        self.add(Content())

# eof
