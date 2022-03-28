import streamlit as st
import ee
import folium
import geemap.foliumap as geemap


m = geemap.Map(center = [41.9027835,12.4963655], zoom = 6)
m.split_map(left_layer='SATELLITE', right_layer='OpenTopoMap')
m