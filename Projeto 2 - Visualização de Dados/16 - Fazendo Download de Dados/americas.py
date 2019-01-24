#
#       Plotando mapas das américas
#

from pygal.maps.world import World 

wm = World()
wm.title = 'North, Centra, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe',
    'py', 'sr', 'uy', 've'])

wm.render_to_file('data/americas.svg')


#       Criamos uma instância da classe 'World()' e definimos o atributo 'title'
#       do mapa. Em seguida usamos o método 'add()', que aceita um rótulo e uma
#       lista de código de países que queremos destacar. Cada chamada a 'add()'
#       define uma nova cor para o ocnjunto de países e acrescenta essa cor a uma
#       legenda à esquerda da imagem, com o rótulo especificado nessa chamada.