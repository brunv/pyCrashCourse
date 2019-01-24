#
#       Plota dados básico no mapa mundi
#

from pygal.maps.world import World 

wm = World()
wm.title = 'Populations of Countries in North America'

wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('data/populacao_americana.svg')


#       Desta vez, ao utilizar método 'add()', passamos um dicionário como segundo
#       argumento em vez de passar uma lista. O dicionário contém os códigos de
#       duas letras do Pygal para os países como chave e as populações como
#       valores. O pygal utiliza automaticamente esses números para sombrear os
#       países, variando da cor mais clara (menos populoso) para a cor mais escura
#       (mais populoso).