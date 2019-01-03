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


#       ESTILIZANDO FUNÇÕES:
#
#       1) As funções devem ter nomes descritivos, e esse nomes dem usar letras
#       minúsculas e underscores.
#
#       2) Toda função deve ter um comentário que explique o que ela faz de modo
#       conciso. Esse comentário deve estar imediatamente após a definição da
#       função e deve utilizar o formato de docstring.
#
#       3) Se você especificar um valor default para um parâmetro, não deve
#       haver espaço em nenhum dos lados do sinal de igualdade:
#           def nome_função(parâmetro_0, parâmetro_1='default')
#       A mesma convenção deve ser usada para argumentos nomeados em chamadas
#       de função:
#           nome_função(valor_0, parâmetro_1='valor')
#
#       4) A PEP 8 recomenda limitar as linhas de código em 79 caracteres para
#       que todas as linhas permaneçam visíveis em uma janela de editor com
#       um tamanho razoável.
#       Se uma funçãooooo ultrapassar os 79 caracteres, utilize a seguinte
#       identação:
#           def nome_da_função(
#                   parâmetro_0, parâmetro_1, parâmetro_2,
#                   parâmetro_3, parâmetro_4, parâmetro_5):
#               corpo da função...
#
#       5) Se seu módulo tiver mais de uma função, você poderá separá-las
#       usando duas linhas em branco para facilitar ver em que lugar uma
#       função termina e a próxima começa.