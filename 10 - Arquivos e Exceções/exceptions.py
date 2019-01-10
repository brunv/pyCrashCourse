#
#       Exceções
#

#       Python usa objetos especiais chamados exceções para administrar erros que
#       surgirem durante a execução de um programa. Sempre que ocorrer um erro que
#       faça Python não ter certeza do que deve fazer em seguida, um objeto
#       exceção será criado. Se você escrever um código que trate a exceção, o
#       programa continuará executando. Se a exceção não for tratada, o programa
#       será interrompido e um traceback, que inclui uma informação sobre a exceção
#       levatanda, será criado.
#
#       Exceções são tratadas com blocos 'try-except'. Um bloco try-except pede que
#       Python faça algo, mas também lhe diz o que deve ser feito se uma exceção
#       for levantada. Em vez de tracebacks, que pode ser confusos para os usuários
#       lerem, os usuários verão mensagem de erros escritas por você.


#
#       Tratando a exceção ZeroDivionError:
#

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")


#
#       Usando exceções para evitar falhas:
#

#       O fato de o programa falhar é ruim, mas também não é uma boa ideia deixar
#       que os usuários vejam os tracebacks. Em um ambiente malicioso, invasores
#       aprenderão mais do que você quer que eles saibam a partir de um traceback.
#
#       Às vezes, você terá um código adicional que deverá ser executado somente
#       se o bloco try tiver sucesso; esse código deve estar dentro do bloco else.

print("Give me two number, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)


#
#       Tratando a exceção FileNotFoundError:
#

filename = "this_file_dont_exist.txt"

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)


#
#       Trabalhando com vários arquivos
#

def count_words(filename):
    """Conta o número aproximado de palavras em um arquivo."""

    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
        # pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = [
    'files/alice.txt',
    'files/this_file_dont_exist.txt',
    'files/siddhartha.txt',
    'files/moby_dick.txt',
    'files/little_women.txt'
    ]

for filename in filenames:
    count_words(filename)


#
#       Falhando silenciosamente:
#

#       Nem sempre precisamos informar todas as exceções capturadas. Para fazer
#       um programa falahar em silêncio, excreva um bloco try como seria feito
#       normalmente, mas diga de forma explícita a Python para não fazer nada no
#       bloco except. Python tem um instrução 'pass' que lhe diz para não fazer
#       nada em um bloco.