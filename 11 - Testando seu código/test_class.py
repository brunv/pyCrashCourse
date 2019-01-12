#
#       Testando uma classe
#

#       Python disponibiliza vários métodos de asserção na classe 'unittest.Test
#       Case'. Como mencionamos, os métodos de asserção testam se uma condição
#       você acredita ser verdadeira em um ponto específico de seu código realmente
#       é verdadeira.
#
#       A tabela a seguir descreve seis métodos de asserção comumente usados:
#
#       ----------------------------------------------------------------------
#               Método                          Uso
#       ----------------------------------------------------------------------
#           assertEqual(a,b)            Verifica se a == b
#           assertNotEqual(a,b)         Verifica se a != b
#           assertTure(x)               Verifica se x é True
#           assertFalse(x)              Verifica se x é False
#           assertIn(item,lista)        Verifica se item está em lista
#           assertNotIn(item,lista)     Verifica se item não está em lista
#       ----------------------------------------------------------------------


#
#       Testando a classe AnonymousSurvey:
#

# import unittest
# from survey import AnonymousSurvey

# class TestAnonymousSurvey(unittest.TestCase):
#     """Testes para a classe AnonymousSurvey."""

#     def test_store_single_responses(self):
#         """Testa se uma única resposta é armazena de forma apropriada."""

#         question = "What language did you first learn to speak?"
#         my_survey = AnonymousSurvey(question)
#         my_survey.store_response('English')

#         self.assertIn('English', my_survey.responses)

#     def test_store_three_responses(self):
#         """Testa se três respostas individuais são armazenadas de forma apropriada."""

#         question = "What language did you first learn to speak?"
#         my_survey = AnonymousSurvey(question)
#         responses = ['English, Spanish', 'Mandarin']

#         for response in responses:
#             my_survey.store_response(response)

#         for response in responses:
#             self.assertIn(response, my_survey.responses)

# unittest.main()


#
#       Método setUp():
#

#       No teste anterior criamos uma nova instância de AnonymousSurvey em cada
#       método de teste e criamos novas respostas para cada método. A classe
#       'unittest.TestCode' tem um método 'setUp()' que permite criar esses objetos
#       uma vez e então usá-los em cada um de seus métodos de teste. Quando um
#       método 'setUp()' é incluído em uma classe 'TestCase', Python excuta esse
#       método antes de qualquer método cujo nome comece com 'test_'. Ou seja,
#       qualquer objeto criado no método 'setUp()' é prefixado com 'self' para que
#       esteja disponível a todos os métodos de teste que você escrever.
#       Vamos reescrever o teste anterior:

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Testes para a classe AnonymousSurvey."""

    def setUp(self):
        """
        Cria uma pesquisa e um conjunto de respostas que poderão ser usados
        em todos os métodos de teste.
        """
        
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English, Spanish', 'Mandarin']

    def test_store_single_responses(self):
        """Testa se uma única resposta é armazena de forma apropriada."""

        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Testa se três respostas individuais são armazenadas de forma apropriada."""

        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()