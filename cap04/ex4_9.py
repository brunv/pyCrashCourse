cubos = []
for value in range(1,101):
    cubo = value**3
    cubos.append(cubo)

print(cubos)

# list comprehension

cubos = [value**3 for value in range(1,101)]

print(cubos)