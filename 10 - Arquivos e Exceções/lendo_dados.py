#       Lendo dados de um arquivo:
#       Quando quiser trabalhar com as informações de um arquivo-texto, o primeiro
#       passo será ler o arquivo em memória. Você pode ler todo o conteúdo de um
#       arquivo ou pode trabalhar com uma linha de cada vez.

#
#       Lendo um arquivo inteiro:
#

with open('files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

#       A função 'open()' precisa de um argumento: o nome do arquivo que você quer
#       abrir. Ela devolve um objeto que representa o arquivo: 'file_object'.
#
#       A palavra reservada 'with' fecha o arquivo depois que não for mais
#       necessário acessá-lo. Você poderia abrir e fechar o arquivo chamando open()
#       e close(), mas se um bug em seu programa impedir que a instrução close()
#       seja executada, o arquivo não será fechado.
#
#       Depois que tivermos um objeto arquivo que represente pi_digits.txt, usamos
#       o método 'read()' para ler todo o conteúdo do arquivo e armazená-lo em uma
#       longa string em 'contents'.
#
#       'rstrip()' é utilizado para remover a linha em braco extra, que a função
#       'read()' devolve como uma string vazio ao encontrar o final do arquivo.


#
#       Paths de arquivo:
#

#       Path relativo:
#       with open('files/pi_digits.txt') as file_object:
#
#       Path absoluto:
#       file_path = 'C:/Users/bruno/Documents/GitHub/pyCrashCourse/10 - Arquivos 
#       e Exceções/files';
#       with open(file_path) as file_object:


#       
#       Lendo dados linha a linha:
#

#       Quando estiver lendo um arquivo, com frequência você vai querer analisar
#       cada linha do arquivo. Assim podemos usar um laço for no objeto do arquivo
#       para analisar cada uma de suas linhas, uma de cada vez:

file_name = 'files/pi_digits.txt'

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())


#
#       Criando uma lista de linhas de um arquivo:
#

#       Quando usamo 'with', o objeto arquivo devolvido por 'open()' estará
#       disponível somente no bloco 'with' que o contém. O exemplo a seguir
#       armazena as linhas de 'pi_digits.txt' em uma lista no bloco 'with'
#       e, em seguida, exibe as linhas fora dese bloco:

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

#       O método 'readlines()' utilizado armazena cada linha do arquivo em
#       uma lista.


#
#       Trabalhando com o conteúdo de um arquivo:
#

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

#       Quando Python lê um arquivo-texto, o texto do arquivo é interpretado como
#       uma string. Se você ler um número e quiser trabalhar com esse valor em um
#       contexto numérico, será necessário convertê-lo em um inteiro usando a
#       função 'int()' ou convertê-lo em um número de ponto flutuante com a função
#       'float()'.


#
#       Arquivos grandes: um milhão de dígitos
#

filename = 'files/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))

#       Python não tem nenhum limite inerente para quantidade de dados com que
#       podemos trabalhar.