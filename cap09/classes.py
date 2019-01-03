#       Na programação orientada a objetos, escrevemos classes do mundo real
#       e criamos objetos com base nessa classes. Quando escrevemos uma classe,
#       definimos o comportamento geral que toda uma categoria de objetos pode
#       ter.
#       Criar um objeto a partir de um classe é um operação conhecida como
#       instanciação, e trabalhamos com instâncias de uma classe.

class Dog():
    """Uma tentativa simples de modelar um cachorro."""

    def __init__(self, name, age):
        """Inicializa os atributos name e age."""
        self.name = name
        self.age = age

    def sit(self):
        """Simula um cachorro sentando em resposta a um comando."""
        print(self.name.title() + " is sitting.")

    def roll_over(self):
        """Simula um cachorro rolando em resposta a um comando."""
        print(self.name.title() + " rolled over!")


#       Por convenção, nomes com a primeira letra maiúscula referem-se a
#       classes em Python. Os parênteses na definição da classe estão vazios
#       porque estamos criando essa classe do zero.

#       Uma função que faz parte de uma classe é um método. Tudo o que 
#       aprendemos sobre funções também se aplica aos métodos; a única
#       diferença, por enquanto, é o modo como chamaremos os métodos.

#       O método '__init__()':
#       É um método especial que Python executa automaticamente sempre que
#       criamos uma nova instância baseada na classe. Esse método tem dois
#       underscores no ínicio e dois no final - uma convenção que ajuda a
#       evitar que os nomes default de métodos em Python entrem em conflito
#       com nomes de métodos criados pelo programador.

#       O parâmetro 'self':
#       É obrigatório na defiinição do método 'init' e deve estar antes dos
#       demais parâmetros. Toda chamada de método associada a uma classe passa
#       self, que é uma referência à própria instância, de modo automático; ele
#       dá acesso aos atributos e métodos da classe à instância individual. Na
#       passagem de argumentos, self é passado automaticamente, portanto não é
#       preciso especificá-lo.
#       Os métodos 'sit' e 'roll_over' possuem o parâmetro 'self', assim, as
#       instâncias que criarmos posteriormente terão acesso a esses métodos.

#       Atributos:
#       As duas variáveis definidas no método 'init' têm o prefixo 'self'.
#       Qualquer variável assim prefixada está disponível a todos os métodos da
#       classe. Além disso, podemos acessar essas variáveis por meio de qualquer
#       instância criada a partir da classe. Variáveis como essas, acessíveis
#       por meio instâncias, são chamadas de atributos. 