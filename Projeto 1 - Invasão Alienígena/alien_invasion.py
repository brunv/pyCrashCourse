import sys
import pygame
from settings import Settings

def run_game():
    #   Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    config = Settings()
    screen = pygame.display.set_mode(
            (config.screen_width, config.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    #   Define a cor de fundo
    bg_color = (230, 230, 230)

    #   Inicia o laço principal do jogo
    while True:

        # Observa eventos de teclado e mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redesenha a tela a cada passagem do laço
        screen.fill(config.bg_color)

        # Deixa a tela mais recente visível
        pygame.display.flip()


run_game()