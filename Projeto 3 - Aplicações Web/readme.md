# Aplicações Web - Projeto 3

Essa seção destina-se ao desenvolvimento do terceiro projeto do livro Curso Intensivo de Python (Python Crash Course) por Eric Matthes.

> Atenção, isto não é a descrição do projeto! É o resumo do livro feito durante os estudos!

## Introdução ao Django
O Django é um framework web - um conjunto de ferramentas projetado para ajudar você a criar sites interativos. Esse framework é capaz de responder a requisições de páginas e facilitar let e escrever em um banco de dados, administrar usuários e outras tarefas.

### Criando um ambiente virtual
Um *ambiente virtual* é um local de seu sistemas em que você pode instalar pacotes e isolá-los de todos os demais pacotes Python. Separar as bibliotecas de um projeto das bibliotecas de outros projetos é vantajoso e será necessário quando implantarmos o projeto em um servidor.

Se você usa Python 3, deverá ser capaz de criar um ambiente virtual com o seguinte comando:
```
$ python -m venv ll_env
```

Nesse caso, estamos executando o módulo *venv* e usando-o para criar o ambiente virtual chamado *ll_env*.

#### Instalando o virtualdev

```
# pip install --user virtualenv
```

#### Ativando o ambiente virtual
Para ativá-lo, use o seguinte comando:
```
$ source ll_env/bin/activate
or (Windows)
$ ll_env/Scripts/activate
```

Esse comando executa o script *activate* em *ll_env/bin*. Quando o ambiente estiver ativo, você verá o nome dele entre parênteses; então você poderá instalar pacotes no ambiente e usar pacotes que já tenham sido instalados. os pacotes que você instalar em *ll_env* estão disponíveis somente enquanto o ambiente estiver ativo.

Para interromper o ambiente, digite:
```
$ deactivate
```

O ambiente também se tornará inativo se você fechar o terminal em que ele estiver executando.

### Instalando o Django

Depois de ter criado e ativado o seu ambiente virtual, instale o Django:
```
$ pip install django
```

Como estamos trabalhando em um ambiente virtual, esse comando é o mesmo em todos os sistemas.
Tenha em mente que o Django estará disponível somente quando o ambiente estiver ativo.

### Criando um projeto em Django
Sem sair do ambiente vritual ativo, execute os comando a seguir para criar um novo projeto:
```
$ django-admin startproject learning_log .
```

O comando acima diz a Django para criar um novo projeto chamado *learning_log*. O ponto final do comando cria o novo projeto com uma estrutura de diretórios que facilitará a implantação da aplicação em um servidor quando terminarmos seu desenvolvimento.

Feito isso, Django criará um novo diretório chamado *learning_log*. Um arquivo chamado *manage.py* também será criado: é um pequeno programa que aceita comandos e os passa para a parte relevante de Django que os executa. Usaremos esses comando para administrar tarefas como trabalhar com bancos de dados e executar servidores.

O diretório *learning_log* contém quatro arquivos, entre os quais os mais importantes são *settings.py*, *urls.py* e *wsgi.py*. O primeiro controla como Django interage com o seu sistema e administra o seu projeto. O arquivo *urls.py* informa a Django quais páginas devem ser criadas em resposta a requisições do navegador. E por último, o arquivo *wsgi.py* ajuda Django a servir os arquivos que ele criar. O nome do arquivo é um acrônimo para *web server gateway interface*.

### Criando o banco de dados
Para criar o banco de dados do projeto Learning Log, digite o comando a seguir:
```
$ python manage.py migrate
```

Sempre que modificarmos um banco de dados, dizemos que estamos *migrando* o banco de dados. Executar o comando **migrate** pela primeira vez informa a Django para garantir que o banco de dados esteja de acordo com o estado atual do projeto. Na primeira vez que executamos esse comando em um novo projeto que use SQLite, o Django criará um novo banco de dados para nós. Você poderá notar que Django criou um outro arquivo chamado *db.sqlite3*. O SQLite é um banco de dados que executa com base em um único arquivo.

### Visualizando o projeto
Para garantir que Django configurou o proejto de modo apropriado, execute o comando **runserver** da seguinte maneira:
```
$ python magage.py runserver
```

Se você receber uma mensagem de erro *That port is already in use*, diga a Django para usar uma porta diferente por meio do comando abaixo e vá passando por números maiores até encontrar uma porta que esteja aberta:
```
$ python manage.py runserver 8001
```


## Iniciando uma Aplicação
Um projeto Django é organizado na forma de um grupo de aplicações individuais que operam em conjunto para fazer o projeto funcionar como um todo. Começaremos criando a aplicação *learning_logs*:
```
$ source ll_env/bin/activate
$ python manage.py startapp learning_logs
```

