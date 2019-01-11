#
#       Armazenando dados
#

#       Quando os usuários fecham um programa, quase sempre você vai querer salvar
#       as informações que eles forneceram. Uma maneira simples de fazer isso
#       envolve armazenar seus dados usando o módulo 'json'.
#
#       O módulo 'json' permite descarregar estruturas de dados Python simples em
#       um arquivo e carregar os dados desse arquivo na próxima vez que o programa
#       executar. O formato de dados JSON não é específico de Python, portanto
#       podemos compartilhar dados armzenados em formato JSON com várias outras
#       linguagens de programação.

#
#       Usando json.dump() e json.load():
#

#       A função json.dump() aceita dois argumentos: um dado para armazenar e um
#       objeto arquivo que pode ser usado para armazenar os dados.

import json

numbers = [2, 3, 4, 5, 8, 9, 0]

filename = 'files/numbers.json'
with open(filename) as file_object:
    json.dump(numbers, file_object)

#       A função json.load() é utilizada para carregar as informações armazenadas
#       em um objeto arquivo.

with open(filename) as file_object:
    numbers = json.load(file_object)


#
#       Salvando e lendo dados gerados pelo usuário (refatorado):
#

import json

def get_stored_username():
    """Obtém o nome do usuário já armazenado se estiver disponível."""

    filename = 'files/username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Pede um novo nome de usuário."""

    username = input("what is you name? ")
    filename = 'files/username.json'
    with open(filename) as file_object:
        json.dump(username, file_object)

    return username

def greet_user():
    """Saúda o usuário pelo nome."""
    
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()

#       Há uma boa prática na linha 51: uma função deve devolver o valor esperado
#       ou None. Isso nos permite fazer um teste simples com o valor de retorno
#       da função.