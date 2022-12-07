# -*- coding: utf-8 -*-

import pandas as pd #importar libreria pandas
import matplotlib.pyplot as plt #importar libreria graficos
import numpy as np
import csv 
import json 
import pymongo
from pymongo import MongoClient
import PIL
import os 
#from app import app, mongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
import msvcrt
import  wget
from PIL import Image


os.system ("cls")






#DESCARGA DEL ARCHIVO CSV
'''
url = "https://sisa.msal.gov.ar/datos/descargas/covid-19/files/covid_total_diario.csv"



wget.download(url, "C:/Users/54112/Desktop/covid19-main/vacs3.csv")

'''


#LECTURA DOCUMENTO CSV
vacunas = pd.read_csv('vacs3.csv')

#CSV A DICCIONARIO DE PYTHON
vacunas.to_dict('records')
vacunas.head()

print("------------------------------------------")
print("------------------------------------------")
print("FUENTE: 'MINISTERIO DE SALUD REPUBLICA ARGENTINA' ")
print("http://datos.salud.gob.ar/dataset/dosis-aplicadas-a-nivel-nacional")
print("------------------------------------------")
print("------------------------------------------")

#PRESENTACION DEL DOCUMENTO COMO DATAFRAME

print("INFO DEL DATAFRAME:  ")
print(vacunas.info())
print('\n'* 3)
print(vacunas.describe())
print('\n'* 3)


print("Presione una tecla para continuar...")
msvcrt.getch()
os.system ("cls")



#INFORME SOLO DATOS ARGENTINA

print("INFORME VACUNAS ARGENTINA")
print('\n')
print("------------------------------------------")
Argentina =vacunas
print(Argentina)

      




#CONVERSION A JSON




# FUNCION PARA CONVERTIR CSV  A JSON
def make_json(csvFilePath, jsonFilePath): 
	
	# CREAMOS DICCIONARIO
	data = {} 
	
	# ABRIMOS Y LEEMOS CSV
	with open(csvFilePath, encoding='utf-8') as csvf: 
		csvReader = csv.DictReader(csvf) 
		
		
		for rows in csvReader: 
			
		 
			key = rows['total_1ra_y_2da_dosis_aplicadas_acumulado'] 
			data[key] = rows 


	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
		jsonf.write(json.dumps(data, indent=4)) 
		

csvFilePath = r'vacs3.csv'
jsonFilePath = r'vacs.json'

make_json(csvFilePath, jsonFilePath)


#EXPORTANDO DATOS A BASE DE DATOS MONGO DB





 

#CONEXION A LA BASE DE MONGO DB 
myclient = MongoClient("mongodb://localhost:27017/")  
   
# SELECCION DE BASE DE DATOS
db = myclient["vacunas"] 
   
#SELECCION DE COLECCON
 
Collection = db["data"] 
  
# CARGA Y LECTURA DE JSON
with open('vacs.json') as file: 
    file_data = json.load(file) 
      
#INSERTAMOS JSON EN DB
if isinstance(file_data, list): 
    Collection.insert_many(file_data)   
else: 
    Collection.insert_one(file_data) 
    
    #------------------------------------------
    





   
     
