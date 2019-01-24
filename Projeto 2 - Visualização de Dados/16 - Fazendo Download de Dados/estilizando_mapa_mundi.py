#
#       Estilizando mapas-mundi com Pygal
#

import json
from pygal.maps.world import World
from pygal.style import RotateStyle, LightColorizedStyle
from country_codes import get_country_code

#   Carrega dados em uma lista
filename = 'data/population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

#   Constrói um dicionário com dados das populações
cc_populations = {}

for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)

        if code:
            cc_populations[code] = population

#   Agrupa os países em três níveis populacionais
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}

for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

#   Vê quantos países estão em cada nível
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

#   Cria o mapa
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = World(style=wm_style)
wm.title = 'World Populations in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('data/estilizando_mapa_mundi.svg')


#       Os estilos do Pygal estão armazenados no módulo 'style' do qual importamos
#       o estilo 'RotateStyle'. Essa classe aceita um argumento, que é uma cor RGB
#       em formato hexa. O Pygal então escolhe as cores para cada um dos grupos de
#       acordo com a cor fornecida.
#
#       'RotateStyle' devolve um objeto estilo, que armazenamos em 'wm_style'. Para
#       usar esse objeto, passe-o como um argumento nomeado ao criar uma instância
#       de 'World'.
#
#       O Pygal tende a usar temas escuros por padrão. Para deixar os mapas mais
#       claros, use a classe 'LightColorizedStyle'. Essa classe altera o tema do
#       mapa como um todo, incluindo a cor de fundo e os rótulos, assim como as 
#       cores individuais dos países. No entanto, essa classe não oferece nenhum
#       controle direto a você sobre a cor usada, portanto o Pygal escolherá uma
#       cor base default. Para definir uma cor, utilize 'LightColorizedStyle' como
#       base para 'RotateStyle'. Isso resulta em um tema, de modo geral, mais
#       claro, porém as cores dos países serão baseadas na cor que você passar como
#       argumento.