import pandas as pd
import numpy as np
import geopandas as gpd

shapefile = "data/TRAMO_VIAL.shp"

gdf = gpd.GeoDataFrame.from_file(shapefile)

print(gdf["geometry"].size) 
