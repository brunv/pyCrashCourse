#
#       Gerando um gráfico linear simples
#

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

#   Define o título do gráfico e nomeia os eixos
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#   Estiliza as marcações dos eixos
plt.tick_params(axis='both', labelsize=14)

plt.show()


#       Inicialmente importamos 'pyplot' usando o alias 'plt', como convenção.
#       A função 'plot()' plota os números e a função 'show()' abre o visualizador
#       do matplotlib para exibir o gráfico e, felizmente, o matplotlib permite
#       ajustar todos os recursos de visualização.
#
#       Quando oferecemos uma sequência de números a 'plot()', ele supôe que o
#       primeiro ponto de dado corresponde a um valor de coordenada x igual a 0,
#       mas nosso primeiro ponto corresponde a um valor de x igual 1. Podemos
#       sobrescrever o comportamento-padrão fornecendo a 'plot' os valores tanto
#       de entrada quanto de saída usados para calcular os quadrados.