import math
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import pandas as pd

archivo = pd.read_csv('WEO_Data.csv', thousands=',', decimal='.')
archivo.rename(columns={'Country': 'Pais'}, inplace=True)
archivo.set_index('Pais', inplace=True)
lista = list(map(str, range(2000, 2024)))

E_Alumnos = pd.read_excel('BI_Alumnos.xlsx', sheet_name='Hoja1', skiprows=0)
data1 = pd.DataFrame(E_Alumnos)
E_Clientes = pd.read_excel('BI_Clientes.xlsx', sheet_name='Hoja1', skiprows=0)
data2 = pd.DataFrame(E_Clientes)


def grafico1():
    peru = archivo.loc['Peru', lista]
    peru.plot(kind='line')
    plt.title('peru - PBI')
    plt.ylabel('Millones de $')
    plt.xlabel('Años')
    plt.show()


def grafico2():
    paises = archivo.loc[['Peru', 'Chile'], lista]
    paises = paises.transpose()
    paises.plot(kind='line')
    plt.title('Peru vs Chile - PBI')
    plt.ylabel('Millones de $')
    plt.xlabel('Años')
    plt.show()


def grafico3():
    archivo.sort_values(by='2022', ascending=False, inplace=True)
    top5 = archivo[lista].head(5)
    top5 = top5.transpose()
    top5.plot(kind='line')
    plt.title('Top 5 - PBI')
    plt.ylabel('Millones de $')
    plt.xlabel('Años')
    plt.show()


def grafico4():
    archivo['2002'].plot(kind='hist')
    plt.title('Paises - PBI')
    plt.ylabel('Numero de paises')
    plt.xlabel('Billones de dolares')
    plt.show()


def grafico5():
    peru = archivo.loc['Peru', lista]
    peru.plot(kind='bar')
    plt.title('peru - PBI')
    plt.ylabel('Millones de $')
    plt.xlabel('Años')
    plt.show()


def grafico6():
    archivo.sort_values(by='2022', ascending=True, inplace=True)
    lista10 = archivo['2022'].tail(10)
    lista10.plot(kind='barh')
    plt.title('Top 10 - PBI')
    plt.ylabel('Millones de $')
    plt.xlabel('Años')
    plt.show()


def tabla1():
    nr = round(1 + 3.3 * math.log(len(data1.index), 10))
    E_Alumnos["NotasG"] = pd.cut(E_Alumnos["Nota"], bins=nr)
    notasG = E_Alumnos.groupby("NotasG").agg(frequency=("Nota", "count"))
    notasG["cum_frequency"] = notasG["frequency"].cumsum()
    notasG["rela_frequency"] = (data1.groupby("NotasG").agg(frequency=("NotasG", "count")) * 100) / len(data1.index)
    notasG["cum_rela_frequency"] = notasG["rela_frequency"].cumsum()
    print(notasG)


def tabla2():
    ChildrenG = data2.groupby("TotalChildren").agg(frequency=("TotalChildren", "count"))
    ChildrenG["cum_frequency"] = ChildrenG["frequency"].cumsum()
    ChildrenG["rela_frequency"] = (data2.groupby("TotalChildren").agg(frequency=("TotalChildren", "count"))*100)/len(data2.index)
    ChildrenG["cum_rela_frequency"] = ChildrenG["rela_frequency"].cumsum()
    print(ChildrenG)


grafico1()
grafico2()
grafico3()
grafico4()
grafico5()
grafico6()
tabla1()
tabla2()
