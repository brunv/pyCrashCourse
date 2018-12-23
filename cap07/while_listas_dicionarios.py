#
#       Utilizando while em listas e dicionários
#


#   Tranferindo de uma lista para outra com while

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


#   Removendo instaâncias de valores específicos para de uma lista

pets = ['dog', 'cat', 'goldfish', 'rabbit', 'cat', 'turtle', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


#    Preenchendo um dicionário com dados de entrada do usuário

responses = {}

active = True

while active:
    name = input("\nWhat is your name? ")
    response = input("What is yout favorite food? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (y/n) ")
    if repeat == 'n':
        active = False

print("\n--- Results ---")
for name, response in responses.items():
    print(response + " is the favorite food of " + name + "!")