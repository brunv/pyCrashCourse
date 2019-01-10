#
#       Passando uma lista para uma função:
#

def greet_users(names):
    """Exibe uma saudação para cada usuário da lista."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'tyler', 'margot']
greet_users(usernames)


#
#       Modificando uma lista em uma função:
#

def doubled_list(numbers, doubled):
    """Dobra todos os números de uma lista"""
    while numbers:
        aux = numbers.pop() ** 2
        doubled.append(aux)

    doubled.reverse()

numbers = [1, 2, 3, 4, 5, 6]
doubled = []
doubled_list(numbers, doubled)
print(numbers)
print(doubled)      


#
#       Impedindo que uma função modifique um lista:
#

num = [1, 2, 3]
dob = []
doubled_list(num[:], dob)   # basta enviar uma cópia da lista
print(num)
print(dob)   


#       Passando um número arbitrário de argumentos: às vezes não é possível saber 
#       com antecedência quantos argumentos serão passados. Para isso, Python utiliza
#       um parâmetro precedido de um * para criar uma tupla vazia que reunirá todos
#       os valores recebidos.

def make_pizza(*toppings):
    """Apresenta a pizza que estamos prestes a preparar."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


#       Misturando argumentos posicionais e arbitrários: para isso, basta colocar o
#       parâmetro que aceita vários argumentos por último na definição da função. Pois
#       Python faz a correspondência de argumentos posicionais e nomeados antes, e depois
#       agrupa qualquer argumento remanescente no último parâmetro.

def make_sandwich(size, *toppings):
    """Apresenta o sanduíche que estamos prestes a preparar."""
    print("\nMaking a " + str(size) + "-inch sandwich with the folling toppings:")
    for topping in toppings:
        print("- " + topping)

make_sandwich(10, 'sausage')
make_sandwich(16, 'sausage', 'barbecue', 'extra cheese')


#       Usando argumentos nomeados e arbitrários: às vezes, você vai querer aceitar um
#       número arbitrário de argumentos, mas não saberá com antecedência qual tipo de
#       informação será passado para a função. Para isso, Python utiliza um parâmetro
#       precedido de ** para criar um dicionário vazio que receberá quaisquer pares
#       nome-valor recebidos.

def build_profile(first, last, **user_info):
    """Constrói um dicionário contendo tudo que sabemos sobre um usuário."""

    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()

    for key, value in user_info.items():
        profile[key] = value
    
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

print("\n\n")
print(user_profile)