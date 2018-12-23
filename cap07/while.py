#
#       Laço while, exemplos com entradas de usuário
#


prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)


#
#       Usando break para sair de um laço
#


prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\nEnter 'quit' when you are finished."

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I\'d love to go to " + city.title() + "!")