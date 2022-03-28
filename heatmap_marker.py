import os
import folium
#import leaflet
import pandas as pd 
import geopandas as gpd


os.chdir('E:\Geospatial_Project\Factories')

df = pd.read_csv('Pisa.csv')

df = gpd.GeoDataFrame(df, crs = 4326)
print(type(df))
print(df.head())
print(df.columns)