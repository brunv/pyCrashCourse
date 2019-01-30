from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """A página inicial de Learning Log."""

    return render(request, 'learning_logs/index.html')


#       Quando uma requisição de URL corresponder ao padrão que definimos em
#       'urls.py' de leraning_logs, o Django procurará uma função chamada 'index()'
#       neste arquivo 'views.py'.
#
#       A função 'render()' utiliza dois argumentos - o objeto 'request' original e
#       um template que pode ser usado para construir a página.


def topics(request):
    """Mostra todos os assuntos."""

    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}

    return render(request, 'learning_logs/topics.html', context)


#       Inicialmente importamos o modelo associado aos dados de que precisamos.
#       A função 'topics()' exige um parâmetro: o objeto 'request' que Django
#       recebeu do servidor. Em seguida, consultamos o banco de dados pedindo os
#       objetos 'Topic', ordenados de acordo com o atributo 'date_added'.
#
#       Na sequência definimos um contexto que será enviado ao template. Um
#       contexto é um dicionário em que as chaves são os nomes que usaremos no
#       template para acessar os dados e os valores são os dados que devemos
#       enviar ao template.
#
#       Ao construir uma página que use dados, passamos a variável 'context' para
#       'render()', além do objeto 'request' e o path do template.


def topic(request, topic_id):
    """Mostra um único assunto e todas as suas entradas."""

    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}

    return render(request, 'learning_logs/topic.html', context)


#       Essa é a primeira função de view que exige um parâmetro que não seja o
#       objeto 'request'. A função aceita o valor capturado por '<int:topic_id>' e
#       o armazena em topic_id. Em seguida, usamos 'get()' para obter o assunto,
#       assim como fizemos no shell de Django. Logo, recuperamos as entradas
#       associadas a esse assunto e as ordenamos de acordo com 'date_added': o
#       sinal de menos na frente ordena os resultados em ordem invesa, o que fará
#       as entradas mais recentes serem exibidas antes. Por último, armazenamos o
#       assunto e as entradas no dicionário de contexto e enviamos 'context' para
#       o template 'topic.html'.
#
#       Os códigos em 45 e 46 são chamados de 'queries', pois fazem queries no
#       banco de dados em busca de informações específicas. Ao executar queries
#       como essas em seus próprios projetos, será bem conveniente testá-las
#       antes no shell de Django.