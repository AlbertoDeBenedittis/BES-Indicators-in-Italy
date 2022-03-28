import os
import mapclassify
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import seaborn as sbn
import contextily 
from functions import * 
#import plotly.io as pio
#pio.renderers.default = "vscode"

# Path where are stored the shape files
Reg_Path = 'E:/Geospatial_Project/Dati/Limiti/Lim/Reg01012021/Reg01012021_WGS84.shp'
Prov_Path = 'E:/Geospatial_Project/Dati/Limiti/Lim/ProvCM01012021/ProvCM01012021_WGS84.shp'
Macro_Path = 'E:/Geospatial_Project/Dati/Limiti/Lim/RipGeo01012021/RipGeo01012021_WGS84.shp'
# Reading the geodaframe
Reg_df = gpd.read_file(Reg_Path)
Prov_df = gpd.read_file(Prov_Path)
Macro_df = gpd.read_file(Macro_Path)

# Anomalous Regions names
Anomalous_Region = ['Trentino-Alto Adige/Südtirol','Friuli-Venezia Giulia',"Valle d'Aosta/Vallée d'Aoste"]
#Sud_Sardinia_Agglomeration
Sud_Sardinia = ['Ogliastra','Olbia-Tempio','Medio Campidano','Carbonia-Iglesias']
# Macro_Areas 
Macro_Areas = ['Centro', 'Mezzogiorno', 'Nord']
# Italy 
Italy = ['Italia']
# Different_Names
Different_Names_BES = ['Bolzano/Bozen', 'Forlì-Cesena', 'Massa-Carrara', 'Reggio Calabria']
Deffirent_Names_ISTAT = ['Bolzano', "Forli'-Cesena", 'Massa Carrara', 'Reggio di Calabria']

# Read the BES_Statistics Dataframe
path_ = 'E:/Geospatial_Project/Nuovi_Dati2/'
List_Statistics = os.listdir(path = path_)
Stat_0 = List_Statistics[0]

# Import the dataframe 
df = read_dati_bes(path_+ '/' + Stat_0)
# Creating the MacroArea Dataframe
df = order_df(df, Macro_Areas)
# Sorting the geodf
df_Macro = aggregate_macros(Macro_df)
# Create the geodaframe used in the representation
df = from_df_to_gdf(df, df_Macro)
# JSON
print(df.to_json())
# Creating the title
titolo = get_title_(Stat_0)
# Static Choropletmap
#static_choroplet(df, variable = 'V_2009', title_ = titolo)
# Dynamic ChoropletMap 
#dynamic_choroplet(df, title_ = titolo, measure = 'V_2009')