from importlib.metadata import files
import os
from pickle import NONE
from unicodedata import name

diz_trad = {
    'Salute': 'Health', 
    'Istruzione e formazione': 'Education & Training'  ,
    'Lavoro e conciliazione dei tempi di vita': "Work & Life Balance"  ,
    'Benessere economico': "Economic well-being",
    'Relazioni sociali': "Social Relationship",
    'Politica e istituzioni': "Politics & Istitutions",
    'Sicurezza': "Security",
    'Paesaggio e patrimonio culturale': "Landscape & Cultural heritage", 
    'Ambiente': "Environment", 
    'Innovazione, ricerca e creatività': "Innovation, Research & Creativity",
    'Qualità dei servizi': "Quality of services"
}

diz_ind = {
    'Health': None, 
    'Education & Training': None,
    "Work & Life Balance": None,
    "Economic well-being": None,
    "Social Relationship": None,
    "Politics & Istitutions": None,
    "Security": None,
    "Subjective well-being": None,
    "Landscape & Cultural heritage": None, 
    "Environment": None, 
    "Innovation, Research & Creativity": None,
    "Quality of services": None
}

cartella = os.listdir('E:/Geospatial_Project/Nuovi_Dati2')

indice = None
for file in cartella:
    nome = file.split('-')
    nome = nome[0] # Indice e.g. Ambiente 
    if indice == None:
        indice = nome
        files = []
    else: 
        if indice != nome: 
            diz_ind[diz_trad[indice]] = {'files': files}
            files = []
            indice = nome
         

    
    files.append(file)


