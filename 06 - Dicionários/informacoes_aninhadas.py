#       Podemos aninhar um conjunto de dicionários em uma lista, uma lista de
#       itens em um dicionário, ou até mesmo um conjunto de dicionários dentro
#       de outro dicionário. Isso é conhecido como Informações Aninhadas.


alien_0 = {
    'cor': 'verde',
    'pontos': 5
}
alien_1 = {
    'cor': 'azul',
    'pontos': 10
}
alien_2 = {
    'cor': 'vermelho',
    'pontos': 15
}


#
#       Uma lista de dicionários
#


aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


#
#       Uma lista em um dicionário
#


pizza = {
    'borda': 'recheada',
    'ingredientes': ['tomate', 'calabresa', 'mussarela', 'cebola']
}

print("Voce pediu uma pizza com borda " + pizza['borda'] + " com os seguintes ingredientes: ")
for ingrediente in pizza['ingredientes']:
    print("\t" + ingrediente)

print(pizza)

linguagem_favorita = {
    'jen': ['python', 'ruby'],
    'sarah': ['go', 'haskell'],
    'edward': ['c'],
    'phil': ['java', 'python']
}

for nome, linguagens in linguagem_favorita.items():
    print("\nAs linguagens favoritas do(a) " + nome.title() + " sao:")
    # o segundo laço itera dentro das listas de linguagens:
    for linguagem in linguagens:
        print("\t" + linguagem.title())


#
#       Um dicionário em um dicionário
#


usuarios = {
    'aeinstein': {
        'nome': 'albert',
        'sobrenome': 'einstein',
        'localizacao': 'princeton'
    },
    'mcurie': {
        'nome': 'marie',
        'sobrenome': 'curie',
        'localizacao': 'paris'
    }
}

for usuario, usuario_info in usuarios.items():
    print("\nUsuario: " + usuario)
    nome_completo = usuario_info['nome'].title() + " " + usuario_info['sobrenome'].title()
    localizacao = usuario_info['localizacao'].title()
    print("\tNome completo: " + nome_completo)
    print("\tLocalizacao: " + localizacao)