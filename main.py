import ssl
from urllib import request as rq
import pandas as pd
import statistics as stat

num_tabla = 3996
download = False
filexls = 'filexls.xls'

if (download):
    url = f"https://www.ine.es/jaxiT3/files/t/es/xls/{num_tabla}.xls?nocab=1 "
    import requests
    local_filename = requests.get(url)
    open(filexls, 'wb').write(local_filename.content)


f_excel = pd.ExcelFile(filexls)
dataframe = f_excel.parse(f'tabla-{num_tabla}')

columnas = dataframe.loc[6]

#todos los generos frame
nframe = dataframe.loc[8:60]
columnas[0] = 'Todos los generos'
nframe.columns = columnas
#print(nframe)
#hombres frame
hframe = dataframe.loc[62:114]
columnas[0] = 'Hombres'
hframe.columns = columnas
print(columnas)
#print(hframe)
#mujeres frame
mframe = dataframe.loc[116:168]
columnas[0] = 'Mujeres'
mframe.columns = columnas
#print(mframe)


#series panda to list
lista1 = nframe.loc[12]
#print(type(lista1))
lista1 = lista1.to_list()
#print(lista1)
#series panda to dict
dict1 = nframe.loc[12]
#print(type(dict1))
dict1 = dict1.to_dict()
#print(dict1)
#series panda to tuple
tuple1 = nframe.loc[12]
#print(type(tuple1))
tuple1 = tuple(tuple1)
#print(tuple1)
#series panda to set
set1 = nframe.loc[12]
#print(type(set1))
set1 = set(set1)
#print(set1)

#abrir archivo y escribir lista
with open('lista.txt', 'w') as f:
    for x in lista1:
        f.write(f"{str(x)} ")

nframe1 = nframe.transpose()
#print(nframe1)
i = len(nframe)

for y in range(i):
    print(y)
    print(nframe1.size)
    tasa = []
    for x in nframe.iloc[y]:
        if type(x) == str:
            print(x)
        else:
            tasa.append(x)
    modes = stat.mode(tasa)
    print(f"La moda es {modes}")
    print(f"La media es {sum(tasa)/len(tasa)}")
    #Calcular la varianza
    varianza = 0
    for x in tasa:
        varianza += (x - sum(tasa)/len(tasa))**2
    varianza = varianza/len(tasa)
    print(f"La varianza es {varianza}")
    
#Dividir entre 100
pmapa = nframe.iloc[1]
print(type(pmapa))
print(pmapa)
pmapa = pmapa.map(lambda x: x if type(x) == str else x/100)
print(pmapa)

#Filter
print("------------------")
print(mframe.filter(regex='2002T1', axis=1))


#Crea una base de datos SQLite desde python
import sqlite3
conn = sqlite3.connect('test.db')
c = conn.cursor()
#Crear tabla a partir de un dataframe
print(hframe)
import xlwt
hframe.to_excel('hombres.xls')
# 
#Leer tabla
# c.execute("SELECT * FROM dataframe")
# print(c.fetchall())
print(columnas)
cSoloParo = columnas[1:84]
print(cSoloParo)
#Crear dataframe a partir de un dataframe de pandas y una lista de columnas
dfSoloParo = hframe.iloc[1:84]
dfSoloParo.to_excel('soloparo.xls')
print("AJSDJDJAD")
print(nframe.iloc[:,1:84])
#Sacar filas de un dataframe
print(nframe1)
dfSoloParo.insert(0, "", nframe1.iloc[0])
dfSoloParo.dropna()
print(dfSoloParo.iloc[:,1:84].to_sql('dfSoloParo', conn, if_exists='replace'))
dfSoloParo.to_excel('soloparo.xls')
#dfSoloParo.to_sql('dfSoloParo', conn)
#Leer tabla
c.execute("SELECT * FROM dfSoloParo")
print(c.fetchall())
# Realiza al menos tres consultas distintas
c.execute("SELECT Mujeres FROM dfSoloParo")
print(c.fetchall())
c.execute("SELECT Mujeres, 2022T3 FROM dfSoloParo")
print(c.fetchall())
#insertar serie en tabla existente
#dfSoloParo.iloc[:,1:84].to_sql('dfSoloParo', conn, if_exists='append')



# ● Guarda los datos de una de las consultas en un nuevo dataset
# ● Guarda el nuevo dataset como una nueva tabla en la base de datos
