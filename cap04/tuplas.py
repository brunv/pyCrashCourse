#
# Diferente das listas, as tuplas contém dados imutáveis.
#

dimensions = (200,50)

print(dimensions[0])    # 200
print(dimensions[1])    # 50

# dimensions[0] = 150   Throws an error

#
# Sobrescrevendo uma tupla
#

print("Original dimensions: ")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("Modified dimensions: ")
for dimension in dimensions:
    print(dimension)