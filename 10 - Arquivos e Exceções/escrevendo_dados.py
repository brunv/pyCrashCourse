#
#       Escrevendo dadas em um arquivo vazio:
#

#       Para escrever um texto em um arquivo, chame 'open()' com um segundo
#       argumento que diga a Python que você quer escrever dados no arquivo.

filename = 'files/programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming")

#       Podemos abrir um arquivo em modo de leitura ('r'), em modo de escrita
#       ('w'), em modo de concatenação ('a') ou em um modo que permita ler e
#       escrever no arquivo ('r+'). Se o argumento for omitido, por padrão Python
#       abrirá o arquivo em modo somente de leitura.
#
#       A função 'open()' cria automaticamente o arquivo no qual você vai escrever
#       caso ele não escista. No entanto, tome cuidado ao abrir um arquivo em modo
#       de escrita ('w') porque se o arquivo já existir, Python o apagará antes de
#       devolver o objeto arquivo.
#
#       Usamos o método 'write()' no objeto arquivo apara escrever uma string nesse
#       arquivo. Python escreve apenas strings em um arquivo-texto. Se quiser
#       armazenar dados numéricos, será necessário converter os dados em um formato
#       de string antes usando a função 'str()'.


#
#       Escrevendo várias linhas:
#

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love learning a new language.\n")


#
#       Concatenando dados em um arquivo:

#       Se quiser acrescentar conteúdos em um arquivo em vez de sobrescrever o
#       conteúdo existente, você pode abrir o arquivo em modo de concatenação.
#       Assim, qualquer linha que você escreverv no arquivo será adicionada no
#       final. Se o arquivo ainda não existe, Python criará um arquivo vazio.

with open(filename, 'a') as file_object:
    file_object.write('I also love finding meanings in large datasets.\n')
    file_object.write('I love creating apps that can run in a browser.\n')