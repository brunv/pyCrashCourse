import sys
import pygame

def check_events():
    """Responde a eventos de pressionamento de teclas e de mouse."""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # clique no botão de fechar janela
            sys.exit()                  # fecha o programa

def update_screen(config, screen, ship):
    """Atualiza as imagens na tela e altera para a nova tela."""

    # Redesenha a tela a cada passagem do laço
    screen.fill(config.bg_color)
    ship.blitme()

    # Deixa a tela mais recente visível
    pygame.display.flip()