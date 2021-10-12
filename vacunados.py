import streamlit as st
import pandas as pd
import numpy as np
import numpy as np
import csv 
import json 
from pymongo import MongoClient
import PIL
import os 
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
import msvcrt
import  wget

st.title('VACUNAS COVID DOS DOSIS')
url = "https://sisa.msal.gov.ar/datos/descargas/covid-19/files/covid_total_acumulado.csv"
wget.download(url, "C:/Users/54112/Desktop/covid19-main/vacs3.csv")

DATE_COLUMN = "total_1ra_y_2da_dosis_aplicadas"
data1 = "vacs3.csv"

@st.cache
def load_data(nrows):
    data = pd.read_csv(data1, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.data([DATE_COLUMN])
    return data

data_load_state = st.text('CARGANDO DATOS...')
data = pd.read_csv(data1)
if st.checkbox('Visualizar Datos'):
    st.subheader('PRESENTACIÒN DE DATOS')
    st.write(data)
data.to_dict('records')

cabeza= data.head(10)
if st.checkbox('encabezado  del dataset'):
    st.subheader('encabezado  del dataset')
    st.write(cabeza)
infor= data.info()
if st.checkbox('informacion  del dataset'):
    st.subheader('informacion  del dataset')
    st.write(infor)
descrip= data.describe()
if st.checkbox('descripcion de dataset'):
    st.subheader('descripcion de dataset')
    st.write(descrip)
if st.button("GRAFICO"):
    hist_values = np.histogram(
        data[DATE_COLUMN])[0]
    st.bar_chart(hist_values)
st.markdown(" GRACIAS POR USAR NUESTROS SERVICIOS ")
st.subheader('Informes Covid Dan Data Scientist')

# The preset Streamlit theme that your custom theme inherits from. One of "light" or "dark".
base ="dark"
# Primary accent color for interactive elements.
# Background color for the main content area.
backgroundColor = "pink"
# Background color used for the sidebar and most interactive widgets.
# Color used for almost all text.
textColor = "blue"
# Font family for all text in the app, except code blocks. One of "sans serif", "serif", or "monospace".
# Default: "sans serif"
font = "sans serif"
