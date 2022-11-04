import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_barrios = pd.read_excel('minmaxed.xlsx')

#######################################
# Function that computes weighted sum #
#######################################
def suma_ponderada(df, p):

    """
    Computes 'Quality of life' scores for the 131 neighborhoods in Madrid as a weighted sum.
    Arguments:
        df: a dataframe of size [131 x n], where n is the number of indicators. All the values must be min-maxed normalized.
        p: list (length n) of coefficients for weighted sum
    """

    sumas = []

    for i in range(len(df)):
        n_educacion = df.loc[i, 'Educacion']
        n_salud = df.loc[i, 'Centros de Salud']
        n_ocio = df.loc[i, 'Ocio']
        n_parques = df.loc[i, 'Parques y jardines']
        n_transporte = df.loc[i, 'Transporte']
        n_deporte = df.loc[i, 'Instalaciones deportivas']
        n_edad = df.loc[i, 'Edad media']
        n_precio = df.loc[i, 'Precio vivienda']

        suma = n_educacion * p[0] + n_salud * p[1] + n_ocio * p[2] + n_parques * p[3] + n_transporte * p[
            4] + n_deporte * p[5] - n_edad * p[6] - n_precio * p[7]
        # suma_f = suma/sum(p)
        sumas.append(suma)

    return sumas

#First example: Young college student
#Selecciona tus pesos
pesos = {'Educacion': 0, 'Salud': 5 ,'Ocio': 10, 'Parques y Jardines': 2,'Transporte': 8, 'Deporte': 7 ,'Edad Media Joven': 9, 'Precio': 10 }
p = list(pesos.values())

#Calcula la suma ponderada y el ranking
suma_p = suma_ponderada (df_barrios , p)
ranking = pd.DataFrame()
ranking['Nombre'] = list(df_barrios['Nombre'])
ranking['Valor'] = suma_p

#Ordenarlo en base al valor
by_value = ranking.sort_values('Valor')
top5 = by_value.tail()
print(top5[::-1])


#Second example: Old lady
#Selecciona tus pesos
pesos = {'Educacion': 2, 'Salud': 10 ,'Ocio': 1, 'Parques y Jardines': 2,'Transporte': 8, 'Deporte': 0,'Edad Media Joven': 0, 'Precio': 5}
p = list(pesos.values())

#Calcula la suma ponderada y el ranking
suma_p = suma_ponderada (df_barrios , p)
ranking = pd.DataFrame()
ranking['Nombre'] = list(df_barrios['Nombre'])
ranking['Valor'] = suma_p
ranking.head()
#Ordenarlo en base al valor
by_value = ranking.sort_values('Valor')
top5 = by_value.tail()
print(top5[::-1])

#Third example: A family
#Selecciona tus pesos
pesos = {'Educacion': 10, 'Salud': 8 ,'Ocio': 3, 'Parques y Jardines': 7,'Transporte': 1, 'Deporte': 5,'Edad Media Joven': 1, 'Precio': 2}
p = list(pesos.values())

#Calcula la suma ponderada y el ranking
suma_p = suma_ponderada (df_barrios , p)
ranking = pd.DataFrame()
ranking['Nombre'] = list(df_barrios['Nombre'])
ranking['Valor'] = suma_p
ranking.head()

#Ordenarlo en base al valor
by_value = ranking.sort_values('Valor')
top5 = by_value.tail()
print(top5[::-1])