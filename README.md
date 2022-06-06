# BES-Indicators-in-Italy 🌍 

## Aim of the project 🎯
This repository has been created for the [Geospatial Analysis and Representation for Data Science](https://napo.github.io/geospatial_course_unitn/) course of the University of Trento, teached by [Diego Giuliani](https://webapps.unitn.it/du/it/Persona/PER0020867/Didattica) and [Maurizio Napolitano](https://ict.fbk.eu/people/detail/maurizio-napolitano/) (a.y. 2021/2022).

The aim is to provide some insights about The fair and sustainable well-being index, the [__BES__](\href{https://www.istat.it/en/well-being-and-sustainability/the-measurement-of-well-being/bes-report) indicators in Italy and to visualize their distribution through (choroplet)maps in order to understand how the sustainability process is evolving in Italy.

## The Website 💻

The results of the analysis are summarized in a [website](https://share.streamlit.io/albertodebenedittis/besapp/main/dash.py).
The code for the website can be found at the following link: https://github.com/AlbertoDeBenedittis/BesApp

The website allows: 

* to visualiza maps and statistics for each of the 12 Bes indicator
* to navigate across the years, from 2004 to 2018, in order to see how variables have changed across the years 
* to look at the data from three different point of view: macroareas, regions and provinces 

## Repository structure 📂

The repository is structured as follows: 

* The folder Dati contains another folder Limiti which containes the shape files that describe the administrative boarders of the italian territories according to [ISTAT](https://www.istat.it/it/archivio/222527)
* The folder Dati Bes contains an excel file where are stored [all the data](https://www.istat.it/en/well-being-and-sustainability/the-measurement-of-well-being/indicators) of each of the Bes indicator.
* Dati Streamlite contains all the data after the data processing stage. This folders contains a folder for each domain where are stored the files containing the data of each indicator
* Dictionaries contains three pickels files. Each of them contains a python dictionary where are saved the results of the best territory analysis. 
* Factories, Freetime, and No_Profit contain the data retrived from osm via pyrosm about all the factories, the non for profit organizations and the amanities of the biggest city in Italy. 
* Medaglie contains the .png files of a gold medal, a silver medal, and a bronze medal. They are used in the maps of the best territories
* Icons contains the .png files of the logos of the 10 biggest city of italy. They are used in the isochrones maps. 


## The code 🐍

The code is fully written in Python. 
For the project I have used two different virtual environments due to some problems with the underlying dependencies of some libraries such as Pyrosm and Geopandas. 
The requirements for the first environment are written in the requirements.txt file while the requirements for the second environment are described in the `requirements2.txt`





