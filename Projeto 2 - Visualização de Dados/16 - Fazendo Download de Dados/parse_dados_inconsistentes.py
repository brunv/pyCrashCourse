#
#       Plota gráfico de temperatura anual com dados faltando
#

import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'data/death_valley_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #   Obtém as datas e as temperaturas máximas e mínimas do arquivo:
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            highs.append(high)
            dates.append(current_date)
            lows.append(low)

    #   Plota os dados
    fig = plt.figure(figsize=(10,8))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='navy', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    #   Formata o gráfico
    plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA", fontsize=18)
    plt.xlabel('', fontsize=10)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=14)

    plt.show()


#       A ausência de dados pode resultar em exceções capazes de causar falhas em
#       nossos programas se não as tratarmos de forma apropriada.
#
#       Nesse arquivo, parece que em 10 de fevereiro de 2014, nenhum dado foi
#       registrado; a string temperatura máxima está vazia. Para cuidar desse
#       problema, executamos um código de verificação de erros quando os valores
#       são lidos do arquivo CSV que trata exceções que possam surgir no parse de
#       nossos conjuntos de dados.
#
#       Muitos conjuntos de dados com os quais você trabalhar terão dados faltando,
#       dados formatados de maneira inapropriada ou dados incorretos. Nesse caso,
#       utilizamos um bloco try-except-else para tratar os dados ausentes. Às vezes
#       você usará 'continue' para ignorar alguns dados ou utilizará 'remove()' ou
#       'del' para eliminá-los depois que forem extraídos.