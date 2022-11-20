import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics

df_barrios = pd.read_excel('minmaxed.xlsx')

#######################################
# Function that computes weighted sum #
#######################################
def suma_poderada_orden(df, orden):

    """
    Computes 'Quality of life' scores for the 131 neighborhoods in Madrid as a weighted sum. It also returns a benchmark value.
    Arguments:
        df: a dataframe of size [131 x n], where n is the number of indicators. All the values must be min-maxed normalized.
        p: list (length n) of coefficients for weighted sum
    """
    benchmark = []
    sumas = []

    p = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}

    median = 3.5

    for i in range(len(df)):
        n_educacion = df.loc[i, 'Educacion']
        n_salud = df.loc[i, 'Salud']
        n_ociodiurno = df.loc[i, 'OcioDiurno']
        n_ocionocturno = df.loc[i, 'OcioNocturno']
        n_entorno = df.loc[i, 'Entorno']
        n_transporte = df.loc[i, 'Transporte']
        n_seguridad = df.loc[i, 'Seguridad']
        n_precio = df.loc[i, 'Precio vivienda']

        suma = n_educacion*p[str(orden[0])] + n_salud*p[str(orden[1])] + n_ociodiurno*p[str(orden[2])] + n_ocionocturno*p[str(orden[3])] + n_transporte*p[str(orden[4])] + n_entorno*p[str(orden[5])] + (1-n_seguridad)*p[str(orden[6])] + (1-n_precio)*p[str(orden[7])]
        bench = n_educacion*median + n_salud*median + n_ociodiurno*median + n_ocionocturno*median + n_transporte*median + n_entorno*median + (1-n_seguridad)*median + (1-n_precio)*median
        
        # suma_f = suma/sum(p)
        sumas.append(suma)
        benchmark.append(bench)

    return sumas, benchmark

#First example: Young college student
#Selecciona tus pesos
pesos = {'Educacion': 8, 'Salud': 6 ,'Ocio Diurno': 7, 'Ocio Nocturno': 1,'Transporte': 3, 'Entorno': 5 ,'Seguridad': 4, 'Precio': 2 }
p = list(pesos.values())

#Calcula la suma ponderada y el ranking
suma_p, benchmark = suma_poderada_orden(df_barrios, p)
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
pesos = {'Educacion': 8, 'Salud': 1 ,'Ocio Diurno': 3, 'Ocio Nocturno': 1,'Transporte': 7, 'Entorno': 4 ,'Seguridad': 2, 'Precio': 6 }
p = list(pesos.values())

#Calcula la suma ponderada y el ranking
suma_p, benchmark = suma_poderada_orden(df_barrios, p)
ranking = pd.DataFrame()
ranking['Nombre'] = list(df_barrios['Nombre'])
ranking['SumaPonderada'] = suma_p
ranking['Benchmark'] = benchmark
ranking.head()

#Ordenarlo en base al valor
by_value = ranking.sort_values('SumaPonderada')
top5 = by_value.tail()
print()
print("SEÑORA MAYOR:")
print(top5[::-1])

#Third example: A family
#Selecciona tus pesos
pesos = {'Educacion': 1, 'Salud': 4 ,'Ocio Diurno': 7, 'Ocio Nocturno': 8,'Transporte': 6, 'Entorno': 5 ,'Seguridad': 2, 'Precio': 3 }
p = list(pesos.values())

#Calcula la suma ponderada y el ranking
suma_p, benchmark = suma_poderada_orden(df_barrios, p)
ranking = pd.DataFrame()
ranking['Nombre'] = list(df_barrios['Nombre'])
ranking['SumaPonderada'] = suma_p
ranking['Benchmark'] = benchmark
ranking.head()

#Ordenarlo en base al valor
by_value = ranking.sort_values('SumaPonderada')
top5 = by_value.tail()
print()
print("FAMILIA:")
print(top5[::-1])
