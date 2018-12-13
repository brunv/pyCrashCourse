#
# Criando listas de números
#

numeros = list(range(1,5))
print(numeros)

# Algumas funções em Python são específicas para listas de números.
# Nesse exemplo, podemos encontrar facilmentes os valores mínimo,
# máximo e a soma da lista de números.

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

minimo = min(digits)
maximo = max(digits)
soma = sum(digits)

print("O valor minimo: " + str(minimo))
print("O valor maximo: " + str(maximo))
print("A soma: " + str(soma))