from joblib import PrintTime
import streamlit as st
import os
import mapclassify
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import seaborn as sbn
import contextily 
from functions import * 
import leafmap
import folium
from streamlit_folium import folium_static
from Testo_Indicatore import * 
from dictionaries import diz_ind

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


# DASHBOARD 

st.title('BES Indicators in Italy')
st.write(
    '''
    The [__Bes project__](https://www4.istat.it/en/well-being-and-sustainability/well-being-measures/bes-report) 
    was launched in 2010 to measure Equitable and Sustainable Well-being,
    and with the aim of evaluating the progress of society not only from an economic,
    but also from a social and environmental point of view. 
    \\
    To this end, the traditional economic indicators, GDP first of all, have been integrated with measures of the quality of people’s life and of the environment.
    \\
    \\
    Since 2016, well-being indicators and welfare analyzes have been presented with indicators for monitoring the objectives of the 2030 Agenda
    for Sustainable Development,
    the so-called [Sustainable Development Goals (SDGs)](https://sdgs.un.org/goals) of the United Nations.
    They were chosen by the global community through a political agreement between the different actors, to represent their values, priorities and objectives.
    The United Nations Statistical Commission (UNSC) has set up a shared set of statistical information to monitor the progress of individual countries towards the SDGs,
    including over two hundred indicators.
    The two sets of indicators are only partially overlapping, but certainly complementary.
    \\
    \\
    Bes' indicators cover [12 domains relevant for the measuramente of the well-being](https://www.istat.it/it/files/2018/04/12-domains-scientific-commission.pdf) 
    and they are the following: 

    1)  Health 
    2)  Education & Training
    3)  Work & Life Balance
    4)  Economic well-being
    5)  Social Relationships
    6)  Politics & Istitutions
    7)  Security 
    8)  Subjective well-being
    9)  Landscape & Cultural heritage
    10) Environment
    11) Innovation, Research & Creativity
    12) Quality of services
    '''
)

selectbox_ind = st.sidebar.selectbox(
    "Which indicator do you what to know about",
    ("Health", "Education & Training", "Work & Life Balance", "Economic well-being", "Social Relationship", 
    "Politics & Istitutions", "Security", "Subjective well-being", "Landscape & Cultural heritage", "Environment", "Innovation, Research & Creativity", "Quality of services")
)

selectbox_area = st.sidebar.selectbox(
    'Level of analysis', 
    ('Macroareas', 'Regions', 'Provinces')
)

selectbox_y = st.sidebar.selectbox(
    'Year of analysis',
    ('2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019')
)

diz_indicatori = {
    'Health': 'Salute', 
    'Education & Training' : 'Istruzione e formazione',
    "Work & Life Balance" : 'Lavoro e conciliazione dei tempi di vita',
    "Economic well-being": 'Benessere economico',
    "Social Relationship": 'Relazioni Sociali',
    "Politics & Istitutions": 'Politica e istituzioni',
    "Security": 'Sicurezza',
    "Subjective well-being" : None,
    "Landscape & Cultural heritage" : 'Paesaggio e patrimonio culturale', 
    "Environment": 'Ambiente', 
    "Innovation, Research & Creativity" : 'Innovazione',
    "Quality of services": 'Qualità dei servizi'
}

if selectbox_ind == "Health" :
    st.subheader('1 Health')
    st.write(health)
elif selectbox_ind == 'Education & Training':
    st.subheader('2 Education & Training')
    st.write(education)
elif selectbox_ind == "Work & Life Balance":
    st.subheader('3 Work & Life Balance')    
    st.write(work)
elif selectbox_ind == "Economic well-being":
    st.subheader('4 Economic well-being')
    st.write(economic)
elif selectbox_ind == "Social Relationship":
    st.subheader('5 Social Relationships')
    st.write(social)
elif selectbox_ind == "Politics & Istitutions":
    st.subheader('6 Politics & Istitutions')
    st.write(politics)
elif selectbox_ind == "Security":
    st.subheader('7 Security')
    st.write(security)
elif selectbox_ind == "Landscape & Cultural heritage":
    st.subheader('9 Landscape & Cultural heritage')
    st.write(landscape)
elif selectbox_ind ==  "Innovation, Research & Creativity":
    st.subheader('11 Innovation, Research & Creativity ')
    st.write(innovation)
elif selectbox_ind == "Environment":
    st.subheader('10 Environment')
    st.write(environment)
elif selectbox_ind == "Quality of services":
    st.subheader('12 Quality of services ')
    st.write(services)
else:
    st.subheader('8 Subjective well-being')
    st.write(subj_wll)

    


#st.pyplot(matplotlib_fig)
#st.pyplot(matplotlib_fig2)
#st.pyplot(matplotlib_fig3)

