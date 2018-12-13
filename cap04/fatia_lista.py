#
# Trabalhando com partes (fatia) de uma lista
#

lista = ['apple', 'orange', 'grape', 'banana', 'strawberry', 'lemon']

print(lista[0:3])       # apple, orange, grape

print(lista[:3])        # apple, orange, grape

print(lista[4:6])       # strawberry, lemon

print(lista[4:])        # strawbeery, lemon

print(lista[-2:])       # strawberry, lemon

print(lista[2:4])       # grape, banana

#
# Copiando listas e fatias de listas
#

frutas = lista[:]       # copia a lista toda para frutas

#frutas = lista         # não copia a lista, apenas faz frutas apontar para lista também

print(lista)
print(frutas)

lista.append('pineapple')
frutas.append('peach')

print(lista)
print(frutas)