O comando **startapp nomeapp** diz a Django para criar a infraestrutura necessária à construção de uma aplicação. Se você observar o diretório de projeto agora verá uma nova pasta chamada *learning_logs*. Dentro dela, os arquivos mais importantes são: *models.py*, *admin.py* e *views.py*. Usaremos *models.py* para definir os dados que queremos administrar em nossa aplicação.

### Definindo Modelos
Um modelo diz a Django como trabalhar com os dados que serão armazenados na aplicação. Do ponto de vista do código, um modelo é apenas uma classe; ele tem atributos métodos, assim como todas as classes que discutimos.

Para ver os diferentes tipos de campos que você pode usar em um modelo, consulte o Django Model Field Reference.

#### Ativando os modelos
Para usar nossos modelos, devemos dizer a Django para incluir nossa aplicação no projeto como um todo. Abra *settings.py* e você verá uma seção INSTALLED_APPS que informa a Django quais aplicações estão instaladas no projeto.

Em seguida, devemos dizer a Django para modificar o banco de dados para que ele possa armazenar informações relacionadas ao modelo **Topic**:
```
$ python manage.py makemigrations learning_logs
```

O comando **makemigrations** diz a Django para descobrir como modificar o bando de dados para que ele possa armazenar os dados associados a qualquer novo modelo que definirmos. A saída nesse caso, provavelmente, mostrará que Django criou um arquivo de migração chamado 0001_initial.py. Essa migração criará uma tabela para o modelo **Topic** no banco de dados. Assim, podemos fazer essa migração:
```
$ python manage.py migrate
```

Sempre que quisermos modificar os dados administrados por Learning Log, executaremos estes três passos: modificaremos *models.py*, chamaremos **makemigrations** em **learning_logs** e diremos a Django para executar um **migrate** no projeto.


## Site de administração de Django
Ao definir modelos para uma aplicação, o Django fará com que seja mais fácil para você trabalhar com seus modelos por meio do *site de administração*.

### Criando um superusuário
O Django permite criar um usuário com todos os privilégios disponíveis no site: esse usuário é conhecido como *superusuário*. Um *privilégio* controla as ações que um usuário pode executar.

Para criar um superusuário em Django, execute o comando a seguir e responda aos prompts:
```
$ python manage.py createsuperuser
Username:
Email adress (optional):
Password:
Password (again):
```

### Registrando um modelo junto ao site de administração
O Django inclui alguns modelos no site de administração de modo automático, por exemplo, **User** e **Group**, mas os modelos que criamos devem ser registrados manualmente.

Quando iniciamos a aplicação **learning_logs**, o Django criou um arquivo chamado *admin.py* no mesmo diretório em que está *models.py*. Para fazer o registro, importe o arquivo e a classe em *admin.py* e o código:
```
admin.site.register(noma_da_classe)
```

### Definindo o modelo Entry
Para o usuário registrar o que aprendeu sobre algum tópico, precisamos definir um modelo para os tipos de entrada que os usuários podem criar em seus registros de aprendizado. Cada entrada deve estar associada a um assunto em particular. Esse relacionamento é chamada de *relacionamento de muitos para um*, o que quer dizer que várias entradas podem estar associadas a um assunto.


## Shell de Django
Após inserirmos alguns dados, podemos analisá-los por meio de programação em mum sessão interativa de terminal. Esse ambiente interativo é chamado de *shell* do Django, e é um ótimo ambiente para testar e resolver problemas de seu projeto.

Eis um exemplo de uma sessão interativa de shell:
```
(ll_env)leraning_logs$ python manage.py shell
>>> from learning_logs.models import Topic
>>> Topic.objects.all()
[<Topic: Chess>, <Topic: Rock Climbing>]
```

O comando **python manage.py shell** (executado em um ambiente virtual ativo) inicia um interpretador Python que você pode usar para explorar os dados armazenados no banco de dados de seu projeto.
Usamos o método **Topic.objects.all()** para obter todas as instâncias do modelo **Topic**; a lista devolvida se chama *queryset*.
Podemos percorrer um queryset do mesmo modo que o fazemos com uma lista:
```
>>> topics = Topic.objects.all()
>>> for topic in topics:
...     print(topic.id, topic)
...
1 Chess
2 Rock Climbing
```

Se você souber qual é o ID de um objeto em particular, poderá acessar esse objeto e analisar qualquer atributo que ele tiver:
```
>>> t = Topic.objects.get(id=1)
>>> t.text
'Chess'
>>> t.date_added
datetime.datetime(...)
```

