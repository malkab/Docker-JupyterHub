
# coding: utf-8

# In[1]:

import os


# In[2]:

import pandas as pd


# In[3]:

import numpy as np


# In[4]:

from random import randint, uniform


# In[5]:

from datetime import datetime


# In[ ]:




# In[6]:

from zipfile import ZipFile


# In[7]:

import geopandas as gpd


# In[8]:

from shapely.geometry import Point


# In[9]:

get_ipython().magic('matplotlib inline')


# In[10]:

import matplotlib.pyplot as plt


# In[11]:

import seaborn as sns


# In[12]:

plt.style.use("bmh")


# In[13]:

plt.rcParams["figure.figsize"]= (10.0, 10.0)


# In[14]:

from ipywidgets import interact, HTML, FloatSlider


# In[15]:

from IPython.display import clear_output, display


# In[16]:

from tqdm import tqdm_notebook, tqdm_pandas


# In[17]:

import warnings


# In[18]:

warnings.filterwarnings("ignore")


# In[19]:

shapefile = "/src/data/TRAMO_VIAL.shp"


# In[20]:

shapefile


# In[21]:

gdf = gpd.GeoDataFrame.from_file(shapefile)


# In[22]:

portales = gpd.GeoDataFrame.from_file("/src/data/PORTAL_PK.shp")


# In[24]:

portales["geometry"].size


# In[25]:

gdf["geometry"].size


# In[26]:

gdf.head(2)


# In[93]:

select = gdf[["ACCESO", "CIRCULACIO", "geometry"]][:5000]


# In[94]:

select.size


# In[95]:

select.to_file("/src/out2.shp", driver="ESRI Shapefile")


# In[96]:

import folium


# In[97]:

m = folium.Map([37, -6], zoom_start=9, tiles="cartodbpositron")


# In[98]:

folium.GeoJson(select).add_to(m)


# In[99]:

m.save("geopandas_0.html")


# In[100]:

m


# In[ ]:




# In[ ]:



