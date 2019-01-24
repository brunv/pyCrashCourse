#
#       Plotando os resultados de um único dado
#

import pygal
from die import Die

#   Cria um D6
die = Die()
times = 1000

#   Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(times):
    result = die.roll()
    results.append(result)

#   Analisa os resultados
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#   Visualiza os resultados
hist = pygal.Bar()

hist.title = "Results of rolling one D6 " + str(times) + " times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.Y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('charts/single_die_plot.svg')

#print(results)
print(frequencies)


#       Gerados um gráfico de barras criando uma instância de 'pygal.Bar()', que
#       armazenamos em 'hist'.
#       Usamos 'add()' para ascrescentar uma série de valores ao gráfico: passando-
#       -lhe um rótulo para o conjunto de valores a ser adicionado e uma lista de
#       valores que aparecerão no gráfico. Por fim, renderizamos o gráfico em um
#       arquivo SVG.
#
#       Observe que o Pygal fez o gráfico ser interativo: passe o cursos sobre
#       qualquer barra e você verá o dado associado a ela.