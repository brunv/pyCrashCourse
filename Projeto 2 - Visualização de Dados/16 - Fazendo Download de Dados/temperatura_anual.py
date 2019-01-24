#
#       Plotando segunda série de dados e sombreando área
#

import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'Data/sitka_weather_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #   Obtém as datas e as temperaturas máximas e mínimas do arquivo:
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)

    #   Plota os dados
    fig = plt.figure(figsize=(10,8))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='navy', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    #   Formata o gráfico
    plt.title("Daily high and low temperatures - 2014", fontsize=18)
    plt.xlabel('', fontsize=10)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=14)

    plt.show()


#       O argumento 'alpha' em 'plot' controla a transparência de uma cor.
#       Em 'fill_between()' passamos a lista 'dates' para os valores de x e então
#       as duas séries com valores de y, 'highs' and 'lows'. O argumento 'faceclor'
#       determina a cor da região sombreada, e lhe fornecemos um valor baixo de 
#       'alpha' para que a região preenchida conecte as duas séries de dados sem
#       provocar distrações.