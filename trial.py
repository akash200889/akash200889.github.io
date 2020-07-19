#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Common commands which should be run everytime


# In[ ]:


#conda install geopandas
#conda upgrade notebook


# In[2]:


#import geopandas as gpd
import pandas as pd
import json


# In[3]:


from bokeh.io import output_notebook, show, output_file
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar
from bokeh.palettes import brewer
from bokeh.io import curdoc, output_notebook
from bokeh.models import Slider, HoverTool, Circle, RangeSlider
from bokeh.layouts import widgetbox, row, column
from bokeh.embed import file_html
from bokeh.resources import CDN


# In[4]:


# Loading State level shape file


# In[5]:


shapefile ='C:/Users/akashp/Desktop/Int_map/States/Admin2.shp'


# In[6]:


gdf = gpd.read_file (shapefile)


# In[7]:


gdf.head()


# In[8]:


# Loading state level data file


# In[9]:


datafile = 'C:/Users/akashp/Desktop/Int_map/state_ov_vul1.xlsx'


# In[10]:


df = pd.read_excel(datafile)


# In[11]:


df.head()


# In[12]:


# Merging shape file with datafile


# In[13]:


merged =gdf.merge (df, left_on = 'ST_NM', right_on='st_nm')


# In[14]:


merged.head()


# In[15]:


# Converting the merged file into JSON file


# In[16]:


merged_json =json.loads(merged.to_json())


# In[17]:


json_data =json.dumps(merged_json)


# In[18]:


geosource = GeoJSONDataSource(geojson = json_data)


# In[19]:


# Color palette for the map


# In[20]:


palette = brewer['Oranges'] [8]


# In[21]:


# Reversing hte order of palette 


# In[22]:


palette = palette[::-1]


# In[23]:


# Defining the palette intensity


# In[24]:


color_mapper = LinearColorMapper(palette = palette, low =0.0 , high = 1.0)


# In[25]:


# Defining the custom tick labels for color bar


# In[26]:


tick_labels = {'0.1': '0.1', '0.2': '0.2', '0.3':'0.3', '0.4':'0.4', '0.5':'0.5', '0.6':'0.6', '0.7':'0.7','0.8':'0.8', '0.9': '0.9', '1.0': '1.0', '11':'1.0' }


# In[27]:


# Creating the hover


# In[28]:


hover = HoverTool(tooltips = [ ('State/UT','@ST_NM'),('Overall vulnerability score', '@pr_ovr_vul{1.11}'),('Socio-economic vulnerability score','@pr_soc_eco{1.11}'),('Demographic vulnerability score','@pr_demo{1.11}'),('Housing & hygiene vulnerability score','@pr_hhtype{1.11}'), ('Epidemiological vulnerability score','@pr_epifac{1.11}'),('Non-availability of healthcare vulnarability score','@pr_hcsfac{1.11}')])


# In[29]:


# Creating the color bar


# In[30]:


color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8,width = 500, height = 20,
border_line_color=None,location = (0,0), orientation = 'horizontal', major_label_overrides = tick_labels)


# In[31]:


# Creating the figure object-- Overall Vulnerability at State level


# In[32]:


p = figure(title = 'Overall vulnerability', plot_height =800 , plot_width = 850, toolbar_location = None, tools = [hover])
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None


# In[33]:


# Adding patch rendered to figure


# In[34]:


p.patches('xs','ys', source = geosource,fill_color = {'field' :'pr_ovr_vul', 'transform' : color_mapper},
          line_color = 'black', line_width = 0.25, fill_alpha = 1)


# In[35]:


# Specify figure layout


# In[36]:


p.add_layout(color_bar, 'below')


# In[37]:


# to display figure inline in notebook


# In[38]:


#output_notebook()


# In[39]:


# To save output file in html format


# In[40]:


#output_file("over_vul_state.html")


# In[41]:


# Display figure


# In[42]:


#show(p)


# In[43]:


curdoc().title = "State level Overall Vulnerability"
curdoc().add_root(p)


# In[ ]:




