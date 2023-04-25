import readcsv
import utils
import chart
import pandas as pd

def run():
    data = readcsv.leercsv('data.csv')
    df = pd.read_csv('data.csv')
    lables, values, pais = utils.filtro(data)
    chart.graficarbar(lables, values, pais)
    chart.graficarpie(lables, values, pais)

if __name__ == '__main__':
    run()