#st.plotly_chart(plotly_fig)
#print('DF MACRO')
#print(df_macro)
#print('DF REG')
#print(df_reg.head())

# Get Provinces
df_ = read_dati_bes(path_ + '/' + List_Statistics[0])
prov_BES = provinces_BES(df_, Anomalous_Regions, Sud_Sardinia, Macro_Areas, Italy, Regions)
# Get Regions
Bes_Regions = regions_BES(Regions)
# Sorting the geodf
geodf_Macro = aggregate_macros(Macro_geodf)
# Clean
Reg_geodf = mod_col_geo(Reg_geodf)
# sorting geodataframe
geodf_reg = order_df_regions(Reg_geodf, Bes_Regions) 
# Extract the set of all Bes provinces
provinces = provinces_BES(df_, Anomalous_Regions, Sud_Sardinia, Macro_Areas, Italy, Regions)
# Adapt the provinces geodf
geodf_prov = clean_prov_geo(Prov_geodf, provinces)

# SET THE YEAR
y_ = 'V_'+ selectbox_y

List_Indicators = os.listdir('E:/Geospatial_Project/Dati_Streamlite/' + selectbox_ind)

if selectbox_ind == 'Environment': 
    _df_ = read_csv_shp('E:\Geospatial_Project\Factories')
    folium_static(marker_cluster(_df_, logo = 'E:/Geospatial_Project/logo2.png'))
    folium_static(heatmap_plot(_df_))


for stat in List_Indicators: 
    # Import the dataframe 
    df = read_dati_bes(path_+ '/' + stat)
    
    # Get_labels 
    labels = get_labels_(df)
    
    #'MACRO-AREA'
    # Creating the MacroArea Dataframe
    df_macro = order_df(df, Macro_Areas)
    
    # Create the geodaframe used in the representation
    df_macro = from_df_to_gdf(df_macro, geodf_Macro)


    #'REGIONS'
    # Creating Regions DataFrame
    df_reg = order_df(df, Bes_Regions)
    # Create the geodaframe used in the representation
    df_reg = from_df_to_gdf(df_reg, geodf_reg)



    #'PROVINCES'

    # Create the provinces df
    df_prov = order_df(df, provinces)

    # Obtain the full geodataframe of provinces 
    df_prov = from_df_to_gdf(df_prov, geodf_prov)


    # Creating the title
    titolo = get_title_(stat)

    # Static Choropletmap
    try :
        matplotlib_fig = static_choroplet(df_macro, variable = y_, title_ = titolo, color_map = 'viridis', scheme = 'quantiles', K = 5)
        matplotlib_fig2 = static_choroplet(df_reg, variable = y_, title_ = titolo, color_map = 'viridis', scheme = 'quantiles', K = 5)
        matplotlib_fig3 = static_choroplet(df_prov, variable = y_, title_ = titolo, color_map = 'viridis', scheme = 'quantiles', K = 5)
    except:
        matplotlib_fig = static_choroplet(df_macro, variable = y_, title_ = titolo, color_map = 'viridis')
        matplotlib_fig2 = static_choroplet(df_reg, variable = y_, title_ = titolo, color_map = 'viridis')
        matplotlib_fig3 = static_choroplet(df_prov, variable = y_, title_ = titolo, color_map = 'viridis')


    # Dynamic ChoropletMap 
    #plotly_fig = dynamic_choroplet(df_macro, title_ = titolo, measure = y_)

    #print(df.head())

    

    if selectbox_area == 'Macroareas':
        if df_macro[y_].isnull().all() :
            st.error('There are no data available for the chosen indicator in the selected year')
        else:
            st.pyplot(matplotlib_fig)
            st.plotly_chart(line_chart_plotly(df, to_hide_1 = provinces, to_hide_2 = Bes_Regions, to_hide_3 = Sud_Sardinia, titolo = titolo))
            folium_static(folium_interactive_map2(df_macro, y_, stat, labels))
    
    elif selectbox_area == 'Regions':
        if df_reg[y_].isnull().all() :
            st.error('There are no data available for the chosen indicator in the selected year')
        else:
            st.plotly_chart(line_chart_plotly(df, to_hide_1= provinces, to_hide_2 = Macro_Areas, to_hide_3 = Sud_Sardinia, titolo = titolo))
            st.pyplot(matplotlib_fig2)
            folium_static(folium_interactive_map2(df_reg, y_, stat, labels))
    else:
        if df_prov[y_].isnull().all() :
            st.error('There are no data available for the chosen indicator in the selected year')
        else:
            st.plotly_chart(line_chart_plotly(df, to_hide_1 = Bes_Regions, to_hide_2 = Macro_Areas, to_hide_3 = Sud_Sardinia, titolo = titolo))
            st.pyplot(matplotlib_fig3)
            folium_static(folium_interactive_map2(df_prov, y_, stat, labels))