import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

barrios = pd.read_excel("Barrios Ajustados.xlsx")

#Delete Neighborhood code
del barrios['Codigo']

#Delete Renta Media
del barrios['RentaMedia']

#Remove names, price, and age for now
barrios_names = barrios.pop('Nombre')


#Scale variables by population
barrios_escalados = pd.DataFrame.copy(barrios, deep=True)

barrios_escalados[['Educacion', 'Entorno','OcioDiurno','OcioNocturno','Salud']] = \
    barrios_escalados[['Educacion', 'Entorno','OcioDiurno','OcioNocturno','Salud']]\
        .div(barrios_escalados.Poblacion, axis=0)
del barrios_escalados["Poblacion"]

#Add bias term to each variable and apply logarithmic function
barrios_escalados['Educacion'] = np.log(barrios_escalados['Educacion']+pd.Series(np.tile(0.000025, 131)))
barrios_escalados['Salud'] = np.log(barrios_escalados['Salud']+pd.Series(np.tile(0.000005, 131)))
barrios_escalados['OcioDiurno'] = np.log(barrios_escalados['OcioDiurno']+pd.Series(np.tile(0.00006, 131)))
barrios_escalados['OcioNocturno'] = np.log(barrios_escalados['OcioNocturno']+pd.Series(np.tile(0.00006, 131)))
barrios_escalados['Entorno'] = np.log(barrios_escalados['Entorno'] + pd.Series(np.tile(0.00003, 131)))
barrios_escalados['Transporte'] = np.log(barrios_escalados['Transporte'] + pd.Series(np.tile(10, 131)))
barrios_escalados['Seguridad'] = np.log(barrios_escalados['Seguridad'] - pd.Series(np.tile(0.0005, 131)))
#Build scaler min-max model
minmax = MinMaxScaler()

#Fit scaler
minmax.fit(barrios_escalados)

#Transform
barrios_minmax = pd.DataFrame(minmax.transform(barrios_escalados))

#Reassign variable names and column bind with neighborhood names
barrios_final = pd.concat([barrios_names,barrios_minmax],axis=1)

print(barrios_final.head())
print(barrios_escalados.columns)

barrios_final.columns = ["Nombre","Educacion","Transporte","Salud","OcioNocturno",
                         "OcioDiurno", "Entorno", "Seguridad", "Precio vivienda"]

print(barrios_final)

barrios_final.to_excel("minmaxed.xlsx", index=False)



