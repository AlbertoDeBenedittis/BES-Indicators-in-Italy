import os 
import pyrosm
import pandas as pd 
import  geopandas as gpd


# Change the working directory
os.chdir('E:/Geospatial_Project/PBFs')
# Create a list with all the pbfs files 
regions_pbf = os.listdir()
custom_filter = {'office' : ['ngo']}
# Define the filter


# Iterate along all the regions
for region in regions_pbf:
    
    name = region.split('_')
    name = name[1]
    
    osm = pyrosm.OSM(region)
    data = osm.get_pois(custom_filter = custom_filter)
    
    try:
        data.to_file('E:/Geospatial_Project/No_Profit/' + name + '/' + name + '.shp')
    except:
        data = pd.DataFrame(data)
        data.to_csv('E:/Geospatial_Project/No_Profit/' + name + '.csv')
