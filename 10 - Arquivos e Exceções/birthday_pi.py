#
#       Seu aniversário está contido em Pi?
#

filename = 'files/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Digite seu aniversaio no formato ddmmaa: ")
if birthday in pi_string:
    print("Seu aniversario esta em pi!")
else:
    print("Seu aniversario nao esta e pi!")