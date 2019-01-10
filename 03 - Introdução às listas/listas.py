#
# Imprimindo lista
#
cores = ['azul', 'rosa', 'verde']
print(cores)

#
# Acessando elementos da lista
#
print("\n**\n** Acessando elementos na lista\n**\n")

print(cores[0])
print(cores[2])
print(cores[-1]) # índice negativo começa pelo final da lista
print(cores[-2])

# 
# Alterando elementos em uma lista 
#
print("\n**\n** Alterando elementos na lista\n**\n")

cores[0] = 'amarelo'
print(cores)

#
# Adicionando elementos em uma lista
#
print("\n**\n** Adicionando elementos na lista\n**\n")

cores.append('vermelho')
print(cores)

comidas = []
print(comidas)
comidas = ['bolacha', 'temaki', 'pizza']
print(comidas)

comidas.insert(1, 'hamburguer')
print(comidas)

#
# Removendo elementos de uma lista
#
print("\n**\n** Removendo elementos da lista\n**\n")

del comidas[0]              # deleta o item da posição
print(comidas)

preferida = comidas.pop()   # pop() no último elemento
print(comidas)
print(preferida)

preferida = comidas.pop(1)  # pop() no elemento da posição passada
print(comidas)
print(preferida)

print(cores)
cores.remove('amarelo')     # remove o item pelo nome
print(cores)

cor_preferida = 'verde'
cores.remove(cor_preferida)
print(cores)

#
# Organizando os itens da lista
#
print("\n**\n** Organizando a lista\n**\n")

lista = ['bruno', 'gabriela', 'pedro', 'gustavo', 'marcela', 'carlos']

print(lista)
lista.sort()                # Ordena a lista por ordem alfabética permanentemente (é case senstive)
print(lista)
lista.sort(reverse=True)    # Ordena a lista em ordem alfabeticamente inversa
print(lista)

lista = ['bruno', 'gabriela', 'pedro', 'gustavo', 'marcela', 'carlos']

print("A lista original: ")
print(lista)
print("A lista imprimida em ordem: ")
print(sorted(lista))                    # Ordena alfabeticamente apenas a exibição da lista
print("A lista imprimida em ordem: ")   
print(sorted(lista, reverse=True))      # Ordena alfabeticamente e inversamente apenas a exibição da lista
print("Mas ainda está como a original: ")
print(lista)

print("A lista invertida:")
lista.reverse()             # Inverte a ordem da lista original
print(lista)

#
# Encontrando o tamanho da lista
#
print("O tamanho da lista é: ")
print(len(lista))