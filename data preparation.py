import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

barrios = pd.read_excel("Barrios_Tabla.xlsx")

#Delete first column (numbers from 0 to 130)
del barrios['Unnamed: 0']

#Delete Neighborhood code
del barrios['Codigo']

#Remove names, price, and age for now
barrios_names = barrios.pop('Nombre')

#Scale variables by population
barrios_escalados = pd.DataFrame.copy(barrios, deep=True)

barrios_escalados[['Educacion', 'Centros de Salud','Ocio','Parques y jardines','Instalaciones deportivas']] = \
    barrios_escalados[['Educacion', 'Centros de Salud','Ocio','Parques y jardines','Instalaciones deportivas']]\
        .div(barrios_escalados.Poblacion, axis=0)
del barrios_escalados["Poblacion"]

#Add bias term to each variable and apply logarithmic function
barrios_escalados['Educacion'] = np.log(barrios_escalados['Educacion']+pd.Series(np.tile(0.00015, 131)))
barrios_escalados['Centros de Salud'] = np.log(barrios_escalados['Centros de Salud']+pd.Series(np.tile(0.00001, 131)))
barrios_escalados['Ocio'] = np.log(barrios_escalados['Ocio']+pd.Series(np.tile(0.0003, 131)))
barrios_escalados['Parques y jardines'] = np.log(barrios_escalados['Parques y jardines'] +
                                                 pd.Series(np.tile(0.00002, 131)))
barrios_escalados['Instalaciones deportivas'] = np.log(barrios_escalados['Instalaciones deportivas'] +
                                                       pd.Series(np.tile(0.00002, 131)))

#Build scaler min-max model
minmax = MinMaxScaler()

#Fit scaler
minmax.fit(barrios_escalados)

#Transform
barrios_minmax = pd.DataFrame(minmax.transform(barrios_escalados))

#Reassign variable names and column bind with neighborhood names
barrios_final = pd.concat([barrios_names,barrios_minmax],axis=1)

barrios_final.columns = ["Nombre","Educacion","Centros de Salud","Ocio","Parques y jardines",
                         "Transporte", "Instalaciones deportivas", "Edad media", "Precio vivienda"]

print(barrios_final)

barrios_final.to_excel("minmaxed.xlsx", index=False)



