# Entender os dicionários permite modelar uma diversidade de OBJETOS do mundo real
# de modo mais preciso.
#

#
# Criando um dicionário
#

alien = {
    'cor': 'azul',
    'pontos': 5,
    'pos_x': 50
    }
alien2 = {}

#
# Acessando os valores de um dicionário
#

print(alien['cor'])     # azul
print(alien['pontos'])  # 5

#
# Adicionando e modificando valores a um dicionário
#

alien2['cor'] = 'verde' # adiciona
alien2['pontos'] = 10   # adiciona
print(alien2)

alien['pos_x'] = 50     # altera
alien['pos_y'] = 25     # adiciona
print(alien)

#
# Deletando valores de um dicionário
#

del alien['pos_x']
del alien['pos_y']
print(alien)