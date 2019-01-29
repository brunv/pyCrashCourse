from django.db import models

# Create your models here.
class Topic(models.Model):
    """Um assunto sobre o qual o usuário está aprendendo."""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representação em string do modelo."""

        return self.text


#       Criamos uma classe chamada Topic que herda Model. Essa classe tem apenas
#       dois atributos: 'text' e 'date_added'.
#       O atributo 'text' é um 'CharField' - um dado composto de caracteres, isto
#       é, um texto. Usamos 'CharField' quando queremos armazenar uma pequena
#       quantidade de texto, por exemplo, um nome, um título ou uma cidade. Quando
#       definimos um atributo 'CharFiel', devemos dizer a Django quanto espaço deve
#       ser reservado ao banco de dados.
#       O atributo 'date_added' é um 'DateTimeField' - um dado que registrará uma
#       e uma hora. Passamos o argumento 'auto_now_add=True', que diz a Django para
#       definir esse atributo automaticamente com a data e hora atuais sempre que o
#       usuário criar um novo assunto.
#
#       Devemos dizer a Django qual atributo deve ser usado como default quando ele
#       exibir informções sobre um assunto. O Django chama um método __str__() para
#       exibir uma representação simples de um método.


class Entry(models.Model):
    """Algo específico aprendido sobre um assunto."""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Devolve uma representação em string do modelo."""

        return self.text[:50] + "..."


#       O primeiro atributo 'topic', é uma instância de 'ForeignKey'. Uma chave
#       estrangeira é um termo usado em banco de dados: é um referência a outro
#       registro do banco de dados. Esse é o código que associa cada entrada a um
#       assunto específico. Cada assunto recebe um chave, isto é, um ID, quando é
#       criado. Quando Django precisa estabelecer uma conexão entre dois dados, ele
#       usa a chave associada a cada informação. O segundo parâmetro 'on_delete' diz
#       a Django que, quando um tópico for deletado, todas as entradas associadas à
#       ele também devem ser deletadas. Isso é conhecido como deleção em cascata.
#
#       Em seguida, temos um atributo chamado 'text', que é uma instância de
#       'TextField'. Esse tipo de campo não precisa de um limite para o tamanho.
#       O atributo 'date_added' nos permite aprensentar as entradas na ordem em que
#       foram criadas e inserir um timestamp junto a cada entrada.
#
#       A classe aninhada 'Meta' armazena informações extras para administrar um
#       modelo. Nesse caso, sem esse atriuto em especial, Django iria referenciar
#       várias entradas como Entrys.