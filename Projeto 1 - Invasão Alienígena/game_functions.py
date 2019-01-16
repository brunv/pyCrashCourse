import sys
import pygame

def check_keydown_events(event, ship):
    """Responde a pressionamentos de tecla."""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    """Responde a solturas de tecla."""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    """Responde a eventos de pressionamento de teclas e de mouse."""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # clique no botão de fechar janela
            sys.exit()                  # fecha o programa
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)          

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            

def update_screen(config, screen, ship):
    """Atualiza as imagens na tela e altera para a nova tela."""

    # Redesenha a tela a cada passagem do laço
    screen.fill(config.bg_color)
    ship.blitme()

    # Deixa a tela mais recente visível
    pygame.display.flip()



# 	    Para fazer nosso programa responder aos eventos, escreveremos um laço
#	    de eventos apara ouvir um evento e executar uma tarefa apropriada de
#	    acordo com o tipo de evento ocorrido utilizando event.get().
#
#       Fornecemos um parâmetro 'ship' à função check_events(). Nela, acrescentamos
#       um bloco 'elif' no laço para responder quando Pygame detectar um evento
#       KEYDOWN. Em seguida verificamos se a tecla pressionada é a seta para a
#       direita (K_RIGHT) lendo o atributo 'event.key'.
#
#       Quando o jogador manter a seta para dirieta pressionada, queremos que a
#       espaçonave continue a se mover para a direita até que o jogador soltar a
#       tecla. Assim, faremos nosso jogo detectar um evento pygame.KEYUP para que
#       possamos saber quando a seta para a direita foi solta; então usaremos os 
#       eventos KEYDOWN e KEYUP juntamente com uma flag, chamava 'moving_right'
#       para implementar o movimento contínuo.
#
#	    Desenhamos a espaçonave na tela chamando 'ship.blitme()' depois de
#	    preencher a cor de fundo; assim a espaçonave aparecerá sobre essa cor.