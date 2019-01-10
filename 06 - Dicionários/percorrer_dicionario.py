#   Python permite percorrer um dicionário com um laço. Dicionários podem
#   ser usados para armazenar informações de várias maneiras. Assim, há
#   diversosmodos diferentes de percorrê-los com um laço.


user = {
    'username': 'brunv',
    'first': 'bruno',
    'last': 'vieira'
}

linguagem_favorita = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}


#
#   Percorrendo todos os pares chave-valor com um laço
#


for key, value in user.items():
    print("\nKey: " + key)
    print("Value: " + value)

for nome, linguagem in linguagem_favorita.items():
    print("A linguagem favorita do(a) " + nome.title() + " eh " + linguagem.title())


#
#   Percorrendo todas as chaves de um dicionário com um laço
#


for nome in linguagem_favorita.keys():
    print(nome.title())

# mesmo resultado de
for nome in linguagem_favorita:
    print(nome.title())

# keys() também pode ser usado como:
if 'john' not in linguagem_favorita.keys():
    print("John, qual a sua linguagem favorita?")

# Ou seja, keys() devolve uma lista de chaves


#
#   Percorrendo as chave de um dicionário em ordem usando um laço
#


for nome in sorted(linguagem_favorita.keys()):
    print(nome.title() + ", obrigado por participar!")


#
#   Percorrendo todos os valores de um dicionário com um laço
#


print("\nAs seguintes linguagens foram mencionadas:\n")
for linguagens in linguagem_favorita.values():
    print(linguagens)

# Essa abordagem extrai todos os valores sem verificar repetições
# Para evitar repetições, podemos trocar listas por conjuntos (set)

print("\nAs seguintes linguagens foram mencionadas:\n")
for linguagens in set(linguagem_favorita.values()):
    print(linguagens)