#
#       Fazendo parser de arquivos CSV
#

import csv
from matplotlib import pyplot as plt

filename = 'Data/sitka_weather_07-2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)   # cabeçalhos

    #   Exibindo os cabeçalhos e suas posições:
    #for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    #   Obtém as temperaturas máximas do arquivo:
    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)

    #   Plota os dados
    fig = plt.figure(figsize=(10,8))
    plt.plot(highs, c='red')

    #   Formata o gráfico
    plt.title("Daily temperatures, July 2014", fontsize=18)
    plt.xlabel('', fontsize=10)
    plt.ylabel('Temperature (F)', fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=14)

    plt.show()



#       O módulo 'csv' contém a função 'next()' que devolve a próxima linha do
#       arquivo quando recebe o objeto reader. Já 'reader()' processa a primeira
#       linha de valores separados por vírgula do arquivo e armazena cada um deles
#       como um item em uma lista. O objeto reader continua a partir de onde parou
#       no arquivo CSV e devolve automaticamente cada linha após a sua posição
#       atual.
#
#       Usamos 'enumerate()' na lista para obter o índice de cada item, assim como
#       o valor.
#
#       