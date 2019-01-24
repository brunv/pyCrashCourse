#
#       Mapeando conjunto de dados globais usando formato JSON
#

import json

#   Carrega dados em uma lista
filename = 'data/population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

#   Exibe a população de cada país em 2010
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        #print(country_name + ": " + str(population))



#       A função 'json.load()' converte os dados em um formato com que Python possa
#       trabalhar: nesse caso, em uma lista. Em seguida, percorremos cada item de
#       'pop_data' com um laço. Cada item é um dicionário com quatro pares
#       chave-valor, e o armazenamos em 'pop_dict'.
#
#       A função 'float()' transforma a string em um decimal, e a função 'int()'
#       remove a parte decimal do número e devolve um inteiro.
#
#       A ferramenta de mapeamento do Pygal espera dados em um formato particular:
#       os países devem ser fornecido na forma de códigos e as populações como
#       valores. Os códigos incluídos em 'population_data.json' são códigos de
#       três letras, mas o Pygal utiliza códigos de duas letras.