Também podemos ver as entradas relacionadas a determinado tópico. Definimos no projeto o atributo **topic** no modelo **Entry**. Esse atributo era uma ForeignKey, isto é, uma conexão entre cada entrada e um tópico. O Django é capaz de usar essa conexão para obter todas as entradas relacionadas a determinado assunto, desta maneira:
```
>>> t.entry_set.all()
[<QuerySet [<Entry: A abertura é a primeira parte do jogo; de modo ger...>, <Entry: Na fase de abertura do jogo, é importante avançar ...>]>]
```

Para obter dados por meio de um relacionamento de chave estrangeira, utilize o nome do modelo relacionado com letras minúsculas, seguido de um underscore e da palavra **set**.

Sempre que modificar seus modelos, será necessário reinicar o shell para ver os efeitos dessas alterações. Para sair de um sessão de shell, tecle CTRL-D; no Windows, tecle CTRL-Z e depois ENTER.


## Criando Páginas
Geralmente a criação de páginas web com Django é constituída de três etapas: definir os URLs, escrever as views e criar os templates. Em primeiro lugar, você deve definir padrões para os URLs. Um padrão de URL descreve o modo como o URL é organizado, e diz a Django o que ele deve procurar quando fizer a correspondência entre um requisição do navegador e o URL de um site para que ele possa saber qua página deverá devolver.

Cada URL então é mapeado para uma *view* em particular - a função de view obtém e processa os dados necessários a essa página. Essa função geralmente chama um *template*, que constrói uma página possível de ser lida por um navegador.

### Mapeando um URL
No momento, o URL base, *http://localhost:8000/*, devolve o site default de Django. Mudaremos isso mapeando o URL base para página inicial de Learning Log. Na pasta principal do projeto *learning_log*, abra o arquivo *urls.py*. Em seguida, precisamos criar um segundo arquivo *urls.py* na pasta *learning_logs*.

### Escrevendo uma view
Uma função de view recebe informações de uma requisição, prepara os dados necesários para gerar uma página e então envia os dados de volta ao navegador, geralmente usando um template que define a aparência da página.
O arquivo *views.py* foi gerado automaticamente quando executamos o comando **startapp**.

### Escrevendo um template
Um template define a estrutura de uma página web. Ele permite acessar qualquer dado oferecido pela view. Na pasta *learning_logs*, crie uma nova pasta chamada *templates*. Nessa pasta, crie outra pasta chamda *learning_logs*. Na pasta *learning_logs* interna, crie um novo arquivo de nome *index.html*.

### Herança de templates
Quando criar um site, quase sempre você precisará de alguns elementos que se repetirão em todas as páginas. Em vez de escrever esses elementos diretamente em cada página, você poderá criar um template base que contenha os elementos repetidos e então fazer cada página herdar esse template. Essa abordagem permite que o enfoque seja dado no desenvolvimento dos aspectos exclusivos de cada página e facilita bastante alterar a aparência do projeto como um todo.

Começaremos criando um template chamado *base.html* no mesmo diretório em que está *index.html*. Esse arquivo conterá elementos comuns a todas as páginas; todos os demais templates herdarão de *base.html*. Feito isso, precisaremos reescrever os templates para que herdem de *base.html*.

Em um projeto grande, é comum ter um template-pai chamado *base.html* para todo o site e templates-pai para cada seção principal do site. Todos os templates de seção herdam de *base.html*, e toda página do site herda de um template se seção.

### Padrão de URL para um assunto
O padrão de URL para a página de um assunto é um pouco diferente dos demais padrões que vimos até agora porque ele usará o atributo **id** do assunto a fim de informar qual é o assunto solicitado. Por exemplo, se o usuário quiser ver a página de detalhes do assunto Chess, cujo **id** é 1, o URL será http://localhost:8000/topics/1/. Esse padrão será incluído em *learning_logs/urls.py*.

### Métodos GET e POST
OS dois tipos principais de requisição que você usará ao criar aplicações web são as requisições GET e POST. Usamos requisições GET para páginas que apenas leem dados do servidor. Geralmente usamos requisições POST quando o usuário precisa submeter informações por meio de um formulário.


## Criando Contas de Usuário
### Aplicação users
Começaremos criando uma nova aplicação chamada **users** utilizando o comando **startapp**:
```
(ll_env)learning_log$ python manage.py startapp users
(ll_env)laerning_log$ ls
db.sqlite3 learning_log learning_logs ll_env manage.py users
(ll_env)laerning_log$ ls users
admin.py __init__.py migrations models.py tests.py views.py
```

Esse comando cria um novo diretório chamado *users*, com um estrutura idêntica àquela da aplicação *learning_logs*.

### Adicionando users em settings.py
É necessário adicionar nossa nova aplicação em **INSTALLED_APPS**, no arquivo *settings.py*. Assim, Django incluirá a aplicação **users** no projeto como um todo.

### Incluindo URLs de users
Em seguida precisamos modificar o *urls.py* raiz para que inclua os URLs que utilizaremos na aplicação users.