#	O módulo 'pygame' contém as funcionalidades necessárias para criar um jogo.
#	O módulo 'sys' será utilizado para sair do jogo quando o usuário quiser.
import sys
import pygame
from settings import Settings

def run_game():
    #   O método init() inicializa as configurações de segundo plano que o Pygame
	#	precisa para funcionar de maneira apropriada.
    pygame.init()
	#	Instancia a classe de configuração (depois da chamada de pygame.init())
    config = Settings()
	#	Chamamos display.set_mode() para criar uma janela de exibição na qual
	#	desenharemos todos os elementos gráficos do jogo.
	#	O argumento passado define as dimensões da janela do jogo.
    screen = pygame.display.set_mode(
            (config.screen_width, config.screen_height)
    )
	#	Chamamos display.set_caption() para dar nome à janela do jogo.
    pygame.display.set_caption("Alien Invasion")

    #   Inicia o laço principal do jogo
    while True:

        # 	Para fazer nosso programa responder aos eventos, escreveremos um laço
		#	de eventos apara ouvir um evento e executar uma tarefa apropriada de
		#	acordo com o tipo de evento ocorrido utilizando event.get().
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()		#	Clicar no botão de saída

        # Redesenha a tela a cada passagem do laço
        screen.fill(config.bg_color)

        # Deixa a tela mais recente visível
        pygame.display.flip()


run_game()