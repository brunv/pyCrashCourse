import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, config, screen, ship, bullets):
    """Responde a pressionamentos de tecla."""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(config, screen, ship, bullets)


def check_keyup_events(event, ship):
    """Responde a solturas de tecla."""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(config, screen, ship, bullets):
    """Responde a eventos de pressionamento de teclas e de mouse."""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # clique no botão de fechar janela
            sys.exit()                  # fecha o programa
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, config, screen, ship, bullets)          

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def fire_bullet(config, screen, ship, bullets):
    """Dispara um projétil se o limite ainda não foi alcançado."""
    
    #   Cria um novo projétil e o adiciona ao grupo de projéteis
    if len(bullets) < config.bullet_allowed:
        new_bullet = Bullet(config, screen, ship)
        bullets.add(new_bullet)

def update_bullets(bullets):
    """Atualiza a posição dos projéteis e se livra dos projéteis antigos."""

    #   Atualiza posição dos projéteis
    bullets.update()

    #   Livra-se dos projéteis que desaparecerem
    for bullet in bullets.copy():
        if bullet.bullet_rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))
            

def update_screen(config, screen, ship, bullets):
    """Atualiza as imagens na tela e altera para a nova tela."""

    #   Redesenha a tela a cada passagem do laço
    screen.fill(config.bg_color)
    
    #   Redesenha todos os projéteis atrás da espaçonave e dos alienígenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Redesenha a espaçonave a cada passagem do laço
    ship.blitme()

    #   Deixa a tela mais recente visível
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