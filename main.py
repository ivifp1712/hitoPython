import ssl
from urllib import request as rq
import pandas as pd

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
#print(dataframe)
dataframe2 = pd.read_excel(filexls, sheet_name=f'tabla-{num_tabla}')
#print(dataframe2)

filas = dataframe.loc[range(177)]
#obtener la fila 10
fila10 = dataframe.loc[10]
#obtener la fila 10 y columna 2

#indices
indices = dataframe.loc[7]
print(indices)
#primera fila, total nacional
fila10col2 = dataframe.loc[8]
fila10col2 = fila10col2.dropna()
print(fila10col2)
print(fila10col2.dtype)

