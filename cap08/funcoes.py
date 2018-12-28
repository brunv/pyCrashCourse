#       Para definirmos uma função em Python começamos utilizando a palavra reservada
#       def, seguida do nome da função e dos parâmetros entre parênteses e terminada
#       em dois pontos.


def greetings():
    """Exibe uma mensagem de saudação."""
    print("Hello! Welcome!")

greetings()


#       Na linha 7, esse tipo de comentário é chamado docstring e descreve o que a
#       função faz. Python procura as docstrings quando gera a documentação das
#       funções do programa.


#
#       Passando informações para uma função:
#

def greet_user(username):
    """Exibe uma mensagem de saudação para um determinado usuário."""
    print("Welcome, " + username.title() + "!")

greet_user('johndoe')