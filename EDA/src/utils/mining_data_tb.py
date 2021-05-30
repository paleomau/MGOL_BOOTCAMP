import pandas as pd
import numpy as np
import sys, os


def limpiar(df):
    dflimpio = df.dropna()
    return dflimpio


def all_nan_columns(lista):
    df = list(map(limpiar, lista))
    df1 = df[0]
    df2 = df[1]
    df3 = df[2]
    return df1, df2, df3
#guardo por posicion no por nombre


'''
import pandas as pd
import numpy as np
def mineria_pacientes(tsv):
    pacientes_bruto = pd.read_csv("../../../../data/" + tsv, sep='\t')
    pacientes_bruto.set_index('track_name', inplace=True)
    pacientes_bruto.drop(['track_type'], axis=1, inplace = True)
    pacientes_bruto
    pacientes_select = pacientes_bruto.loc[['Sex', 'Diagnosis Age', 'Progress Free Survival (Months)', 'Ethnicity Category', 'Mutation Count']]
    pacientes_select = pacientes_select.dropna(axis=1, how='any')
    pacientes = pacientes_select.T
    return pacientes'''

def mineria_pacientes_parcial(df):
    df.set_index('track_name', inplace=True)
    df.drop(['track_type'], axis=1, inplace = True)
    df
    pacientes_select = df.loc[['Sex', 'Diagnosis Age', 'Progress Free Survival (Months)', 'Ethnicity Category', 'Mutation Count']]
    pacientes_select = pacientes_select.dropna(axis=1, how='any')
    pacientes = pacientes_select.T
    return pacientes

'''
if __name__ == "__main__":
ruta = __file__
print(ruta)
N = 3  # Mi carpeta EDA raiz está 3 carpetas por encima de mi fichero actual
for i in range(N):
    ruta = os.path.dirname(ruta)
    print(ruta)
print("---------")
sys.path.append(ruta)
print(sys.path)
'''