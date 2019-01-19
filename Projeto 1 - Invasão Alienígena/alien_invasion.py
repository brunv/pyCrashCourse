import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
from button import Button
from scoreboard import Scoreboard
import game_functions as gf

def run_game():
    """Inicializa o jogo e cria um objeto para a tela."""

    #	Inicializa o jogo
    pygame.init()
    config = Settings()
    screen = pygame.display.set_mode((config.screen_width, config.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #   Cria o botão Play
    play_button = Button(config, screen, "Play")

    #   Cria uma instância para armazenar dados estatísticos do jogo
    stats = GameStats(config)

    #   Cria uma instância para armazenar o placar
    sb = Scoreboard(config, screen, stats)

    #	Cria uma espaçonave
    ship = Ship(config, screen)

    #   Cria um alienígena
    alien = Alien(config, screen)

    #   Cria um grupo no qual serão armazenados os projéteis e aliens
    bullets = Group()
    aliens = Group()

    #   Cria a frota de alienígenas
    gf.create_fleet(config, screen, ship, aliens)

    #   Inicia o laço principal do jogo
    while True:

        #   Observa eventos de teclado e de mouse
        gf.check_events(config, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            #   Atualiza posição da espaçonave
            ship.update()
            #   Atualiza a posição e deleta os projéteis
            gf.update_bullets(config, screen, stats, sb, ship, aliens, bullets)
            #   Atualiza a posição dos alienígenas
            gf.update_aliens(config, stats, screen, ship, aliens, bullets)

        #   Resenha a tela a cada passagem do laço
        gf.update_screen(config, screen, stats, sb, ship, aliens, bullets,
             play_button)

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
