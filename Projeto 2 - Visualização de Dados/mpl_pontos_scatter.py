#
#       Plotando e estilizando pontos com 'scatter()'
#

import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
     edgecolor='none', s=20)

#   Define o título do gráfico e nomeia os eixos
plt.title("Square Numbers", fontsize=18)
plt.xlabel("Value", fontsize=8)
plt.ylabel("Square of Value", fontsize=8)

#   Define o intervalo do para cada eixo
plt.axis([0, 1000, 0, 1100000])

#   Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both', which='major', labelsize=8)

#   Salvando o gráfico automaticamente
#   O segundo argumento remove espaços em branco extras ao redor do gráfico
#plt.savefig('squares_plot.png', bbox_inches='tight')

plt.show()


#       Para plotar um único ponto, utilize a função 'scatter()'. Passe um único
#       par (x, y) do ponto em que você estiver interessado para 'scatter()', e
#       esse valor deverá ser plotado.
#       Para plotar mais de um ponto, basta passar listas separadas com pontos de
#       x e de y.
#
#       x_values recebe uma lista com valores de 1 até 1000. Em seguida, uma 'list
#       comprehension' gera os valores de y percorrendo os valor de x com um laço
#       elevando cada número ao quadrado e armazenando os resultados em y_values.
#
#       Como esse é um conjunto bem grande de dados, utilizamos a função 'axis()'
#       para especificar o intervalo de cada eixo. A função 'axis()' exige quatro
#       argumentos: os valores mínimo e máximo para o eixo x e para o eixo y.
#
#       Para mudar a cor dos pontos, passe 'c' para 'scatter()' como o nome de uma
#       cor a ser usada. Exemplo: c='red'.
#       Podemos também definir cores personalizadas usando o modelo RGB. Para isso,
#       passe uma tupla utilizando valores entre 0 e 1. Exemplo: c=(0,0,0.8)
#
#       Um 'colormap' é uma série de cores em um gradiente que varia de uma cor
#       inicial até uma cor final. Por exemplo, você pode deixar os valores
#       menores com uma cor clara e os valores maiores com uma cor mais escura.
#       O módulo 'pyplot' inclui um conjunto de colormaps embutidos.
#       No exemplo da linha 10, passamos a lista de valores y para 'c' e, em
#       seguida, informamos ao pyplot qual é o colormap a ser usado por meio do
#       argumento 'cmap'. Esse código pinta os pontos com valores menorores de y
#       com azul claro e os pontos com valores maiores de y com azul escuro.