import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics

df_barrios = pd.read_excel('minmaxed.xlsx')

#######################################
# Function that computes weighted sum #
#######################################
def suma_ponderada(df, p):

    """
    Computes 'Quality of life' scores for the 131 neighborhoods in Madrid as a weighted sum. It also returns a benchmark value.
    Arguments:
        df: a dataframe of size [131 x n], where n is the number of indicators. All the values must be min-maxed normalized.
        p: list (length n) of coefficients for weighted sum
    """
    benchmark = []
    sumas = []

    p = [i/10 for i in p]

    for i in range(len(df)):
        n_educacion = df.loc[i, 'Educacion']
        n_salud = df.loc[i, 'Salud']
        n_ociodiurno = df.loc[i, 'OcioDiurno']
        n_ocionocturno = df.loc[i, 'OcioNocturno']
        n_entorno = df.loc[i, 'Entorno']
        n_transporte = df.loc[i, 'Transporte']
        n_seguridad = df.loc[i, 'Seguridad']
        n_precio = df.loc[i, 'Precio vivienda']

        median = 0.5

        suma = n_educacion*p[0] + n_salud*p[1] + n_ociodiurno*p[2] + n_ocionocturno*p[3] + n_transporte*p[4] + n_entorno*p[5] + (1-n_seguridad)*p[6] + (1-n_precio)*p[7]
        bench = n_educacion*median + n_salud*median + n_ociodiurno*median + n_ocionocturno*median + n_transporte*median + n_entorno*median + (1-n_seguridad)*median + (1-n_precio)*median
        
        # suma_f = suma/sum(p)
        sumas.append(suma)
        benchmark.append(bench)

    return sumas, benchmark

#First example: Young college student
#Selecciona tus pesos
pesos = {'Educacion': 0, 'Salud': 3 ,'Ocio Diurno': 3, 'Ocio Nocturno': 10,'Transporte': 5, 'Entorno': 2,'Seguridad': 2, 'Precio': 10 }
p = list(pesos.values())

#Calcula la suma ponderada y el ranking
suma_p, benchmark = suma_ponderada (df_barrios , p)
ranking = pd.DataFrame()
ranking['Nombre'] = list(df_barrios['Nombre'])
ranking['SumaPonderada'] = suma_p
ranking['Benchmark'] = benchmark
ranking.head()

#Ordenarlo en base al valor
by_value = ranking.sort_values('SumaPonderada')
top5 = by_value.tail()
print("ESTUDIANTE UNIVERSITARIO:")
print(top5[::-1])


#Second example: Old lady
#Selecciona tus pesos
pesos = {'Educacion': 2, 'Salud': 10 ,'Ocio Diurno': 1, 'Ocio Nocturno': 2,'Transporte': 8, 'Entorno': 0,'Seguridad': 0, 'Precio': 5}
p = list(pesos.values())

#Calcula la suma ponderada y el ranking
suma_p, benchmark = suma_ponderada (df_barrios , p)
ranking = pd.DataFrame()
ranking['Nombre'] = list(df_barrios['Nombre'])
ranking['SumaPonderada'] = suma_p
ranking['Benchmark'] = benchmark
ranking.head()

#Ordenarlo en base al valor
by_value = ranking.sort_values('SumaPonderada')
top5 = by_value.tail()
print("SEÑORA MAYOR:")
print(top5[::-1])

#Third example: A family
#Selecciona tus pesos
pesos = {'Educacion': 10, 'Salud': 1 ,'Ocio Diurno': 1, 'Ocio Nocturno': 0,'Transporte': 0, 'Entorno': 3,'Seguridad': 9, 'Precio': 1}
p = list(pesos.values())

#Calcula la suma ponderada y el ranking
suma_p, benchmark = suma_ponderada (df_barrios , p)
ranking = pd.DataFrame()
ranking['Nombre'] = list(df_barrios['Nombre'])
ranking['SumaPonderada'] = suma_p
ranking['Benchmark'] = benchmark
ranking.head()

#Ordenarlo en base al valor
by_value = ranking.sort_values('SumaPonderada')
top5 = by_value.tail()
print("FAMILIA:")
print(top5[::-1])
