from cgitb import html
import codecs
import streamlit as st
import geopandas as gpd 
import pandas as pd 
import matplotlib as plt
from functions2 import * 
from functions2 import autocorrelation
import streamlit.components.v1 as components


Reg_Path = 'E:/Geospatial_Project/Dati/Limiti/Lim/Reg01012021/Reg01012021_WGS84.shp'
Prov_Path = 'E:/Geospatial_Project/Dati/Limiti/Lim/ProvCM01012021/ProvCM01012021_WGS84.shp'
# Reading the geodaframe

Reg_df = gpd.read_file(Reg_Path)
Prov_df = gpd.read_file(Prov_Path)

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

# Get the Istat regions 
Regions = Reg_df.DEN_REG.to_list()
# Get  BES Regions
Bes_Regions = regions_BES(Regions)
# Extract the set of all Bes provinces
## PREPARE REG GEO DF ##
Reg_df = mod_col_geo(Reg_df)
Reg_df = order_df_regions(Reg_df, Bes_Regions)

path_ = 'E:/Geospatial_Project/Nuovi_Dati2/Benessere economico-Patrimonio pro capite-Totale-euro.xlsx'

df = read_dati_bes(path_)

provinces = provinces_BES(df, Anomalous_Regions, Sud_Sardinia, Macro_Areas, Italy, Regions)

Prov_df = clean_prov_geo(Prov_df, provinces)

# 'PROVINCES' #
# Create the provinces df
df_prov = order_df(df, provinces)
# Obtain the full geodataframe of provinces 
df_prov = from_df_to_gdf(df_prov, Prov_df)

try:
    st.pyplot(autocorrelation(path = path_, df_prov = df_prov, Reg_df = Reg_df, var = 'V_2017' ))

except:
    st.write(autocorrelation(path = path_, df_prov = df_prov, Reg_df = Reg_df, var = 'V_2017' ))

#rep_points = []
#for prov in df_prov:
#    rep_points.append(representative_point(df_prov))
selectbox_ind = st.sidebar.selectbox(
    "Which indicator do you what to know about",
    ("Health", "Education & Training", "Work & Life Balance", "Economic well-being", "Social Relationship", 
    "Politics & Istitutions", "Security", "Subjective well-being", "Landscape & Cultural heritage", "Environment", "Innovation, Research & Creativity", "Quality of services")
)


file = open("E:/Geospatial_Project/m1.txt", "r")
file2 = open("E:/Geospatial_Project/m2.txt", "r")

components.html(file.read(),  width=1000, height=1000)
st.write('Second Plot')
components.html(file2.read(),  width=1000, height=1000)

#territories = df_prov.reset_index()['TERRITORIO'].tolist()
#rep_points_df = gpd.GeoDataFrame([territories,rep_points], columns = ['TERRITORIO', 'geometry'], crs = 4326) 