#       A biblioteca-padrão de Python é um conjunto de módulos incluído em todas
#       as instalações de Python.
#       Exemplo de utilização da biblioteca-padrão 'collections'.


#       Os dicionários permitem associar informações de uma lista, mas eles não
#       mantêm um controle da ordem em que os pares chave-valor são armazenados.
#       Instâncias da classe 'OrderedDict' do módulo 'collections' se coportam
#       do mesmo modo que os dicionários, exceto que mantêm o controle da ordem
#       em que os pares chave-valor são armazenados.

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'java'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")