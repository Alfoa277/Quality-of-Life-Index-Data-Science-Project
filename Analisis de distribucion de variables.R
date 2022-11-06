setwd("D:/OneDrive - Universidad Carlos III de Madrid/41/Data Science Project/Segundo Informe")
#setwd("C:/Users/ALF/OneDrive - Universidad Carlos III de Madrid/41/Data Science Project/Segundo Informe")


#Cargar los datos y preparar dataframe para visualizaciones. El objetivo de este
# archivo es mediante inspección de las distribuciones, decidir si es necesario
# aplicar alguna transformacion a las variables y en caso afirmativo, decidir
# el valor del bias que se le sumara para lidiar con el problema del logaritmo
# de 0.

library(readxl)
barrios <- read_excel("Barrios_Tabla.xlsx")
#Remove some columns
barrios = barrios[,-1]
barrios = barrios[,-2]
nombre_barrios = barrios$Nombre

barrios = barrios[,-1]
row.names(barrios) = nombre_barrios
library(corrplot)
corrplot(cor(barrios[,-7]))

barrios_escalados = data.frame(Educacion = barrios$Educacion/barrios$Poblacion,
                               Salud = barrios$`Centros de Salud`/barrios$Poblacion,
                               Ocio = barrios$Ocio/barrios$Poblacion,
                               ParqJar = barrios$`Parques y jardines`/barrios$Poblacion,
                               Transporte = barrios$Transporte,
                               InstDepor = barrios$`Instalaciones deportivas`/barrios$Poblacion,
                               EdadMedia = barrios$`Edad Media`,
                               PrecioVivienda = barrios$`Precio vivienda`)
corrplot(cor(barrios_escalados))


summary(barrios)
"""La gran mayoria de las variables contienen outliers"""

#Analisis de distribuciones####
#Educacion
plot(barrios_escalados$Educacion, ylab = '', xlab = '')
plot(log(barrios_escalados$Educacion+rep(0.00015),131), ylab = '', xlab = '')
new_educacion = log(barrios_escalados$Educacion+rep(0.00015),131)
"""Dejar la distribución más o menos simétrica"""
#Salud
plot(barrios_escalados$Salud, ylab = '', xlab = '')
plot(log(barrios_escalados$Salud+rep(0.00001,131)), ylab = '', xlab = '')
"""Una diferencia grande entre tener y no tener centros de salud. Dejamos un
hueco para que los scores de los barrios con por lo menos un centro de salud 
sean significativamente más altos que los barrios sin centros de salud."""
new_salud = log(barrios_escalados$Salud+rep(0.00001,131))
#Ocio
plot(barrios_escalados$Ocio)
plot(log(barrios_escalados$Ocio+rep(0.0003,131)))
"""Mantener mas o menos las distancias entre los barrios con mas ocio por
persona y los que tienen menos."""
new_ocio = log(barrios_escalados$Ocio+rep(0.0003,131))
#Parques y jardines
plot(barrios_escalados$ParqJar)
plot(log(barrios_escalados$ParqJar+rep(0.00002,131)))
"""Diferencia grande entre tener 0 parques a tener alguno. Diferencia tambien
entre tener algun parque a tener varios parques. 'Hueco' menos diferenciado
que en el caso de los centros de salud."""
new_parques = log(barrios_escalados$ParqJar+rep(0.00002,131))
#Transporte
"""No escalamos el transporte por el numero de habitantes por barrio."""
plot(barrios$Transporte)
"""Ninguna transformacion es necesaria. Comparando con la variable educacion,
no tiene sentido hacer la distribucion mas simetrica porque tener un mayor
numero de paradas de transporte publico es significativamente mejor que tener
menos, mientras que en el caso de educacion una vez tu hijo escoge ir a un 
colegio o instituto en particular, es irrelevante que haya muchos mas centros
en el barrio. Por ese motivo no es necesario dar una mayor puntuacion a barrios
con un numero de centros educativos superior al resto."""
plot(log(barrios_escalados$Transporte+rep(0.0001,131)))
new_tranporte = log(barrios_escalados$Transporte+rep(0.0001,131))
#Instalaciones deportivas
plot(barrios_escalados$InstDepor)
plot(log(barrios_escalados$InstDepor+rep(0.00002,131)))
new_instalacionesdeportivas = log(barrios_escalados$InstDepor+rep(0.00002,131))
"""Distribucion de instalaciones deportivas mas o menos simetrica tras la 
transformacion."""
#Edad media
plot(barrios$`Edad Media`)
"""No requiere transformacion"""
#Precio
plot(barrios$`Precio vivienda`)
"""No requiere transformacion"""

#Apply Min-max normalization
library(scales)

minmaxed = data.frame(Barrio = nombre_barrios,
                      Educacion = rescale(new_educacion),
                      'Centros de Salud' = rescale(new_salud),
                      Ocio = rescale(new_ocio),
                      'Parques y Jardines' = rescale(new_parques),
                      Transporte = rescale(new_tranporte),
                      'Instalaciones Deportivas' = rescale(new_instalacionesdeportivas),
                      'Edad Media' = rescale(barrios$`Edad Media`),
                      'Precio Vivienda' = rescale(barrios$`Precio vivienda`))

#library(writexl)
#write_xlsx(minmaxed, "D:/OneDrive - Universidad Carlos III de Madrid/41/Data Science Project/Segundo Informe/minmaxedd.xlsx")
