#
#       Testes de unidade e casos de teste:
#

#       O módulo 'unittest' da biblioteca-padrão de Python oferece as ferramentas
#       para testar seu código.
#       Um 'teste de unidade' verifica se um aspecto específico do comportamento
#       de uma função está correto.
#       Um 'caso de teste' é uma coleção de teste de unidade que, em conjunto,
#       prova que uma função se comporta como deveria em todas as situações que
#       você espera que ela trate. Um bom caso de teste considera todos os tipos
#       possíveis de entradas que uma função poderia receber e inclui teste para
#       representar cada uma dessas situações.
#       Um caso de teste com 'cobertura completa' é composto de uma variedade de
#       teste de unidade que inclui todas as possíveis maneiras de usar uma função.
#       Em geral, é suficiente escrever testes para os comportamentos críticos de
#       seu código e então visar a uma cobertura completa somente se o projeto
#       começar a ter uso disseminado.


#
#       Testes que passam:
#

#       Para escrever um caso de teste para uma função, importe o módulo 'unittest'
#       e a função que você quer testar. Em seguida crie uma classe que herde
#       'unittest.TestCase' e escreva uma série de métodos para testar diferentes
#       aspectos do comportamento da função:

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Testes para 'name_function.py'."""

    def test_first_last_name(self):
        """Nomes como 'Janis Joplin' funcionam?"""

        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Nomes como 'Wolfgang Amadeus Mozart' funcionam?"""

        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()

#       Você pode dar o nome que quiser para a classe, mas é melhor nomeá-la com
#       palavras relacionadas à função que você está prestes a testar e usar a 
#       palavra Test no nome da classe.
#
#       Qualquer método que comece com 'test_' será executado de modo automático.
#       Nomes longos para os métodos em nossas classes TestCase não são um
#       problema. Eles devem ser descritivos para que você possa compreender a
#       saída quando seus teste falharem.
#
#       Nesse método de teste, chamamos a função que queremos testar e armazenamos
#       um valor de retorno que estamos interessados em testar. Em seguida, usamos
#       um dos recursos mais úteis de 'unittest': um método de asserção. Os métodos
#       de asserção verificam se um resultado recebido é igual ao resultado que
#       você esperava receber (linhas 40 e 46).
#
#       A linha 'unittest.main()' diz a Python para executar os teste desse arquivo.


#
#       Analisando a saída:
#

#   ..
#   ----------------------------------------------------------------------
#   Ran 2 tests in 0.000s
#
#   OK

#       Os dois pontos na primeira linha da saída nos informam que dois testes
#       passaram. A segunda linha nos informa quantos testes rodaram e quanto
#       tempo levou. O OK no final informa que todos os testes da unidade do
#       caso de teste passaram.
#
#       Durante a execução de um caso de teste, Python exibe um caractere para
#       cada teste de unidade à medida que ele termianr. Um teste que passar exibe
#       um ponto, um teste que resulte em erro exibe E e um teste que resultar em
#       uma asserção com falha exibe F.
#       Se um caso de teste demorar muito para excutar por conter muitos teste de
#       unidade, você poderá observar esses resultados para ter uma noção de
#       quantos teste estão passando.


#
#       Um teste que falha:
#

# def test_first_last_middle_extra_name(self):
#     """Nomes como 'Pedro de Alcântara de Bragança e Bourbon' funcionam?"""

#     formatted_name = get_formatted_name('Pedro', 'de Alcântarra', 'de Bragança', 'e Bourbon')
#     self.assertEqual(formatted_name, 'Pedro De Alcântara De Bragança E Bourbon')


#
#       Analisando a saída:
#

# E..
# ======================================================================
# ERROR: test_first_last_middle_extra_name (__main__.NamesTestCase)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
# TypeError: get_formatted_name() takes from 2 to 3 positional arguments but 4 were given
#
# ----------------------------------------------------------------------
# Ran 3 tests in 0.000s
#
# FAILED (errors=1)