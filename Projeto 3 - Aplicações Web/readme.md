# Aplicações Web - Projeto 3

Essa seção destina-se ao desenvolvimento do terceiro projeto do livro Curso Intensivo de Python (Python Crash Course) por Eric Matthes.

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
$ ll_env/Source/activate
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
