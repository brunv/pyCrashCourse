#       Para estar de acordo com a filosofia de Python, quanto menos entulhados
#       estiverem seus arquivos, melhor será. Para ajudar, Python permite
#       armazenar classes em módulos e então importar classes em seu programa
#       principal.

#       É uma boa prática incluir um docstring no nível de módulo que descreve
#       rapidamente o conteúdo desse módulo. Portanto, escreva uma docstring
#       para cada módulo que criar.

#
#       Importando uma única classe:
#

from car import Car

my_new_car = Car('audi', 'r8', 2017)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 230
my_new_car.read_odometer()


#       Podemos armazenar tantas classes quantas forem necessárias em um único
#       módulo, embora cada classe deva estar, de algum modo, relacionada com
#       outra classe. Exemplo: automobile.py

from automobile import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2018)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


#
#       Importando várias classes de um mesmo módulo:
#

from automobile import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2015)
print(my_beetle.get_descriptive_name())

my_old_tesla = ElectricCar('tesla', 'roadster', 2015)
print(my_old_tesla.get_descriptive_name())


#
#       Importando um módulo completo:
#

import automobile

my_porsche = automobile.Car('porsche', '911', 2001)
print(my_porsche.get_descriptive_name())

my_bmw = automobile.ElectricCar('bmw', 'i3', 2019)
print(my_bmw.get_descriptive_name())


#       Importando todas as classes de um módulo: 'from nome_módulo import * '
#       Essa abordagem não é recomendada por dois motivos: não fica claro quais
#       as classes do módulo que estão sendo usadas; pode resultar em confusão
#       com nomes presentes no arquivo.

#       Se precisar importar muitras classes de um módulo, é melhor importar o
#       módulo todo e usar a sintaxe nome_do_módulo.nome_da_classe. Você não
#       verá todas as classes usadas no início do arquivo, mas verá claramente
#       em que lugares o módulo é utilizado no programa.