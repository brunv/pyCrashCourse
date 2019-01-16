import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """Inicializa o jogo e cria um objeto para a tela."""

    #	Inicializa o jogo
    pygame.init()
    config = Settings()
    screen = pygame.display.set_mode((config.screen_width, config.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #	Cria uma espaçonave
    ship = Ship(screen)

    #   Inicia o laço principal do jogo
    while True:

        #   Observa eventos de teclado e de mouse
        gf.check_events()
        #   Resenha a tela a cada passagem do laço
        gf.update_screen(config, screen, ship)

run_game()


#	    O módulo 'pygame' contém as funcionalidades necessárias para criar um jogo.
#	    O módulo 'sys' será utilizado para sair do jogo quando o usuário quiser.
#
#   	O método init() inicializa as configurações de segundo plano que o Pygame
#	    precisa para funcionar de maneira apropriada.
#
#	    Instanciamos Settings() em config após o início de pygame.init()
#
#	    Chamamos display.set_mode() para criar uma janela de exibição na qual
#	    desenharemos todos os elementos gráficos do jogo. O argumento passado
# 	    define as dimensões da janela do jogo.
#
#	    Chamamos display.set_caption() para dar nome à janela do jogo.
#
# 	    Para fazer nosso programa responder aos eventos, escreveremos um laço
#	    de eventos apara ouvir um evento e executar uma tarefa apropriada de
#	    acordo com o tipo de evento ocorrido utilizando event.get().
#
#	    Desenhamos a espaçonave na tela chamando 'ship.blitme()' depois de
#	    preencher a cor de fundo; assim a espaçonave aparecerá sobre essa cor.