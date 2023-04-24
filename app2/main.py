import readcsv
import utils
import chart

def run():
    data = readcsv.leercsv('data.csv')
    lables, values, pais = utils.filtro(data)
    chart.graficarbar(lables, values, pais)
    chart.graficarpie(lables, values, pais)

if __name__ == '__main__':
    run()