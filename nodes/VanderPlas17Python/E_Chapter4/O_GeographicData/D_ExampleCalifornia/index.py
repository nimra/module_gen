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
# Example: California Cities
# Recall that in “Customizing Plot Legends” on page 249, we demonstrated the use of
# size and color in a scatter plot to convey information about the location, size, and
# population of California cities. Here, we’ll create this plot again, but using Basemap to
# put the data in context.
# We start with loading the data, as we did before:
#       In[10]: import pandas as pd
#               cities = pd.read_csv('data/california_cities.csv')
# 
#                 # Extract the data we're interested in
#                 lat = cities['latd'].values
#                 lon = cities['longd'].values
#                 population = cities['population_total'].values
#                 area = cities['area_total_km2'].values
# Next, we set up the map projection, scatter the data, and then create a colorbar and
# legend (Figure 4-109):
#       In[11]: # 1. Draw the map background
#               fig = plt.figure(figsize=(8, 8))
#               m = Basemap(projection='lcc', resolution='h',
#                           lat_0=37.5, lon_0=-119,
#                           width=1E6, height=1.2E6)
#               m.shadedrelief()
#               m.drawcoastlines(color='gray')
#               m.drawcountries(color='gray')
#               m.drawstates(color='gray')
# 
#                 # 2. scatter city data, with color reflecting population
#                 # and size reflecting area
#                 m.scatter(lon, lat, latlon=True,
#                           c=np.log10(population), s=area,
#                           cmap='Reds', alpha=0.5)
# 
#                 # 3. create colorbar and legend
#                 plt.colorbar(label=r'$\log_{10}({\rm population})$')
#                 plt.clim(3, 7)
# 
#                 # make legend with dummy points
#                 for a in [100, 300, 500]:
#                     plt.scatter([], [], c='k', alpha=0.5, s=a,
#                                 label=str(a) + ' km$^2$')
#                 plt.legend(scatterpoints=1, frameon=False,
#                            labelspacing=1, loc='lower left');
# 
# 
# 
# 
# 308   |   Chapter 4: Visualization with Matplotlib
# 
# Figure 4-109. Scatter plot over a map background
# 
# This shows us roughly where larger populations of people have settled in California:
# they are clustered near the coast in the Los Angeles and San Francisco areas,
# stretched along the highways in the flat central valley, and avoiding almost completely
# the mountainous regions along the borders of the state.
# 
# Example: Surface Temperature Data
# As an example of visualizing some more continuous geographic data, let’s consider
# the “polar vortex” that hit the eastern half of the United States in January 2014. A
# great source for any sort of climatic data is NASA’s Goddard Institute for Space Stud‐
# ies. Here we’ll use the GIS 250 temperature data, which we can download using shell
# commands (these commands may have to be modified on Windows machines). The
# data used here was downloaded on 6/12/2016, and the file size is approximately 9
# MB:
#     In[12]: # !curl -O http://data.giss.nasa.gov/pub/gistemp/gistemp250.nc.gz
#             # !gunzip gistemp250.nc.gz
# 
# The data comes in NetCDF format, which can be read in Python by the netCDF4
# library. You can install this library as shown here:
#     $ conda install netcdf4
# 
# 
# 
# 
#                                                          Geographic Data with Basemap   |   309
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Example: California Cities",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ExampleCalifornia(HierNode):
    def __init__(self):
        super().__init__("Example: California Cities")
        self.add(Content())

# eof
