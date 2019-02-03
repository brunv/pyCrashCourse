from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

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


@login_required
def topics(request):
    """Mostra todos os assuntos."""

    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}

    return render(request, 'learning_logs/topics.html', context)


#       Inicialmente importamos o modelo associado aos dados de que precisamos.
#       A função 'topics()' exige um parâmetro: o objeto 'request' que Django
#       recebeu do servidor. Em seguida, consultamos o banco de dados pedindo os
#       objetos 'Topic', ordenados de acordo com o atributo 'date_added' e 
#       pertecentes ao usuário que requisitou os tópicos..
#
#       Na sequência definimos um contexto que será enviado ao template. Um
#       contexto é um dicionário em que as chaves são os nomes que usaremos no
#       template para acessar os dados e os valores são os dados que devemos
#       enviar ao template.
#
#       Ao construir uma página que use dados, passamos a variável 'context' para
#       'render()', além do objeto 'request' e o path do template.


@login_required
def topic(request, topic_id):
    """Mostra um único assunto e todas as suas entradas."""

    topic = Topic.objects.get(id=topic_id)

    # Garante que o assunto pertence ao usuário atual
    if topic.owner != request.user:
        raise Http404

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


@login_required
def new_topic(request):
    """Adiciona um novo assunto."""

    if request.method != 'POST':
        # Nenhuma dado submetido; cria um formulário em branco
        form = TopicForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
            
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


#       A função 'new_topic()' deve tratar duas situações diferentes: requisições
#       iniciais para a página 'new_topic' e o processamento de qualquer dado
#       submetido no formulário.
#
#       Importamos a classe HttpResponseRedirect, que usamos para redirecionar o
#       leitor de volta à pagina 'topics', depois que tiver submetido seu assunto.
#       A função 'reverse()' determina o URL a partir de um padrão de URL nomeado,
#       o que quer dizer que Django gerará o URL quando a página for solicitada.
#
#       A função acima aceita o objeto de requisição como parâmetro. Quando o
#       usuário inicialmente solicita essa página, o navegador envia uma requisição
#       GET. Depois que o usuário tiver preenchido e submetido o formulário, o
#       navegador enviará uma requisição POST.
#
#       Portanto, se o método de requisição não for POST, precisamos devolver um
#       formulário em branco (se for outro tipo de requisição, continua sendo
#       seguro devolver um formulário em branco). Se for POST, criamos uma
#       instância de 'TopicForm' e passamos os dados fornecidos pelo usuário,
#       armazenados em 'request.POST'. O objeto 'form' devolvido contém as
#       informações submetidas pelo usuário.
#
#       A função 'is_valid()' verifica se todos os campos necessários foram
#       preenchidos (todos os campos em um formulário são obrigatórios por padrão)
#       e se os dados fornecidos são do tipo esperado para o campo.
#       Se tiver estiver válido, adicionamos o usuário atual por meio de
#       'request.user' ao campo 'ownwer' do novo objeto a ser salvo. Por fim 
#       chamamos 'save()', que grava os dados no banco de dados.


@login_required
def new_entry(request, topic_id):
    """Acrescenta uma nova entrada para um assunto em particular."""

    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
        
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco
        form = EntryForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                            args=[topic_id]))
    
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


#       Quando chamamos 'save()', incluímos o argumento 'commit=False' para dizer a
#       Django que crie um novo objeto de entrada e o armazene em 'new_entry' sem
#       salvá-lo no banco de dados por enquanto. Definimos o atributo 'topic' de
#       'new_entry' com o assunto extraído do anco de dados no início da função;
#       então chamamos 'save()'.
#
#       A chamada a 'reverse()' exige dois argumentos: o nome do padrão de URL para
#       o qual queremos gerar um UL e uma lista 'args' contendo qualquer argumento
#       que deva ser incluído no URL. A lista 'args' contém um item: 'topic_id'. A
#       chamada a 'HttpResponseRedirect()' então redireciona o usuário para a
#       página do assunto para o qual uma entrada foi criada.


@login_required
def edit_entry(request, entry_id):
    """Edita uma entrada existente."""

    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Requisição inicial; preenche previamente o formulário com a entrada atual
        form = EntryForm(instance=entry)
    else:
        # Dados de POST submetidos; processa os dados
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic.id]))
    
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


#       Ao processador uma requisição POST, passamos os argumentos 'instance=entry'
#       e 'data=request.POST' para dizer a Django que crie uma instância de
#       formulário com qualquer dado relevante de 'request.POST'.
#       Em seguida redirecionamos o usuário para a página 'topic', na qual ele
#       deverá ver a versão atualizada da entrada editada.