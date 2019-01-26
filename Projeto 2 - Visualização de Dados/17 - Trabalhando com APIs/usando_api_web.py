#
#       Usando uma API web
#

#       Uma API web é uma parte de um site projetada para interagir com programas
#       que usam URLs bem específicos a fim de requisitar determinadas informações.
#       Esse tipoe de requisição é conhecido como 'chamada de API'. Os dados
#       solicitados serão devolvidos em um formato facilmente processável, por
#       exemplo, JSON ou CSV.
#
#       Requisitando dados usando uma chamada de API:
#       A API do GitHub permite requisitar várias informações por meio de chamadas
#       de API. Para ver como é a aparência de uma chamada de API, digite o
#       seguinte na barra de endereço do navegador:
#
#       https://api.github.com/search/repositories?q=language:python&sort=stars
#
#       Essa chama devolve o número de projetos Python hospedados no GitHub no
#       momento, bem como informações sobre os repositórios Python mais populares.
#       A primeira parte 'https://api.github.com/', direciona a requisição para a
#       parte do site que responde a chamadas de API. A próxima parte,
#       'search/repositories', diz à API para conduzir uma pesquisa por todos os
#       repositórios do GitHub.
#       O ponto de interrogação indica que estamos preste a passar um argumento. A
#       letra 'q' quer dizer query e o sinal de igualdade nos permite começar a
#       especificá-la. Ao usar 'language:python', sinalizamos que queremos
#       informações somente sobre os repositórios que tenham Python como linguagem
#       principal. A última parte, '&sort=stars', ordena os projetos de acordo com
#       o número de estrelas que receberam.
#
#       {
#       "total_count": 3426783,
#       "incomplete_results": false,
#       "items": [
#           {
#           "id": 21289110,
#           "node_id": "MDEwOlJlcG9zaXRvcnkyMTI4OTExMA==",
#           "name": "awesome-python",
#           "full_name": "vinta/awesome-python",
#           --- trecho omitido ---
#
#       Na primeira linha podemos ver a quantidade de repositórios encontrada pela
#       busca. Como o valor de 'incomplete_results' é 'false', sabemos que a
#       requisição foi bem-sucedida. Se o GitHub não tivesse sido capaz de
#       processar totalmente a requisição da API, ele teria devolvido 'true' aqui.
#       os 'items' devolvidos são exibidos na lista que está na sequência, a qual
#       contém detalhes sobre os projetos Python mais populares no GitHub.
#
#       Instalando o pacote 'requests':
#       "python -m pip install --user requests"
#       O pacote 'requests' permite que um programa Python solicite informações a
#       um site e analise a resposta devolvida.
#
#       Monitorando os limites da taxa de uso da API:
#       A maioria das APIs tem uma taxa de uso limitada, o que significa que há um
#       limite para quantas requisições podemos fazer em determinado perído de
#       tempo. Para ver os limites da API do GitHub, acesse:
#       'http://api.github.com/rate_limit'. É importante lembrar que muitas APIs
#       exigem que você se registre e obtenha uma chave para fazer chamadas de API.


import requests

#   Faz uma chamada de API e armazena a resposta
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code:", r.status_code)

#   Armazena a resposta da API em uma variável
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

#   Explora informações sobre os repositórios
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repositoty:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])

#   Analisa o primeiro repositório e exibe todas as suas chaves
# print("\nKeys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)


#       Chamamos 'get()', passamos o URL e armazenamos o objeto com a resposta na
#       variável 'r'. O objeto com resposta tem um atributo chamado 'status_code',
#       que nos informa se a reqisição foi bem-sucedida (um código de status igual
#       a 200 indica sucesso).
#       A API devolve as informações em formato JSON, portanto usamos o método
#       'json()' para convertê-las em um dicionário Python. Armazenamos o
#       dicionário resultante em 'response_dict'.
#
#       Chamadas simples como essa devem devolver um conjunto completo de
#       resultados, portanto é seguro ignorar o valor associado a
#       'incomplete_results'. Porém, quando fizer chamadas de API mais complexas,
#       seu programa deverá conferir esse valor.