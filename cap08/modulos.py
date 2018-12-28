#       Podemos armazenar as funções em arquivos separados chamados módulos
#       e, então, importar esses módulos em um programa principal. Isso permite
#       ocultar detalhes do código de seu programa, reutilizar funções em
#       muitos programas diferentes, compartilhar parte da implementação com
#       outros programadores e possibilita montar/utilizar bibliotecas prontas.


#       Importando um módulo completo: 'import nome_do_módulo'
#       Essa primeira abordagem à importação, deixa todas as funções do módulo
#       disponíveis ao seu programa.
#       Para acessar as funções do módulo: 'nome_do_módulo.nome_da_função()'

import cook

cook.make_pizza('pepperoni')
cook.make_pizza('mushrooms', 'green peppers', 'extra cheese')


#       Importando funções específicas: 'from nome_do_módulo import nome_da_função'
#       Com essa sintaxe, não precisamos usar a notação de ponto ao chamar
#       uma função, pois elas são importadas explicitamente.

from cook import make_sandwich

make_sandwich(10, 'sausage')
make_sandwich(18, 'sausage', 'barbecue', 'extra cheese')


#       Se o nome de uma função que importar puder entrar em conflito com
#       um nome existente no programa ou se o nome da função for longo, podemos
#       utilizar a palavra reservada 'as' para atribuir um alias a uma função

from cook import make_pizza as mp, make_sandwich as ms

mp('portuguese')
ms(14, 'chicken', 'salad', 'double chesse')


#       Também podemos utilizar a palavra reservada 'as' para atribuir
#       um alias a um módulo.
#       'import nome_do_módulo as alias_módulo'

import cook as c

c.make_pizza('pepperoni')
c.make_sandwich(8, 'beef', 'barbecue')


#       É possível importar todas as funções de um módulo e não utilizar
#       a notação de ponto. No entanto, é melhor não usar essa abordagem
#       quando trabalhar com módulo grandes.

from cook import *

make_pizza('portuguese')
make_sandwich(12, 'sausage', 'ketchup', 'salad')