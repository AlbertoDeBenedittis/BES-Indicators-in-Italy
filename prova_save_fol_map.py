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
from functions2 import * 
import leafmap
import folium
from streamlit_folium import folium_static
from Testo_Indicatore import * 
from dictionaries import diz_ind

_df_ = read_csv_shp('E:\Geospatial_Project\Factories')

marker_cluster(_df_, logo = 'E:/Geospatial_Project/logo2.png').save('E:/Geospatial_Project/m1.html')

