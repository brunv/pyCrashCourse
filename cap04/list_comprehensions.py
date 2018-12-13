#
# Gerando uma lista de números quadrados de 1 a 10.
#

quadrados = []
for value in range(1,11):
    quadrado = value**2
    quadrados.append(quadrado)

print(quadrados)

#
# Agora, o mesmo exercício usando List Comprehensions
#

quadrados = [value**2 for value in range(1,11)]

print(quadrados)