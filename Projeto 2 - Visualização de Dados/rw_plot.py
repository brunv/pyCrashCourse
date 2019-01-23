#
#       Plotando os pontos de Random Walk
#

import matplotlib.pyplot as plt

from random_walk import RandomWalk

#   Cria um passeio aleatório e plota os pontos
rw = RandomWalk()
rw.fill_walk()

#   Define o tamanho da janela de plotagem
plt.figure(figsize=(8, 8))

#   Define o título do gráfico e nomeia os eixos
plt.title("Random Walk - " + str(rw.num_points) + " Points", fontsize = 18)
plt.xlabel("X", fontsize=10)
plt.ylabel("Y", fontsize=10)

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=1)

#   Enfatiza o primeiro e último ponto
plt.scatter(0, 0, c='green', s=30)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=30)

#   Remove os eixos
#plt.axes().get_xaxis().set_visible(False)
#plt.axes().get_yaxis().set_visible(False)

plt.show()