#
# testando condições lógicas
#

age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 15         # true
age_0 >= 21 or age_1 >= 21          # true

#
# verificando nulidade da lista
#

requested_toppings = []

if requested_toppings:
    print("Há algo na lista")       # true
else:
    print("Lista vazia!")           # false

#
# verificando existência na lista
#

requested_toppings = ['mushrooms', 'onions', 'pineapple']

'mushroom' in requested_toppings    # true
'pepperoni' in requested_toppings   # false

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", você pode postar o que desejar.")

#
# expressões booleanas
#

game_active = True
can_edit = False

#
# if-else normal com igualdade
#

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#
# if normal com diferença
#

requested_topping = 'mushrooms'

if requested_topping != 'achovies':
    print("Hold the anchovies!!")

#
# sintexa if-elif-else
#

age = 12

if age <= 4:
    price = 0
    print("Your admission cost is " + str(price))
elif age < 18:
    price = 5
    print("Your admission cost is " + str(price))
else:
    price = 10
    print("Your admission cost is " + str(price))
    # python não exige um bloco else (que captura tudo) ao final de um if-elif-else