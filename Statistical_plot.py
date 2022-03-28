import matplotlib.pyplot as plt
import seaborn 
import plotly.express as px
import os
import pandas as pd 
import geopandas as gpd
from functions import * 


Reg_Path = 'E:/Geospatial_Project/Dati/Limiti/Lim/Reg01012021/Reg01012021_WGS84.shp'
Prov_Path = 'E:/Geospatial_Project/Dati/Limiti/Lim/ProvCM01012021/ProvCM01012021_WGS84.shp'
Macro_Path = 'E:/Geospatial_Project/Dati/Limiti/Lim/RipGeo01012021/RipGeo01012021_WGS84.shp'
# Reading the geodaframe

Reg_geodf = gpd.read_file(Reg_Path)
Prov_geodf = gpd.read_file(Prov_Path)
Macro_geodf = gpd.read_file(Macro_Path)

# Regions 
Regions = Reg_geodf.DEN_REG.to_list()
# Anomalous Regions names
Anomalous_Regions = ['Trentino-Alto Adige/Südtirol','Friuli-Venezia Giulia',"Valle d'Aosta/Vallée d'Aoste"]
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
Stat_0 = List_Statistics[61]


# Import the dataframe 
df = read_dati_bes(path_+ '/' + Stat_0)
# Get_labels 
labels = get_labels_(df)
#'PROVINCES'
# Extract the set of all Bes provinces
provinces = provinces_BES(df, Anomalous_Regions, Sud_Sardinia, Macro_Areas, Italy, Regions)
df_prov = order_df(df, provinces)
# Get Regions
Bes_Regions = regions_BES(Regions)
#'MACRO-AREA'
# Creating the MacroArea Dataframe
df_macro = order_df(df, Macro_Areas)
#'REGIONS'
# Creating Regions DataFrame
df_reg = order_df(df, Bes_Regions)



['numero medio di anni', 'per 1.000 nati vivi', 'tassi standardizzati per 10.000 residenti', 'valori percentuali',
 'valori percentuali (tasso specifico di coorte)', 'per 10.000 occupati', 'euro', 'per 10.000 abitanti', 'per 100.000 abitanti', 
 'per 100 km2', 'per 100 m2', 'm2 per abitante', 
'per milioni di abitanti', 'per 1.000 laureati residenti', 'numero medio per utente', 'valori per abitante']


