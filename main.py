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
    
#Calcular media con map
pmapa = nframe.iloc[0:i]
map(lambda x: sum(x)/len(x), pmapa)
print(pmapa)