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